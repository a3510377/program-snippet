declare module "format" {
    type format = (this: string, ...data: Array<{
        [key: string]: string;
    } | string>) => string;
    global {
        interface String {
            format: format;
        }
    }
    export {};
}
//# sourceMappingURL=index.d.ts.map
