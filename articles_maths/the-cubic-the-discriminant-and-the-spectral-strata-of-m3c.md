# __The Cubic, the Discriminant and the Spectral Strata of $M_3(\mathbb{C})$__

## Introduction

Every element $A\in M_{3}(\mathbb{C})$ has a characteristic polynomial of degree three,
$$
\chi_{A}(\lambda)=\det(\lambda I-A)=\lambda^{3}-t\lambda^{2}+s\lambda-d,
$$
with
$$
t=\operatorname{tr}A,\qquad
s=\tfrac12\bigl(t^{2}-\operatorname{tr}A^{2}\bigr),\qquad
d=\det A.
$$
The three roots, counted with multiplicity, are the eigenvalues. The **discriminant** $\Delta$ is the product of the squared differences of the roots:
$$
\Delta=\prod_{i<j}(\lambda_{i}-\lambda_{j})^{2}.
$$
It vanishes exactly when two roots coincide, so it is the polynomial that detects the collision of the spectrum. The article computes $\Delta$ in the coefficients and in the entries, describes the three spectral strata by the root multiplicities and their dimensions, proves the centraliser statement for a cyclic element, and treats the spectral projectors at a repeated root, where the Lagrange formula degenerates.

The construction is root-first. For a root $H$ with $H^{3}=I$ and simple spectrum the three eigenvalues are the cube roots of unity, and the Lagrange projectors $P_{1},P_{2},P_{3}$ are the idempotents of *Roots of Unity and the Lagrange Idempotents of $M_3(\mathbb{C})$*. The general element of this article need not be a root: its eigenvalues are arbitrary complex numbers, and the cubic is the general cubic. The root case is the special case $t=0$, $s=0$, $d=1$ up to the ordering of the roots, since $\lambda^{3}-1=0$.

The article uses the trace and the determinant of *The Matrix Algebra $M_{3}(\mathbb{C})$*, the Peirce coordinates of *The Peirce Decomposition of $M_{3}(\mathbb{C})$*, and the Jordan decomposition of *The Element, the Coordinates and the Trace of $M_3(\mathbb{C})$*. The spectral theorem for a single matrix is the content here; the Hermitian spectral theorem is *The Involution and the Hermitian Structure of $M_3(\mathbb{C})$*.

## The Characteristic Cubic

**Definition.** For $A\in M_{3}(\mathbb{C})$ the characteristic polynomial is $\chi_{A}(\lambda)=\det(\lambda I-A)$, and the three coefficients are
$$
t=\operatorname{tr}A,\qquad
s=\tfrac12\bigl((\operatorname{tr}A)^{2}-\operatorname{tr}A^{2}\bigr),\qquad
d=\det A.
$$

**Proposition.** The polynomial is
$$
\chi_{A}(\lambda)=\lambda^{3}-t\lambda^{2}+s\lambda-d,
$$
and its roots are the eigenvalues of $A$, counted with algebraic multiplicity.

**Proof.** Expand the determinant of $\lambda I-A$ by the Leibniz formula. The constant term is $\det(-A)=-\det A$; the coefficient of $\lambda^{3}$ is $1$; the coefficient of $\lambda^{2}$ is $-\operatorname{tr}A$; the coefficient of $\lambda$ is the sum of the principal $2\times2$ minors:
$$
s=(a_{11}a_{22}-a_{12}a_{21})+(a_{11}a_{33}-a_{13}a_{31})+(a_{22}a_{33}-a_{23}a_{32}).
$$
The trace identity $s=\tfrac12(t^{2}-\operatorname{tr}A^{2})$ follows by expanding $t^{2}=\sum_{i,j}a_{ii}a_{jj}$ and $\operatorname{tr}A^{2}=\sum_{i,j}a_{ij}a_{ji}$ and subtracting. The roots are the eigenvalues by the fundamental theorem of algebra, and the algebraic multiplicities are the multiplicities of the roots.

**Cayley–Hamilton.** $\chi_{A}(A)=0$. This is the Cayley–Hamilton theorem of *The Matrix Algebra $M_{3}(\mathbb{C})$*; it implies that every power $A^{n}$ with $n\geq3$ is a linear combination of $I,A,A^{2}$, and that the algebra $\mathbb{C}[A]$ has dimension at most three.

**The root case.** For $H$ with $H^{3}=I$ and simple spectrum, the eigenvalues are $1,\omega,\omega^{2}$, so
$$
\chi_{H}(\lambda)=\lambda^{3}-1,
$$
with $t=0$, $s=0$, $d=1$. The three Lagrange projectors of *Roots of Unity and the Lagrange Idempotents of $M_3(\mathbb{C})$* are the spectral projectors of this cubic. The general cubic of this article is the deformation of $\lambda^{3}-1$ in which the three roots move independently.

**The trace and the determinant of the roots.** By Vieta,
$$
\lambda_{1}+\lambda_{2}+\lambda_{3}=t,\qquad
\lambda_{1}\lambda_{2}+\lambda_{2}\lambda_{3}+\lambda_{3}\lambda_{1}=s,\qquad
\lambda_{1}\lambda_{2}\lambda_{3}=d.
$$
These are the elementary symmetric functions of the spectrum. The coefficients $t,s,d$ are polynomial in the nine entries, of degrees $1,2,3$ respectively, and they are invariant under conjugation.

## The Discriminant

**Definition.** For a monic cubic $\lambda^{3}-t\lambda^{2}+s\lambda-d$ with roots $\lambda_{1},\lambda_{2},\lambda_{3}$, the **discriminant** is
$$
\Delta=\prod_{i<j}(\lambda_{i}-\lambda_{j})^{2}.
$$

**Theorem (the discriminant in the coefficients).**
$$
\boxed{\;\Delta=t^{2}s^{2}-4s^{3}-4t^{3}d+18tsd-27d^{2}.\;}
$$

**Proof.** The discriminant of a cubic $x^{3}+ax^{2}+bx+c$ is
$$
a^{2}b^{2}-4b^{3}-4a^{3}c+18abc-27c^{2}.
$$
Substituting $a=-t$, $b=s$, $c=-d$ gives
$$
t^{2}s^{2}-4s^{3}-4t^{3}d+18tsd-27d^{2}.
$$
The formula is the standard discriminant of the cubic; it is also obtained by eliminating $\lambda$ from $\chi$ and $\chi'$, or by expanding the Vandermonde product.

**The discriminant detects a repeated root.** Over $\mathbb{C}$, the cubic has a repeated root if and only if $\Delta=0$.

**Proof.** If $\lambda_{i}=\lambda_{j}$ for $i\neq j$, the product has a zero factor. Conversely, if $\Delta=0$, some difference $\lambda_{i}-\lambda_{j}$ is zero, because $\mathbb{C}$ is a field and a product is zero only when a factor is zero.

**The resultant form.** For a monic cubic,
$$
\operatorname{Res}(\chi,\chi')=\prod_{i}\chi'(\lambda_{i})=\prod_{i\neq j}(\lambda_{i}-\lambda_{j})=(-1)^{3}\prod_{i<j}(\lambda_{i}-\lambda_{j})^{2}=-\Delta.
$$
So $\Delta=-\operatorname{Res}(\chi,\chi')$, and $\Delta=0$ is the condition $\gcd(\chi,\chi')\neq1$. This is the cleanest proof that the discriminant detects the collision: a repeated root is a common root of $\chi$ and $\chi'$.

**Homogeneity.** The coefficients $t,s,d$ have degrees $1,2,3$ in the entries, and every term of $\Delta$ has degree $6$: $t^{2}s^{2}$ has $2+4=6$, $s^{3}$ has $6$, $t^{3}d$ has $3+3=6$, $tsd$ has $1+2+3=6$, $d^{2}$ has $6$. So $\Delta$ is a homogeneous polynomial of degree $6$ in the nine entries. It is invariant under conjugation, because $t,s,d$ are.

**Worked example.** For
$$
A=\begin{pmatrix}1&2&3\\4&5&6\\7&8&9\end{pmatrix},
$$
the trace is $15$, and
$$
\operatorname{tr}A^{2}=30+81+150=261,
$$
because the diagonal of $A^{2}$ is $(30,81,150)$. Hence
$$
s=\tfrac12(15^{2}-261)=\tfrac12(225-261)=-18,\qquad d=0,
$$
and
$$
\chi_{A}(\lambda)=\lambda^{3}-15\lambda^{2}-18\lambda=\lambda(\lambda^{2}-15\lambda-18).
$$
The roots are
$$
0,\qquad \frac{15+\sqrt{297}}{2},\qquad \frac{15-\sqrt{297}}{2},
$$
because $15^{2}+4\cdot18=225+72=297$. The discriminant is
$$
\Delta=15^{2}(-18)^{2}-4(-18)^{3}=225\cdot324+4\cdot5832=72900+23328=96228.
$$
The Vandermonde check gives
$$
\left(\frac{15+\sqrt{297}}{2}\right)\left(\frac{15-\sqrt{297}}{2}\right)\sqrt{297}
=\frac{225-297}{4}\sqrt{297}
=-18\sqrt{297},
$$
whose square is $324\cdot297=96228$. The three principal $2\times2$ minors are $-3,-12,-3$, and their sum is $-18=s$, as it must be.

**The root case in the formula.** For $t=0$, $s=0$, $d=1$, the discriminant is $\Delta=-27(1)^{2}=-27$. The roots $1,\omega,\omega^{2}$ give
$$
(1-\omega)^{2}(1-\omega^{2})^{2}(\omega-\omega^{2})^{2}=-27,
$$
which is the product of the three squared differences; the negative sign is the sign of the Vandermonde product for three roots. The discriminant of $\lambda^{3}-1$ is $-27$, not $+27$; the ordering of the roots is part of the definition of the Vandermonde product.

## The Spectral Strata

**The three strata.** The spectrum of $A$ falls into one of three multiplicity patterns:

1. **Simple spectrum:** three distinct roots, $\Delta\neq0$.
2. **Double root:** one root of multiplicity two and one simple root, $\Delta=0$ but $\chi\neq(\lambda-a)^{3}$.
3. **Triple root:** one root of multiplicity three, $\chi=(\lambda-a)^{3}$.

**Theorem (the dimensions).** In $M_{3}(\mathbb{C})$, of complex dimension $9$ and real dimension $18$, the strata have dimensions

| Stratum | Condition | Complex dimension | Real dimension |
|---|---|---|---|
| simple spectrum | $\Delta\neq0$ | $9$ | $18$ |
| double root | $\Delta=0$, not triple | $8$ | $16$ |
| triple root | $\chi=(\lambda-a)^{3}$ | $7$ | $14$ |

The simple stratum is open and dense; the double stratum is a hypersurface minus the triple stratum; the triple stratum is a codimension-two subvariety of the algebra, of codimension one in the discriminant hypersurface.

**Proof.** The simple stratum is the complement of the zero set of the polynomial $\Delta$, which is not identically zero; a nonzero polynomial vanishes on a hypersurface, so the complement is open and dense, of dimension $9$.

The discriminant $\Delta$ is one polynomial in the entries, not identically zero, so its zero set has dimension $8$; the double stratum is the part of this hypersurface where the cubic is not a cube, and it has dimension $8$ as well (removing a proper subvariety does not change the dimension).

The triple-root condition is $\chi=(\lambda-a)^{3}$ for some $a$, equivalently
$$
t=3a,\qquad s=3a^{2},\qquad d=a^{3}.
$$
Eliminating $a$ gives the two equations
$$
s=\frac{t^{2}}{3},\qquad d=\frac{t^{3}}{27},
$$
which are independent, so the triple stratum has dimension $9-2=7$. Equivalently, every matrix with a triple root is $aI+N$ with $N$ nilpotent; the scalar $a$ contributes one dimension, and the nilpotent cone in $M_{3}$ is the set $\chi=x^{3}$, equivalently $t=s=d=0$, of dimension $9-3=6$, so the total is $1+6=7$. The scalar matrices $aI$ form the one-dimensional semisimple part of this stratum. The double stratum is the discriminant hypersurface minus the triple stratum, hence of dimension $8$.

**The generic Jordan forms.** The three strata have the following generic Jordan forms:

| Stratum | Generic Jordan form | Centraliser dimension |
|---|---|---|
| simple | $\operatorname{diag}(\lambda_{1},\lambda_{2},\lambda_{3})$, distinct | $3$ |
| double | $\operatorname{diag}(J_{2}(a),b)$, $a\neq b$ | $3$ |
| triple | $J_{3}(a)$ | $3$ |

The centraliser of a generic element is three-dimensional in all three cases; the difference is the structure of the centraliser, not its dimension. For the simple spectrum it is the diagonal torus $\mathbb{C}^{\times}\times\mathbb{C}^{\times}\times\mathbb{C}^{\times}$, of dimension $3$; for the double root it is $\mathbb{C}[A]\cong\mathbb{C}[x]/((x-a)^{2}(x-b))$, of dimension $3$, with a nilpotent; for the triple root it is $\mathbb{C}[A]\cong\mathbb{C}[x]/((x-a)^{3})$, of dimension $3$, local.

**The centraliser of a cyclic element.** An element $A$ is **cyclic** when its minimal polynomial has degree $3$, equivalently when $\mathbb{C}[A]$ has dimension $3$, equivalently when there is a vector $v$ such that $v,Av,A^{2}v$ is a basis. For a cyclic element the centraliser is exactly $\mathbb{C}[A]$, of dimension $3$.

**Proof.** The centraliser of $A$ contains $\mathbb{C}[A]$. Conversely, if $B$ commutes with $A$, then $B$ is determined by $Bv$: the vectors $v,Av,A^{2}v$ are a basis, and $BA^{k}v=A^{k}Bv$ for every $k$, so the values of $B$ on the basis are determined by $Bv$, which is a vector of $\mathbb{C}^{3}$; hence the centraliser has dimension at most $3$. Since $\mathbb{C}[A]$ already has dimension $3$ for a cyclic element, the two are equal.

**The torus case.** For a cyclic element with simple spectrum, $\mathbb{C}[A]\cong\mathbb{C}[x]/(\chi)\cong\mathbb{C}\times\mathbb{C}\times\mathbb{C}$ by the Chinese remainder theorem, and the centraliser is the diagonal torus of dimension $3$. For a cyclic element with a repeated root, the algebra $\mathbb{C}[A]$ has nilpotents and is not a torus, but its dimension is still $3$. The menu phrase “the centraliser of a cyclic element is the torus of dimension three” refers to the simple-spectrum case; the repeated-root case has the same dimension and a different algebra.

**The scalar element.** The scalar $aI$ is not cyclic: its minimal polynomial is $x-a$, of degree one, and its centraliser is all of $M_{3}$, of dimension $9$. The scalars are exactly the elements whose centraliser has dimension $9$; the centraliser dimension is upper semicontinuous and jumps up on the smaller strata, with the scalar line at the top.

## The Spectral Projectors at a Repeated Root

**The simple case.** If the spectrum is simple, the Lagrange projectors are
$$
P_{k}=\prod_{l\neq k}\frac{A-\lambda_{l}I}{\lambda_{k}-\lambda_{l}},\qquad k=1,2,3,
$$
with $P_{k}^{2}=P_{k}$, $P_{k}P_{l}=0$ for $k\neq l$, $\sum_{k}P_{k}=I$, and $AP_{k}=\lambda_{k}P_{k}$. They are the spectral projectors of *Roots of Unity and the Lagrange Idempotents of $M_3(\mathbb{C})$*, with the cube roots replaced by the three eigenvalues.

**The double root.** Suppose the spectrum is $\{a,a,b\}$ with $a\neq b$. The Lagrange formula on the **distinct** eigenvalues gives
$$
P_{a}=\frac{A-bI}{a-b},\qquad P_{b}=\frac{A-aI}{b-a},
$$
and these are well defined because $a-b\neq0$. The projector $P_{a}$ has rank $2$: it is the spectral projector onto the generalised eigenspace of $a$, not onto a single line. The projector $P_{b}$ has rank $1$. They satisfy $P_{a}+P_{b}=I$, $P_{a}P_{b}=0$, and $AP_{a}=aP_{a}+N_{a}$ with $N_{a}=P_{a}N$ nilpotent; on the generalised eigenspace the matrix is $aI+N$, and $P_{a}$ is the projection onto that space, not a diagonalisation of $A$.

**The degeneration.** Split the double root into $a+\varepsilon$ and $a-\varepsilon$. For $\varepsilon\neq0$ the spectrum is simple, and there are two rank-one Lagrange projectors $P_{+}(\varepsilon)$ and $P_{-}(\varepsilon)$ with
$$
P_{+}(\varepsilon)+P_{-}(\varepsilon)\longrightarrow P_{a}\qquad(\varepsilon\to0).
$$
The individual limits depend on the splitting: in a basis where the generalised eigenspace of $a$ is spanned by $u,v$ and $A$ acts by $aI+N$, a perturbation that splits the eigenvalues chooses a direction in that plane, and the two rank-one projectors tend to the projections onto the two lines of that direction. Different perturbations give different pairs of lines; only the sum is canonical. This is the **degeneration of the Lagrange projectors**: the Lagrange interpolation is continuous in the eigenvalues as long as they are distinct, but at a collision the individual projectors have no canonical limit, while their sum over the colliding cluster is the Dunford projector.

**The Dunford calculus.** The canonical projector is the residue
$$
P_{a}=\frac{1}{2\pi i}\oint_{\gamma}(\lambda I-A)^{-1}\,d\lambda,
$$
where $\gamma$ is a small circle around $a$ enclosing no other eigenvalue. The contour integral is well defined at a repeated root and gives the spectral projector onto the generalised eigenspace. The Lagrange formula is the evaluation of the same contour integral when the roots are simple; at a collision the contour encloses both roots and the two Lagrange projectors are replaced by their sum.

**The triple root.** If $\chi=(\lambda-a)^{3}$, the only eigenvalue is $a$ and the spectral projector is $P_{a}=I$. The Jordan decomposition is $A=aI+N$ with $N$ nilpotent, and the "spectral" content is the single scalar $a$; the nilpotent $N$ is not detected by the spectrum. The Lagrange formula has all denominators zero and no limit that separates the three roots; the Dunford projector is $I$, and the finer decomposition is the Jordan decomposition of $N$, not a spectral decomposition.

**Worked example of the double root.** Let
$$
A=\begin{pmatrix}a&1&0\\0&a&0\\0&0&b\end{pmatrix},\qquad a\neq b.
$$
Then $\chi=(\lambda-a)^{2}(\lambda-b)$, and
$$
P_{a}=\frac{A-bI}{a-b}=\begin{pmatrix}1&0&0\\0&1&0\\0&0&0\end{pmatrix},\qquad
P_{b}=\frac{A-aI}{b-a}=\begin{pmatrix}0&0&0\\0&0&0\\0&0&1\end{pmatrix}.
$$
The projector $P_{a}$ has rank $2$ and does not diagonalise the Jordan block: $AP_{a}=aP_{a}+E_{12}$, with $E_{12}$ nilpotent. The Lagrange projectors of a nearby matrix with eigenvalues $a\pm\varepsilon$ tend to two rank-one projectors whose sum is $P_{a}$; the individual limits depend on the perturbation.

## Summary

The characteristic cubic of $A\in M_{3}(\mathbb{C})$ is
$$
\boxed{\;\chi_{A}(\lambda)=\lambda^{3}-t\lambda^{2}+s\lambda-d,\qquad
t=\operatorname{tr}A,\quad s=\tfrac12(t^{2}-\operatorname{tr}A^{2}),\quad d=\det A,\;}
$$
and its discriminant is
$$
\boxed{\;\Delta=t^{2}s^{2}-4s^{3}-4t^{3}d+18tsd-27d^{2}=\prod_{i<j}(\lambda_{i}-\lambda_{j})^{2}.\;}
$$
The cubic has a repeated root exactly when $\Delta=0$.

The spectral strata have dimensions

| Stratum | Complex dimension | Real dimension |
|---|---|---|
| simple spectrum | $9$ | $18$ |
| double root | $8$ | $16$ |
| triple root | $7$ | $14$ |

A cyclic element has centraliser $\mathbb{C}[A]$ of dimension $3$; it is a torus exactly when the spectrum is simple. The scalar element has centraliser $M_{3}$, of dimension $9$.

At a simple spectrum the Lagrange projectors are the spectral projectors. At a double root the projector of the repeated eigenvalue is the rank-two Dunford projector $(A-bI)/(a-b)$; the individual Lagrange projectors of a splitting have no canonical limit, but their sum tends to the Dunford projector. At a triple root the only spectral projector is $I$, and the nilpotent part is the Jordan decomposition.

| Quantity | Value for $M_{3}(\mathbb{C})$ |
|---|---|
| Degree of the characteristic polynomial | $3$ |
| Degree of the discriminant in the entries | $6$ |
| Simple spectrum dimension | $9$ complex, $18$ real |
| Double root dimension | $8$ complex, $16$ real |
| Triple root dimension | $7$ complex, $14$ real |
| Centraliser of a cyclic element | $3$ |
| Centraliser of a scalar | $9$ |
| Discriminant of $\lambda^{3}-1$ | $-27$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\chi_{A}(\lambda)$ | the characteristic polynomial $\det(\lambda I-A)$ |
| $t,s,d$ | $\operatorname{tr}A$, $\tfrac12(t^{2}-\operatorname{tr}A^{2})$, $\det A$ |
| $\Delta$ | the discriminant $\prod_{i<j}(\lambda_{i}-\lambda_{j})^{2}$ |
| $P_{k}$ | a spectral projector, Lagrange at a simple spectrum |
| $P_{a}$ | the Dunford projector of the eigenvalue $a$ |
| $J_{2}(a),J_{3}(a)$ | Jordan blocks of size $2$ and $3$ at $a$ |
| $\mathbb{C}[A]$ | the algebra generated by $A$, the centraliser of a cyclic element |

## Further Reading

- [Roots of Unity and the Lagrange Idempotents of $M_3(\mathbb{C})$](roots-of-unity-and-the-lagrange-idempotents-of-m3c.html), for the root case and the Lagrange projectors.
- [The Matrix Algebra $M_3(\mathbb{C})$](the-matrix-algebra-m3c.html), for the trace, the determinant and Cayley–Hamilton.
- [The Element, the Coordinates and the Trace of $M_3(\mathbb{C})$](the-element-the-coordinates-and-the-trace-of-m3c.html), for the Jordan decomposition.
- [Spectral Theory and the Spectral Projectors of $M_3(\mathbb{C})$](spectral-theory-and-the-spectral-projectors-of-m3c.html), for the Dunford calculus.
- [The Involution and the Hermitian Structure of $M_3(\mathbb{C})$](the-involution-and-the-hermitian-structure-of-m3c.html), for the Hermitian spectral theorem.
- [Eigenvalues and Diagonalisation](eigenvalues-and-diagonalisation.html), for the general spectral theory.
- [The Determinant and Alternating Forms](the-determinant-and-alternating-forms.html), for the determinant and its properties.
