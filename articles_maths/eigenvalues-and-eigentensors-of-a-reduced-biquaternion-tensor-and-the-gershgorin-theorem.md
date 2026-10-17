# __Eigenvalues and Eigentensors of a Reduced Biquaternion Tensor and the Gershgorin Theorem__

## Introduction

A square tensor of even order acts on the tensors of half its order by the Einstein product of *The Einstein Product of Reduced Biquaternion Tensors*, and an **eigentensor** $X$ with **eigenvalue** $\lambda$ satisfies $AX=\lambda X$. The eigenvalue is written on the right as well as on the left, because the algebra is commutative; there is no separate left spectrum as in the quaternion case. But the algebra has zero divisors, and an eigentensor may lie in a single idempotent coordinate of the algebra; the other coordinate of the eigenvalue is then free. The spectrum is therefore not a finite set: it is the union of two families of complex lines. This is the structural difference from the complex and the quaternion cases, and it governs everything the article proves.

The article defines the problem, proves the reduction to the two complex coordinate tensors, states the pairing theorem of the source for the eigentensors with both coordinates nonzero, proves the **Gershgorin theorem** in the coordinate form, and closes with the eigenvalues of a power and the roots.

**The results.** The spectrum of a square tensor is the union of the two coordinate spectra of its two complex coordinate tensors; it is nonempty and unbounded. The eigenvalues with an eigentensor whose two coordinates are both nonzero are exactly the pairs of an eigenvalue of each coordinate tensor, which is the pairing theorem of the source. The Gershgorin theorem locates at least one coordinate of an eigenvalue in the Gershgorin set of the corresponding complex tensor, so the spectrum lies in the union of the two sets over the complex Gershgorin sets. If $A^{n}=a\mathrm I$, every coordinate of an eigenvalue whose eigentensor coordinate does not vanish is an $n$-th root of the corresponding coordinate of $a$; the $n^{2}$ roots of the source, displayed for a unit $a$, are computed coordinatewise but are neither the spectrum, nor a subset of it, nor a superset of it.

**Boundaries.** The Einstein product, the matricisation and the units are *The Einstein Product of Reduced Biquaternion Tensors*, above this article. The spectrum of an **element**, the pair of its idempotent coordinates, is *Reduced Biquaternion Spectral Theory*; this article treats the spectrum of a **tensor**. The bar, the natural sign and the star are *The Two Involutions and the Group of Involutions*, and the algebraic norm $\langle\cdot\rangle_{\natural}$ is *The Four Products, Their Forms and Their Algebraic Norms*. The t-product is a different product, and its spectral reading is not the subject here. The complex eigenvalue problem, the discs and the maximal-entry argument are the classical ones of Horn and Johnson, *Matrix Analysis*.

**Conventions.** The tensor is a plain capital typed by its exponent, $A\in\mathbb{B}_{\mathrm{r}}^{n_{1}\times\cdots\times n_{m}\times n_{1}\times\cdots\times n_{m}}$ in the square case, and its entries are $a_{PL}$ at the row multi-index $P$ and the column multi-index $L$. The two complex coordinate tensors are $A_{(1)}$ and $A_{(2)}$, with $A=A_{(1)}\Pi_++A_{(2)}\Pi_-$, and the element $\lambda$ is written $\lambda_{(1)}\Pi_++\lambda_{(2)}\Pi_-$; the coordinates $\lambda_{(1)},\lambda_{(2)}$ are the idempotent coordinates written $q_{1},q_{2}$ in *Reduced Biquaternion Spectral Theory*. The **spectrum** of $A$ is $\sigma(A)$; the **spectrum** of a complex tensor $M$ is the set of complex $z$ with $MX=zX$ for some nonzero $X$, and its Gershgorin set is $\Gamma(M)$. The idempotents are $\Pi_+=\tfrac12(1+j)$ and $\Pi_-=\tfrac12(1-j)$.

## The Eigenvalue Problem

**Definition.** Let $A$ be square of order $2m$, with the modes $n_{1},\dots,n_{m}$ on both sides, and let $X$ be a tensor of order $m$ with the modes $n_{1},\dots,n_{m}$. A reduced biquaternion $\lambda$ is an **eigenvalue** of $A$ when $AX=\lambda X$ for some nonzero $X$, and $X$ is an **eigentensor** of $\lambda$. The **spectrum** $\sigma(A)$ is the set of eigenvalues.

**Proposition (the orders two and four).** For $m=1$ the definition is the eigenvalue problem of a square matrix over $\mathbb{B}_{\mathrm{r}}$, with the matrix product; for $m=2$ it is the problem of a tensor of order four acting on a tensor of order two.

*Proof.* The Einstein product of an order-$2m$ tensor and an order-$m$ tensor is the contraction of the $m$ trailing indices of the first against the $m$ indices of the second, which is the matrix-vector product when $m=1$ and its multi-index form otherwise.

**Remark (the two sides).** The algebra is commutative, so the eigenvalue may be written on either side of $X$, $AX=\lambda X=X\lambda$; there is no asymmetric spectrum as in the quaternion case.

**Theorem (the coordinate reduction).** Write $A=A_{(1)}\Pi_++A_{(2)}\Pi_-$, $X=X_{(1)}\Pi_++X_{(2)}\Pi_-$ and $\lambda=\lambda_{(1)}\Pi_++\lambda_{(2)}\Pi_-$. Then $AX=\lambda X$ if and only if
$$
A_{(1)}X_{(1)}=\lambda_{(1)}X_{(1)},\qquad A_{(2)}X_{(2)}=\lambda_{(2)}X_{(2)}.
$$

*Proof.* The idempotents are orthogonal and idempotent, $\Pi_+\Pi_-=0$ and $\Pi_\pm^{2}=\Pi_\pm$, and the algebra is commutative, so $AX=A_{(1)}X_{(1)}\Pi_++A_{(2)}X_{(2)}\Pi_-$ and $\lambda X=\lambda_{(1)}X_{(1)}\Pi_++\lambda_{(2)}X_{(2)}\Pi_-$; the two sides are equal exactly when the two coordinates are equal.

## The Spectrum as the Union of the Two Coordinate Spectra

**Theorem (the spectrum is the union of the two coordinate spectra).**
$$
\sigma(A)=\bigl\{\lambda_{(1)}\Pi_++\lambda_{(2)}\Pi_-:\lambda_{(1)}\in\sigma(A_{(1)})\ \text{or}\ \lambda_{(2)}\in\sigma(A_{(2)})\bigr\}.
$$

*Proof.* If $\lambda$ is an eigenvalue with eigentensor $X$, then $X\neq0$, so at least one coordinate $X_{(i)}$ is nonzero, and the coordinate equation of the reduction makes $\lambda_{(i)}$ an eigenvalue of $A_{(i)}$. Conversely, if $\lambda_{(1)}\in\sigma(A_{(1)})$ with eigentensor $Y\neq0$, the tensor $X=Y\Pi_+$ is nonzero and $AX=\lambda X$ for every $\lambda_{(2)}$, because the second coordinate of $X$ vanishes; symmetrically for the second coordinate.

**Corollary (the source's pairing theorem).** An eigenvalue $\lambda$ has an eigentensor with both coordinates nonzero if and only if $\lambda_{(1)}\in\sigma(A_{(1)})$ and $\lambda_{(2)}\in\sigma(A_{(2)})$. The source writes the two complex tensors $B_{1}$ and $B_{2}$; they are $A_{(1)}$ and $A_{(2)}$ here.

*Proof.* If $X$ has both coordinates nonzero, the two coordinate equations hold with $X_{(i)}\neq0$, so each $\lambda_{(i)}$ is an eigenvalue of $A_{(i)}$. Conversely, given nonzero eigentensors $Y_{1}$ of $A_{(1)}$ and $Y_{2}$ of $A_{(2)}$, the tensor $X=Y_{1}\Pi_++Y_{2}\Pi_-$ has $X_{(1)}=Y_{1}$ and $X_{(2)}=Y_{2}$, both nonzero, and $AX=A_{(1)}Y_{1}\Pi_++A_{(2)}Y_{2}\Pi_-=\lambda_{(1)}Y_{1}\Pi_++\lambda_{(2)}Y_{2}\Pi_-=\lambda X$.

**Remark (the labels of the source).** The source labels its idempotents $e_{1}=\tfrac12(1-j)$ and $e_{2}=\tfrac12(1+j)$, the reverse of $\Pi_+$ and $\Pi_-$. Its display $q=(a+b)e_{1}+(a-b)e_{2}$ gives $a-bj$, so the labels are interchanged in that display; with the labels read the other way, its $B_{1}$, the sum of its two complex tensors, is the $\Pi_+$ coordinate $A_{(1)}$ and its $B_{2}$, their difference, is $A_{(2)}$.

**Remark (the hypothesis of the source).** The source states the equivalence for an arbitrary eigentensor, and the "only if" direction then fails when one idempotent coordinate of the eigentensor vanishes: for $A=\mathrm I$ of order two and $\lambda=\Pi_++100\Pi_-$, the tensor $X$ with the entry $\Pi_+$ at the first row and first column and zeros elsewhere has $X_{(2)}=0$ and $AX=\lambda X$; the source writes $X=X_{1}+X_{2}j$, so its second condition would require $X_{1}-X_{2}=X_{(2)}$ to be a nonzero eigentensor of $B_{2}$, and it is the zero tensor; the zero tensor is not an eigentensor, so the condition fails and $\lambda_{(2)}$ is not made an eigenvalue, while the left-hand side holds. The restriction to the eigentensors with both coordinates nonzero is what the equivalence needs.

**Corollary (the spectrum is nonempty and unbounded).** For positive sizes each coordinate tensor has an eigenvalue, and through each one passes a complex line of eigenvalues of $A$; consequently $\sigma(A)$ is nonempty and unbounded.

*Proof.* A square complex tensor of order $2m$ has an eigenvalue, being the eigenvalue problem of its matricisation over $\mathbb{C}$; if $\lambda_{(1)}\in\sigma(A_{(1)})$, the proof of the theorem gives the eigenvalue $\lambda_{(1)}\Pi_++\lambda_{(2)}\Pi_-$ for every $\lambda_{(2)}\in\mathbb{C}$, a complex line.

## The Gershgorin Theorem

**Definition (the Gershgorin set of a complex tensor).** For a square complex tensor $M$ of order $2m$,
$$
\Gamma(M)=\bigcup_{P}\Bigl\{z\in\mathbb{C}:\lvert z-m_{PP}\rvert\le\sum_{L\neq P}\lvert m_{PL}\rvert\Bigr\}.
$$

**Lemma (the complex theorem).** $\sigma(M)\subseteq\Gamma(M)$.

*Proof.* Let $MX=zX$ with $X\neq0$ and choose $Q$ with $\lvert x_{Q}\rvert\ge\lvert x_{L}\rvert$ for every $L$. The $Q$-th entry of $MX=zX$ reads $(z-m_{QQ})x_{Q}=\sum_{L\neq Q}m_{QL}x_{L}$; taking moduli, dividing by $\lvert x_{Q}\rvert>0$ and bounding $\lvert x_{L}\rvert\le\lvert x_{Q}\rvert$ gives $\lvert z-m_{QQ}\rvert\le\sum_{L\neq Q}\lvert m_{QL}\rvert$.

**Theorem (the Gershgorin theorem for reduced biquaternion tensors).**
$$
\sigma(A)\subseteq\bigl\{\lambda_{(1)}\Pi_++\lambda_{(2)}\Pi_-:\lambda_{(1)}\in\Gamma(A_{(1)})\ \text{or}\ \lambda_{(2)}\in\Gamma(A_{(2)})\bigr\}.
$$

*Proof.* Let $\lambda$ be an eigenvalue with eigentensor $X$. Some coordinate $X_{(i)}$ is nonzero, and the coordinate reduction makes $\lambda_{(i)}$ an eigenvalue of $A_{(i)}$; the complex lemma gives $\lambda_{(i)}\in\Gamma(A_{(i)})$, and the conclusion follows.

**Remark (the modulus of the source).** The source equips an element $\lambda$ with the modulus
$$
\lVert\lambda\rVert=\bigl\lvert\lambda\bar\lambda\lambda^{\natural}\lambda^{*}\bigr\rvert^{1/4}=\lvert\lambda_{(1)}\lambda_{(2)}\rvert^{1/2}=\lvert\langle\lambda\rangle_{\natural}\rvert^{1/2},
$$
where $\lambda\bar\lambda\lambda^{\natural}\lambda^{*}=\langle\lambda\rangle_{\natural}\overline{\langle\lambda\rangle_{\natural}}$ and $\langle\lambda\rangle_{\natural}=\lambda_{(1)}\lambda_{(2)}$; it states the inclusion with this modulus. That expression is not a norm on the algebra. It vanishes on the nonzero zero divisors, $\lVert\Pi_+\rVert=\lVert\Pi_-\rVert=0$, so the division by the modulus of the maximal entry of $X$, which is the last step of the source's proof, is a division by zero when that entry is a zero divisor; and it fails the triangle inequality, $\lVert\Pi_++\Pi_-\rVert=1$ while $\lVert\Pi_+\rVert+\lVert\Pi_-\rVert=0$, so the bound of the modulus of a sum by the sum of the moduli, which is the step before, does not follow. **The inclusion of the source itself fails**: for $A=\begin{smallmatrix}0&1\\1&0\end{smallmatrix}$ and $\lambda=\Pi_++100\Pi_-$, the tensor whose first column is $(\Pi_+,\Pi_+)^{\mathsf T}$ and whose second column is zero is an eigentensor of $\lambda$, while $\lVert\lambda\rVert=\sqrt{\lvert1\cdot100\rvert}=10$ and the radius is $1$ at each of the two diagonal indices. The coordinate form above is the correct statement, and the maximal-entry argument over $\mathbb{C}$ proves it.

**Remark (the shape of the bound).** The containing set of the theorem is $\Gamma(A_{(1)})\times\mathbb{C}\cup\mathbb{C}\times\Gamma(A_{(2)})$ in the two coordinates: a union of two cylinders over the complex plane, each with the other coordinate as its axis. It constrains one coordinate only and is unbounded, unlike a classical Gershgorin disc, and it can be strictly larger than the spectrum.

## Powers and Roots

**Theorem (the eigenvalues of a power).** Let $A^{n}=a\mathrm I$ for a positive integer $n$ and an element $a$, and let $\lambda$ be an eigenvalue of $A$ with eigentensor $X$. Then $\lambda_{(i)}^{n}=a_{(i)}$ for each coordinate $i$ with $X_{(i)}\neq0$. In particular
$$
\sigma(A)\subseteq\bigl\{\lambda_{(1)}\Pi_++\lambda_{(2)}\Pi_-:\lambda_{(1)}^{n}=a_{(1)}\ \text{or}\ \lambda_{(2)}^{n}=a_{(2)}\bigr\}.
$$

*Proof.* By induction $A^{n}X=\lambda^{n}X$, and $A^{n}=a\mathrm I$ gives $\lambda^{n}X=aX$. In the coordinate $i$ with $X_{(i)}\neq0$ this is $(\lambda_{(i)}^{n}-a_{(i)})X_{(i)}=0$, and $X_{(i)}$ has a nonzero entry, so $\lambda_{(i)}^{n}=a_{(i)}$. The inclusion follows because some coordinate of $X$ is nonzero.

**Corollary (the roots).** With $a$ a unit, so that $a_{(1)},a_{(2)}\neq0$, and $a_{(k)}=r_{k}e^{i\theta_{k}}$, $0\le\theta_{k}<2\pi$, the roots of $\lambda^{n}=a$ are
$$
\lambda_{s,t}=(\sqrt[n]{a_{(1)}})_{s}\Pi_++(\sqrt[n]{a_{(2)}})_{t}\Pi_-,\qquad (\sqrt[n]{z})_{s}=r^{1/n}e^{i(\theta+2\pi s)/n},
$$
with $s,t=0,\dots,n-1$.

*Proof.* The equation $\lambda^{n}=a$ is the pair of the two coordinate equations $\lambda_{(i)}^{n}=a_{(i)}$, and the $n$-th roots of a nonzero complex number are the displayed $n$ values.

**Remark (the list of the source).** The source writes the $n^{2}$ values $\lambda_{s,t}$ as the set of eigenvalues, and deduces $\lambda^{n}=a$ from $\lambda^{n}X=aX$ by cancelling $X$; the cancellation is invalid when $\lambda^{n}-a$ is a nonzero zero divisor, and then one coordinate of $X$ is zero. The values are neither the spectrum, nor a subset of it, nor a superset of it: for $A=\mathrm I$ and $n=2$, the value $\lambda=(-1)\Pi_++(-1)\Pi_-$ is one of the four and is not an eigenvalue of $\mathrm I$, since $\lambda-1=-2$ and $-2X\neq0$ for $X\neq0$; and $\lambda=(1)\Pi_++(5)\Pi_-$ is an eigenvalue of $\mathrm I$, with the eigentensor whose first entry is $\Pi_+$ and whose other entries are zero, and is not one of the four. The $n^{2}$ values are the points whose two coordinates are both roots of the corresponding coordinates of $a$, and the exact statement is the union of the two coordinate spectra, each coordinate spectrum a subset of the $n$-th roots of the corresponding coordinate of $a$.

## Verification

The statements were checked by recomputation on random order-four tensors with modes of size two, and on constructed eigenpairs of matrices and of order-four tensors, the deviations found at the level of the floating-point noise.

- The union theorem: an eigentensor of one coordinate tensor, its other coordinate zero, is an eigentensor of $A$ at every value of the free coordinate of $\lambda$.
- The maximal-entry step of the Gershgorin lemma, on a constructed eigenpair.
- The restriction in the pairing theorem: for $A=\mathrm I$ and $\lambda=\Pi_++100\Pi_-$, the eigentensor with $X_{(2)}=0$ satisfies $AX=\lambda X$, while $100$ is not an eigenvalue of the second coordinate tensor.
- The counterexample to the source's inclusion: for $A=\begin{smallmatrix}0&1\\1&0\end{smallmatrix}$ and $\lambda=\Pi_++100\Pi_-$ the modulus is $10$ and the radius is $1$.
- The two counterexamples of the roots: for $A=\mathrm I$ and $n=2$, the value $(-1)\Pi_++(-1)\Pi_-$ is not an eigenvalue, and $(1)\Pi_++(5)\Pi_-$ is.
- The clause of the power theorem: for $A=2\mathrm I$ and $n=2$, the eigenvalue $2\Pi_++3\Pi_-$ has $\lambda_{(2)}^{2}=9\neq4=a_{(2)}$, and its eigentensor has zero second coordinate.
- The relaxed hypothesis of the power theorem: for $A=\mathrm I\Pi_++A_{(2)}\Pi_-$ with $A_{(2)}^{2}=0$ and $a=\Pi_+$, the eigenvalue $\Pi_++5\Pi_-$ has $\lambda_{(2)}^{2}=25\neq0=a_{(2)}$, and its eigentensor has zero second coordinate.

## Summary

A square tensor of order $2m$ acts on the tensors of order $m$ by the Einstein product, and its **eigenvalues** are the reduced biquaternions $\lambda$ with $AX=\lambda X$ for a nonzero **eigentensor** $X$. The algebra is commutative, so the eigenvalue is written on either side and there is no left-right asymmetry. The algebra has zero divisors, so the spectrum is not a finite set: the **coordinate reduction** gives the pair of the two complex eigenvalue problems, and the **spectrum is the union of the two coordinate spectra** of the two complex coordinate tensors, nonempty and unbounded. An eigenvalue has an eigentensor with both coordinates nonzero exactly when its two coordinates are eigenvalues of the two coordinate tensors, which is the pairing theorem of the source restricted to those eigentensors, the two complex tensors $B_{1}$ and $B_{2}$ of the source being $A_{(1)}$ and $A_{(2)}$. The **Gershgorin theorem** holds in the coordinate form: at least one coordinate of an eigenvalue lies in the Gershgorin set of the corresponding complex tensor, with the maximal-entry proof over $\mathbb{C}$; the source's single inclusion with the modulus $\lvert\langle\cdot\rangle_{\natural}\rvert^{1/2}$ fails: that modulus vanishes on the zero divisors, fails the triangle inequality, and the counterexample of the remark violates the inclusion. If $A^{n}=a\mathrm I$, each coordinate of an eigenvalue is an $n$-th root of the corresponding coordinate of $a$ whenever the eigentensor coordinate is nonzero; for a unit $a$ the roots are displayed coordinatewise, and the $n^{2}$ roots of the source are not the spectrum.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$ | a square tensor of order $2m$, with the modes $n_{1},\dots,n_{m}$ on both sides |
| $X$ | an eigentensor, a tensor of order $m$ |
| $\lambda$ | an eigenvalue, an element of the algebra |
| $\sigma(A)$ | the spectrum, the set of eigenvalues |
| $A_{(1)},A_{(2)}$ | the two complex coordinate tensors, $A=A_{(1)}\Pi_++A_{(2)}\Pi_-$ |
| $\lambda_{(1)},\lambda_{(2)}$ | the idempotent coordinates of $\lambda$ |
| $\Pi_+,\Pi_-$ | the idempotents $\tfrac12(1\pm j)$ |
| $\mathrm I$ | the unit tensor of the square case, $\mathrm I_{PL}=\delta_{PL}$ |
| $\langle\lambda\rangle_{\natural}$ | the algebraic norm of an element, $\lambda_{(1)}\lambda_{(2)}$ |
| $\Gamma(M)$ | the Gershgorin set of a square complex tensor $M$ |
| $(\sqrt[n]{z})_{s}$ | the $n$-th root $r^{1/n}e^{i(\theta+2\pi s)/n}$ of $z=re^{i\theta}$ |

## Further Reading

- *The Einstein Product of Reduced Biquaternion Tensors* (`articles_maths/the-einstein-product-of-reduced-biquaternion-tensors.md`), above this article, for the product, the matricisation and the units.
- *Reduced Biquaternion Spectral Theory* (`articles_maths/reduced-biquaternion-spectral-theory.md`), for the spectrum of an element and the idempotent coordinates.
- *The Two Involutions and the Group of Involutions* (`articles_maths/the-two-involutions-and-the-group-of-involutions-of-the-reduced-biquaternions.md`), for the bar, the natural sign and the star.
- *The Four Products, Their Forms and Their Algebraic Norms* (`articles_maths/the-four-products-their-forms-and-their-algebraic-norms-of-the-reduced-biquaternions.md`), for the algebraic norm $\langle\cdot\rangle_{\natural}$.
- Ting-Ting Liu and Shao-Wen Yu, "Some Properties of Reduced Biquaternion Tensors", *Symmetry* 16 (2024), 1260, for the eigenvalue problem, the Gershgorin theorem and the roots of the source.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis*, 2nd edition (Cambridge University Press, 2013), for the Gershgorin disc theorem and its maximal-entry proof.
- Y. C. Wang and Y. M. Wei, "Generalized eigenvalue for even order tensors via Einstein product and its applications in multilinear control systems", *Computational and Applied Mathematics* 41 (2022), 419, for the eigenvalue problem of the Einstein product in the real case.
