(function (global, factory) {
  typeof exports === 'object' && typeof module !== 'undefined' ? factory(exports) :
  typeof define === 'function' && define.amd ? define(['exports'], factory) :
  (global = typeof globalThis !== 'undefined' ? globalThis : global || self, factory(global.example = {}));
})(this, (function (exports) { 'use strict';

  const isDict = (data) => {
    let string = "";
    try {
      string = JSON.stringify(data);
    } catch {
      return false;
    } finally {
      return string && string.startsWith("{") && string.endsWith("}");
    }
  };
  function format(...data) {
    let _data = {},
      all = 0;
    for (let _ of data) {
      if (isDict(_)) _data = { ..._data, ..._ };
      else _data[all++] = _;
    }

    return this.toString()
      .replace(/{(?!{)[A-Za-z0-9_]*}(?!})/gm, (src) => {
        let _ = src.match(/^{(.*)}$/)?.[1];
        if (_ in _data) return _data[_];
        return `{${_}}`;
      })
      .replaceAll("{{", "{")
      .replaceAll("}}", "}");
  }

  String.prototype.format = function (...data) {
    let _data = {},
      all = 0;
    for (let _ of data) {
      if (isDict(_)) _data = { ..._data, ..._ };
      else _data[all++] = _;
    }

    return this.toString()
      .replace(/{(?!{)[A-Za-z0-9_]*}(?!})/gm, (src) => {
        let _ = src.match(/^{(.*)}$/)?.[1];
        if (_ in _data) return _data[_];
        return `{${_}}`;
      })
      .replaceAll("{{", "{")
      .replaceAll("}}", "}");
  };

  exports.format = format;

  Object.defineProperty(exports, '__esModule', { value: true });

}));
