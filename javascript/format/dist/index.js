/*! *****************************************************************************
Copyright (c) Microsoft Corporation.

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.
***************************************************************************** */

var __assign = function() {
    __assign = Object.assign || function __assign(t) {
        for (var s, i = 1, n = arguments.length; i < n; i++) {
            s = arguments[i];
            for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p)) t[p] = s[p];
        }
        return t;
    };
    return __assign.apply(this, arguments);
};

var isDict = function (data) {
    var string = "";
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
String.prototype.format = function () {
    var data = [];
    for (var _i = 0; _i < arguments.length; _i++) {
        data[_i] = arguments[_i];
    }
    var _data = {}, all = 0;
    data.forEach(function (_) {
        if (typeof _ !== "string" && isDict(_))
            _data = __assign(__assign({}, _data), _);
        else
            _data[(all++).toString()] = _;
    });
    return this.toString()
        .replace(/{(?!{)(([$A-Za-z_][$A-Za-z0-9_]?)*|[0-9]*)}(?!})/gm, function (_, src) {
        if (src && src in _data)
            return _data[src];
        return _;
    })
        .replace("{{", "{")
        .replace("}}", "}");
};
//# sourceMappingURL=index.js.map
