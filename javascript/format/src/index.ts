type format = (
  this: string,
  ...data: Array<{ [key: string]: string } | string>
) => string;

declare global {
  interface String {
    format: format;
  }
}

export {};
const isDict = (data: Object | string): boolean => {
  let string = "";
  try {
    string = JSON.stringify(data);
  } catch {
    return false;
  } finally {
    return !!string && string.startsWith("{") && string.endsWith("}");
  }
};

String.prototype.format = function (...data) {
  let _data: { [key: string]: any } = {},
    all = 0;

  data.forEach((_) => {
    if (isDict(_)) _data = { ..._data, ..._ };
    else _data[(all++).toString()] = _ as string;
  });

  return this.toString()
    .replace(/{(?!{)(([$A-Za-z_][$A-Za-z0-9_]?)*|[0-9]*)}(?!})/gm, (_, src) => {
      if (src && src in _data) return _data[src];
      return _;
    })
    .replace("{{", "{")
    .replace("}}", "}");
};
