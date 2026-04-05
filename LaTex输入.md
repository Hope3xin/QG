🔴 关键提醒：写论文 / 复杂公式，**必须在导言区加载 `amsmath` 宏包**（页面开头重点强调），否则很多环境无法使用：

\usepackage{amsmath} % 导言区添加，mathtools 会自动加载它，更推荐



行内公式 `$...$`

行间公式 `$$...$$`

上标 `^`、下标 `_`

平方根 `\sqrt{}`、n 次方根 `\sqrt[n]{}`

分数 `\frac{分子}{分母}`、二项式系数 `\binom{n}{k}`

求和 `\sum`、积分 `\int`、极限 `\lim`

括号 `()`、`[]`、`{}`、绝对值 `

矩阵 `matrix`、`pmatrix`、`bmatrix`

在公式中插入文字（如「if」「for all」）

| 环境类型           | 语法                                       | 适用场景                    | 示例                                 |
| ------------------ | ------------------------------------------ | --------------------------- | ------------------------------------ |
| 行内公式           | `$公式内容$`                               | 嵌入正文段落                | 质能公式 `$E=mc^2$`                  |
| 行间公式（无编号） | `\[公式内容\]` 或 `$$公式内容$$`           | 单独成行的重要公式          | `\[ \int_{0}^{\pi} \sin x dx = 2 \]` |
| 行间公式（带编号） | `\begin{equation} 公式内容 \end{equation}` | 论文 / 作业中需要引用的公式 | 自动生成公式编号，论文必备           |

| 小写 | 命令       | 大写 | 命令       |
| :--- | ---------- | ---- | ---------- |
| α    | `\alpha`   | A    | `\Alpha`   |
| β    | `\beta`    | B    | `\Beta`    |
| γ    | `\gamma`   | Γ    | `\Gamma`   |
| δ    | `\delta`   | Δ    | `\Delta`   |
| ϵ    | `\epsilon` | E    | `\Epsilon` |
| ζ    | `\zeta`    | Z    | `\Zeta`    |
| η    | `\eta`     | H    | `\Eta`     |
| θ    | `\theta`   | Θ    | `\Theta`   |
| λ    | `\lambda`  | Λ    | `\Lambda`  |
| μ    | `\mu`      | M    | `\Mu`      |
| π    | `\pi`      | Π    | `\Pi`      |
| ρ    | `\rho`     | P    | `\Rho`     |
| σ    | `\sigma`   | Σ    | `\Sigma`   |
| τ    | `\tau`     | T    | `\Tau`     |
| ϕ    | `\phi`     | Φ    | `\Phi`     |
| ψ    | `\psi`     | Ψ    | `\Psi`     |
| ω    | `\omega`   | Ω    | `\Omega`   |

3. 常用运算符与关系符

| 符号 | 命令        | 符号 | 命令                              |
| ---- | ----------- | ---- | --------------------------------- |
| +    | `+`         | ±    | `\pm`                             |
| −    | `-`         | ∓    | `\mp`                             |
| ×    | `\times`    | ÷    | `\div`                            |
| ⋅    | `\cdot`     | =   | `\neq`                            |
| =    | `=`         | ≈    | `\approx`                         |
| ≤    | `\leq`      | ≥    | `\geq`                            |
| ∞    | `\infty`    | ∀    | `\forall`                         |
| ∃    | `\exists`   | ∈    | `\in`                             |
| ⊂    | `\subset`   | ⊃    | `\supset`                         |
| ∪    | `\cup`      | ∩    | `\cap`                            |
| ∅    | `\emptyset` | R    | `\mathbb{R}`（需 `amssymb` 宏包） |

4. 函数与极限

| 函数    | 命令                  | 符号    | 命令                                          |
| ------- | --------------------- | ------- | --------------------------------------------- |
| sinx    | `\sin x`              | cosx    | `\cos x`                                      |
| tanx    | `\tan x`              | cotx    | `\cot x`                                      |
| secx    | `\sec x`              | cscx    | `\csc x`                                      |
| arcsinx | `\arcsin x`           | arccosx | `\arccos x`                                   |
| logx    | `\log x`              | lnx     | `\ln x`                                       |
| limx→a  | `\lim_{x \to a}`      | x→alim  | `\lim\limits_{x \to a}`（行间公式用，更美观） |
| ∑n=1∞   | `\sum_{n=1}^{\infty}` | ∏n=1∞   | `\prod_{n=1}^{\infty}`                        |
| ∫ab     | `\int_{a}^{b}`        | ∬D      | `\iint_{D}`（二重积分）                       |
| ∮C      | `\oint_{C}`           | ∇       | `\nabla`（梯度）                              |

5. 括号与定界符

| 符号 | 命令              | 自适应大小（推荐）               |      |      |      |        |            |      |
| ---- | ----------------- | -------------------------------- | ---- | ---- | ---- | ------ | ---------- | ---- |
| ()   | `()`              | `\left( ... \right)`             |      |      |      |        |            |      |
| []   | `[]`              | `\left[ ... \right]`             |      |      |      |        |            |      |
| {}   | `\{\}`            | `\left\{ ... \right\}`           |      |      |      |        |            |      |
| $    |                   | $（绝对值）                      | `    |      | `    | `\left | ... \right | `    |
| ⟨⟩   | `\langle \rangle` | `\left\langle ... \right\rangle` |      |      |      |        |            |      |

1. 矩阵

| 矩阵类型              | 语法                                                   | 效果     |
| --------------------- | ------------------------------------------------------ | -------- |
| 无括号矩阵            | `\begin{matrix} a & b \\ c & d \end{matrix}`           | acbd     |
| 圆括号矩阵（pmatrix） | `\begin{pmatrix} a & b \\ c & d \end{pmatrix}`         | (acbd)   |
| 方括号矩阵（bmatrix） | `\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}` | [142536] |
| 行列式（vmatrix）     | `\begin{vmatrix} a & b \\ c & d \end{vmatrix}`         | acbd     |

### 2. 多行公式对齐（`align` 环境，`amsmath` 必备）

用于长公式、方程组、推导过程，用 `&` 对齐等号，`\\` 换行：

```
\begin{align}
f(x) &= (x+a)(x+b) \\
&= x^2 + (a+b)x + ab
\end{align}
```

效果：

f(x)=(x+a)(x+b)=x2+(a+b)x+ab

### 3. 分段函数（`cases` 环境，`amsmath` 必备）

```
f(x) = 
\begin{cases} 
x^2, & x \geq 0 \\
-x, & x < 0 
\end{cases}
```

效果：

f(x)={x2,−x,x≥0x<0

------

## 四、大一课程高频公式模板（直接套用）

### 1. 高数核心公式

- 牛顿 - 莱布尼茨公式：`$\int_{a}^{b} f(x) dx = F(b) - F(a)$`
- 泰勒展开：`$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n$`
- 极限定义：`$\lim_{x \to x_0} f(x) = A \iff \forall \varepsilon > 0, \exists \delta > 0, 0 < |x-x_0| < \delta \implies |f(x)-A| < \varepsilon$`
- 二重积分：`$\iint_{D} f(x,y) d\sigma = \int_{a}^{b} dx \int_{y_1(x)}^{y_2(x)} f(x,y) dy$`

### 2. 线代核心公式

- 矩阵乘法：`$(AB)_{ij} = \sum_{k=1}^{n} A_{ik}B_{kj}$`
- 行列式展开：`$|A| = \sum_{j=1}^{n} a_{ij}A_{ij}$`
- 特征值方程：`$|A - \lambda E| = 0$`
- 向量内积：`$(\alpha, \beta) = \sum_{i=1}^{n} a_i b_i$`