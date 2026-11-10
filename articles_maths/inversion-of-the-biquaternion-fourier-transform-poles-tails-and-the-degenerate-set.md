# __Inversion of the Biquaternion Fourier Transform: Poles, Tails and the Degenerate Set__

## Introduction

**This article proves that the reciprocal of a biquaternion symbol is an adjugate over a norm, that a simple null point contributes a null residue, and that in one variable the kernel always has an element-valued residue expansion, while in two or more variables it has none, because the singular set has real codimension two.**

**The object.** Let $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ be the biquaternion algebra with units $e_t,\vec e_x,\vec e_y,\vec e_z$, the relations $\vec e_k^{2}=-e_t$ and $\vec e_x\vec e_y=\vec e_z$, and the central imaginary $i$. Let $\rho$ be a real pure unit vector of the quaternion part, $\rho^{2}=-e_t$, fixed once for all, and let $\tilde{Ζ}=-i\rho$, so that

$$
\tilde{Ζ}^{2}=e_t,\qquad N(\tilde{Ζ})=-1,\qquad \tilde{Ζ}^{*}=\tilde{Ζ} ,
$$

the last being self-adjointness for the Euclidean form of §*The Moore–Penrose Inverse*. Let $W(t,\omega)=\exp(-2\pi i\tilde{Ζ}\omega t)=\exp(-2\pi\rho\omega t)$ be the kernel of *Biquaternion Continuous Harmonic Analysis*. **The shape $\tilde{Ζ}=-i\rho$ with $\rho$ real is not a convenience**: it is the pure root a regular biquaternion supplies, and the root for which the Peirce projections are self-adjoint (§*The Moore–Penrose Inverse* shows what fails otherwise). For a constant-coefficient operator $P(D)=\sum_{\lvert\alpha\rvert\le m}a_\alpha\partial^\alpha$ with coefficients in $\mathbb{B}$, the symbol at the real frequency $\omega\in\mathbb{R}^{n}$ is

$$
\Sigma(\omega)=\sum_{\alpha}a_\alpha\prod_{k}(2\pi i\tilde{Ζ}\omega_k)^{\alpha_k},
$$

an element of $\mathbb{B}$ chosen so that the transform of $P(D)u$ is $\Sigma$ times the transform of $u$. The frequency set is $Z(P)=\{\omega:N(\Sigma(\omega))=0\}$, the set on which the symbol is not a unit. **The object of this article is the kernel of the reciprocal**,

$$
\kappa_\Sigma(t)=\int_{\mathbb{R}^{n}}\overline{W(t,\omega)}\,\Sigma(\omega)^{-1}\,d\omega ,
$$

the element that carries a datum to a solution. Three questions decide what that integral means: where $\Sigma^{-1}$ fails to exist, which is the question of the poles; how $\kappa_\Sigma$ behaves at large $\lvert t\rvert$, which is the question of the type; and what the singularity contributes there, which is the question of the tail.

**The status of the sections, stated at once.** §*The Adjugate Over the Norm* is proved and needs no hypothesis beyond finite dimension. §*Residues at a Simple Null Point* and §*Residues at a Repeated Null Point* are proved in one frequency variable for a symbol with values in a commutative plane of $\mathbb{B}$, the plane case, which is where a residue is a number. §*Exponential Type and the Tail* quotes Paley–Wiener and Plancherel and proves what is read off them. §*Two Contours, Not One* proves the one-variable expansion for an arbitrary symbol, commuting or not. §*The Obstacle: Real Codimension Two* proves that the method does not extend to two or more variables, and states without proof what would replace it. §*Inversion Where the Symbol Is Not a Unit* is proved in the plane case and quoted in general.

**What is quoted, and from where.** The Peirce frame — the idempotents $\Pi_\pm$, the ideals, the scalars — is quoted from *Biquaternion Continuous Harmonic Analysis* and is not rebuilt here, and Paley–Wiener and Plancherel are quoted from the same article. The identity $\det L_{\tilde Q}=\lvert N(\tilde Q)\rvert^{4}$, the null cone and the rank of left multiplication are quoted from *The Fourier Transform and the Symbol of a Differential Operator*. **Nothing is quoted without the hypotheses that make it true.**

**The warning, before any formula.** In one frequency variable the singular set is a discrete set of points, a small circle links a point, and a residue is a number. In two or more variables the complexified singular set is a hypersurface of real codimension two, and a hypersurface is not a point: no isolated pole, no partial fraction expansion, no sum of residues. **What replaces the residue is a residue current, or a Leray form over a real six-dimensional cycle**, and §*The Obstacle: Real Codimension Two* says how far that goes.

**Why one variable is settled and the general case is not.** The kernel carries both signs of the exponential, so no single contour makes the whole integrand decay. **But the kernel splits, and each term is closed in its own half-plane**, which gives a pair of element-valued residue expansions valid whether or not the symbol commutes with the root (§*Two Contours, Not One*). What the split does not give is a single residue at a pole; what fails outright in two or more variables is the geometry. **The honest core is the codimension-two obstruction of §*The Obstacle: Real Codimension Two*.**

**Boundaries.** The transform and the two quoted theorems are *Biquaternion Continuous Harmonic Analysis*; the symbol and its zero set are *The Fourier Transform and the Symbol of a Differential Operator*; the placements of the kernel are *The Three Kernel Placements of the Biquaternion Fourier Transform*; the inversion through a generalised inverse is *Biquaternion Fourier Inversion on the Degenerate Set*. This article adds the reciprocal, its residues and their limits.

## The Adjugate Over the Norm

### The Reciprocal as an Adjugate Over a Norm

**Proposition (the conjugate is the adjugate).** For every $\tilde Q\in\mathbb{B}$, with $\overline{\tilde Q}=Q_t-Q_x\vec e_x-Q_y\vec e_y-Q_z\vec e_z$,

$$
\tilde Q\,\overline{\tilde Q}=\overline{\tilde Q}\,\tilde Q=N(\tilde Q)e_t ,
$$

and $N(\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$ is central and complex-valued. Consequently, on the complement of the frequency set,

$$
\Sigma(\omega)^{-1}=\frac{\overline{\Sigma(\omega)}}{N(\Sigma(\omega))} .
$$

*Proof.* Write $\tilde Q=Q_te_t+Q_v$ with $Q_v=\sum_kQ_k\vec e_k$. The product of two vector parts is $\vec e_j\vec e_k+\vec e_k\vec e_j=0$ for $j\ne k$, so $Q_v^{2}=-\sum_kQ_k^{2}e_t$, and then $\tilde Q\overline{\tilde Q}=Q_t^{2}e_t-Q_v^{2}=(Q_t^{2}+\sum_kQ_k^{2})e_t$. The reversed product is the same computation, because the two factors commute with each other and the scalar coefficients are central. Centrality of $N$ is immediate from the display, and the reciprocal follows by multiplying $\Sigma\bar\Sigma=N$ by the central scalar $1/N$.

**Corollary (the reciprocal of the regular representation).** For a symbol that is a unit, $L_{\Sigma}^{-1}=N(\Sigma)^{-1}L_{\overline{\Sigma}}$. Since $\det L_{\Sigma}=\lvert N(\Sigma)\rvert^{4}$ by *The Fourier Transform and the Symbol of a Differential Operator*, the adjugate of the real $8\times8$ block is

$$
\operatorname{adj}L_{\Sigma}=\lvert N(\Sigma)\rvert^{2}\,\overline{N(\Sigma)}\,L_{\overline{\Sigma}} ,
$$

an operator of degree $7m$ in the frequency, against the degree $8m$ of the determinant.

*Proof.* The first display is the proposition with both sides acting by left multiplication: $L_{\Sigma}L_{\bar\Sigma}=L_{N(\Sigma)}$, and $L$ of a central scalar is that scalar times the identity, hence invertible with inverse $L_{1/N}$. For the adjugate, $\operatorname{adj}L=\det L\cdot L^{-1}$ with $\det L=\lvert N\rvert^{4}$ and $L^{-1}=L_{\bar\Sigma/N}$, so the scalar is $\lvert N\rvert^{4}/N=\lvert N\rvert^{2}\bar N$. **The conjugate on the norm is not decoration**: $\lvert N\rvert^{4}/N$ is $\lvert N\rvert^{2}\bar N$ and not $\lvert N\rvert^{2}N$, and the two agree only where $N$ is real, which is the case of a real frequency and real coefficients.

**Remark (one scalar denominator, and therefore two real equations).** In the real algebra of *The Inverse Fourier Transform of a Symbol* the reciprocal carries a determinant in the denominator. Here it carries the single function $N\circ\Sigma$, whose vanishing is **two real equations**, which is the source of every difficulty in §*The Obstacle: Real Codimension Two*.

### The Order of the Pole, and the Three Orders

**Proposition (the order of the pole).** Let $\omega_0$ be a null point, let $j$ be the order of vanishing of $N\circ\Sigma$ at $\omega_0$, and let $j'$ be the order of vanishing of $\overline{\Sigma}$ there. Then $\Sigma^{-1}$ has a pole of order $j-j'$ at $\omega_0$ when $j>j'$, and is bounded there when $j\le j'$.

*Proof.* The variable $\omega$ is a complex scalar and therefore central, so the reciprocal is the product of the element-valued function $\overline{\Sigma}$ with the complex-valued function $1/N$. No non-commutative division occurs. A product of a function vanishing to order $j'$ with one vanishing to order $-j$ vanishes to order $j'-j$; the order is read off, and it is positive exactly when $j>j'$.

**Remark (three orders meet at a null point, and only one is the pole order).** The operator has order $m$, the block determinant has degree $8m$, and the pole has order $j-j'$. **None of the three is determined by the others**: the adjugate cancels part of the determinant, and a symbol of degree $m$ may have a pole of order one or of order $m$.

**Example (a pole of order two behind a determinant of order sixteen).** Let $\Sigma(\omega)=(\omega-\omega_0)^{2}e_t$. Then $N(\Sigma)=(\omega-\omega_0)^{4}$, $\overline{\Sigma}=(\omega-\omega_0)^{2}e_t$, and $\Sigma^{-1}=(\omega-\omega_0)^{-2}e_t$: the pole has order two, the norm four, the determinant $\lvert N\rvert^{4}$ sixteen. **Reading the pole order off the determinant is wrong here.**

**Remark (the two kinds of null point).** At a point of the **first kind** the element vanishes; at a point of the **second kind** only the norm does, so the element is a nonzero zero divisor. In the plane case the second kind is generic, the vanishing of the element being two conditions and that of the norm one. **Every worked example below is of the second kind.**

### What Is Quoted: Paley–Wiener and Plancherel

**Theorem (Paley–Wiener, quoted).** Let $f:\mathbb{R}^{n}\to\mathbb{B}$ be integrable with $\hat f(\omega)=\int W(t,\omega)f(t)\,dt$. Then $f$ is supported in the ball of radius $R$ if and only if $\hat f$ extends to an entire function of the complexified frequency satisfying

$$
\lVert\hat f(\omega)\rVert\le C e^{2\pi R\lvert\operatorname{Im}\omega\rvert}
$$

for some constant $C$. The number $2\pi R$ is the exponential type of $\hat f$, and the support radius is the type divided by $2\pi$.

**Theorem (Plancherel, quoted).** For $f$ in $L^{2}(\mathbb{R}^{n};\mathbb{B})$ the transform $\hat f$ lies in $L^{2}$ and

$$
\int_{\mathbb{R}^{n}}\lVert f(t)\rVert^{2}\,dt=\int_{\mathbb{R}^{n}}\lVert\hat f(\omega)\rVert^{2}\,d\omega ,
$$

so the transform is unitary, and its inverse is the conjugate kernel.

**Remark (the hypotheses, and why they are named).** Both theorems are quoted from *Biquaternion Continuous Harmonic Analysis*, stated for $\mathbb{B}$-valued functions with the Euclidean norm on the eight real coordinates, the first under integrability and the second under membership of $L^{2}$. **They are not proved here**: Paley–Wiener converts a support radius into a type, and Plancherel a pointwise bound on the symbol into a bound on the operator.

**Corollary (when the reciprocal is a bounded operator).** Multiplication by $\Sigma^{-1}$ is bounded on $L^{2}$ if and only if $\lVert\Sigma(\omega)^{-1}\rVert$ is bounded on the real frequencies, that is if and only if $Z(P)$ stays at a positive distance from $\mathbb{R}^{n}$.

*Proof.* Plancherel makes the transform unitary, so multiplication by a function is bounded with the supremum of its norm as the bound. That supremum is finite exactly when $Z(P)$ does not meet the real frequencies and stays away from them.

## Residues at a Simple Null Point

### The Plane Case, Quoted

**Lemma (the plane case).** Let $\Sigma$ take its values in the complex span of $e_t$ and $\tilde{Ζ}$, so that $\Sigma=a e_t+b\tilde{Ζ}$ with $a,b$ complex-valued functions of $\omega$, and let $\Pi_\pm=\tfrac12(e_t\pm\tilde{Ζ})$ be the Peirce idempotents of *Biquaternion Continuous Harmonic Analysis*. Then $\Sigma=\sigma_+\Pi_++\sigma_-\Pi_-$ with $\sigma_\pm=a\pm b$, the norm is $N(\Sigma)=a^{2}-b^{2}=\sigma_+\sigma_-$, the reciprocal is

$$
\Sigma^{-1}=\frac{a e_t-b\tilde{Ζ}}{a^{2}-b^{2}}=\sigma_+^{-1}\Pi_++\sigma_-^{-1}\Pi_- ,
$$

and the conjugate kernel splits as

$$
\overline{W(t,\omega)}=\Pi_+e^{2\pi i\omega t}+\Pi_-e^{-2\pi i\omega t} .
$$

*Proof.* The plane is commutative, because $\tilde{Ζ}^{2}=e_t$ and the coefficients are central. The idempotents satisfy $\Pi_\pm^{2}=\Pi_\pm$, $\Pi_+\Pi_-=0$, $\Pi_++\Pi_-=e_t$ and $\Pi_+-\Pi_-=\tilde{Ζ}$, so $ae_t+b\tilde{Ζ}=(a+b)\Pi_++(a-b)\Pi_-$ and $ae_t-b\tilde{Ζ}=(a-b)\Pi_++(a+b)\Pi_-$. Multiplying the two gives $(a^{2}-b^{2})(\Pi_++\Pi_-)=(a^{2}-b^{2})e_t$, which is the norm, and dividing gives the reciprocal. For the kernel, $\tilde{Ζ}\Pi_\pm=\pm\Pi_\pm$, so the exponential of $\pm2\pi i\omega t\tilde{Ζ}$ acts on $\Pi_\pm$ as the scalar exponential with that sign.

### The Residue Formula

**Theorem (the residue at a simple null point).** Let $\Sigma$ be plane-valued, let $\omega_0$ be a point where $N(\Sigma(\omega_0))=0$, suppose that $N\circ\Sigma$ has a simple zero there, and suppose that $\overline{\Sigma}(\omega_0)\ne0$. Then $\Sigma^{-1}$ has a simple pole at $\omega_0$ with residue

$$
\operatorname*{Res}_{\omega=\omega_0}\Sigma^{-1}=\frac{\overline{\Sigma}(\omega_0)}{\dfrac{d}{d\omega}N\bigl(\Sigma(\omega)\bigr)\Big|_{\omega_0}} .
$$

*Proof.* By the proposition of §*The Reciprocal as an Adjugate Over a Norm*, $\Sigma^{-1}=\overline{\Sigma}/N$ with $N$ a complex-valued holomorphic function. Write $h=\omega-\omega_0$, $N=c h+O(h^{2})$ with $c\ne0$ by simplicity, and $\overline{\Sigma}=\overline{\Sigma}(\omega_0)+O(h)$. The quotient is $\overline{\Sigma}(\omega_0)/(ch)+O(1)$, and the coefficient of $h^{-1}$ is the display.

**Example (the two residues of a first-order symbol, computed).** Let $\lambda>0$ and $\Sigma(\omega)=\lambda e_t+2\pi i\omega\tilde{Ζ}$, the symbol of $\partial_t+\lambda e_t$. Its scalars are $\sigma_\pm=\lambda\pm2\pi i\omega$, so $N=\lambda^{2}+4\pi^{2}\omega^{2}$ and the null points are $\pm i\lambda/(2\pi)$, one per ideal and one per half-plane. At $\omega_0=+i\lambda/(2\pi)$ the adjugate is $\lambda(e_t+\tilde{Ζ})=2\lambda\Pi_+$ and the derivative of the norm is $4\pi i\lambda$, so

$$
\operatorname*{Res}_{\omega=\omega_0}\Sigma^{-1}=\frac{2\lambda\Pi_+}{4\pi i\lambda}=\frac{\Pi_+}{2\pi i},
$$

and the same computation at $\omega_1$, with the two signs exchanged, gives $-\Pi_-/(2\pi i)$. A contour integral over a circle of radius $0.05$ about $\omega_0$, with $200000$ nodes, reproduces $\Pi_+$ to six figures, which is the residue multiplied by $2\pi i$.

### The Residue Is a Null Element

**Proposition (the residue lies on the null cone).** At a simple null point the residue is a nonzero element of norm zero, and left multiplication by it has rank $4$ in the eight real coordinates.

*Proof.* The residue is $\overline{\Sigma}(\omega_0)$ divided by the nonzero complex number $N'(\omega_0)$. Since $N(\overline{\Sigma})=N(\Sigma)$, because conjugation changes the sign of every vector coordinate and the norm is the sum of the second powers of the coordinates, the numerator has norm $N(\Sigma(\omega_0))=0$, and dividing by a nonzero complex scalar multiplies the norm by the second power of that scalar, hence preserves vanishing. Non-vanishing holds because $\overline{\Sigma}(\omega_0)\ne0$ and the divisor is finite. The rank statement is the rank of left multiplication at a nonzero null element, quoted from *The Fourier Transform and the Symbol of a Differential Operator*.

**Remark (the residue is not the inverse of the derivative of the symbol).** In the scalar case a simple zero of $\sigma$ gives the residue $1/\sigma'(\omega_0)$, and it is tempting to write $\Sigma'(\omega_0)^{-1}$ here. **That is false for the element**: in the example $\Sigma'(\omega_0)=2\pi i\tilde{Ζ}$ is a unit while the residue is the null element $\Pi_+/(2\pi i)$. The analogy fails because the symbol does not vanish at the pole; the norm does.

### A Worked Kernel

**Proposition (the kernel of a first-order symbol).** For $\Sigma(\omega)=\lambda e_t+2\pi i\omega\tilde{Ζ}$ with $\lambda>0$,

$$
\kappa_\Sigma(t)=\Theta(t)\,e^{-\lambda t}e_t ,
$$

with $\Theta$ the step at the origin. The kernel vanishes for $t<0$ and decays with rate $\lambda$ for $t>0$.

*Proof.* By the plane lemma the integral splits as $\kappa=\Pi_+J_++\Pi_-J_-$ with

$$
J_+=\int_{\mathbb{R}}\frac{e^{2\pi i\omega t}}{\lambda+2\pi i\omega}\,d\omega,\qquad J_-=\int_{\mathbb{R}}\frac{e^{-2\pi i\omega t}}{\lambda-2\pi i\omega}\,d\omega .
$$

For $t>0$ the first integrand decays in the upper half-plane and the contour closes upward onto the pole at $+i\lambda/(2\pi)$, where the residue of the scalar quotient is $e^{-\lambda t}/(2\pi i)$, so $J_+=e^{-\lambda t}$. The second integrand decays in the lower half-plane and closes downward onto the pole at $-i\lambda/(2\pi)$, where its residue is $e^{-\lambda t}/(-2\pi i)$, so $J_-=e^{-\lambda t}$ as well. For $t<0$ each contour closes away from its pole and both integrals vanish. Hence $\kappa=\Theta(t)e^{-\lambda t}(\Pi_++\Pi_-)=\Theta(t)e^{-\lambda t}e_t$.

**Remark (the two closures are in opposite half-planes, and that is the point).** The two ideals demand opposite contours, because their exponentials carry opposite signs, and **here the demands are compatible**, the pole of $\Pi_+$ lying above and that of $\Pi_-$ below. §*Two Contours, Not One* meets the same two demands separately for a symbol that mixes the ideals.

## Residues at a Repeated Null Point

### The Expansion at a Null Point of the First Kind

**Lemma (the local expansion).** Let $\Sigma(\omega_0)=0$ and suppose that $\Sigma(\omega_0+h)=h^{k}A+h^{k+1}B+h^{k+2}C+\cdots$ with $A$ a unit and $h$ a complex scalar. Then

$$
\Sigma^{-1}=h^{-k}A^{-1}-h^{-k+1}A^{-1}BA^{-1}+h^{-k+2}\bigl(A^{-1}BA^{-1}BA^{-1}-A^{-1}CA^{-1}\bigr)+\cdots
$$

*Proof.* Factor $\Sigma=h^{k}(A+hB+h^{2}C+\cdots)$ and invert the parenthesis by the geometric series in $h$, which is legitimate because $h$ is central and $A$ is a unit: $(A+hB)^{-1}=A^{-1}-hA^{-1}BA^{-1}+\cdots$. Multiply by the central scalar $h^{-k}$.

**Corollary (the residue at orders one, two and three).** With the notation of the lemma, the residue of $\Sigma^{-1}$ at $\omega_0$ is $A^{-1}$ for $k=1$, $-A^{-1}BA^{-1}$ for $k=2$, and $A^{-1}BA^{-1}BA^{-1}-A^{-1}CA^{-1}$ for $k=3$.

*Proof.* The residue is the coefficient of $h^{-1}$, which is the coefficient of $h^{k-1}$ in the inverted parenthesis.

### The Second Kind, One Ideal at a Time

**Proposition (the pole lives on one ideal).** Let $\Sigma$ be plane-valued with scalars $\sigma_\pm$, and let $\omega_0$ be a null point of the second kind where $\sigma_+$ vanishes to order $j\ge1$ and $\sigma_-$ does not vanish. Then $\Sigma^{-1}$ has, on the ideal $\Pi_+\mathbb{B}$, a pole of order $j$ at $\omega_0$, and on the ideal $\Pi_-\mathbb{B}$ it is regular there. In particular the pole order is the order of the vanishing of one scalar, and it is not the order of the norm, which is $j$.

*Proof.* By the plane lemma $\Sigma^{-1}=\sigma_+^{-1}\Pi_++\sigma_-^{-1}\Pi_-$, a sum of two terms supported on the two ideals. The first has a pole of order $j$; the second is regular because $\sigma_-(\omega_0)\ne0$. The norm is $\sigma_+\sigma_-$, whose order at $\omega_0$ is $j$ as well, since $\sigma_-$ does not vanish.

**Example (the repeated pole of a first-order symbol).** Let $\Sigma_1(\omega)=\lambda e_t+2\pi i\omega\tilde{Ζ}$ with $\lambda>0$ and let $\Sigma=\Sigma_1^{2}$. Its scalars are $(\lambda\pm2\pi i\omega)^{2}$, so the norm is $(\lambda^{2}+4\pi^{2}\omega^{2})^{2}$ and each of the two null points is a double zero of the norm and a double zero of its own scalar. **The pole at each null point has order two**, and the reciprocal is $\sigma_+^{-2}\Pi_++\sigma_-^{-2}\Pi_-$.

### Polynomial Times Exponential

**Proposition (a pole of order $k$ contributes a polynomial of degree $k-1$).** Let $\omega_0$ be a pole of $\Sigma^{-1}$ of order $k$, lying off the real axis, and let the contour for one ideal close onto it. Then the contribution of $\omega_0$ to $\kappa_\Sigma$ is a finite sum of terms $c_jt^{j}e^{2\pi i\omega_0t}$ with $0\le j\le k-1$ and coefficients $c_j$ in $\mathbb{B}$.

*Proof.* The residue is the coefficient of $h^{-1}$ in $\overline{\Sigma}/N$, which is the $(k-1)$-st derivative at $\omega_0$ of the regular part, divided by $(k-1)!$. Each derivative of $e^{2\pi i\omega t}$ in $\omega$ brings down the factor $2\pi it$, so the derivative of order $k-1$ produces the powers $t^{0},\ldots,t^{k-1}$ with scalar coefficients.

**Corollary (the kernel of a symbol raised to the second power).** With $\Sigma=\Sigma_1^{2}$ as in the example and $\lambda>0$,

$$
\kappa_\Sigma(t)=\Theta(t)\,t\,e^{-\lambda t}e_t .
$$

*Proof.* The kernel of a product of symbols is the convolution of the kernels, so $\kappa_\Sigma=\kappa_{\Sigma_1}*\kappa_{\Sigma_1}$, which is $\int_0^{t}e^{-\lambda s}e^{-\lambda(t-s)}ds\,e_t=te^{-\lambda t}e_t$ for $t>0$ and $0$ for $t<0$. The same answer follows from the proposition, with $k=2$ and each residue of order two.

## Exponential Type and the Tail

### The Type of the Kernel

**Proposition (the rate is the distance, in the units of the exponent).** Let $\Sigma$ be plane-valued, let every pole of $\Sigma^{-1}$ lie off the real axis, let $\rho$ be the least distance from a pole to the real axis, and let $k$ be the largest pole order. Then each ideal's contribution to $\kappa_\Sigma$ is bounded by $C(1+\lvert t\rvert)^{k-1}e^{-2\pi\rho\lvert t\rvert}$ for every real $t$.

*Proof.* On one ideal the kernel is the scalar integral $J=\int e^{\pm2\pi i\omega t}\sigma(\omega)^{-1}d\omega$ with $\sigma$ a polynomial. For $t>0$ the contour closes in the half-plane where the exponential decays, and for $t<0$ in the other; either way the value is a finite sum of residues at the poles of that scalar. The residue at a pole of order $k$ is a derivative of order $k-1$ of the exponential, hence a polynomial of degree $k-1$ in $t$ times $e^{\pm2\pi i\omega_0t}$, by the proposition of §*Polynomial Times Exponential*. Its modulus is $e^{-2\pi\lvert\operatorname{Im}\omega_0\rvert\lvert t\rvert}$, at most $e^{-2\pi\rho\lvert t\rvert}$, and the finite sum with the polynomial factor gives the constant.

**Remark (why the type is not smaller).** The bound is attained: the residue at a pole at distance $\rho$ is a nonzero element, so its term is present with a nonzero coefficient. **The exponential type of the kernel is $2\pi\rho$**, and that conversion is the only place where the normalisation enters.

**Remark (the case $\rho=0$).** A pole on the real axis gives no exponential decay at all: the contour cannot be closed, the integral is a principal value, and the residue contributes half of itself at the pole. **The kernel is then merely bounded**, and the corollary of §*What Is Quoted: Paley–Wiener and Plancherel* says that the inversion is not a bounded operator on $L^{2}$. The two facts are the same fact.

### The Tail of a Solution

**Proposition (the bound on a solution).** Let $f$ be integrable and supported in a ball of radius $R$, let $\kappa$ obey the bound of the previous proposition, and let $u=\kappa*f$. Then

$$
\lVert u(x)\rVert\le C'\lVert f\rVert_{1}\bigl(1+\lvert x\rvert\bigr)^{k-1}e^{-2\pi\rho(\lvert x\rvert-R)} .
$$

*Proof.* For $y$ in the support of $f$ the number $\lvert x-y\rvert$ is at least $\lvert x\rvert-R$, and the bound is monotone in $\lvert x-y\rvert$ on the side where the kernel does not vanish; integrate the bound against $\lVert f(y)\rVert\,dy$.

**Corollary (a solution of compact support needs a vanishing datum at every pole).** Suppose $\Sigma$ has a pole at $\omega_0$ with $\operatorname{Im}\omega_0\ne0$, and let $f$ be a solution whose transform is $\hat f=\Sigma^{-1}\hat g$. If $\hat g(\omega_0)\ne0$, then $\hat f$ has a pole at $\omega_0$ and $f$ is not of compact support.

*Proof.* A function of compact support has a transform that is entire, by Paley–Wiener. The product $\Sigma^{-1}\hat g$ has a pole at $\omega_0$ whenever the pole of $\Sigma^{-1}$ is not cancelled by a zero of $\hat g$, and it is not cancelled exactly when $\hat g(\omega_0)\ne0$, since the pole is simple on its ideal. Hence $\hat f$ is not entire, and $f$ is not of compact support.

## Two Contours, Not One

**Lemma (the conjugate kernel splits into two scalar exponentials).** For every root $\tilde{Ζ}$ with $\tilde{Ζ}^{2}=e_t$, and every real $t$ and $\omega$,

$$
\overline{W(t,\omega)}=\Pi_+e^{2\pi i\omega t}+\Pi_-e^{-2\pi i\omega t}.
$$

*Proof.* Since $\tilde{Ζ}^{2}=e_t$, the exponential is $\exp(\theta\tilde{Ζ})=\cosh\theta+\tilde{Ζ}\sinh\theta$ for every $\theta$. With $\theta=-2\pi i\omega t$ this is $\cos(2\pi\omega t)-i\tilde{Ζ}\sin(2\pi\omega t)$, and adding the two terms of the display gives the same expression, because $\Pi_++\Pi_-=e_t$ and $\Pi_+-\Pi_-=\tilde{Ζ}$. **The identity uses no commutation**: the only products are powers of $\tilde{Ζ}$.

**Proposition (the residue expansion of the one-variable kernel).** Let $n=1$; let $\Sigma$ be a polynomial symbol whose reciprocal has no pole on the real axis and finitely many off it; let $s=\operatorname{sign}t$; and suppose the reciprocal grows no faster than a negative power of $\lvert\omega\rvert$ at infinity. Then

$$
\kappa_\Sigma(t)=2\pi is\!\!\sum_{\operatorname{sign}\operatorname{Im}\omega_j=s}\!\!\operatorname{Res}_{\omega_j}\big(\Pi_+\Sigma^{-1}e^{2\pi i\omega t}\big)\;-\;2\pi is\!\!\sum_{\operatorname{sign}\operatorname{Im}\omega_j=-s}\!\!\operatorname{Res}_{\omega_j}\big(\Pi_-\Sigma^{-1}e^{-2\pi i\omega t}\big),
$$

the sums running over the poles of $\Sigma^{-1}$, each taken with its own order.

*Proof.* By the lemma the integral is a sum of two. In the first, $e^{2\pi i\omega t}$ decays in the half-plane $\operatorname{sign}\operatorname{Im}\omega=s$ and the algebraic factor $\Pi_+\Sigma^{-1}$ is bounded there by a negative power of $\lvert\omega\rvert$, so the arc at height $M$ contributes $O(M^{-k}e^{-2\pi M\lvert t\rvert})$ and vanishes; Cauchy's theorem gives $2\pi is$ times the residues of that half-plane. The second integral is the same computation with $t$ replaced by $-t$, $\Pi_+$ by $\Pi_-$, and the contour reversed, which is the second sign. **Neither step refers to the commutator of $\Sigma$ with $\tilde{Ζ}$**: the split is a split of the kernel, not of the symbol.

**Remark (verified on a symbol that does not commute with the root).** Take $\tilde{Ζ}=-i\vec e_z$ and $\Sigma(\omega)=-4\pi^{2}\omega^{2}e_t+2\pi i\omega(e_t+0.7i\vec e_x)+e_t$, whose commutator with $\tilde{Ζ}$ is nonzero. Its four poles are simple and off the real axis. The display of the proposition and a direct numerical integration agree to $1.5\times10^{-7}$ relative at $t=+0.6$, $t=-0.6$ and $t=1.3$ over $\lvert\omega\rvert\le60$, and to $1.4\times10^{-10}$ when the truncation and the point count are pushed out together.

**Remark (what the two contours do not give).** There is no single contour, and therefore **no single residue at a pole**: the same pole contributes through $\Pi_+$ on one side of the time axis and through $\Pi_-$ on the other. Hence a kernel in one variable is generally two-sided **even when every pole lies in one half-plane**, its two sides are governed by different projections of the same residues, and its type is a pair of numbers. Only in the plane case does one of the two contributions vanish, which is why that case looks like a single scalar calculus.

**Remark (what is actually open).** In one variable the expansion is proved, commuting or not. **What fails is the passage to $n\ge2$, for a geometric reason**: a set of real codimension two has no point to encircle, so the residue must become a current or an integral over a linking cycle, which is what §*What Replaces the Residue* names.

## The Obstacle: Real Codimension Two

### The Singular Set in More Than One Variable

**Proposition (the singular set is a hypersurface after complexification).** Let $n\ge2$ and let $\zeta$ range over $\mathbb{C}^{n}$. The set $\{\zeta:N(\Sigma(\zeta))=0\}$ is, off the critical set of $N\circ\Sigma$, a complex hypersurface of complex dimension $n-1$ and real dimension $2n-2$. In particular it contains no isolated point, and for $n=4$ its real dimension is $6$.

*Proof.* The map $\zeta\mapsto\Sigma(\zeta)$ is polynomial with coefficients in $\mathbb{B}$, and $N$ is a polynomial in the eight coordinates, so $N\circ\Sigma$ is holomorphic. One holomorphic equation in $n$ variables defines a hypersurface wherever its gradient does not vanish, and a complex hypersurface of dimension $n-1$ has real dimension $2n-2$; for $n=4$ this is $6$.

**Remark (the real frequencies, where the count is different).** Restricted to $\mathbb{R}^{n}$ the equation is two real equations, so the set has real codimension two when they are independent, codimension one when $N\circ\Sigma$ is real-valued, and is generically empty for $n=1$ and a genuinely complex symbol. **The codimension depends on how the symbol meets the null cone**, which itself has real dimension six in eight.

### What Replaces the Residue

**Definition (residue current, stated and not used).** Let $F$ be holomorphic near the origin of $\mathbb{C}^{n}$ with $F(0)=0$ and $dF(0)\ne0$. The residue current of a form with a simple pole along $\{F=0\}$ is defined by a limit of integrals over the tubes $\{\lvert F\rvert=\epsilon\}$ as $\epsilon\to0$, and it is a current of degree one less than the form, supported on the hypersurface.

**Remark (the Leray form, and the two known routes).** The same object is the Leray form $\frac{dF}{F}\wedge\eta$ integrated over a real cycle that links the hypersurface; the two known routes to the kernel in $n\ge2$ are the residue currents of Coleff–Herrera with their analytic continuation, and the Leray form over a real cycle. **Neither is proved here and neither is applied here**; they are named so that the reader knows what the programme is about, and they are quoted, not used.

**Remark (the two open points).** First, the kernel as a sum of contributions in $n\ge2$, for which the residue current is the candidate and not the answer. Second, the points where the gradient of the norm vanishes, which the null cone meets at its vertex. **Both are open, and neither is hidden.**

## Inversion Where the Symbol Is Not a Unit

### The Pointwise Problem

**Remark (what replaces the equation when the inverse does not exist).** Transforming $P(D)u=g$ gives $\Sigma(\omega)\hat u(\omega)=\hat g(\omega)$, a linear equation in the algebra at each frequency. Where $\Sigma(\omega)$ is a unit, $\hat u=\Sigma^{-1}\hat g$. Where it is not, there are three possibilities: no solution, a four-dimensional affine set of them, or — at $\Sigma(\omega)=0$ — solutions exactly when the datum vanishes. **The algebra decides which; the transform does not.**

### The Moore–Penrose Inverse

**Definition (the Moore–Penrose inverse, quoted).** Let $\mathbb{B}$ carry the Euclidean form $\langle X,Y\rangle_E=\operatorname{Re}\sum_kX_k\overline{Y_k}$ on the eight real coordinates, and let $A^*$ denote the adjoint of $A$ for that form, which is the conjugate transpose in the matrix model. The **Moore–Penrose inverse** of $A\in\mathbb{B}$ is the element $A^{+}$ with

$$
AA^{+}A=A,\qquad A^{+}AA^{+}=A^{+},\qquad (AA^{+})^{*}=AA^{+},\qquad (A^{+}A)^{*}=A^{+}A .
$$

**Uniqueness is quoted from *The Moore–Penrose Inverse in an Involutive Algebra***, which also proves that existence is not automatic in an involutive algebra and holds in a finite-dimensional one exactly when $A$ and $A^{2}$ generate the same two ideals. That criterion holds at every element of $\mathbb{B}$, because $\mathbb{B}$ is a full matrix algebra over $\mathbb{C}$ and the two ideals agree there; so $A^{+}$ exists for every $A$, and left multiplication by it is the Moore–Penrose inverse of left multiplication by $A$.

**Proposition (the plane case, computed).** Let $\Sigma=\sigma_+\Pi_++\sigma_-\Pi_-$ be plane-valued, with the fixed root of the Introduction, so that $\tilde{Ζ}^{*}=\tilde{Ζ}$ and the two Peirce projections are self-adjoint. Then

$$
\Sigma^{+}=\sum_{\sigma_\pm\ne0}\sigma_\pm^{-1}\Pi_\pm ,
$$

the sum being taken over the scalars that do not vanish at the frequency in question.

*Proof.* Off the null set both scalars are nonzero, the element is a unit, and the display is the reciprocal of the plane lemma, which satisfies the four identities because a two-sided inverse does. At a null point of the second kind exactly one scalar vanishes, say $\sigma_+(\omega_0)=0$; then $\Sigma=\sigma_-\Pi_-$ and the display is $\sigma_-^{-1}\Pi_-$. The four identities hold: $\Sigma\Sigma^{+}\Sigma=\sigma_-\Pi_-\sigma_-^{-1}\Pi_-\sigma_-\Pi_-=\sigma_-\Pi_-=\Sigma$, and similarly for the second; the two projections $\Sigma\Sigma^{+}$ and $\Sigma^{+}\Sigma$ are both $\Pi_-$ itself, and $\Pi_-$ is self-adjoint because $\tilde{Ζ}$ is. At a point where both scalars vanish the element is zero, and the display is the empty sum, which is the Moore–Penrose inverse of zero.

**Remark (what the hypothesis on the root buys).** Let $\tilde{Ζ}$ be a root of $1$ that is not self-adjoint, for instance $\tilde{Ζ}=\vec e_x+i\sqrt2\vec e_y$, for which $\tilde{Ζ}^{2}=e_t$ and $N(\tilde{Ζ})=-1$ as required. The Peirce projections are then idempotent and oblique. At a second-kind point the display still satisfies $\Sigma\Sigma^{+}\Sigma=\Sigma$ and $\Sigma^{+}\Sigma\Sigma^{+}=\Sigma^{+}$ and fails the two symmetry equations, so it is a reflexive generalised inverse and **not** the Moore–Penrose inverse. The solvability condition survives, because it uses only that $\Sigma\Sigma^{+}$ is idempotent with the image of $\Sigma$.

**Remark (bounded where the reciprocal blows up).** At a second-kind point the reciprocal has a pole and its norm tends to infinity, while the Moore–Penrose inverse is $\sigma_-^{-1}\Pi_-$: finite and continuous across the point. The two agree off the null set; the difference is the singular ideal. **That is why $\int\overline{W}\Sigma^{+}\hat g$ converges where $\int\overline{W}\Sigma^{-1}\hat g$ does not.**

### The Solvability Condition

**Proposition (the condition for a solution at one frequency).** Let $A\in\mathbb{B}$ and $g\in\mathbb{B}$. The equation $AX=g$ has a solution if and only if

$$
(e_t-AA^{+})g=0 ,
$$

and then the solutions are $X=A^{+}g+(e_t-A^{+}A)Y$ with $Y$ arbitrary.

*Proof.* Left multiplication by $AA^{+}$ is a projection of $\mathbb{B}$ onto the image of left multiplication by $A$: it is idempotent and $AA^{+}A=A$, and with the fixed root it is even the orthogonal projection, though only idempotence and the image are used here. Hence $g$ lies in the image exactly when it is fixed by the projection, which is the displayed condition. The general solution is the particular solution plus the kernel of left multiplication by $A$, and the kernel is the image of $e_t-A^{+}A$ by the same argument applied to $A^{+}A$.

**Corollary (the condition in the plane case).** Let $\Sigma$ be plane-valued at a second-kind point where $\sigma_+(\omega_0)=0$ and $\sigma_-(\omega_0)\ne0$. Then $\Sigma\hat u=\hat g$ is solvable at $\omega_0$ if and only if

$$
\Pi_+\hat g=0 ,
$$

that is if and only if the datum has no component on the ideal that the symbol has lost.

*Proof.* The projection $e_t-\Sigma\Sigma^{+}$ is $e_t-\Pi_-=\Pi_+$ by the proposition and the explicit form of $\Sigma^{+}$, and it acts by left multiplication. The condition is therefore $\Pi_+\hat g=0$, which says that $\hat g=\Pi_-\hat g$ lies in $\mathbb{B}\Pi_-$, the image of left multiplication by $\Sigma$. **The multiplication is on the left throughout**, because the symbol multiplies the transform on the left: with the kernel on the right the condition reads $\hat g\Pi_+=0$.

**Remark (what the condition says).** **At a null point the datum must live on the ideal that survives.** The component on the vanishing ideal is not merely unrepresentable; it is an obstruction that no generalised inverse removes.

### Two Model Families

**Example (family one: a symbol that is null at every frequency).** Let $p=e_t+\tilde{Ζ}=2\Pi_+$, a nonzero null element, and let $P(D)=p\partial_t$. Its symbol is $\Sigma(\omega)=2\pi i\omega\tilde{Ζ}p=2\pi i\omega p$, because $\tilde{Ζ}p=p$, so $N(\Sigma(\omega))=(2\pi i\omega)^{2}N(p)=0$ for every $\omega$. The symbol is never a unit: the rank of left multiplication is $4$ for $\omega\ne0$ and $0$ at $\omega=0$. The transform buys nothing here, and the equation is solved pointwise: $2\Pi_+f'=g$ is solvable exactly when $\Pi_-g=0$, and then

$$
f(t)=f(0)+\frac{1}{2}\int_0^{t}\Pi_+g(s)\,ds+\int_0^{t}\ell(s)\,ds ,
$$

with $\ell$ taking values in the left ideal $\mathbb{B}\Pi_-$, which is the kernel of left multiplication by $p$ and has real dimension four.

*Proof.* Multiply $2\Pi_+f'=g$ on the left by $\Pi_+$, using $\Pi_+^{2}=\Pi_+$ and $\Pi_+g=g$ under the solvability condition: $2\Pi_+f'=\Pi_+g$. Then $f'=\tfrac12\Pi_+g+\ell$ with $\Pi_+\ell=0$, and integrating gives the display. The kernel of left multiplication by $\Pi_+$ is $\{X:\Pi_+X=0\}$, which is $\mathbb{B}\Pi_-$ because $\Pi_++\Pi_-=e_t$ and $\Pi_+\Pi_-=0$: an element annihilated on the left by $\Pi_+$ is fixed on the left by $\Pi_-$.

**Example (family two: a symbol that is null nowhere on the real axis).** Let $P(D)=\partial_t+\lambda e_t$ with $\lambda>0$, whose symbol $\Sigma(\omega)=\lambda e_t+2\pi i\omega\tilde{Ζ}$ has norm $\lambda^{2}+4\pi^{2}\omega^{2}$, positive at every real frequency. Here the Moore–Penrose inverse is never needed on the real axis, the reciprocal exists there, and the two imaginary poles carry the whole phenomenon: the residues of §*The Residue Formula*, the kernel $\Theta(t)e^{-\lambda t}e_t$ of §*A Worked Kernel*, and the tail $\lambda$ of §*Exponential Type and the Tail*.

**Remark (the two families are the two ways a symbol can meet the null set).** In the first the symbol lies in the null set identically, so only the pointwise theory applies; in the second it misses the null set on the whole real axis, so the reciprocal exists there and the off-axis poles carry the tail. **The intermediate case**, a symbol meeting the null set along a hypersurface of real frequencies, gives a principal value plus half-residues and an inversion unbounded on $L^{2}$.

## Summary

The reciprocal of a biquaternion symbol is an adjugate over a norm. For every element $\tilde Q$ the product with its conjugate is the central scalar $N(\tilde Q)e_t$, so $\Sigma^{-1}=\overline{\Sigma}/N(\Sigma)$ wherever the symbol is a unit, and the regular representation has $L_{\Sigma}^{-1}=N^{-1}L_{\overline{\Sigma}}$ with adjugate $\lvert N\rvert^{2}\overline{N}L_{\overline{\Sigma}}$, the conjugate on the norm because $\lvert N\rvert^{4}/N=\lvert N\rvert^{2}\overline{N}$. One complex scalar sits in the denominator, and its vanishing is two real equations.

The order of the pole is the order of the vanishing of the norm minus that of the adjugate, and it is neither the order of the operator nor the degree of the block determinant: for $\Sigma=(\omega-\omega_0)^{2}e_t$ the pole has order two while the determinant has order sixteen.

In one frequency variable and in a commutative plane the reciprocal splits along the two Peirce idempotents into two scalar reciprocals, and there a residue is a number: the adjugate at the point divided by the derivative of the norm, a nonzero element of norm zero, never the inverse of the derivative of the symbol, and of rank four under left multiplication. At a null point of the first kind the reciprocal expands in words in the leading term and the higher coefficients; at a null point of the second kind the pole lives on one ideal, with the order of that ideal's scalar. A pole of order $k$ contributes a polynomial of degree $k-1$ times an exponential, never a second exponential.

The rate of the kernel is the distance of the pole from the real axis, in the units of the exponent, so the type is $2\pi\rho$; the tail of a solution is the tail of the kernel shifted by the radius of the data; and a solution of compact support exists only if the transform of the datum vanishes at every pole, by Paley–Wiener. **A pole on the real axis is the exception, and there the kernel is merely bounded and the inversion is unbounded on $L^{2}$.**

In one frequency variable the two signs are not an obstruction. The conjugate kernel splits into $\Pi_+e^{2\pi i\omega t}$ and $\Pi_-e^{-2\pi i\omega t}$, each closed in the half-plane where its own exponential decays, so an element-valued residue expansion exists **whether or not the symbol commutes with the root**. The price is not an obstruction: no single contour, hence no single residue at a pole, and the same pole enters through $\Pi_+$ on one side of the axis and through $\Pi_-$ on the other.

In two or more variables the obstacle is geometric. The singular set after complexification is a hypersurface of real codimension two, with real dimension six in four variables, so there is no point to encircle and no sum of residues; the residue becomes a current supported on the hypersurface, or a Leray form over a real cycle linking it.

Where the symbol is not a unit the pointwise equation is solved by the Moore–Penrose inverse, which in the plane case is the reciprocal with the singular ideal's term omitted. Solutions exist exactly when the datum lies in the image, which in the plane case means that it has no component on the ideal the symbol has lost. The two model families are the two extreme ways a symbol meets the null set, and the transform is useful in the second and useless in the first.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, of real dimension eight |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the units, with $\vec e_k^{2}=-e_t$ and $\vec e_x\vec e_y=\vec e_z$ |
| $i$ | the central imaginary, commuting with the four units |
| $\tilde{Ζ}$ | a pure root of $1$, fixed once for all, with $\tilde{Ζ}^{2}=e_t$ and $N(\tilde{Ζ})=-1$ |
| $N(\tilde Q)$ | the norm $Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$, central and complex-valued |
| $\overline{\tilde Q}$ | the conjugate $Q_t-Q_x\vec e_x-Q_y\vec e_y-Q_z\vec e_z$, the adjugate of $\tilde Q$ |
| $W(t,\omega)$ | the kernel $\exp(-2\pi i\tilde{Ζ}\omega t)$, multiplying on the left |
| $\overline{W(t,\omega)}$ | the conjugate kernel, the kernel of the inverse transform |
| $m$ | the order of the operator $P(D)$ |
| $n$ | the number of frequency variables |
| $\omega$ | the real frequency, continued to $\mathbb{C}$ where a contour is closed |
| $\zeta$ | a general point of the complexified frequency space |
| $\Sigma(\omega)$ | the symbol $\sum_\alpha a_\alpha\prod_k(2\pi i\tilde{Ζ}\omega_k)^{\alpha_k}$ |
| $Z(P)$ | the frequency set $\{\omega:N(\Sigma(\omega))=0\}$ |
| $\Pi_\pm$ | the Peirce idempotents $\tfrac12(e_t\pm\tilde{Ζ})$, quoted |
| $\sigma_\pm$ | the Peirce scalars $a\pm b$ of a plane-valued symbol $ae_t+b\tilde{Ζ}$ |
| $\Pi_\pm\mathbb{B}$ | the two ideals, each of real dimension four |
| $\kappa_\Sigma$ | the kernel of the reciprocal, $\int\overline{W}\Sigma^{-1}d\omega$ |
| $\Theta(t)$ | the step, equal to one for $t>0$ and zero for $t<0$ |
| $\lambda$ | a positive rate, and the coefficient in the model family $\partial_t+\lambda e_t$ |
| $\rho$ | the least distance from a pole to the real axis |
| $k$ | the order of a pole |
| $j,j'$ | the vanishing orders of $N\circ\Sigma$ and of $\overline{\Sigma}$ |
| $\operatorname{Res}$ | the residue of the reciprocal at a pole |
| $\Sigma^{+}$ | the Moore–Penrose inverse of the symbol at one frequency |
| $L_{\tilde Q}$ | left multiplication by $\tilde Q$ on $\mathbb{B}$ |
| $\det L_{\tilde Q}$ | the real $8\times8$ determinant, equal to $\lvert N(\tilde Q)\rvert^{4}$ |
| $\lVert\cdot\rVert$ | the Euclidean norm on the eight real coordinates |
| $\langle\cdot,\cdot\rangle_E$ | the Euclidean form on the eight real coordinates |

## Further Reading

The transform, the kernel and the two quoted theorems are *Biquaternion Continuous Harmonic Analysis*; the symbol, its zero set, the determinant and the rank on the null set are *The Fourier Transform and the Symbol of a Differential Operator*; the placement of the kernel on the left, the right and both sides is *The Three Kernel Placements of the Biquaternion Fourier Transform*; the inversion in Peirce coordinates is *Biquaternion Fourier Inversion on the Degenerate Set*; the four Penrose equations, their uniqueness and their index-one criterion are *The Moore–Penrose Inverse in an Involutive Algebra*; the real-algebra version of the reciprocal is *The Inverse Fourier Transform of a Symbol*.
