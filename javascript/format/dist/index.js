const isDict = (data) => {
    let string = "";
    try {
        string = JSON.stringify(data);
    }
    catch (_a) {
        return false;
    }
    finally {
        return !!string && string.startsWith("{") && string.endsWith("}");
    }
};
String.prototype.format = function (...data) {
    let _data = {}, all = 0;
    data.forEach((_) => {
        if (isDict(_))
            _data = Object.assign(Object.assign({}, _data), _);
        else
            _data[(all++).toString()] = _;
    });
    return this.toString()
        .replace(/{(?!{)(([$A-Za-z_][$A-Za-z0-9_]?)*|[0-9]*)}(?!})/gm, (_, src) => {
        if (src && src in _data)
            return _data[src];
        return _;
    })
        .replace("{{", "{")
        .replace("}}", "}");
};
//# sourceMappingURL=index.js.map
