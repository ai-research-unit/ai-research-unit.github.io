# __The Involution and the Hermitian Structure__

## Introduction

**The conjugate transpose $A^*=\bar A^{\mathsf T}$ is a $\mathbb{C}$-antilinear involution of $M_4(\mathbb{C})$, and the form $\langle A,B\rangle=\operatorname{tr}(A^*B)$ is a positive definite Hermitian form.** The form defines the Frobenius norm, the Hermitian and skew-Hermitian subspaces, the unitary group $U(4)$ and the compact real forms $\mathfrak{u}(4)$ and $\mathfrak{su}(4)$. It is definite: the only isotropic vector is $0$, and there is no null cone. This is the sharp contrast with the biquaternion algebra, whose norm is indefinite and whose zero divisors form a null cone.

The article defines the involution, proves its properties, constructs the positive definite trace form and the Frobenius norm, identifies the Hermitian and skew-Hermitian subspaces and the unitary groups, and contrasts the definite case with the null cone of $\mathbb{B}$.

The algebra is *The Matrix Algebra $M_4(\mathbb{C})$*; the element and the trace pairing $\operatorname{tr}(AB)$ are *The Element, the Coordinates and the Trace*; the polar decomposition is *The Polar Decomposition*; the forms and the singular set are *The Forms, the Norms and the Singular Set*.

## The Conjugate Transpose

**Definition.** The **conjugate transpose** of $A$ is

$$
A^*=\bar A^{\mathsf T},\qquad (A^*)_{ij}=\overline{A_{ji}}.
$$

**Proposition.** The map $A\mapsto A^*$ is a $\mathbb{C}$-antilinear involution and an anti-automorphism:

$$
(A+B)^*=A^*+B^*,\qquad
(\lambda A)^*=\bar\lambda A^*,\qquad
(AB)^*=B^*A^*,\qquad
A^{**}=A.
$$

It is not $\mathbb{C}$-linear and it is not an algebra automorphism.

**Proof.** The entries of $(A+B)^*$ are $\overline{A_{ji}+B_{ji}}=\overline{A_{ji}}+\overline{B_{ji}}$. For the scalar, $\overline{\lambda A_{ji}}=\bar\lambda\overline{A_{ji}}$. For the product, the $(i,j)$ entry of $(AB)^*$ is $\overline{(AB)_{ji}}=\sum_k\overline{A_{jk}B_{ki}}=\sum_k\overline{B_{ki}}\overline{A_{jk}}$, which is the $(i,j)$ entry of $B^*A^*$. The double star is the entrywise double conjugate and double transpose, which is the identity.

**The real structure.** The involution is the composition of the entrywise conjugation and the transpose. The fixed points of the conjugation are the real matrices $M_4(\mathbb{R})$, of real dimension $16$; the fixed points of the transpose are the symmetric matrices, of complex dimension $10$. The fixed points of the conjugate transpose are the Hermitian matrices, a real subspace of dimension $16$.

**Hermitian, skew-Hermitian and unitary elements.** An element is

- **Hermitian** if $A^*=A$;
- **skew-Hermitian** if $A^*=-A$;
- **unitary** if $A^*A=AA^*=I$.

The Hermitian and skew-Hermitian conditions are real-linear conditions, not complex-linear ones: if $A$ is Hermitian, then $iA$ is skew-Hermitian.

**The Hermitian and skew-Hermitian parts.** Every matrix splits uniquely as

$$
A=\frac{A+A^*}{2}+\frac{A-A^*}{2}=H+K,
$$

with

$$
H=\frac{A+A^*}{2}\ \text{Hermitian},\qquad
K=\frac{A-A^*}{2}\ \text{skew-Hermitian}.
$$

The decomposition is a **real** direct sum:

$$
M_4(\mathbb{C})=\operatorname{Herm}_4\oplus\mathfrak{u}(4),
\qquad
\dim_\mathbb{R}\operatorname{Herm}_4=16,\quad
\dim_\mathbb{R}\mathfrak{u}(4)=16,
\qquad
16+16=32.
$$

It is the eigenspace decomposition of the real-linear involution $A\mapsto A^*$ for the eigenvalues $+1$ and $-1$. The summands are not complex subspaces: $i\operatorname{Herm}_4=\mathfrak{u}(4)$.

**The alternative Cartesian form.** Every matrix can also be written uniquely as

$$
A=H+iK,\qquad H,K\in\operatorname{Herm}_4,
$$

with

$$
H=\frac{A+A^*}{2},\qquad
K=\frac{A-A^*}{2i}.
$$

The two Hermitian matrices $H,K$ are the **real and imaginary Hermitian parts**. The map $A\mapsto(H,K)$ is an $\mathbb{R}$-linear isomorphism $M_4\to\operatorname{Herm}_4\oplus\operatorname{Herm}_4$. The decomposition $A=H+iK$ is not the decomposition into the real and imaginary parts of the coordinates; the coordinate real part of $A$ is $X=(A+\bar A)/2$, which is not Hermitian in general.

**Explicit example.** For

$$
A=E_{12}+iE_{34},
$$

the conjugate transpose is

$$
A^*=E_{21}-iE_{43}.
$$

The Hermitian part is

$$
H=\frac12(E_{12}+E_{21})+\frac{i}{2}(E_{34}-E_{43}),
$$

and the skew-Hermitian part is

$$
K=\frac12(E_{12}-E_{21})+\frac{i}{2}(E_{34}+E_{43}).
$$

The two parts are nonzero and $A=H+K$.

## The Positive Definite Trace Form

**Definition.** The **trace form** is

$$
\langle A,B\rangle=\operatorname{tr}(A^*B).
$$

It is linear in $B$, conjugate-linear in $A$, and conjugate-symmetric:

$$
\langle A,B\rangle=\overline{\langle B,A\rangle}.
$$

**Theorem.** The trace form is positive definite:

$$
\langle A,A\rangle=\operatorname{tr}(A^*A)=\sum_{i,j=1}^{4}\lvert A_{ij}\rvert^2\ge0,
$$

with equality if and only if $A=0$. The only isotropic vector is the zero matrix.

**Proof.** The diagonal entry $(A^*A)_{ii}$ is $\sum_k\overline{A_{ki}}A_{ki}=\sum_k\lvert A_{ki}\rvert^2$, so the trace is the sum of the squares of the moduli of all sixteen entries. A sum of non-negative real numbers is zero exactly when every entry is zero.

**The Frobenius norm.** The form defines the **Frobenius norm**

$$
\lVert A\rVert_F=\sqrt{\langle A,A\rangle}
=\Bigl(\sum_{i,j=1}^{4}\lvert A_{ij}\rvert^2\Bigr)^{1/2}.
$$

It is the Euclidean norm of $A$ as a vector in $\mathbb{C}^{16}$, and it satisfies the Cauchy–Schwarz and triangle inequalities:

$$
\lvert\langle A,B\rangle\rvert\le\lVert A\rVert_F\lVert B\rVert_F,
\qquad
\lVert A+B\rVert_F\le\lVert A\rVert_F+\lVert B\rVert_F.
$$

It is invariant under unitary conjugation and under left and right multiplication by unitaries:

$$
\lVert UAV\rVert_F=\lVert A\rVert_F,\qquad U,V\in U(4).
$$

**Proof.** The norm is the Euclidean norm of the entries. For unitarity, $\operatorname{tr}((UAV)^*(UAV))=\operatorname{tr}(V^*A^*U^*UAV)=\operatorname{tr}(V^*A^*AV)=\operatorname{tr}(A^*A)$, using the cyclic property of the trace and $U^*U=I$, $VV^*=I$.

**The real inner product.** The real part

$$
(A,B)_\mathbb{R}=\operatorname{Re}\operatorname{tr}(A^*B)
$$

is a real inner product on the $32$-dimensional real space $M_4(\mathbb{C})$. The imaginary part is a symplectic form. The Hermitian form is recovered from the real inner product and the complex structure $J(A)=iA$:

$$
\langle A,B\rangle=(A,B)_\mathbb{R}+i(A,JB)_\mathbb{R}.
$$

**The trace form versus the trace pairing.** The form $\langle A,B\rangle=\operatorname{tr}(A^*B)$ is positive definite. The pairing $\beta(A,B)=\operatorname{tr}(AB)$ of *The Element, the Coordinates and the Trace* is symmetric, complex-bilinear and indefinite. They agree on the real symmetric matrices and differ elsewhere; for example, $\beta(A,A)=\operatorname{tr}(A^2)$ can be zero for $A\ne0$, while $\langle A,A\rangle=0$ only for $A=0$.

**The orthogonality of the Hermitian decomposition.** The subspaces $\operatorname{Herm}_4$ and $\mathfrak{u}(4)$ are orthogonal for the real inner product:

$$
\operatorname{Re}\langle H,K\rangle=\operatorname{Re}\operatorname{tr}(HK)=0
$$

for $H$ Hermitian and $K$ skew-Hermitian. The complex form has a purely imaginary cross term in general, so the decomposition is orthogonal for the real inner product, not for the complex Hermitian form.

**Proof.** For $H^*=H$ and $K^*=-K$,

$$
\overline{\operatorname{tr}(HK)}=\operatorname{tr}((HK)^*)=\operatorname{tr}(K^*H^*)=-\operatorname{tr}(KH)=-\operatorname{tr}(HK),
$$

so $\operatorname{tr}(HK)$ is purely imaginary.

## The Hermitian Subspace

**The real vector space.** The Hermitian matrices form a real vector space of dimension $16$:

$$
\operatorname{Herm}_4=\{A:A^*=A\}.
$$

A Hermitian matrix has real diagonal entries and conjugate-symmetric off-diagonal entries:

$$
A_{ii}\in\mathbb{R},\qquad
A_{ij}=\overline{A_{ji}}.
$$

There are four real diagonal parameters and six complex off-diagonal parameters, hence $4+2\cdot6=16$ real dimensions.

**The spectral theorem.** Every Hermitian matrix is unitarily diagonalisable with real eigenvalues:

$$
H=U\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3,\lambda_4)U^*,
\qquad
\lambda_k\in\mathbb{R},\quad U\in U(4).
$$

The eigenvalues are the critical values of the Rayleigh quotient, and the eigenvectors are orthogonal. The spectral theorem is the basis of *Spectral Theory and the Spectral Projectors* and *The Polar Decomposition*.

**The positive semidefinite cone.** The Hermitian matrix $H$ is **positive semidefinite** if

$$
\langle v,Hv\rangle\ge0
$$

for every $v\in\mathbb{C}^4$, equivalently if all its eigenvalues are non-negative. The positive definite matrices are the interior of the cone; the boundary is the set of positive semidefinite matrices with $\det H=0$. The cone is a symmetric cone, and $\operatorname{Herm}_4$ is a Jordan algebra under the anticommutator

$$
H\circ K=\frac12(HK+KH).
$$

The Jordan algebra is not associative; its associators measure the failure. The cone and the Jordan structure are the real form of the Hermitian structure.

**The unitary group.** The **unitary group** is

$$
U(4)=\{U:U^*U=UU^*=I\}.
$$

It is a compact Lie group of real dimension $16$. Its Lie algebra is the skew-Hermitian space

$$
\mathfrak{u}(4)=\{K:K^*=-K\},
$$

with the commutator bracket. The **special unitary group** is

$$
SU(4)=U(4)\cap SL_4(\mathbb{C})=\{U\in U(4):\det U=1\},
$$

of real dimension $15$, with Lie algebra

$$
\mathfrak{su}(4)=\{K\in\mathfrak{u}(4):\operatorname{tr}K=0\}.
$$

**The real forms.** The compact real form $\mathfrak{u}(4)$ complexifies to $\mathfrak{gl}_4(\mathbb{C})$:

$$
\mathfrak{u}(4)\otimes_\mathbb{R}\mathbb{C}\cong\mathfrak{gl}_4(\mathbb{C}),
$$

and $\mathfrak{su}(4)$ complexifies to $\mathfrak{sl}_4(\mathbb{C})$:

$$
\mathfrak{su}(4)\otimes_\mathbb{R}\mathbb{C}\cong\mathfrak{sl}_4(\mathbb{C}).
$$

The dimensions are $16$ and $15$ over $\mathbb{R}$, and $16$ and $15$ over $\mathbb{C}$ after complexification. The compact forms are the real forms on which the trace form $\operatorname{tr}(A^*B)$ is positive definite, as on the whole space; the Killing form, by contrast, is negative semidefinite on $\mathfrak{u}(4)$ and negative definite on $\mathfrak{su}(4)$. For $K\in\mathfrak{u}(4)$, write $K=iH$ with $H$ Hermitian; then $K^2=-H^2$ and $\operatorname{tr}(K^2)=-\operatorname{tr}(H^2)\le0$.

**The action on the algebra.** The unitary group acts on $M_4$ by conjugation:

$$
A\longmapsto UAU^*.
$$

The action preserves the trace form:

$$
\langle UAU^*,UBU^*\rangle
=\operatorname{tr}(UA^*U^*UBU^*)
=\operatorname{tr}(UA^*BU^*)
=\operatorname{tr}(A^*B).
$$

It preserves the Hermitian, skew-Hermitian, positive semidefinite and unitary subsets, and it preserves the Frobenius norm.

## The Definite Form and the Absence of a Null Cone

**The isotropic set.** For a positive definite form, the **isotropic set** is

$$
\{A:\langle A,A\rangle=0\}=\{0\}.
$$

There is no nonzero isotropic vector and no null cone. The zero divisors of $M_4$ are the singular matrices $\{\det A=0\}$; they are not the isotropic set of the form. The singular set is a complex hypersurface of real codimension $2$, and it contains many nonzero matrices, but every nonzero matrix has positive Frobenius norm.

**The contrast with $\mathbb{B}$.** The biquaternion algebra $\mathbb{B}=M_2(\mathbb{C})$ carries the quaternionic norm

$$
N(\tilde Q)=Q_t^2+B^2,
$$

which is complex-valued and indefinite on the real algebra; its zero set is the **null cone** of the zero divisors. The regular representation $M_4(\mathbb{C})_L$ inherits the determinant as the square of the norm, and its singular set is the null cone. The full algebra $M_4(\mathbb{C})$ is different: its determinant is not a norm, and its singular set is not the zero set of a definite form. The positive definite form $\operatorname{tr}(A^*B)$ exists on the full algebra, but its zero set is only the origin. The null cone of $\mathbb{B}$ and the singular set of $M_4$ are different objects.

**The two determinants.** The determinant of the full algebra is the usual $4\times4$ determinant; the determinant of the regular model is the square of the biquaternion norm. The full determinant vanishes on the singular matrices; the biquaternion norm vanishes on the null cone. The two singular sets have different dimensions and different geometry. The full algebra has no null cone; the regular model does.

**The singular set is not the isotropic cone.** The set $\{\det A=0\}$ is the zero locus of a holomorphic polynomial of degree four, of complex dimension $15$ and real codimension $2$. The set $\{\langle A,A\rangle=0\}$ is the origin, of real dimension $0$. The two sets are not comparable: the first is large and complex, the second is a point. The definite form does not detect the zero divisors; the determinant does.

## Summary

The conjugate transpose $A^*=\bar A^{\mathsf T}$ is a $\mathbb{C}$-antilinear involution and anti-automorphism of $M_4(\mathbb{C})$. Its fixed real subspace is the Hermitian matrices $\operatorname{Herm}_4$, of real dimension $16$; the skew-Hermitian matrices $\mathfrak{u}(4)$ form the other eigenspace, also of real dimension $16$; the real direct sum $M_4=\operatorname{Herm}_4\oplus\mathfrak{u}(4)$ has real dimension $32$. The trace form $\langle A,B\rangle=\operatorname{tr}(A^*B)$ is positive definite, with Frobenius norm $\lVert A\rVert_F^2=\sum_{i,j}\lvert A_{ij}\rvert^2$; its only isotropic vector is $0$, and there is no null cone. The Hermitian matrices are a Jordan algebra with the positive semidefinite cone; the skew-Hermitian matrices are the Lie algebra $\mathfrak{u}(4)$ of the unitary group $U(4)$, and the traceless part is $\mathfrak{su}(4)$ of dimension $15$. The compact real forms complexify to $\mathfrak{gl}_4$ and $\mathfrak{sl}_4$. The singular set of the full algebra is the determinantal hypersurface $\{\det A=0\}$, of real codimension $2$, not the isotropic cone of the form; the null cone belongs to the biquaternion algebra and its regular model, not to the full matrix algebra.

$$
\boxed{\ \langle A,B\rangle=\operatorname{tr}(A^*B)>0\ \text{for }A\ne0,\quad \dim_\mathbb{R}\operatorname{Herm}_4=16,\quad \dim_\mathbb{R}\mathfrak{u}(4)=16,\quad \dim_\mathbb{R}\mathfrak{su}(4)=15. }
$$

| Object | Real dimension | Condition |
|---|---|---|
| $M_4(\mathbb{C})$ | $32$ | — |
| Hermitian matrices | $16$ | $A^*=A$ |
| Skew-Hermitian matrices | $16$ | $A^*=-A$ |
| $\mathfrak{u}(4)$ | $16$ | $A^*=-A$ |
| $\mathfrak{su}(4)$ | $15$ | $A^*=-A$, $\operatorname{tr}A=0$ |
| $U(4)$ | $16$ | $U^*U=I$ |
| $SU(4)$ | $15$ | $U^*U=I$, $\det U=1$ |
| Isotropic set of the trace form | $0$ | $A=0$ |
| Singular set | $30$ | $\det A=0$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A^*=\bar A^{\mathsf T}$ | the conjugate transpose |
| $\operatorname{Herm}_4$ | the Hermitian matrices |
| $\mathfrak{u}(4)$ | the skew-Hermitian matrices |
| $\mathfrak{su}(4)$ | the traceless skew-Hermitian matrices |
| $\langle A,B\rangle=\operatorname{tr}(A^*B)$ | the positive definite trace form |
| $\lVert A\rVert_F$ | the Frobenius norm |
| $U(4)$, $SU(4)$ | the unitary and special unitary groups |
| $H,K$ | the Hermitian and skew-Hermitian parts of $A$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the conjugate transpose, the spectral theorem, the Frobenius norm and the unitary group.
- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for the positive definite cone, the trace form and the operator norms.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2015), for $U(4)$, $\mathfrak{u}(4)$, $\mathfrak{su}(4)$ and the compact real forms.
- [The Matrix Algebra $M_4(\mathbb{C})$](the-matrix-algebra-m4c.html), for the algebra and the trace pairing.
- [The Element, the Coordinates and the Trace](the-element-the-coordinates-and-the-trace-of-m4c.html), for the trace pairing and the Jordan decomposition.
- [The Forms, the Norms and the Singular Set](the-forms-the-norms-and-the-singular-set-of-m4c.html), for the singular set and the rank stratification.
- [The Polar Decomposition](the-polar-decomposition-of-m4c.html), for the unitary polar factor and the positive factor.
- [The Involution and the Hermitian Structure](the-involution-and-the-hermitian-structure.html), for the biquaternion case and the null cone.
