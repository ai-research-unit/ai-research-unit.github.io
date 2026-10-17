# __Reduced Biquaternion Regular Functions__

## Introduction

This article studies **regular** reduced biquaternion-valued functions, the solutions of the first-order system defined by the reduced biquaternion Cauchy–Riemann operator. It follows *Reduced Biquaternion Analysis*, where the operator and its conjugate are constructed, and it records the system of equations, the examples, the harmonicity and the factorization of the Laplacian, the role of the zero divisors, and the relations to the biquaternion regular functions and to Clifford analysis. The treatment is purely mathematical, and the operator is only ever called the **Cauchy–Riemann operator**.

Throughout the basis is $1,i,j,ij$ with $i^{2}=-1$, $j^{2}=+1$ and $ji=ij$; the element is $Q_\pm=Q_++jQ_-$ with $Q_+=q_++iq'_+$ and $Q_-=q_-+iq'_-$; the idempotent coordinates are $Q_{++}=Q_++Q_-$ and $Q_{--}=Q_+-Q_-$, and $Q_\pm=Q_{++}\Pi_++Q_{--}\Pi_-$ with $\Pi_{\pm}=\tfrac12(1\pm j)$. The squared Euclidean norm is $\langle Q_\pm\rangle_{\natural*}=\lvert Q_+\rvert^{2}+\lvert Q_-\rvert^{2}=\tfrac12(\lvert Q_{++}\rvert^{2}+\lvert Q_{--}\rvert^{2})$, and a general function is written $f$ or $\Phi$.

## The Variable and Its Structure

**The algebra carries two commuting complex structures, and the two idempotent coordinates are the two independent complex variables of the theory.**

**Definition.** On the real algebra $\mathbb{B}_{\mathrm{r}}$ define the two real-linear maps
$$
J_{i}(Q_\pm)=iQ_\pm,\qquad J_{ij}(Q_\pm)=ijQ_\pm .
$$
They are the **two complex structures** of the algebra, and they commute.

**Theorem (the coordinate structure).** $J_{i}$ and $J_{ij}$ are real-linear, satisfy $J_{i}^{2}=J_{ij}^{2}=-\mathrm{id}$, and commute, so each makes $\mathbb{B}_{\mathrm{r}}$ a two-dimensional complex vector space. The maps $Q_\pm\mapsto Q_{++}=Q_++Q_-$ and $Q_\pm\mapsto Q_{--}=Q_+-Q_-$ are complex-linear isomorphisms onto $\mathbb{C}$, and
$$
Q_\pm\longmapsto(Q_{++},Q_{--})
$$
is a complex-linear isomorphism $\mathbb{B}_{\mathrm{r}}\to\mathbb{C}^{2}$ under which the multiplication is componentwise and the norm is $K=\tfrac12(\lvert Q_{++}\rvert^{2}+\lvert Q_{--}\rvert^{2})$.

*Proof.* $i^{2}=-1$ and $(ij)^{2}=i^{2}j^{2}=-1$, and the two multiplications commute because the algebra is commutative. The coordinates $Q_{++},Q_{--}$ are the two characters $\lambda_+,\lambda_-$, and the idempotents $\Pi_+,\Pi_-$ diagonalise the product, $(Q_{++}\Pi_++Q_{--}\Pi_-)(Q_{++}'\Pi_++Q_{--}'\Pi_-)=Q_{++}Q_{++}'\Pi_++Q_{--}Q_{--}'\Pi_-$; the norm statement is $K=\lvert Q_+\rvert^{2}+\lvert Q_-\rvert^{2}$ with $Q_+=\tfrac12(Q_{++}+Q_{--})$ and $Q_-=\tfrac12(Q_{++}-Q_{--})$.

## The Cauchy–Riemann Operator and Its Conjugate

**Definition (Wirtinger derivatives).** On the complex coordinates $Q_{++},Q_{--}$, equivalently $Q_+,Q_-$, the **Wirtinger derivatives** are
$$
\partial/\partial Q_{++}=\tfrac12\bigl(\partial/\partial Q_++\partial/\partial Q_-\bigr),\quad
\partial/\partial\bar Q_{++}=\tfrac12\bigl(\partial/\partial\bar Q_++\partial/\partial\bar Q_-\bigr),\quad
\partial/\partial Q_{--}=\tfrac12\bigl(\partial/\partial Q_+-\partial/\partial Q_-\bigr),\quad
\partial/\partial\bar Q_{--}=\tfrac12\bigl(\partial/\partial\bar Q_+-\partial/\partial\bar Q_-\bigr),
$$
with the real-coordinate forms
$$
\partial/\partial\bar Q_{++}=\tfrac14\bigl[(\partial/\partial q_++\partial/\partial q_-)+i(\partial/\partial q'_++\partial/\partial q'_-)\bigr],\qquad
\partial/\partial\bar Q_{--}=\tfrac14\bigl[(\partial/\partial q_+-\partial/\partial q_-)+i(\partial/\partial q'_+-\partial/\partial q'_-)\bigr].
$$

**Definition (the operator).** The **reduced Cauchy–Riemann operator** and its **conjugate** are
$$
\bar\partial=\Pi_+\partial/\partial\bar Q_{++}+\Pi_-\partial/\partial\bar Q_{--},\qquad
\partial=\Pi_+\partial/\partial Q_{++}+\Pi_-\partial/\partial Q_{--}.
$$
On the idempotent decomposition $f=g_{1}\Pi_++g_{2}\Pi_-$ they act coefficientwise,
$$
\bar\partial f=\bigl(\partial/\partial\bar Q_{++}\,g_{1}\bigr)\Pi_++\bigl(\partial/\partial\bar Q_{--}\,g_{2}\bigr)\Pi_-,\qquad
\partial f=\bigl(\partial/\partial Q_{++}\,g_{1}\bigr)\Pi_++\bigl(\partial/\partial Q_{--}\,g_{2}\bigr)\Pi_-.
$$

**Theorem (second order and the factorization).** The two operators commute and their product is
$$
\bar\partial\partial=\partial\bar\partial=\partial^2/\partial Q_{++}\partial\bar Q_{++}\,\Pi_++\partial^2/\partial Q_{--}\partial\bar Q_{--}\,\Pi_-,
$$
and the Euclidean Laplacian is the sum of the two idempotent components of $8\bar\partial\partial$,
$$
\Delta=\partial^2/\partial q_+^2+\partial^2/\partial q'^2_++\partial^2/\partial q_-^2+\partial^2/\partial q'^2_-=8\bigl(\partial^2/\partial Q_{++}\partial\bar Q_{++}+\partial^2/\partial Q_{--}\partial\bar Q_{--}\bigr).
$$

*Proof.* The idempotents are orthogonal and act as the identity on the two coordinates, so the products collapse to the diagonal terms; the two Wirtinger derivatives commute because partial derivatives do; and the identity for $\Delta$ is the Laplacian theorem of *Reduced Biquaternion Analysis*, §*The Differential Operators*.

**Theorem (the symbol and the characteristic set).** The principal symbol of $\partial/\partial\bar Q_{++}$ at a covector $(\xi_{a},\xi_{a'},\xi_{b},\xi_{b'})$ is $\tfrac14[(\xi_{a}+\xi_{b})+i(\xi_{a'}+\xi_{b'})]$, which vanishes exactly on the two-plane $\xi_{a}+\xi_{b}=0$, $\xi_{a'}+\xi_{b'}=0$; the symbol of $\partial/\partial\bar Q_{--}$ vanishes on the two-plane $\xi_{a}-\xi_{b}=0$, $\xi_{a'}-\xi_{b'}=0$. The characteristic set of the operator is the union of the two two-planes, and the operator is elliptic at no point.

*Proof.* The symbols are read off the real-coordinate forms above, and a complex expression $p+iq$ vanishes exactly when both real functions vanish; the two conditions are each two independent real linear equations, hence a two-plane, and the characteristic set is the zero set of the product of the two symbols.

## Regular Functions and the System of Equations

**Definition.** Let $\Omega$ be a domain and $f:\Omega\to\mathbb{B}_{\mathrm{r}}$ of class $C^{1}$. Then $f$ is **regular** if $\bar\partial f=0$ on $\Omega$. Because the algebra is **commutative**, the right operator equals the left one, $f\bar\partial=\bar\partial f$, so no distinction of left and right regularity arises.

**Theorem (the regularity system).** Writing $f=g_{1}\Pi_++g_{2}\Pi_-$, the function $f$ is regular if and only if
$$
\partial/\partial\bar Q_{++}\,g_{1}=0,\qquad\partial/\partial\bar Q_{--}\,g_{2}=0,
$$
the pair of complex Cauchy–Riemann systems. In the real coordinates $\alpha=q_++q_-$, $\alpha'=q'_++q'_-$ of $Q_{++}$ and $\beta=q_+-q_-$, $\beta'=q'_+-q'_-$ of $Q_{--}$, with $g_{1}=p_{1}+ir_{1}$ and $g_{2}=p_{2}+ir_{2}$, the system is
$$
\partial/\partial\alpha\,p_{1}=\partial/\partial\alpha'\,r_{1},\quad \partial/\partial\alpha'\,p_{1}=-\partial/\partial\alpha\,r_{1},\qquad
\partial/\partial\beta\,p_{2}=\partial/\partial\beta'\,r_{2},\quad \partial/\partial\beta'\,p_{2}=-\partial/\partial\beta\,r_{2}.
$$

*Proof.* The operator acts coefficientwise, so $\bar\partial f=0$ is the pair of complex equations; each is the ordinary Cauchy–Riemann system of one complex variable, $\partial/\partial\bar Q_{++}=\tfrac12(\partial/\partial\alpha+i\partial/\partial\alpha')$ up to the change of variables, and the real form is the usual pair of equations.

**Remark (the dependence on the second variable).** The equation $\partial/\partial\bar Q_{++}\,g_{1}=0$ is the Cauchy–Riemann system in $Q_{++}$ with $Q_{--}$ entering only as a parameter, so a $C^{1}$ solution has $g_{1}(Q_{++},Q_{--})$ holomorphic in $Q_{++}$ for each fixed $Q_{--}$, and symmetrically $g_{2}(Q_{++},Q_{--})$ holomorphic in $Q_{--}$ for each fixed $Q_{++}$. The narrower class of functions differentiable in the reduced sense — the difference-quotient class of *Reduced Biquaternion Analysis*, §*The Problem of Differentiability* — is the class in which $g_{1}$ does not depend on $Q_{--}$ and $g_{2}$ does not depend on $Q_{++}$, that is
$$
f(Q_\pm)=G_{1}(Q_{++})\,\Pi_++G_{2}(Q_{--})\,\Pi_-
$$
with $G_{1},G_{2}$ holomorphic in one complex variable. The operator condition alone is the weaker and larger class; the reduced-analytic class is the one that carries the derivative and the integral theory, and it is meant when a statement needs a genuine difference quotient.

## Examples and Basic Properties

**Constants.** A constant $f=C$ is regular on every domain, since both derivatives vanish.

**The identity is regular.** $\bar\partial Q_\pm=\Pi_+\partial/\partial\bar Q_{++}\,Q_{++}+\Pi_-\partial/\partial\bar Q_{--}\,Q_{--}=0$, the component $Q_{++}$ being holomorphic in $Q_{++}$ and the component $Q_{--}$ in $Q_{--}$. The identity is therefore regular, in contrast with the Clifford case, where $\sum_{\mu}e_{\mu}^{2}\neq0$ makes the coordinate function non-regular.

**Powers and polynomials.** Since $Q_\pm^{n}=Q_{++}^{n}\Pi_++Q_{--}^{n}\Pi_-$, every power is regular, and so is every polynomial $\sum_{n}c_{n}Q_\pm^{n}$ with constant coefficients; more generally $f=G_{1}(Q_{++})\Pi_++G_{2}(Q_{--})\Pi_-$ is reduced-analytic and regular for every pair of holomorphic functions $G_{1},G_{2}$.

**The Cauchy kernel.** The function
$$
G(Q_\pm)=\frac{1}{2\pi i}\Bigl(\frac{\Pi_+}{Q_{++}}+\frac{\Pi_-}{Q_{--}}\Bigr)
$$
is regular on the complement of the zero-divisor set $Z=\mathbb{C}\Pi_+\cup\mathbb{C}\Pi_-$, since each component is holomorphic in its own coordinate.

**Closure.** Regular functions are closed under addition and multiplication: by the product rule for the derivation $\bar\partial$,
$$
\bar\partial(fh)=(\bar\partial f)h+f(\bar\partial h),
$$
so the regular functions form a commutative algebra over $\mathbb{C}$. They are **not** closed under the bar, which conjugates the coefficients and turns a holomorphic component into an antiholomorphic one.

**The conjugations.** The natural sign $Q_\pm\mapsto Q_\pm^{\natural}=Q_+-jQ_-$ swaps the two coordinates, $Q_{++}\leftrightarrow Q_{--}$, so it maps a reduced-analytic function $G_{1}(Q_{++})\Pi_++G_{2}(Q_{--})\Pi_-$ to $G_{1}(Q_{--})\Pi_-+G_{2}(Q_{++})\Pi_+$, which is again reduced-analytic; the bar conjugates the coefficients and produces the antiholomorphic twins, and the star does both.

## Harmonicity and the Factorization of the Laplacian

**Theorem (reduced-analytic functions are harmonic).** Every reduced-analytic function $f=G_{1}(Q_{++})\Pi_++G_{2}(Q_{--})\Pi_-$ satisfies $\Delta f=0$. A general regular function of the weaker class $\bar\partial f=0$ need not be harmonic: the function $f=\lvert Q_{--}\rvert^{2}\Pi_+$ is regular, $\partial/\partial\bar Q_{++}\,\lvert Q_{--}\rvert^{2}=0$, but $\Delta f=8\Pi_+\neq0$, because $\lvert Q_{--}\rvert^{2}$ carries a dependence on $\bar Q_{--}$ that the single equation $\partial/\partial\bar Q_{++}\,g_{1}=0$ does not see.

*Proof.* For $f=G_{1}(Q_{++})\Pi_++G_{2}(Q_{--})\Pi_-$ one has $\Delta f=8\partial^2/\partial Q_{++}\partial\bar Q_{++}G_{1}\Pi_++8\partial^2/\partial Q_{--}\partial\bar Q_{--}G_{2}\Pi_-$, and each term vanishes because $\partial/\partial\bar Q_{++}\,G_{1}=0$ and $\partial/\partial\bar Q_{--}\,G_{2}=0$, the derivative of a vanishing quantity being zero.

**The converse fails.** The first real coordinate $f=q_+$ is harmonic, $\Delta q_+=0$, but it is not regular: $\partial/\partial\bar Q_{++}\,q_+=\tfrac14\neq0$.

**Corollary (the elliptic tools are available).** On the reduced biquaternion algebra the Laplacian is the ordinary Euclidean Laplacian in four real variables, so every reduced-analytic function satisfies the mean value property, the maximum principle and Liouville's theorem for bounded functions, and is real-analytic. This is the definite case of the family; on an indefinite subspace of the split biquaternion algebra the same second-order operator is a wave operator and those tools are not available.

*Proof.* A harmonic function of four real variables has all the listed properties, and a $C^{1}$ solution of an equation whose second-order part is the Laplacian is harmonic by the theorem above; real-analyticity follows from the holomorphy of each component in one complex variable.

## The Role of the Zero Divisors

The zero-divisor set is $Z=\mathbb{C}\Pi_+\cup\mathbb{C}\Pi_-$, the union of the two idempotent **complex lines**, each of real dimension two. The set therefore has codimension two in the four-dimensional algebra, not one, and this single fact governs every difference from the complex theory.

**The inverse is local.** The inverse $Q_\pm^{-1}=Q_{++}^{-1}\Pi_++Q_{--}^{-1}\Pi_-$ requires both coordinates non-zero, so the difference quotient exists only for increments off $Z$; since $Z$ has codimension two, the excluded increments form a set of measure zero but are not a hypersurface, and the quotient is defined on a dense open subset.

**The kernel is local.** The Cauchy kernel has the two simple poles on the two lines $Q_{++}=0$ and $Q_{--}=0$; it is defined and regular off $Z$, but it is not a classical fundamental solution of a single elliptic operator, because the singular set is a union of two codimension-two planes rather than a point.

**The operator is not elliptic.** The characteristic set is the union of the two two-planes of the symbol theorem, so the operator has no elliptic point, its kernel is infinite-dimensional, and the honest first-order theory is the pair of one-variable theories, one in $Q_{++}$ and one in $Q_{--}$.

## The Relation to the Biquaternion Case and to Clifford Analysis

The biquaternion algebra $\mathbb{B}=M_{2}(\mathbb{C})$ is simple and non-commutative; its regular functions are the Fueter-regular functions, the Cauchy kernel $Q^{\natural}/\lVert Q\rVert_{E}^{4}$ is a genuine fundamental solution, and the theory is the complex-coefficient case of Clifford analysis. The reduced biquaternion algebra replaces the simple algebra by the **product** $\mathbb{C}\times\mathbb{C}$: the operator decouples, the kernel factors into the two one-variable kernels, and the class of regular functions is the pair of holomorphic classes. The split biquaternion algebra is the middle case, its two factors being the quaternion algebra; there the regularity is the pair of quaternionic regularities, whereas here it is the pair of complex ones.

In the language of Clifford algebras the reduced algebra is $\mathrm{Cl}_{1,0}\otimes\mathrm{Cl}_{0,1}$, with the definite generator $i$ and the split generator $j$. The first-order operator defined by the Clifford units is not the operator studied here; the reduced Cauchy–Riemann operator is built instead from the two Wirtinger derivatives of the two idempotent coordinates, which is why it is not elliptic and why it factors the Euclidean Laplacian only through its two components. The replacement of the Fueter construction by the reduced Dirac-type operator and its solutions is *Fueter Theory for Reduced Biquaternions*.

## Summary

The reduced biquaternion algebra carries two commuting complex structures, $J_{i}(Q_\pm)=iQ_\pm$ and $J_{ij}(Q_\pm)=ijQ_\pm$, and the two idempotent coordinates $Q_{++}=Q_++Q_-$, $Q_{--}=Q_+-Q_-$ form the two independent complex variables. The reduced Cauchy–Riemann operator $\bar\partial=\Pi_+\partial/\partial\bar Q_{++}+\Pi_-\partial/\partial\bar Q_{--}$ and its conjugate $\partial=\Pi_+\partial/\partial Q_{++}+\Pi_-\partial/\partial Q_{--}$ act coefficientwise, commute, and satisfy $\bar\partial\partial=\Pi_+\partial^2/\partial Q_{++}\partial\bar Q_{++}+\Pi_-\partial^2/\partial Q_{--}\partial\bar Q_{--}$, the two components summing to $\Delta/8$. A $C^{1}$ function is regular when $\bar\partial f=0$, equivalently when its two components satisfy the pair of complex Cauchy–Riemann systems $\partial/\partial\bar Q_{++}\,g_{1}=0$, $\partial/\partial\bar Q_{--}\,g_{2}=0$; because the algebra is commutative, left and right regularity coincide. The reduced-analytic class is $f=G_{1}(Q_{++})\Pi_++G_{2}(Q_{--})\Pi_-$ with $G_{1},G_{2}$ holomorphic, and the identity function belongs to it. The characteristic set is the union of two two-planes, so the operator is elliptic nowhere and the operator condition alone defines a larger class than the reduced-analytic one. Every reduced-analytic function is harmonic for the Euclidean Laplacian, the elliptic tools of the mean value property, the maximum principle and Liouville's theorem being available, and the zero-divisor set is the union of the two idempotent complex lines, of codimension two, which makes the inverse and the kernel local without making them hypersurface singular. The theory is the pair of the complex one-variable theories, against the pair of quaternionic ones of the split biquaternions and the single Fueter theory of the simple biquaternion algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\times\mathbb{C}$ | Reduced biquaternion algebra |
| $Q_\pm=Q_++jQ_-$ | Element, $Q_+=q_++iq'_+$, $Q_-=q_-+iq'_-$ |
| $Q_{++}=Q_++Q_-$, $Q_{--}=Q_+-Q_-$ | Idempotent coordinates |
| $\Pi_{\pm}=\tfrac12(1\pm j)$ | Idempotents |
| $J_{i},J_{ij}$ | The two complex structures $Q_\pm\mapsto iQ_\pm$, $Q_\pm\mapsto ijQ_\pm$ |
| $\partial/\partial Q_{++},\partial/\partial\bar Q_{++},\partial/\partial Q_{--},\partial/\partial\bar Q_{--}$ | Wirtinger derivatives of the two coordinates |
| $\bar\partial=\Pi_+\partial/\partial\bar Q_{++}+\Pi_-\partial/\partial\bar Q_{--}$ | Reduced Cauchy–Riemann operator |
| $\partial=\Pi_+\partial/\partial Q_{++}+\Pi_-\partial/\partial Q_{--}$ | Conjugate operator |
| $\Delta=\partial^2/\partial q_+^2+\partial^2/\partial q'^2_++\partial^2/\partial q_-^2+\partial^2/\partial q'^2_-$ | Euclidean Laplacian |
| $f=G_{1}(Q_{++})\Pi_++G_{2}(Q_{--})\Pi_-$ | Reduced-analytic function |
| $G(Q_\pm)=\tfrac{1}{2\pi i}(\Pi_+/Q_{++}+\Pi_-/Q_{--})$ | Cauchy kernel |
| $Z=\mathbb{C}\Pi_+\cup\mathbb{C}\Pi_-$ | Zero-divisor set |

## Further Reading

- R. Fueter, "Die Funktionentheorie der Differentialgleichungen $\Delta u = 0$ und $\Delta\Delta u = 0$ mit vier reellen Variablen", *Commentarii Mathematici Helvetici* 7 (1934), for the origin of the hypercomplex regularity system.
- F. Brackx, R. Delanghe and F. Sommen, *Clifford Analysis*, Research Notes in Mathematics 76 (Pitman, 1982), for the Cauchy–Riemann operator and monogenic functions.
- Klaus Gürlebeck and Wolfgang Sprößig, *Quaternionic and Clifford Calculus for Physicists and Engineers* (Wiley, 1997), for the componentwise regularity system and its elliptic theory.
- G. Baley Price, *An Introduction to Multicomplex Spaces and Functions* (Marcel Dekker, 1991), for the multicomplex and bicomplex calculus.
- M. Elena Luna-Elizarrarás, Michael Shapiro, Daniele C. Struppa and Adrian Vajiac, *Bicomplex Holomorphic Functions: The Algebra, Geometry and Analysis of Bicomplex Numbers* (Birkhäuser, 2015), for the holomorphic functions and the idempotent decomposition of the commutative algebra.
