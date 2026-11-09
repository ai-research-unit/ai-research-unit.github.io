# __The Inverse Fourier Transform of a Symbol__

## Introduction

This article computes the inverse Fourier transform of the reciprocal of a symbol, and reads three things off it: where its poles are, how fast it grows, and how many zeros of the symbol produce them. The object is therefore not the symbol itself but the kernel attached to it, $\kappa_\sigma=\mathcal{F}^{-1}[\sigma^{-1}]$, which is the operator that carries a datum to a solution of the equation.

**The setting.** Let $A$ be a finite-dimensional real algebra with unit, of dimension $d$, and let $A_{\mathbb{C}}=A\otimes_{\mathbb{R}}\mathbb{C}$ be its complexification. Let $\sigma:\mathbb{R}^n\to A_{\mathbb{C}}$ be the symbol of a constant-coefficient operator $P(D)=\sum_{\lvert\alpha\rvert\le m}a_\alpha\partial^\alpha$ of order $m$, so that $\sigma(\zeta)=\sum a_\alpha(i\zeta)^\alpha$; the symbol of $P$ is written $\sigma_P$ when the operator has to be named. The Fourier transform is the one of *The Fourier Transform and the Symbol of a Differential Operator*,

$$
\mathcal{F}[u](\zeta)=\int_{\mathbb{R}^n}e^{-i\zeta\cdot x}\,u(x)\,dx ,
$$

the exponential a scalar and the integration entrywise, so that $\mathcal{F}[u]$ is $A_{\mathbb{C}}$-valued; the inverse transform carries the constant $(2\pi)^{-n}$,

$$
\mathcal{F}^{-1}[v](x)=(2\pi)^{-n}\int_{\mathbb{R}^n}e^{i\zeta\cdot x}\,v(\zeta)\,d\zeta .
$$

**The three regimes.** The reciprocal $\sigma^{-1}$ is defined at a frequency exactly when $\sigma(\zeta)$ is a unit, and there are three cases. If $\sigma$ is a unit everywhere and $\lVert L_{\sigma(\zeta)^{-1}}\rVert$ is bounded on $\mathbb{R}^n$, the reciprocal is a bounded multiplier and the solution obeys an $L^2$ bound with no constant in it beyond the sup of the multiplier. If $\sigma$ is a unit everywhere but the reciprocal grows polynomially, the multiplier is tempered and the solution exists in the space of tempered distributions, with a loss of smoothness read from the growth. If the symbol is not a unit somewhere, the reciprocal is defined off the zero set, is unbounded near it, and the product $\sigma^{-1}\mathcal{F}[f]$ is a division problem; that is the case this article is about, and its three themes — poles, growth, counting — live there.

**The status of the five results.** The adjugate description of the reciprocal, and with it the order of the pole at a point of the zero set, is proved here from scratch; it is the article's own contribution and it is complete. The Plancherel identity is proved here for $A_{\mathbb{C}}$-valued functions by reduction to the scalar identity of *Real and Complex Analysis* of Rudin, which is quoted with its constant. The Paley–Wiener correspondence between the support of a function and the exponential type of its transform is proved in the direction that needs nothing but the integral, and in the converse direction under the translate estimate that belongs to the theorem itself; that estimate is quoted, and the reduction from the scalar case to the $A_{\mathbb{C}}$-valued case is proved here. The growth rate that a pole forces on the kernel is proved in one frequency variable; in $n\ge2$ it is labelled *programme*, because the zero set is then a hypersurface and there is no isolated pole to take a residue at. The stationary phase asymptotics are quoted from Hörmander with their hypotheses and applied in one model case; the degenerate case is left open. The argument principle is quoted from Ahlfors in the scalar form, and the section that uses it says plainly why it does not transfer.

**Boundaries.** The general inversion theory, the transform of a general tempered distribution and the two-sided inversion formula are *The Fourier Operator*; the symbol, its zero set and the rank on it are *The Fourier Transform and the Symbol of a Differential Operator*; the distributional reading of the transform is *Distributions and Fundamental Solutions*; the global equation $P(D)u=f$ on $\mathbb{R}^n$ is *The Fundamental Solution Operator*. This article takes all four as given, and adds only the analysis of one object, the kernel of the reciprocal of the symbol. Nothing here is about variable coefficients.

**The trap, stated at once.** Three integers are in play and they are different. The order of the operator is $m$. The degree of $\det L_\sigma$ is $dm$, by the proposition of *The Fourier Transform and the Symbol of a Differential Operator*. The order of the pole of the reciprocal at a point of the zero set is a third number, $k$, which is at least one and at most $dm$, and which is usually neither of the other two. **The pole order is not the order of the operator, and it is not the degree of the symbol.** The whole of §*The Reciprocal as an Adjugate* is the separation of the three.

## The Multiplier and the Inverse Integral

**Definition (the multiplier and its kernel).** Let $\Omega\subseteq\mathbb{R}^n$ be the open set on which $\sigma$ is a unit. The **reciprocal multiplier** is the $A_{\mathbb{C}}$-valued function $m_\sigma(\zeta)=\sigma(\zeta)^{-1}$ on $\Omega$, and the **kernel of the symbol** is its inverse transform,

$$
\kappa_\sigma=\mathcal{F}^{-1}\big[m_\sigma\big],
$$

read on $\Omega$ as a function and on $\mathbb{R}^n$ as a distribution.

**Proposition (the transform of a solution).** Let $f$ be $A_{\mathbb{C}}$-valued and of compact support, and suppose $\mathcal{F}[P(D)u]=\mathcal{F}[f]$ holds with $\mathcal{F}[u]$ supported in $\Omega$. Then

$$
\mathcal{F}[u](\zeta)=\sigma(\zeta)^{-1}\,\mathcal{F}[f](\zeta)
$$

at every $\zeta\in\Omega$.

*Proof.* By the theorem of *The Fourier Transform and the Symbol of a Differential Operator*, $\mathcal{F}[P(D)u](\zeta)=L_{\sigma(\zeta)}\mathcal{F}[u](\zeta)$; the hypothesis identifies this with $\mathcal{F}[f](\zeta)$; and on $\Omega$ the map $L_{\sigma(\zeta)}$ is invertible, with inverse $L_{\sigma(\zeta)^{-1}}$. Applying the inverse to both sides gives the formula.

**The inversion integral.** The proposition is a statement about transforms, and it becomes a statement about functions only after the inversion is carried out,

$$
u(x)=(2\pi)^{-n}\int_{\mathbb{R}^n}e^{i\zeta\cdot x}\,\sigma(\zeta)^{-1}\,\mathcal{F}[f](\zeta)\,d\zeta .
$$

That integral is the object of the article. Three questions decide whether it means anything, and they are the three the article answers in order: whether the integrand is integrable or only a distribution, which is the question of the poles; how fast the result can grow as $\lvert x\rvert\to\infty$, which is the question of the exponential type; and how many points of the singular set a curve meets, which is the question of the counting.

**The complexification.** The zero set $Z(P)$ is a subset of $\mathbb{R}^n$, and it is the trace on the real frequencies of a complex object. Extend $\sigma$ to a polynomial on $\mathbb{C}^n$ by the same formula, with $\zeta$ now complex and the powers read in $A_{\mathbb{C}}$; the extension is holomorphic, and it is again written $\sigma$. Then

$$
Z(P)=\mathbb{R}^n\cap\{\zeta\in\mathbb{C}^n:\det L_{\sigma(\zeta)}=0\}.
$$

The set on the right is the zero set of one holomorphic function, hence a hypersurface of $\mathbb{C}^n$ when that function is not identically zero, and it is on that hypersurface that the reciprocal has its singularities. **The real problem sees only the trace; the poles live on the hypersurface.** That sentence is the reason the rest of the article works in $\mathbb{C}^n$ and returns to $\mathbb{R}^n$ only to state what is seen there.

**Remark (what the three regimes look like in the complex picture).** In the first regime the hypersurface misses the real subspace entirely and $\det L_\sigma$ is bounded away from zero there. In the second it meets the real subspace only at infinity. In the third it meets the real subspace, and the intersection is exactly the set where the equation has no solution at that frequency.

## Paley–Wiener: Support against Exponential Type

**Definition (exponential type).** An entire $A_{\mathbb{C}}$-valued function $F$ on $\mathbb{C}^n$ is of **exponential type at most** $R$ when for every $\varepsilon>0$ there is $C_\varepsilon$ with

$$
\lvert F(\zeta)\rvert\le C_\varepsilon\,e^{(R+\varepsilon)\lvert\zeta\rvert}
$$

for all $\zeta\in\mathbb{C}^n$, the modulus on the left being any fixed norm on $A_{\mathbb{C}}$ and $\lvert\zeta\rvert$ the Euclidean modulus on $\mathbb{C}^n$. The **type** $\tau(F)$ is the infimum of the admissible $R$. Write $K_R=\{x\in\mathbb{R}^n:\lvert x\rvert\le R\}$ for the closed ball.

**Proposition (support gives type).** Let $u:\mathbb{R}^n\to A_{\mathbb{C}}$ be integrable with support in $K_R$. Then $\mathcal{F}[u]$ extends to an entire $A_{\mathbb{C}}$-valued function, and

$$
\lvert\mathcal{F}[u](\zeta)\rvert\le\lVert u\rVert_1\,e^{R\lvert\operatorname{Im}\zeta\rvert}
$$

for every $\zeta\in\mathbb{C}^n$. In particular $\tau(\mathcal{F}[u])\le R$.

*Proof.* The integral $\int e^{-i\zeta\cdot x}u(x)\,dx$ converges for complex $\zeta$, because $\lvert e^{-i\zeta\cdot x}\rvert=e^{\langle\operatorname{Im}\zeta,x\rangle}$ and $\operatorname{supp}u\subseteq K_R$ gives $\langle\operatorname{Im}\zeta,x\rangle\le R\lvert\operatorname{Im}\zeta\rvert$ by the Cauchy–Schwarz inequality. Differentiation under the integral is legitimate for the same reason, on compact sets of $\zeta$, and gives an entire function. The bound is the bound on the integrand times the measure of the support.

**Proposition (type gives support).** Let $u$ be a tempered $A_{\mathbb{C}}$-valued distribution whose transform extends to an entire function of exponential type at most $R$, and suppose that transform is a Schwartz function on $\mathbb{R}^n$. Then $\operatorname{supp}u\subseteq K_R$.

*Proof.* Let $x_0\notin K_R$, put $\varrho=\lvert x_0\rvert$ and $\nu=x_0/\varrho$, and choose $\delta>0$ with $\varrho-\delta>R$. Let $\varphi\in C_c^\infty$ be supported in the ball of radius $\delta$ about $x_0$. Since $\mathcal{F}[u]$ is a Schwartz function, $u$ is a Schwartz function and the pairing is an integral,

$$
\langle u,\varphi\rangle=(2\pi)^{-n}\int_{\mathbb{R}^n}\mathcal{F}[u](\xi)\,\overline{\mathcal{F}[\varphi](\xi)}\,d\xi ,
$$

which is the distributional form of the Plancherel identity of §*Plancherel with the Constant*. Both factors are entire, so the integration can be moved to the translate $\xi\mapsto\xi+i\tau\nu$ with $\tau>0$; the shift is the classical step of the Paley–Wiener theorem, and it uses the translate estimate $\int\lvert F(\xi+i\tau\nu)\rvert\,d\xi\le C e^{R\tau}$ for an entire function $F$ of exponential type at most $R$. That estimate is quoted with the theorem and is not reproved here. On the translate the two bounds are

$$
\lvert\mathcal{F}[u](\xi+i\tau\nu)\rvert\le C\,(1+\lvert\xi\rvert)^{N}e^{R\tau},
\qquad
\lvert\mathcal{F}[\varphi](\xi+i\tau\nu)\rvert\le\lVert\varphi\rVert_1\,e^{\tau(\nu\cdot x_0+\delta)} ,
$$

the first from the exponential type and the polynomial growth, the second from the support of $\varphi$ and the estimate of the previous proposition. The product is bounded by a constant times $(1+\lvert\xi\rvert)^{N}e^{-\tau(\varrho-\delta-R)}$, which decays in $\xi$ and tends to zero as $\tau\to\infty$ for fixed $\xi$. Letting $\tau\to\infty$ gives $\langle u,\varphi\rangle=0$. Every $\varphi$ supported outside $K_R$ is a locally finite sum of such functions, by a partition of unity subordinate to a cover by balls of radius $\delta$, so $u$ vanishes there.

**Remark (the two propositions together).** They say that the support radius and the exponential type are the same number, read from two sides. The passage from the scalar case to $A_{\mathbb{C}}$-valued functions costs nothing: the estimates above are entrywise in a basis of $A_{\mathbb{C}}$ over $\mathbb{C}$, and the modulus of an element is comparable to the maximum of the moduli of its coordinates. What the two propositions do not settle in the generality stated is the tempered case without the Schwartz hypothesis; that is the Paley–Wiener theorem in the form given by Hörmander, and it is quoted, not proved here.

**Corollary (when a solution operator has finite reach).** The kernel $\kappa_\sigma$ is supported in $K_R$ exactly when $m_\sigma$ is entire of exponential type at most $R$. Hence the reach of the solution operator is a property of the reciprocal multiplier alone: it is finite exactly when the singularities of the reciprocal are absent from the whole of $\mathbb{C}^n$, that is, exactly when the reciprocal is entire.

**Example (an entire reciprocal with compact support).** Let $\chi\in C_c^\infty$ be supported in $K_R$ and nowhere zero there, and take $m_\sigma=\mathcal{F}[\chi]$, which is entire of type $R$ by the first proposition. Then $\kappa_\sigma=\chi$ by the inversion formula, and the reach is exactly $R$. An entire multiplier of finite type is the same thing as a compactly supported kernel.

**Remark (a polynomial symbol never has finite reach).** If $\sigma$ is a polynomial of positive degree, then $m_\sigma=1/\sigma$ has poles and is not entire, so $\kappa_\sigma$ is not compactly supported, whatever the algebra and whatever the order. **A constant-coefficient operator of positive order has a kernel of infinite reach.** The statement is about the reciprocal and not about the equation: it says that the value of the solution at a point depends on the datum everywhere, and it is the exact sense in which the constant-coefficient problem is global.

## Plancherel with the Constant

**The scalar identity, quoted.** For $f\in L^1\cap L^2(\mathbb{R}^n;\mathbb{C})$ the transform lies in $L^2$ and

$$
\lVert\mathcal{F}[f]\rVert_2^2=(2\pi)^n\lVert f\rVert_2^2 ,
$$

which is the Plancherel theorem in the normalisation with $e^{-i\zeta\cdot x}$ in the kernel and no $2\pi$ in the exponent. The identity is quoted from *Real and Complex Analysis* of Rudin, where the constant is computed in this normalisation.

**Theorem (the $A_{\mathbb{C}}$-valued identity).** Let $f\in L^1\cap L^2(\mathbb{R}^n;A_{\mathbb{C}})$. Then $\mathcal{F}[f]\in L^2(\mathbb{R}^n;A_{\mathbb{C}})$ and

$$
\lVert\mathcal{F}[f]\rVert_2^2=(2\pi)^n\lVert f\rVert_2^2 ,
$$

for any Hermitian inner product on $A_{\mathbb{C}}$ used to form the two norms.

*Proof.* Choose a complex basis $e_1,\dots,e_d$ of $A_{\mathbb{C}}$ and write $f=\sum_j f_j e_j$ with scalar $f_j$. The transform is entrywise, so $\mathcal{F}[f]=\sum_j\mathcal{F}[f_j]e_j$. Expanding the squared norm of the right side gives $\sum_{j,k}g_{jk}\int\mathcal{F}[f_j]\overline{\mathcal{F}[f_k]}$, where $g_{jk}$ are the entries of the Gram matrix of the inner product. Each scalar Plancherel identity reads $\int\mathcal{F}[f_j]\overline{\mathcal{F}[f_k]}=(2\pi)^n\int f_j\overline{f_k}$, and the same is true of the pair in the other order, so the cross terms are $(2\pi)^n$ times the corresponding cross terms of $\lVert f\rVert_2^2$. Summing with the weights $g_{jk}$ gives the identity. The constant does not depend on the basis, nor on the inner product, because both sides are computed with the same weights.

**Corollary (the unitary normalisation).** The operator $\mathcal{U}=(2\pi)^{-n/2}\mathcal{F}$ is an isometry of $L^2(\mathbb{R}^n;A_{\mathbb{C}})$ onto itself, and it extends from $L^1\cap L^2$ to the whole of $L^2$ by continuity. The constant $(2\pi)^{n/2}$ is exactly what the inversion formula carries, and it is the whole content of the phrase "unitary up to a constant".

**Corollary (the stability bound, with the constants cancelled).** Suppose $\sigma$ is a unit everywhere and $M=\sup_{\zeta}\lVert L_{\sigma(\zeta)^{-1}}\rVert<\infty$, the norm on the right being the operator norm on $A_{\mathbb{C}}$. Then the solution of the transformed equation obeys

$$
\lVert u\rVert_2\le M\,\lVert f\rVert_2 .
$$

*Proof.* From the proposition of §*The Multiplier and the Inverse Integral*, $\mathcal{F}[u]=m_\sigma\mathcal{F}[f]$; taking $L^2$ norms and using $\lVert m_\sigma v\rVert\le M\lVert v\rVert$ pointwise gives $\lVert\mathcal{F}[u]\rVert_2\le M\lVert\mathcal{F}[f]\rVert_2$; and by the theorem twice, with the same constant on both sides, $\lVert u\rVert_2\le M\lVert f\rVert_2$. **The $(2\pi)$ factors cancel, and this is the reason the Plancherel constant has to be got right rather than absorbed into a symbol.**

**Remark (what the bound does and does not say).** It is sharp for a constant scalar symbol, where equality holds. It says nothing when $M$ is infinite, which is the third regime, and nothing about smoothness, which is controlled by the growth of $m_\sigma$ at infinity and not by its size: how large the multiplier is and how fast it grows are separate questions, and only the first is about the zero set.

## The Reciprocal as an Adjugate

### The element

**Proposition (the reciprocal is an adjugate over a determinant).** Let $a\in A_{\mathbb{C}}$ be a unit. Then

$$
L_{a^{-1}}=(\det L_a)^{-1}\operatorname{adj}(L_a),
$$

where $\operatorname{adj}$ is the adjugate of the matrix of $L_a$ in a basis of $A_{\mathbb{C}}$ over $\mathbb{C}$ that comes from a real basis of $A$, and the right side is read as a linear map of $A_{\mathbb{C}}$ into itself.

*Proof.* The identity $L_a\operatorname{adj}(L_a)=\det(L_a)\operatorname{id}$ holds for the matrix of any endomorphism, and $L_a$ is invertible exactly when $\det L_a\ne0$. Multiplying by $L_a^{-1}=L_{a^{-1}}$ on the left gives the formula. The adjugate of a matrix is polynomial in the entries, and the entries of the matrix of $L_a$ are linear in $a$, so the numerator is polynomial in $a$ of degree $d-1$ in each entry.

### The symbol

**Corollary (the pole order is the order of the zero of the determinant).** Let $\zeta_0\in\mathbb{C}^n$ and let $k$ be the order of vanishing of $\det L_\sigma$ at $\zeta_0$ along a complex line through $\zeta_0$. Then every entry of the matrix of $L_{\sigma(\zeta)^{-1}}$ has a pole of order at most $k$ at $\zeta_0$ along that line, and the order is exactly $k$ at those $\zeta_0$ where some $(d-1)\times(d-1)$ minor of $L_{\sigma(\zeta_0)}$ does not vanish.

*Proof.* The entries of $L_{\sigma^{-1}}$ are the entries of the adjugate divided by $\det L_\sigma$, by the proposition. The adjugate is polynomial in the entries of $L_\sigma$, hence holomorphic in $\zeta$, so its entries are bounded near $\zeta_0$ and the pole order is at most the order of the denominator. If a minor of size $d-1$ does not vanish at $\zeta_0$, the corresponding entry of the adjugate does not vanish there, and the order is exactly $k$.

**Corollary (the range of $k$).** At a point of the complex zero set, $1\le k\le dm$, and both ends occur. The upper end is the degree of $\det L_\sigma$; the lower end is the generic value, since $\det L_\sigma$ vanishes to first order at a smooth point of its zero hypersurface.

**Remark (three integers, and only one of them is a pole order).** The order of the operator is $m$; the degree of $\det L_\sigma$ is $dm$; the order of the pole at a point is $k$. In the scalar case $d=1$ the last two are bounded by $m$, but they are still different numbers, and the difference is the whole content of the distinction. Take $\sigma(\zeta_1)=\zeta_1^2-1$. Here $m=2$, and the reciprocal has two simple poles, so $k=1$ at each. Take $\sigma(\zeta_1)=(\zeta_1-1)^2$. Here $m=2$ again, and the reciprocal has one pole of order $k=2$. **The same order of operator, the same degree of symbol, and two different pole orders.** A count of poles is not a count of degrees, and neither is a bound on the size of the reciprocal.

**Remark (the multiplicity added by the regular representation).** For $A=M_r(\mathbb{R})$ the determinant is $\det L_\sigma=(\det\sigma)^{r}$, by the proposition of *The Fourier Transform and the Symbol of a Differential Operator*. If $\det\sigma$ vanishes to order $j$ at a point, then $\det L_\sigma$ vanishes to order $rj$, and the pole of the reciprocal has order $rj$ at a point where the adjugate survives. The factor $r$ is the multiplicity that the left regular representation adds to the vanishing of the reduced norm; it is the exponent of the determinant, and it is not the order of any operator. **The pole order is the multiplicity of the factor in $\det L_\sigma$, and $\det L_\sigma$ is a power of the reduced norm in the matrix case.** In a division algebra the determinant is a power of the norm and the same sentence holds with the norm in place of $\det\sigma$.

**Remark (what a pole of the reciprocal is, when the reciprocal does not exist).** At a point of the zero set the element $\sigma(\zeta)$ has no inverse, so "the pole of $\sigma^{-1}$" cannot mean a pole of an algebra-valued function. It means a pole of the entries of the inverse of the regular matrix, which is what the proposition describes and what the inversion integral needs: the element fails to exist at the point, while the regular inverse blows up there at a definite order, and the order is what the growth of the kernel reads.

## The Growth Rate a Pole Forces

**The one-variable case, in full.** Let $n=1$, let $\sigma$ be a monic polynomial of degree $m\ge1$ with distinct complex zeros $\zeta_1,\dots,\zeta_m$, and write $\zeta_j=\xi_j+i\eta_j$ with $\xi_j,\eta_j$ real. The reciprocal has the partial fraction expansion

$$
\frac{1}{\sigma(\zeta)}=\sum_{j=1}^{m}\frac{c_j}{\zeta-\zeta_j},
\qquad
c_j=\prod_{l\ne j}\frac{1}{\zeta_j-\zeta_l},
$$

the numerators being constants since the degree of the denominator is larger. Each term has a single pole, and the inverse transform of a single term is an elementary contour integral.

**Proposition (the kernel of a rational symbol).** With the notation above, and with $\theta$ the function equal to one on $(0,\infty)$ and to zero on $(-\infty,0)$,

$$
\kappa_\sigma(x)=i\sum_{\eta_j>0}c_j\,e^{i\zeta_jx}\,\theta(x)\;-\;i\sum_{\eta_j<0}c_j\,e^{i\zeta_jx}\,\theta(-x),
$$

and consequently

$$
\lvert\kappa_\sigma(x)\rvert\le\sum_{j=1}^{m}\lvert c_j\rvert\,e^{\lvert\eta_j\rvert\,\lvert x\rvert}.
$$

*Proof.* By linearity it is enough to treat $1/(\zeta-\zeta_0)$ with $\zeta_0=\xi_0+i\eta_0$ and $\eta_0>0$. For $x>0$ close the contour in the upper half-plane, where the exponential $e^{i\zeta x}$ decays; the residue at $\zeta_0$ gives $2\pi i\,e^{i\zeta_0x}$, and the factor $(2\pi)^{-1}$ of the inverse transform leaves $i\,e^{i\zeta_0x}$. For $x<0$ close in the lower half-plane, which contains no pole, and the integral vanishes. The case $\eta_0<0$ is the same with the two half-planes exchanged and the orientation reversed, which is the minus sign in the second sum. The bound follows from $\lvert e^{i\zeta_jx}\rvert=e^{-\eta_jx}$ on the half-line where the term lives.

**Corollary (the growth rate is the distance of the zeros from the real axis).** The exponential type of $\kappa_\sigma$ is $\max_j\lvert\eta_j\rvert$, and it is attained. If every zero is real, $\kappa_\sigma$ grows at most like a polynomial in $\lvert x\rvert$, of degree one less than the largest multiplicity of a real zero. If every zero is real and simple, $\kappa_\sigma$ is bounded.

*Proof.* The bound of the proposition gives the upper estimate with $R=\max_j\lvert\eta_j\rvert$. For the attainment, let $\eta_J$ be maximal in modulus. On its half-line the term is $\lvert c_J\rvert e^{\lvert\eta_J\rvert\lvert x\rvert}$ in modulus, with $\lvert c_J\rvert\ne0$; the other terms either have a strictly smaller rate or, at the same rate, a different frequency or a polynomial factor, and neither can cancel an exponential. If all $\eta_j$ vanish, the expansion runs over the powers $(\zeta-\zeta_j)^{-l}$ for $l$ up to the multiplicity, and the inverse transform of such a power is, up to a constant, a step multiplied by $x^{l-1}$; the growth is then polynomial of degree one less than the largest multiplicity.

**Two examples, one degree, two behaviours.** Take $\sigma(\zeta)=\zeta^2+1$. The zeros are $\pm i$, at distance one from the real axis, and the kernel is $\kappa_\sigma(x)=\tfrac12e^{-\lvert x\rvert}$, of type one. The solution of the corresponding equation is therefore a convolution with a kernel that decays at the rate the distance prescribes. Take $\sigma(\zeta)=\zeta^2$. The only zero is $0$, of multiplicity two and on the real axis, and the kernel is $-\tfrac12\lvert x\rvert$, which grows linearly; the integral diverges at the pole and the kernel is the finite part, which is why a zero on the axis produces polynomial growth rather than an exponential. A double real zero produces growth of degree one, and an equation whose solutions grow linearly in the absence of a datum of matching size.

**The dictionary.** The corollary is a table, and the table is the content of this section.

| Zeros of $\sigma$ | Kernel $\kappa_\sigma$ | Growth |
|---|---|---|
| all real and simple | bounded, oscillatory | none |
| all real, a zero of multiplicity $j$ | $\lvert x\rvert^{j-1}$ times a bounded factor | polynomial of degree $j-1$ |
| a zero at distance $\eta$ from the axis | exponential on one half-line | rate $\lvert\eta\rvert$ |

**Remark (two types, two variables).** The reach of the kernel and the exponential type of the multiplier are one number, read by the two propositions of §*Paley–Wiener*, and it exists only when the reciprocal is entire. The growth rate of the kernel is a different quantity: it exists for every rational symbol, it is the distance of the zeros from the real axis, and no compact support is involved. **A polynomial symbol of positive order has an infinite reach and a finite growth rate**, and the two statements are consistent because the growth rate is read from the singularities of the multiplier and the reach from their absence.

**The case $n\ge2$: a programme.** In two or more frequency variables the argument above fails at its first step. The zero set of $\det L_\sigma$ in $\mathbb{C}^n$ is a hypersurface and not a finite set, so there is no isolated pole, no partial fraction expansion, and no residue at a point. What survives is the type estimate, which needs only the entire extension and is the content of §*Paley–Wiener*, and the local order of the pole along a normal line, which is the content of §*The Reciprocal as an Adjugate*. What is missing is a formula for the kernel as a sum of contributions of the hypersurface, and two routes to it are known: the residue currents of Coleff–Herrera and their analytic continuation by Andersson and Wulcan, and the Leray form integrated over a real cycle of dimension $2n-1$ that links the hypersurface. **This is a programme and not a theorem.** The case in which the real zero set has codimension two rather than one is the case of the biquaternion algebra; *Biquaternion Continuous Harmonic Analysis* gives the kernel there, and *Inversion of the Biquaternion Fourier Transform: Poles, Tails and the Degenerate Set* develops the residues, with the warning that the normal direction is then not a single variable.

## Counting: the Argument Principle and Why It Fails Here

### The quoted scalar principle

**The scalar principle, quoted.** Let $\sigma$ be holomorphic on and inside a simple closed contour $\gamma$ in $\mathbb{C}$, with no zeros on $\gamma$. Then

$$
\frac{1}{2\pi i}\oint_\gamma\frac{\sigma'(\zeta)}{\sigma(\zeta)}\,d\zeta
$$

is the number of zeros of $\sigma$ inside $\gamma$, each counted with its multiplicity. This is the argument principle, quoted from *Complex Analysis* of Ahlfors, where it is proved from the argument function of $\log\sigma$ along the contour.

**Corollary (the count for a polynomial of degree $m$).** For a monic $\sigma$ of degree $m$ and a contour enclosing all of its zeros, the integral equals $m$. The number of zeros is therefore exactly the degree, and the argument principle computes it without locating them; the location is what the growth rate of §*The Growth Rate a Pole Forces* reads instead.

### The algebra case

Jacobi's formula for the derivative of a determinant gives

$$
\frac{d}{d\zeta}\log\det L_{\sigma(\zeta)}=\operatorname{tr}\big(L_{\sigma(\zeta)^{-1}}\,L_{\sigma'(\zeta)}\big)
$$

at every point where $\sigma$ is a unit, so the logarithmic derivative of the determinant is a trace and the argument principle applies to $\det L_\sigma$ along a contour. It counts the zeros of the determinant, with multiplicity, inside the contour.

**Proposition (the count on a generic complex line).** Let $\sigma$ have degree $m$ and let $\zeta=\zeta_0+\lambda v$ with $v\in\mathbb{C}^n$ be a complex line. Then the restriction of $\det L_\sigma$ to the line is a polynomial in $\lambda$ of degree at most $dm$, of degree exactly $dm$ for all $v$ outside a proper algebraic subset of $\mathbb{C}^n$, and it has $dm$ zeros counted with multiplicity.

*Proof.* The determinant is a polynomial of degree $dm$ in $\zeta$, by the proposition of *The Fourier Transform and the Symbol of a Differential Operator*; substituting an affine line gives a polynomial in $\lambda$ of degree at most $dm$, and its top coefficient is the value at $v$ of the top-degree homogeneous part of $\det L_\sigma$, which is a nonzero polynomial in $v$ and therefore vanishes only on a proper algebraic subset. For the remaining $v$ the degree is $dm$, and the fundamental theorem of algebra gives $dm$ zeros with multiplicity.

**Why the count is not a count of obstructions.** The proposition is true and it is not the theorem one wants, for four reasons, and they are the four the section is for.

- The zeros are points of $\mathbb{C}^n$ on a chosen complex line, not points of $\mathbb{R}^n$. For a matrix or split algebra the real zero set is a hypersurface of $\mathbb{R}^n$, by the classification of the shapes in *The Fourier Transform and the Symbol of a Differential Operator*; it is a set of real dimension $n-1$ and not a finite set, and a line meets it in points that are not the obstruction itself.
- The count $dm$ is a count with multiplicity along a line, so it does not distinguish a simple zero from a multiple one, and it does not see the rank at the zero. Two symbols with the same determinant have the same count and different kernels, because the kernel depends on the adjugate and the count does not.
- The contour can be moved inside the domain of holomorphy without changing the count, so the count is a property of the complexified symbol; the real problem is the trace, and the trace is not invariant under that motion.
- Rouché's theorem compares $\sigma$ with a perturbation on the contour and concludes equality of the counts. The comparison needs a lower bound for the perturbing term, and in the algebra case the only available bound is on $\lvert\det L_\sigma\rvert$; but a lower bound for a determinant is not a lower bound for the inverse, since the inverse is the adjugate divided by the determinant and the adjugate can be large exactly where the determinant is small. **The quantity that decides convergence, the supremum of $\lVert L_{\sigma^{-1}}\rVert$, is not controlled by the infimum of $\lvert\det L_\sigma\rvert$**, which is why the Rouché argument has no algebra analogue.

**Remark (a zero divisor is not a small element).** The last point has a name in the algebra: an element can satisfy $\det L_a=0$ while being far from zero, since the determinant is a polynomial of degree $d$ and its vanishing is one equation. **The vanishing of the determinant is not a statement about the size of the element, and no perturbation argument that treats it as one can be correct.** This is the precise failure of the scalar intuition, and it is the reason the counting in the algebra case is done by degree and not by perturbation.

## Stationary Phase as the Local Reading

**The theorem, quoted.** Let $\varphi:\mathbb{R}^n\to\mathbb{R}$ be smooth and real-valued, let $a\in C_c^\infty(\mathbb{R}^n)$, and suppose $\varphi$ has exactly one critical point $x_0$ in the support of $a$, with $\varphi'(x_0)=0$ and $\varphi''(x_0)$ nonsingular. Then, as $\lambda\to+\infty$,

$$
\int_{\mathbb{R}^n}e^{i\lambda\varphi(x)}a(x)\,dx
=e^{i\lambda\varphi(x_0)}\,e^{\frac{i\pi}{4}\operatorname{sgn}\varphi''(x_0)}\,
\frac{(2\pi)^{n/2}}{\lambda^{n/2}\lvert\det\varphi''(x_0)\rvert^{1/2}}
\Big(a(x_0)+O(\lambda^{-1})\Big),
$$

where $\operatorname{sgn}$ is the signature, the number of positive eigenvalues minus the number of negative ones. This is the stationary phase theorem, quoted from Theorem 7.7.5 of *The Analysis of Linear Partial Differential Operators I* of Hörmander, together with its hypotheses: a single critical point, non-degeneracy of the Hessian, and an amplitude of compact support. Without the critical point the integral is rapidly decreasing in $\lambda$, and with a degenerate Hessian the exponent $n/2$ is replaced by a larger one determined by the first non-vanishing jet.

**Remark (why the theorem does not apply to the inversion integral directly).** The phase of the inversion integral is $\varphi(\zeta)=\langle\zeta,x\rangle$, which is linear. It has no critical point at all, its Hessian vanishes identically, and the stationary phase theorem therefore has nothing to say about the integral as it stands. What holds instead is this: a smooth compactly supported multiplier gives a kernel that decays faster than any power, by integration by parts, since $\frac{1}{ix_j}\partial_{\zeta_j}e^{i\zeta\cdot x}=e^{i\zeta\cdot x}$ moves the derivative onto the multiplier and each integration gains a factor $\lvert x\rvert^{-1}$.

**The place where it does apply.** The decay of the kernel is not governed by the smooth part of the multiplier but by its singularity. Model the singularity of $m_\sigma$ across the zero hypersurface $\Sigma=\{\det L_\sigma=0\}$ by a jump: let $\mu$ equal a smooth function on one side of $\Sigma$ and zero on the other, with $\Sigma$ smooth near a point $\zeta_0$ and $\nabla\det L_\sigma\ne0$ there. Then integration by parts in the normal direction turns the inverse transform of $\mu$ into an integral over $\Sigma$ with the phase $\langle\cdot,x\rangle$ restricted to $\Sigma$. The critical points of that restriction are the points where $x$ is normal to $\Sigma$, and the Hessian of the restriction at such a point is the second fundamental form of $\Sigma$ there.

**Corollary (the decay produced by a smooth zero hypersurface).** If the second fundamental form of $\Sigma$ is nonsingular at the point where $x$ is normal, the contribution of a neighbourhood of that point to $\kappa_\sigma(x)$ is of size $\lvert x\rvert^{-(n-1)/2}$, and the total decay of the kernel is that rate along the normal directions and faster along the others.

*Proof.* The reduction to a surface integral is the integration by parts above; the phase on the $(n-1)$-dimensional surface has a non-degenerate critical point exactly when the second fundamental form is nonsingular; and the quoted theorem with $n$ replaced by $n-1$ gives the exponent $(n-1)/2$.

**Remark (what this adds to the two previous sections).** The pole order gives the strength of the singularity, the position of the hypersurface gives the directions of slow decay, and the second fundamental form gives the rate. **The three readings are of one object: the kernel is the inverse transform of the reciprocal, its growth is read from the distance of the singular set, and its decay is read from the curvature of that set.** The counting of §*Counting* says how many points of the set a line meets; the present section says what the set contributes to the kernel at a point.

**The open part.** Three cases are not covered: a point where $\nabla\det L_\sigma$ vanishes, so that the hypersurface is singular and the normal direction is undefined; a point where the second fundamental form degenerates, so that the exponent is larger and depends on the first non-vanishing jet; and a pole of order greater than one, where the jump is replaced by a derivative of a jump and the reduction produces derivatives of the surface measure. **These three cases are open in this article.** The biquaternion case meets the first of them at the origin of its null cone, where the gradient of the determinant vanishes. What is proved here is the model case, and it is enough to say what the mechanism is.

## Summary

The reciprocal of a symbol is a multiplier, and its inverse transform is the kernel that carries a datum to a solution. The reciprocal is an adjugate over a determinant, so its poles lie exactly on the complex zero set of $\det L_\sigma$ and their order is the order of vanishing of that determinant, at most $dm$ and generically one. The kernel of a rational symbol in one variable is a sum of step functions times exponentials, one term per zero, so its exponential type is the largest distance of a zero from the real axis, its growth is polynomial exactly when the zeros are real, and it is bounded exactly when they are real and simple. On the real frequencies the zeros are the set where the equation has no solution at that frequency, and the count of them along a complex line is $dm$; the count is not a count of obstructions, because the real zero set is the trace of a hypersurface.

Three sentences carry the article. **The pole order is a property of the point and not of the operator.** **The growth rate is the distance of the zero from the real axis.** **The count is the degree of the determinant along a line, and it is an upper bound rather than a census.**

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$ | A finite-dimensional real associative algebra with unit, of dimension $d$ |
| $A_{\mathbb{C}}$ | The complexification $A\otimes_{\mathbb{R}}\mathbb{C}$, where the symbol and the reciprocal take their values |
| $d$ | The dimension of $A$ over $\mathbb{R}$, and the size of the regular matrix |
| $n$ | The number of frequency variables, and the dimension of the space on which the functions live |
| $x$ | The variable of the function, in $\mathbb{R}^n$ |
| $\zeta$ | The frequency, real in $\mathbb{R}^n$ and complex in $\mathbb{C}^n$ after the extension |
| $P(D)$ | A constant-coefficient operator $\sum_{\lvert\alpha\rvert\le m}a_\alpha\partial^\alpha$ with $a_\alpha\in A$ |
| $\sigma,\sigma_P$ | The symbol $\sum a_\alpha(i\zeta)^\alpha$, an $A_{\mathbb{C}}$-valued polynomial of degree $m$ |
| $m$ | The order of $P$, and the degree of $\sigma$ |
| $L_a$ | Left multiplication by $a$, an endomorphism of $A$ as a real vector space |
| $\det L_a$ | The determinant of the regular representation, of degree $d$ in $a$ and $dm$ in $\zeta$ |
| $Z(P)$ | The zero set of the symbol, the real trace of $\{\det L_\sigma=0\}$ |
| $\mathcal{F},\mathcal{F}^{-1}$ | The transform $\int e^{-i\zeta\cdot x}u\,dx$ and its inverse, with the constant $(2\pi)^{-n}$ |
| $m_\sigma$ | The reciprocal multiplier $\sigma^{-1}$, defined where $\sigma$ is a unit |
| $\kappa_\sigma$ | The kernel of the symbol, $\mathcal{F}^{-1}[m_\sigma]$ |
| $K_R$ | The closed ball $\{x:\lvert x\rvert\le R\}$ of radius $R$ |
| $\tau(F)$ | The exponential type of an entire function $F$, the infimum of the admissible $R$ |
| $\eta_j$ | The imaginary part of the zero $\zeta_j=\xi_j+i\eta_j$ of a scalar symbol |
| $c_j$ | The partial fraction coefficient at the zero $\zeta_j$ |
| $\theta$ | The function equal to one on $(0,\infty)$ and zero on $(-\infty,0)$ |
| $k$ | The order of the pole of the reciprocal at a point of the complex zero set |
| $r$ | The size of the matrix algebra in the case $A=M_r(\mathbb{R})$ |
| $M$ | The supremum of $\lVert L_{\sigma^{-1}}\rVert$ over the frequencies, in the bounded case |
| $\operatorname{adj}$ | The adjugate of a square matrix |
| $\operatorname{tr}$ | The trace of a square matrix |
| $\varphi$ | The phase of a stationary phase integral, and a test function in the Paley–Wiener proof |
| $\lambda$ | The large parameter of the stationary phase asymptotics |
| $\nu$ | A unit vector in $\mathbb{R}^n$, the direction of a contour shift |
| $\Sigma$ | The complex zero hypersurface $\{\det L_\sigma=0\}$ near a smooth point |
| $\Omega$ | The open set of frequencies at which $\sigma$ is a unit |
| $\xi$ | The real part of a complex frequency, and the real variable in the shifted contour |
| $\varrho,\delta$ | The distance of a point $x_0$ from the origin and the radius of the ball about it |
| $\gamma$ | A simple closed contour in $\mathbb{C}$ |
| $\chi$ | A compactly supported function whose transform is used as a multiplier |
| $\mu$ | A model multiplier with a jump across the zero hypersurface |
| $C_c^\infty$ | The smooth functions of compact support |

## Further Reading

- *The Fourier Transform and the Symbol of a Differential Operator*, for the symbol, the zero set, the determinant of the regular representation and the rank on the zero set, all of which this article takes as given.
- *The Fourier Operator*, for the general inversion formula, the transform of a tempered distribution and the two-sided reading of the transform.
- *The Adjoint of the Fourier Operator*, for the adjoint and its relation to the inverse, which is what makes the inversion integral a pairing rather than a formal sum.
- *Distributions and Fundamental Solutions*, for the distributional reading of the transform and for the division of a distribution by a polynomial, which is the operation the third regime needs.
- *The Fundamental Solution Operator*, for the global equation on $\mathbb{R}^n$ and the passage from the pointwise reciprocal to a fundamental solution.
- *Pseudodifferential Operators*, for symbols that are not polynomials and for the calculus in which the growth of the reciprocal is a symbol class rather than a rate.
- Walter Rudin, *Real and Complex Analysis* (3rd ed., McGraw-Hill, 1987), for the Plancherel theorem with its constant in the normalisation used here, and for the Paley–Wiener theorems on which §*Paley–Wiener* rests.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I* (2nd ed., Springer, 1990), for the Paley–Wiener theorem in the tempered case, for the division of distributions by a polynomial, and for the stationary phase theorem of Theorem 7.7.5 quoted in §*Stationary Phase*.
- Lars Ahlfors, *Complex Analysis* (3rd ed., McGraw-Hill, 1979), for the argument principle and the residue theorem, both used in the one-variable section.
- Elias M. Stein, *Harmonic Analysis* (Princeton University Press, 1993), for the decay of the Fourier transform of a measure supported on a curved hypersurface, which is the corollary of §*Stationary Phase*.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the reduced norm, the regular representation and the structure of a finite-dimensional algebra.
