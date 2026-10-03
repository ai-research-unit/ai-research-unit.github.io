# __Bohr's Phenomenon for Monogenic Functions__

## Introduction

Bohr's theorem states that the Taylor series of a holomorphic function of the unit disk bounded by one is majorised by its value at the origin on a disk of radius $1/3$, and that $1/3$ cannot be enlarged. It is one of the few one-variable statements whose several-variable analogues are still an active subject, and it has an analogue in the three-dimensional quaternionic theory of the reduced quaternions, in which the Taylor series is replaced by the expansion of a monogenic function in the orthonormal system of the Riesz system.

This article records the monogenic Bohr phenomenon as it stands after the paper of Gürlebeck and Morais that improved the earlier radii and proved an estimate for the hypercomplex derivative by the supremum norm. The classical theorem and the arithmetic behind its radius are the first section; the monogenic setting is quoted from *Quaternion Regular Functions*, which owns the reduced-quaternion operator, the Riesz system, the basis polynomials and their properties; then the coefficient estimate, the two Bohr inequalities, with the radii $0.125$ for $f(0)=0$ and $0.026$ in the general case, and the estimate for the hypercomplex derivative. The sibling article is *Bloch's Theorem and the Bloch Constant for Monogenic Functions*, which treats the other half of the geometric theory on the same class of functions: the Bloch radius is the size of the largest schlicht ball, while the Bohr radius is the largest ball on which the coefficient series is majorised.

## The Classical Theorem and Its Radius

**Theorem (Bohr, 1914).** Let $f(A) = \sum_{n\ge 0} a_n A^n$ be holomorphic in the unit disk with $\lvert f(A)\rvert \le 1$ there. Then

$$
\sum_{n\ge 0} \lvert a_n\rvert r^n \le 1 \qquad \text{for } 0 \le r \le \frac13,
$$

and the radius $1/3$ is optimal.

**Why the threshold is $1/3$.** The one-variable proof bounds every coefficient by the first, through the Schwarz–Pick estimate $\lvert a_n\rvert \le 1 - \lvert a_0\rvert^2$ for $n \ge 1$. Writing $t = r/(1-r)$, the sum of the moduli is then at most $\lvert a_0\rvert + (1-\lvert a_0\rvert^2)t$, whose derivative in $a_0$ vanishes at $a_0 = 1/(2t)$; that critical point is admissible, $\lvert a_0\rvert \le 1$, exactly when $t \ge 1/2$, and the maximum is then $t + 1/(4t) > 1$. For $t \le 1/2$ the maximum over the admissible interval is at $a_0 = 1$ and equals $1$. The threshold is therefore exactly $t = 1/2$, that is $r = 1/3$.

Two remarks belong here. The estimate shows that $1/3$ is the threshold of the coefficient bound, while the harder half of Bohr's theorem is that no larger radius works; both facts are classical and are quoted, not reproved. And the value $1/3$ is a one-variable accident in the sense that the several-variable theory depends on the domain, on the norm chosen for the coefficients and on whether the constant term is included; the results below show the same sensitivity in the three-dimensional non-commutative case, where the two natural readings of the theorem give radii that differ by a factor of about five.

## The Monogenic Setting

The algebra is the reduced quaternions $\mathcal{A} = \operatorname{span}_\mathbb{R}\{e_0,e_1,e_2\} \cong \mathbb{R}^3$, a real subspace of $\mathbb{H}$ closed under conjugation but not under multiplication, since $e_1e_2 = e_3$ leaves it. The reduced Cauchy–Riemann operator $D = \partial_0 + e_1\partial_1 + e_2\partial_2$ and its conjugate $\bar D = \partial_0 - e_1\partial_1 - e_2\partial_2$ satisfy $D\bar D = \bar D D = \Delta_3$; a function $f : B \to \mathcal{A}$ with $Df = 0$ is **monogenic**, and $Df = 0$ is equivalent to the **Riesz system** $\operatorname{div}F = \operatorname{curl}F = 0$ for $F = (f_0,-f_1,-f_2)$. The **hypercomplex derivative** of a monogenic $f$ is $\tfrac12\bar Df$, and a **hyperholomorphic constant** is a monogenic function that the hypercomplex derivative annihilates; the non-trivial ones take values in $\operatorname{span}_\mathbb{R}\{e_1,e_2\}$. The space of monogenic functions on the unit ball $B$ is written $\mathcal{R}^+(B;\mathcal{A})$, and the homogeneous monogenic polynomials of degree $n$ form a space $\mathcal{R}^+(B;\mathcal{A};n)$ of dimension $2n+3$. All of this, with its proofs, is owned by *Quaternion Regular Functions*.

**The basis, quoted.** The explicit homogeneous monogenic polynomials $X_n^{l,\dagger}$, $l = 0,\dots,n+1$, and $Y_n^{m,\dagger}$, $m = 1,\dots,n+1$, built from the associated Legendre functions $P_n^{l}$ and the Chebyshev polynomials $T_l$, $U_l$, form an orthogonal system in $L^2(B;\mathcal{A};\mathbb{R})$, and their normalisations $X_n^{0,\dagger,*}$, $X_n^{m,\dagger,*}$, $Y_n^{m,\dagger,*}$ an orthonormal basis of $\mathcal{R}^+(B;\mathcal{A};n)$. Every $f \in \mathcal{R}^+(B;\mathcal{A})$ has the Fourier expansion

$$
f = \sum_{n\ge 0}\Big[ X_n^{0,\dagger,*}\,a_n^0 + \sum_{m=1}^{n+1} \big( X_n^{m,\dagger,*}\,a_n^m + Y_n^{m,\dagger,*}\,b_n^m \big) \Big],
$$

with real coefficients, and it splits orthogonally as $f = f(0) + g + h$, where the **main part** $g$ is the series with $m$ running only to $n$ and $h$ is a hyperholomorphic constant expanded in $X_n^{n+1,\dagger,*}$ and $Y_n^{n+1,\dagger,*}$. Two properties of the basis are the analytic input of everything below, and both are stated in *Quaternion Regular Functions*:

| Input | Statement |
|---|---|
| Ladder | $\tfrac12\bar D X_n^{l,\dagger} = (n+l+1)X_{n-1}^{l,\dagger}$ for $0 \le l \le n$, and $\tfrac12\bar D Y_n^{m,\dagger} = (n+m+1)Y_{n-1}^{m,\dagger}$ for $1 \le m \le n$ |
| Pointwise bound | $\lvert X_n^{l,\dagger}(\tilde q)\rvert \le \tfrac12(n+1)\sqrt{\frac{(n+1+l)!}{(n+1-l)!}}\,\lvert \tilde q\rvert^n$, and the same with $Y_n^{m,\dagger}$ and $m$ |

## The Coefficient Estimate

The classical proof needs to bound every coefficient by the first. In the monogenic case there is no Schwarz–Pick estimate, and the bound is obtained instead by integrating the function against the scalar parts of the basis, which are themselves orthogonal.

**Lemma (coefficient estimate).** Let $f$ be a monogenic function with $\lvert f(\tilde q)\rvert < 1$ in $B$ such that $f(\tilde q)-f(0)$ is orthogonal to the hyperholomorphic constants in $L^2(B;\mathcal{A};\mathbb{R})$. Then each coefficient satisfies

$$
\lvert a_n^{l}\rvert \le \max_{B}\lvert \operatorname{Sc}(X_n^{l,\dagger})\rvert \, \frac{\lVert X_n^{l,\dagger}\rVert_{L^2(B;\mathcal{A};\mathbb{R})}}{\lVert \operatorname{Sc}(X_n^{l,\dagger})\rVert^2_{L^2(B)}} \, \frac{4\pi}{3}\big( \mathcal{M}_f(1) - \operatorname{Sc}f(0) \big),
$$

and the same inequality holds with $Y_n^{m,\dagger}$ and $b_n^m$; here $\mathcal{M}_f(1) = \sup_{\lvert \tilde q\rvert<1}\lvert f(\tilde q)\rvert$. In the normalised form of the source, in which $\mathcal{M}_f(1) = 1$, the last factor is written as $2\sqrt{\pi/3}\,(2\sqrt{\pi/3} - a_0^0)$.

**The two constants in the estimate.** The factor $4\pi/3$ is the volume of the unit ball and enters through the norm of the normalised constant. Its equivalent normalised form is arithmetic: $X_0^{0,\dagger} = \tfrac12$ and therefore $\lVert X_0^{0,\dagger}\rVert^2_{L^2(B)} = \tfrac14\cdot\tfrac{4\pi}{3} = \pi/3$; since the scalar part of $f$ at the origin is carried by that single basis element, $\operatorname{Sc}f(0) = \tfrac12\sqrt{3/\pi}\,a_0^0$, that is $a_0^0 = 2\sqrt{\pi/3}\,\operatorname{Sc}f(0)$. With $\mathcal{M}_f(1) = 1$ this gives

$$
2\sqrt{\frac{\pi}{3}}\Big(2\sqrt{\frac{\pi}{3}} - a_0^0\Big) = \frac{4\pi}{3}\big(1 - \operatorname{Sc}f(0)\big),
$$

so the two printed forms are the same factor. Both normalisations were recomputed here.

**The role of the orthogonality.** The hypothesis that $f - f(0)$ be orthogonal to the hyperholomorphic constants is not a technical convenience: the constants form a subspace of dimension $2$ in every degree rather than the single function $1$ of the complex case, and the estimate of a coefficient by the value at the origin fails if the constant part is not removed. This is the same obstruction that the decomposition theorem removes, and it is the reason the general statement below is made for functions orthogonal to the constants.

## The Two Monogenic Bohr Inequalities

The monogenic analogue of Bohr's theorem has two readings, which differ in where the modulus is taken. The source proves both, and the resulting radii differ by a factor of about five.

**Corollary (the case $f(0) = 0$).** Let $f$ be a square-integrable monogenic function with $f(0) = 0$ and $\lvert f(\tilde q)\rvert < 1$ in $B$. Then

$$
\sum_{n\ge 1}\Big\lvert X_n^{0,\dagger,*}\,a_n^0 + \sum_{m=1}^{n+1} \big( X_n^{m,\dagger,*}\,a_n^m + Y_n^{m,\dagger,*}\,b_n^m \big) \Big\rvert < 1
$$

in the ball $\lvert \tilde q\rvert = r < 0.125$.

The modulus is taken of the whole cluster of summands of one degree, which is the form the theorem has in the complex case and the reason the corollary is a genuine generalisation. The result improves the first quaternionic version of the theorem, in which the same inequality was asserted only for $r < 0.047$; the improvement comes from the pointwise bound of the table above.

**Theorem (the general case, summand by summand).** Let $f$ be a monogenic function such that $f(\tilde q)-f(0)$ is orthogonal to the hyperholomorphic constants, with $\lvert f(\tilde q)\rvert < 1$ in $B$. Then

$$
\sum_{n\ge 0}\Big[ \lvert X_n^{0,\dagger,*}\rvert\,\lvert a_n^0\rvert + \sum_{m=1}^{n} \big( \lvert X_n^{m,\dagger,*}\rvert\,\lvert a_n^m\rvert + \lvert Y_n^{m,\dagger,*}\rvert\,\lvert b_n^m\rvert \big) \Big] < 1
$$

in the ball of radius $r$ with $0 \le r < 0.026$.

Here the modulus is taken of every single summand, and the sum runs over the main part only, the constants being excluded by the orthogonality hypothesis and by the fact that $m$ stops at $n$. This statement refines the earlier monogenic Bohr-type theorem of the source's companion paper.

**The comparison.** In the complex case the two readings coincide, because there is one coefficient of each degree. In the reduced quaternions they do not: the first takes the modulus after summing the $2n+3$ terms of degree $n$ and gives $0.125$, the second takes the modulus before summing and gives $0.026$, about a fifth as large. Both are far below the classical $1/3$, and the loss is structural rather than the fault of the estimates. The Schwarz–Pick estimate, on which the classical threshold rests, bounds every coefficient of a bounded holomorphic function by its value at the origin; in the monogenic case the constants form a two-dimensional subspace in each degree, a non-trivial hyperholomorphic constant is $\operatorname{span}_\mathbb{R}\{e_1,e_2\}$-valued, and the coefficients to be controlled multiply as $2n+3$ per degree. The Bohr sum is therefore controlled one index at a time by the pointwise bound of the basis, and the two positions of the modulus require different estimates of the same coefficients.

The radii $0.125$, $0.026$ and the earlier $0.047$ are the results of the source. What was verified here are the inputs: the basis polynomials and their properties in all four quaternion components, and the pointwise bound, whose sharpness was checked by maximising the ratio over the directions of the sphere. The passage from the coefficient estimate to the two radii rests on the quoted estimates of the norms of the scalar parts in the companion paper and was not rebuilt.

One further observation of the source belongs with the comparison. The value obtained for the radius depends on which Fourier expansion is chosen in the proof, and therefore on which pointwise estimates of the homogeneous monogenic polynomials are available: the improvement from $0.047$ to $0.125$ came from replacing the estimates used in the earlier paper by the pointwise bound of the table above, with the same expansion. In one variable there is only one expansion to choose, and this freedom does not exist; it is a further respect in which the monogenic theory is less rigid than the classical one.

## The Estimate for the Hypercomplex Derivative

The engine of the coefficient estimate is an inequality for the hypercomplex derivative, the monogenic counterpart of the classical bounds connecting a function to its derivative. It uses the maximum modulus function, which by the maximum principle can be taken either on the sphere or in the closed ball.

**Theorem.** Let $f$ be a square-integrable monogenic function in $B$. Then for $0 \le r < 1$,

$$
\mathcal{M}\Big( \tfrac12\bar Df, r \Big) \le \frac{8(3r+1)}{(1-r)^5}\Big( \mathcal{M}_f(1) - \lvert \operatorname{Sc}f(0)\rvert \Big).
$$

**Corollary.** Let $\tilde f$ be a square-integrable monogenic function in $B$ orthogonal to the non-trivial hyperholomorphic constants. Then for $0 \le r < 1$,

$$
\mathcal{M}\Big( \tfrac12\bar D\tilde f, r \Big) \le \frac{8(3r+1)}{(1-r)^5}\Big( \mathcal{M}_{\tilde f}(1) - \lvert \tilde f(0)\rvert \Big),
$$

and $\tilde f(0)$ is real, because the orthogonality removes the $e_1$- and $e_2$-valued parts of the constant term.

**The decisive step, and its arithmetic.** The proof replaces $f$ by its main part $g$, applies the ladder to the Fourier series, estimates each term by the pointwise bound and sums, which gives

$$
\Big\lvert \tfrac12\bar Dg(\tilde q)\Big\rvert \le \frac43\big( \mathcal{M}_f(1) - \operatorname{Sc}f(0) \big) \sum_{n\ge 1} n^2(n+1)(n+2)\lvert \tilde q\rvert^{n-1}.
$$

The series is elementary. With $\lvert \tilde q\rvert = r$,

$$
\sum_{n\ge 1} n^2(n+1)(n+2)r^{n-1} = \frac{6(1+3r)}{(1-r)^5},
$$

since $n^2(n+1)(n+2) = n^4+3n^3+2n^2$ and the four Euler sums combine to $6(1+3r)/(1-r)^5$; the factor $\tfrac43$ then turns it into $8(3r+1)/(1-r)^5$ exactly. This closed form was recomputed here symbolically, term by term, so no numerical constant of the theorem is left undetermined.

**What the estimate says.** It bounds the hypercomplex derivative of a monogenic function by the supremum of the function on the ball and by the scalar part of the function at the origin, and it is the inequality that makes the Bohr sums converge to a value below one on a fixed ball. It differs in kind from the estimate of the companion Bloch article, which bounds the oscillation of the hypercomplex derivative, $\lvert \tfrac12\bar Df(\tilde q) - \tfrac12\bar Df(0)\rvert$, by the maximum modulus of the derivative itself; the present inequality bounds the derivative of $f$ by the modulus of $f$, and it is its growth factor $(1-r)^{-5}$ that the Bohr radius must absorb.

## Summary

**Bohr's theorem** says that a holomorphic function of the unit disk bounded by one satisfies $\sum_n\lvert a_n\rvert r^n \le 1$ for $r \le 1/3$, and that $1/3$ is optimal. The radius is the threshold of the Schwarz–Pick coefficient bound $\lvert a_n\rvert \le 1-\lvert a_0\rvert^2$: the maximum of $\lvert a_0\rvert + (1-\lvert a_0\rvert^2)t$ over the admissible $a_0$, with $t = r/(1-r)$, equals $1$ up to $t = 1/2$ and exceeds it afterwards, which is $r = 1/3$.

In the **reduced quaternions** the class is the monogenic functions of the Riesz system; the series is the expansion in the orthonormal system $X_n^{l,\dagger}$, $Y_n^{m,\dagger}$ of the graded pieces of dimension $2n+3$, whose ladder and pointwise bound are the analytic input, and every monogenic function splits as $f = f(0) + g + h$ into a main part and a hyperholomorphic constant. The **coefficient estimate** bounds each Fourier coefficient by the basis element carrying the scalar part at the origin, with the factor $\frac{4\pi}{3}(\mathcal{M}_f(1)-\operatorname{Sc}f(0))$, equivalently $2\sqrt{\pi/3}(2\sqrt{\pi/3}-a_0^0)$ when $\mathcal{M}_f(1)=1$.

The **two monogenic Bohr inequalities** take the modulus of a whole degree cluster and give the radius $0.125$ for $f(0)=0$, improving the earlier $0.047$, or take the modulus of every summand of the main part and give $0.026$; both are far below the classical $1/3$ because the Schwarz–Pick estimate has no analogue here, the constants being a two-dimensional subspace per degree with values in $\operatorname{span}_\mathbb{R}\{e_1,e_2\}$. The **engine** is the estimate $\mathcal{M}(\tfrac12\bar Df,r) \le \frac{8(3r+1)}{(1-r)^5}(\mathcal{M}_f(1)-\lvert\operatorname{Sc}f(0)\rvert)$, whose series $\sum_{n\ge1}n^2(n+1)(n+2)r^{n-1} = 6(1+3r)/(1-r)^5$ was verified exactly here. The basis and its properties, the pointwise bound, the two normalisation constants and the arithmetic of the derivative estimate were recomputed; the radii $0.125$, $0.026$ and $0.047$ are quoted from the source.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{A} = \operatorname{span}_\mathbb{R}\{e_0,e_1,e_2\}$ | Reduced quaternions, $\cong\mathbb{R}^3$; closed under conjugation, not a subalgebra of $\mathbb{H}$ |
| $D = \partial_0+e_1\partial_1+e_2\partial_2$, $\bar D$ | Reduced Cauchy–Riemann operator and its conjugate, $D\bar D = \bar D D = \Delta_3$ |
| $Df = 0$ | Monogenicity; equivalently the Riesz system $\operatorname{div}F = \operatorname{curl}F = 0$ |
| $\tfrac12\bar Df$ | Hypercomplex derivative of the monogenic function $f$ |
| hyperholomorphic constant | Monogenic function annihilated by $\tfrac12\bar D$; non-trivial ones are $\operatorname{span}_\mathbb{R}\{e_1,e_2\}$-valued |
| $\mathcal{R}^+(B;\mathcal{A})$, $\mathcal{R}^+(B;\mathcal{A};n)$ | Monogenic functions on the unit ball, and their homogeneous part of degree $n$, $\dim = 2n+3$ |
| $X_n^{l,\dagger}$, $Y_n^{m,\dagger}$ | Explicit homogeneous monogenic polynomials, $l = 0,\dots,n+1$, $m = 1,\dots,n+1$ |
| $X_n^{0,\dagger,*}$, $X_n^{m,\dagger,*}$, $Y_n^{m,\dagger,*}$ | Their normalisations, an orthonormal basis of $\mathcal{R}^+(B;\mathcal{A};n)$ |
| $a_n^0$, $a_n^m$, $b_n^m$ | Real Fourier coefficients of $f$ in that basis |
| $f = f(0)+g+h$ | Orthogonal decomposition into main part $g$ and hyperholomorphic constant $h$ |
| $\mathcal{M}(f,r) = \max_{\lvert \tilde q\rvert=r}\lvert f(\tilde q)\rvert$ | Maximum modulus function |
| $\mathcal{M}_f(r) = \sup_{\lvert\xi\rvert<r}\lvert f(\xi)\rvert$ | Supremum over the ball; equal to $\mathcal{M}(f,r)$ by the maximum principle |
| $P_n^{l}$, $T_l$, $U_l$ | Associated Legendre function with $P_n^{l} = 0$ for $l \ge n+1$; Chebyshev polynomials of the first and second kinds |
| $1/3$ | The classical Bohr radius, optimal |
| $0.125$ | Monogenic radius, case $f(0) = 0$, modulus of each degree cluster |
| $0.026$ | Monogenic radius, general case, modulus of each summand of the main part |
| $0.047$ | The earlier monogenic radius, improved to $0.125$ |
| $\frac{4\pi}{3}\big(\mathcal{M}_f(1)-\operatorname{Sc}f(0)\big)$ | Coefficient-estimate factor, equivalently $2\sqrt{\pi/3}(2\sqrt{\pi/3}-a_0^0)$ |
| $\frac{8(3r+1)}{(1-r)^5}$ | Constant of the hypercomplex-derivative estimate, from $\frac43\sum_{n\ge1}n^2(n+1)(n+2)r^{n-1}$ |

## Further Reading

- K. Gürlebeck and J. Morais, "On the development of Bohr's phenomenon in the context of Quaternionic analysis and related problems", in *Proceedings of the 17th International Conference on Finite or Infinite Dimensional Complex Analysis and Applications*, Ho Chi Minh City (2009), arXiv:1004.1188 [math.CV], the source of this article: the basis and its properties, the pointwise bound, the coefficient estimate, the two Bohr inequalities with the radii $0.125$ and $0.026$, and the estimate for the hypercomplex derivative. The basis, its properties, the pointwise bound and the arithmetic of the derivative estimate were recomputed here; the radii are quoted.
- K. Gürlebeck and J. Morais, "Bohr type theorems for monogenic power series", *Computational Methods and Function Theory* **9** (2011) 633–651, for the general-case Bohr type theorem that the Theorem above refines, for the decomposition of a monogenic function, and for the estimates of the norms of the scalar parts that the passage from coefficients to radii uses.
- K. Gürlebeck and J. Morais, "Bohr's theorem for monogenic functions", *AIP Conference Proceedings* **936** (2007) 750–753, for the first quaternionic Bohr result, with the radius $0.047$ that the Corollary improves.
- J. Morais, *Approximation by Homogeneous Polynomial Solutions of the Riesz System in $\mathbb{R}^3$*, Ph.D. dissertation, Bauhaus-Universität Weimar (2009), for the construction of the orthonormal system of monogenic polynomials and the complete list of its properties.
- K. Gürlebeck and H. Malonek, "A hypercomplex derivative of monogenic functions in $\mathbb{R}^{n+1}$ and its applications", *Complex Variables and Elliptic Equations* **39** (1999) 199–228, for the hypercomplex derivative, the primitive and the role of the hyperholomorphic constants.
- H. Leutwiler, "Quaternionic analysis in $\mathbb{R}^3$ versus its hyperbolic modification", in *Clifford Analysis and Its Applications*, NATO Science Series II **25** (Kluwer, 2001) 193–211, for the Riesz system and the dimension $2n+3$ of the polynomial solutions of fixed degree.
- M. Riesz, *Clifford Numbers and Spinors*, Lecture Series 38, Institute for Physical Science and Technology, University of Maryland (1958), for the system that carries his name.
- H. Bohr, "A theorem concerning power series", *Proceedings of the London Mathematical Society* **13** (1914) 1–5, for the classical theorem and the optimal radius $1/3$.
- H. S. Boas and D. Khavinson, "Bohr's power series theorem in several variables", *Proceedings of the American Mathematical Society* **125** (1997) 2975–2979; L. Aizenberg, "Multidimensional analogues of Bohr's theorem on power series", *Proceedings of the American Mathematical Society* **128** (2000) 1147–1155; S. Dineen and R. Timoney, "On a problem of H. Bohr", *Bulletin de la Société Royale des Sciences de Liège* **60** (1991) 401–404; V. I. Paulsen, G. Popescu and D. Singh, "On Bohr's inequality", *Proceedings of the London Mathematical Society* **85** (2002) 493–512, for the several-variable developments in which the quaternionic results sit.
