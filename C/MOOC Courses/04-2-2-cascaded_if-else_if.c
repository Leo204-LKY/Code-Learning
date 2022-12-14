// 级联的 if-else if

// 例：分段函数的表示
// >> if (x < 0) {
// >>    f = -1;
// >> } else if (x == 0) {
// >>    f = 0;
// >> } else {
// >>    f = 2 * x;
// >> }

// else 与前一个 if 匹配
// 如果不使用这种方法，而是 else { if (<条件>) { }}
// 这样条件过多时，代码的缩进可能会很夸张
// 因此使用 else if 来使缩进一致，更加美观