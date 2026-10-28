# __The Matrix Algebra $M_3(\mathbb{C})$__

## Introduction

The algebra $M_{3}(\mathbb{C})$ is the algebra of $3\times3$ complex matrices under the ordinary product. It is the model of a central simple algebra, the algebra of endomorphisms of $\mathbb{C}^{3}$, and the ambient algebra of the whole $M_{3}(\mathbb{C})$ category. This article fixes it: the basis of matrix units and the product rule, the trace and the determinant, the centre and the simplicity, the real dimension, the unit group and the projective group, and the reading of the algebra over the real numbers as the complexification of the skew-Hermitian matrices.

No quadratic form is used in the proofs here. The trace form $\operatorname{tr}(AB)$ is mentioned only to record that it is symmetric and nondegenerate; the positive definite Hermitian form $\operatorname{tr}(A^{*}B)$ and the norm it defines are *The Involution and the Hermitian Structure*. The dimensions are algebraic dimensions, not homotopy invariants; the topology of the algebra and of its unit group is *The Topology of $M_{3}(\mathbb{C})$*.

The article is the first of the category. The element and its coordinates are *The Element, the Coordinates and the Trace*; the root and its idempotents are *Roots of Unity and the Lagrange Idempotents*; the Peirce decomposition is *The Peirce Decomposition of $M_{3}(\mathbb{C})$*.

## The Algebra

**Definition.** $M_{3}(\mathbb{C})$ is the set of $3\times3$ arrays of complex numbers with the entrywise sum and the product

$$
(AB)_{ij}=\sum_{k=1}^{3}a_{ik}b_{kj}.
$$

The **matrix units** $E_{ij}$ are the arrays with a $1$ in position $(i,j)$ and $0$ elsewhere, for $i,j\in\{1,2,3\}$.

**Proposition (the matrix-unit table).** The nine matrix units form a $\mathbb{C}$-basis of $M_{3}(\mathbb{C})$, and

$$
\boxed{\;E_{ij}E_{kl}=\delta_{jk}E_{il}.\;}
$$

**Proof.** The entry in position $(p,q)$ of $E_{ij}E_{kl}$ is

$$
\sum_{r}(E_{ij})_{pr}(E_{kl})_{rq}=\sum_{r}\delta_{ip}\delta_{jr}\delta_{kr}\delta_{lq}
=\delta_{jk}\delta_{ip}\delta_{lq},
$$

which is the $(p,q)$-entry of $\delta_{jk}E_{il}$. The nine units are linearly independent because the entry $(i,j)$ of a linear combination is its coefficient, and they span because every matrix is the sum of its entries times the corresponding units.

**Theorem.** With this product, $M_{3}(\mathbb{C})$ is an associative unital non-commutative $\mathbb{C}$-algebra of complex dimension $9$ and real dimension $18$.

**Proof.** The product is $\mathbb{C}$-bilinear by the definition of the entries. It is associative because the product of matrices is the composition of the linear maps they represent, and composition is associative; equivalently, both $(AB)C$ and $A(BC)$ have $(i,l)$-entry $\sum_{j,k}a_{ij}b_{jk}c_{kl}$. The unit is the identity matrix $I$, with entries $\delta_{ij}$: $IE_{kl}=E_{kl}=E_{kl}I$. The algebra is not commutative, since $E_{12}E_{21}=E_{11}$ while $E_{21}E_{12}=E_{22}$, and $E_{11}\neq E_{22}$. The nine matrix units are a complex basis, so the complex dimension is nine and the real dimension is eighteen.

**The product is the composition of endomorphisms.** Let $\mathbb{C}^{3}$ be the space of column vectors and let $A$ act by $x\mapsto Ax$. The map

$$
M_{3}(\mathbb{C})\longrightarrow\operatorname{End}_{\mathbb{C}}(\mathbb{C}^{3}),\qquad A\longmapsto(x\mapsto Ax),
$$

is an isomorphism of $\mathbb{C}$-algebras: it is linear, it is injective because $Ae_{j}$ is the $j$-th column of $A$, and it is surjective because a linear map is determined by the images of the standard basis, which are the columns of its matrix. This is the reading of $M_{3}$ as the endomorphism algebra of the defining space.

**The coordinate rule.** For $A=(a_{ij})$ and $B=(b_{ij})$ the entries of the product are

$$
(AB)_{ij}=\sum_{k=1}^{3}a_{ik}b_{kj},
$$

and the diagonal entries are $(AB)_{ii}=\sum_{k}a_{ik}b_{ki}$. The rule is the only multiplication used in the category; the matrix units are the case in which one entry is $1$ and the others are $0$.

**The opposite algebra.** The opposite algebra $M_{3}^{\mathrm{opp}}$ has the product $A\cdot^{\mathrm{opp}}B=BA$. The transpose $A\mapsto A^{\mathsf T}$ is an isomorphism $M_{3}\to M_{3}^{\mathrm{opp}}$, because $(AB)^{\mathsf T}=B^{\mathsf T}A^{\mathsf T}$. The algebra is therefore isomorphic to its opposite, as every matrix algebra is; this is the first sign that it is a full matrix algebra and not a division algebra.

## Trace and Determinant

**Definition.** The **trace** of $A$ is

$$
\operatorname{tr}A=\sum_{i=1}^{3}a_{ii},
$$

and the **determinant** is

$$
\det A=\sum_{\sigma\in S_{3}}\operatorname{sgn}(\sigma)\,a_{1,\sigma(1)}a_{2,\sigma(2)}a_{3,\sigma(3)}.
$$

**Proposition (the trace).** The trace is linear, it satisfies

$$
\operatorname{tr}(AB)=\operatorname{tr}(BA)
$$

for all $A,B$, and it is the unique linear functional on $M_{3}(\mathbb{C})$, up to a scalar, that vanishes on every commutator.

**Proof.** Linearity is immediate from the definition. For the cyclic invariance,

$$
\operatorname{tr}(AB)=\sum_{i}\sum_{k}a_{ik}b_{ki}=\sum_{k}\sum_{i}b_{ki}a_{ik}=\operatorname{tr}(BA).
$$

A linear functional $f$ vanishes on all commutators exactly when $f(AB)=f(BA)$ for all $A,B$. The commutator subspace is the kernel of the trace, the traceless matrices $\mathfrak{sl}_{3}$, which has dimension $8$; its annihilator in the dual of the nine-dimensional space is one-dimensional. Since the trace vanishes on commutators and is nonzero, it spans the annihilator.

**Proposition (the determinant).** The determinant is multiplicative,

$$
\det(AB)=\det A\,\det B,
$$

and it is the unique multiplicative polynomial of degree three in the entries that takes the value $1$ at $I$ and vanishes on singular matrices.

**Proof.** The multiplicativity is the multiplicativity of the determinant of a linear map, $\det(AB)=\det A\det B$; it can also be checked from the Leibniz formula, where the sums over the two permutations compose. The characterisation is the standard one of the determinant as the alternating multilinear form in the columns normalised at the identity; the details are *Determinants and the Leibniz Formula* and *The Determinant of a Linear Map*.

**The explicit formulas for $3\times3$.** For

$$
A=\begin{pmatrix}a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\\a_{31}&a_{32}&a_{33}\end{pmatrix}
$$

the determinant is

$$
\det A=a_{11}(a_{22}a_{33}-a_{23}a_{32})
-a_{12}(a_{21}a_{33}-a_{23}a_{31})
+a_{13}(a_{21}a_{32}-a_{22}a_{31}),
$$

the Laplace expansion along the first row. The trace is $a_{11}+a_{22}+a_{33}$.

**Cayley–Hamilton.** The characteristic polynomial is

$$
\chi_{A}(\lambda)=\det(\lambda I-A)=\lambda^{3}-t\lambda^{2}+s\lambda-d,
$$

with

$$
t=\operatorname{tr}A,\qquad
s=\tfrac12\bigl(t^{2}-\operatorname{tr}A^{2}\bigr),\qquad
d=\det A,
$$

and $\chi_{A}(A)=0$. The identity is the Cayley–Hamilton theorem for $3\times3$ matrices; it is used in *The Element, the Coordinates and the Trace* and in *The Cubic, the Discriminant and the Spectral Strata*. The coefficients are the elementary symmetric functions of the eigenvalues, counted with multiplicity.

**Worked example.** Take

$$
A=\begin{pmatrix}1&2&3\\4&5&6\\7&8&10\end{pmatrix}.
$$

Then $\operatorname{tr}A=1+5+10=16$, and

$$
\det A=1(5\cdot10-6\cdot8)-2(4\cdot10-6\cdot7)+3(4\cdot8-5\cdot7)
=2+4-9=-3.
$$

The matrix is invertible, with determinant $-3$. Its characteristic polynomial begins $\lambda^{3}-16\lambda^{2}+s\lambda+3$ with $s=\tfrac12(16^{2}-\operatorname{tr}A^{2})$; the trace of $A^{2}$ is computed from the entries and is not needed here.

**The trace form.** The bilinear form

$$
\langle A,B\rangle_{\mathrm{tr}}=\operatorname{tr}(AB)
$$

is symmetric, $\mathbb{C}$-bilinear and nondegenerate: if $\operatorname{tr}(AB)=0$ for every $B$, then taking $B=E_{ij}$ gives $a_{ji}=0$ for all $i,j$, so $A=0$. It is not positive definite over $\mathbb{C}$, because $\operatorname{tr}(E_{12}^{2})=0$ with $E_{12}\neq0$. The positive definite Hermitian form is

$$
\langle A,B\rangle=\operatorname{tr}(A^{*}B),
$$

with $A^{*}=\bar A^{\mathsf T}$, and it is the subject of *The Involution and the Hermitian Structure*. The two forms agree on Hermitian matrices, where $A^{*}=A$, and differ by a sign on skew-Hermitian matrices, where $A^{*}=-A$; the trace form of this article is the complex bilinear one.

**No null cone.** The form $\langle A,B\rangle=\operatorname{tr}(A^{*}B)$ is positive definite, so its only isotropic vector is $0$. The singular set $\{\det A=0\}$ is a complex hypersurface of real codimension two, not the null cone of a quadratic form. At $n=2$ the algebra is the biquaternion algebra $\mathbb{B}\cong M_{2}(\mathbb{C})$, where the determinant is the N-norm, an indefinite quadratic form with a genuine null cone; that cone is a feature of the two-dimensional case and is not imported here.

## The Centre and Simplicity

**Theorem (the centre).** The centre of $M_{3}(\mathbb{C})$ is the line of scalar matrices:

$$
Z(M_{3}(\mathbb{C}))=\mathbb{C}I.
$$

**Proof.** Let $A$ commute with every matrix. Commuting with $E_{kk}$ gives

$$
AE_{kk}=E_{kk}A.
$$

The left side has columns: the $k$-th column of $A$ in position $k$, the other columns zero; the right side has only the $k$-th row of $A$ in row $k$. Comparing the entries, $a_{ik}=0$ for $i\neq k$ and $a_{kj}=0$ for $j\neq k$; so $A$ is diagonal. Commuting with $E_{kl}$ for $k\neq l$ then gives $a_{kk}E_{kl}=a_{ll}E_{kl}$, so $a_{kk}=a_{ll}$ for all $k,l$. Hence $A=aI$. Conversely every scalar matrix is central. The centre is one-dimensional.

**Theorem (simplicity).** $M_{3}(\mathbb{C})$ is simple: its only two-sided ideals are $0$ and the whole algebra.

**Proof.** Let $I$ be a nonzero two-sided ideal and $0\neq A\in I$. Some entry $a_{ij}$ is nonzero. The element

$$
E_{ii}AE_{jj}=a_{ij}E_{ij}
$$

lies in $I$, so $E_{ij}\in I$. For any $k,l$, the product

$$
E_{ki}E_{ij}E_{jl}=E_{kl}
$$

lies in $I$, because $I$ is a two-sided ideal. The matrix units span, so $I=M_{3}(\mathbb{C})$.

**Corollary.** $M_{3}(\mathbb{C})$ is a **central simple** $\mathbb{C}$-algebra: simple, with centre $\mathbb{C}$. Its only finite-dimensional modules are the multiples of the defining module $\mathbb{C}^{3}$, by the structure theory of simple algebras; the modules are *The Modules and the Minimal Left Ideals*.

**The algebra is not a division algebra.** It has zero divisors: $E_{12}E_{21}=E_{11}\neq0$ but $E_{12}E_{12}=0$, and more simply $E_{12}\neq0$ with $E_{12}^{2}=0$. Every off-diagonal matrix unit is nilpotent. The algebra is therefore not a division ring, and the singular matrices are exactly the non-units.

## The Unit Group and the Projective Group

**Definition.** The **unit group** is

$$
GL_{3}(\mathbb{C})=\{A\in M_{3}(\mathbb{C}):\det A\neq0\},
$$

with the multiplication of matrices. The **projective linear group** is

$$
PGL_{3}(\mathbb{C})=GL_{3}(\mathbb{C})/\mathbb{C}^{\times}I,
$$

the quotient by the scalar matrices.

**Proposition.** $GL_{3}(\mathbb{C})$ is a complex algebraic group of complex dimension $9$ and real dimension $18$. The determinant is a surjective homomorphism

$$
\det:GL_{3}(\mathbb{C})\longrightarrow\mathbb{C}^{\times},
$$

whose kernel is $SL_{3}(\mathbb{C})$, of complex dimension $8$.

**Proof.** The unit group is the complement of the zero set of the determinant, an open subset of the nine-dimensional complex space, so it has complex dimension nine. The determinant is a polynomial homomorphism, multiplicative by the proposition of §*Trace and Determinant*, and it is surjective because $\operatorname{diag}(d,1,1)$ has determinant $d$. The kernel is the hypersurface $\det=1$, of dimension $9-1=8$.

**Proposition.** The projective group is

$$
PGL_{3}(\mathbb{C})\cong SL_{3}(\mathbb{C})/\mu_{3},
$$

where $\mu_{3}$ is the group of cube roots of unity acting by scalar matrices, and

$$
\dim_{\mathbb{C}}PGL_{3}(\mathbb{C})=8,\qquad
\dim_{\mathbb{R}}PGL_{3}(\mathbb{C})=16.
$$

**Proof.** Every class $[A]\in PGL_{3}$ has a representative of determinant $1$: multiply $A$ by a scalar $\lambda$ with $\lambda^{3}=(\det A)^{-1}$. Two such representatives differ by a scalar $\mu$ with $\mu^{3}=1$, so the quotient is $SL_{3}/\mu_{3}$. The dimension is $\dim SL_{3}=8$. The quotient by the finite group $\mu_{3}$ does not change the dimension.

**The action on the algebra.** $PGL_{3}$ acts on $M_{3}(\mathbb{C})$ by conjugation, $[g]\cdot A=gAg^{-1}$; the scalar matrices act trivially, so the action is well defined. The orbits are the conjugacy classes, and their classification by Jordan type is *The Adjoint Action, the Orbits and the Flag Variety*. The stabiliser of a root with simple spectrum is the maximal torus $(\mathbb{C}^{\times})^{2}$, of dimension two; this is the gauge of *The Frame, the Simple Nilpotents and the Gauge*.

## The Reading over the Real Numbers

**The real vector space is the complexification of the skew-Hermitian matrices.**

Let $A^{*}=\bar A^{\mathsf T}$ be the conjugate transpose. The **Hermitian** matrices are the fixed points of the star, $H^{*}=H$, and the **skew-Hermitian** matrices are the anti-fixed points, $S^{*}=-S$. They are real vector subspaces of $M_{3}(\mathbb{C})$, read as a real vector space of dimension $18$.

**Proposition.** Every matrix splits uniquely as

$$
A=H+S,\qquad H=\tfrac12(A+A^{*}),\quad S=\tfrac12(A-A^{*}),
$$

with $H$ Hermitian and $S$ skew-Hermitian. Consequently

$$
M_{3}(\mathbb{C})=\mathfrak{u}(3)\oplus i\mathfrak{u}(3)
$$

as real vector spaces, where

$$
\mathfrak{u}(3)=\{S:S^{*}=-S\}
$$

is the real Lie algebra of skew-Hermitian matrices, of real dimension $9$, and

$$
\mathfrak{su}(3)=\{S\in\mathfrak{u}(3):\operatorname{tr}S=0\}
$$

has real dimension $8$.

**Proof.** The two combinations are Hermitian and skew-Hermitian because the star is conjugate-linear and involutive: $(A+A^{*})^{*}=A^{*}+A=A+A^{*}$ and $(A-A^{*})^{*}=A^{*}-A=-(A-A^{*})$. Their sum is $A$ and their intersection is zero: a matrix both Hermitian and skew-Hermitian satisfies $H=-H$, so $H=0$. The dimension of $\mathfrak{u}(3)$ is the real dimension of the Hermitian matrices, which is $9$: the diagonal is real (three parameters) and each of the three upper entries is complex (six real parameters). The trace is a real linear functional on $\mathfrak{u}(3)$; its kernel has dimension $8$.

**The complex Lie algebra.** With the commutator bracket $[A,B]=AB-BA$, the real vector space $M_{3}(\mathbb{C})$ is the real Lie algebra $\mathfrak{gl}_{3}(\mathbb{C})$, of real dimension $18$. Its complexification is

$$
\mathfrak{gl}_{3}(\mathbb{C})\cong\mathbb{C}\otimes_{\mathbb{R}}\mathfrak{u}(3),
$$

because $\mathfrak{u}(3)$ spans $M_{3}$ over $\mathbb{C}$ and the complex dimension of the span is $9$. The real form $\mathfrak{u}(3)$ is compact; $\mathfrak{su}(3)$ is its traceless part, of dimension $8$.

**The associative product does not preserve $\mathfrak{u}(3)$.** The product of two skew-Hermitian matrices is not skew-Hermitian in general: $(ST)^{*}=T^{*}S^{*}=(-T)(-S)=TS$, which equals $-ST$ only when $S$ and $T$ anticommute. The decomposition above is a decomposition of the real vector space and of the real Lie algebra, not of the associative algebra. The associative algebra $M_{3}(\mathbb{C})$ is the complexification of the real vector space $\mathfrak{u}(3)$, and its product is the complex bilinear extension of the product of matrices, not a product internal to $\mathfrak{u}(3)$.

**Worked example.** For the matrix $A$ of §*Trace and Determinant*,

$$
H=\tfrac12(A+A^{*})=\begin{pmatrix}1&3&5\\3&5&7\\5&7&10\end{pmatrix},
\qquad
S=\tfrac12(A-A^{*})=\begin{pmatrix}0&-1&-2\\1&0&-1\\2&1&0\end{pmatrix},
$$

and $A=H+S$. The matrix $H$ is Hermitian, the matrix $S$ is skew-Hermitian, $\operatorname{tr}H=16$ and $\operatorname{tr}S=0$. The real dimension of the space of such $H$ is $9$, and the real dimension of the space of such $S$ is $9$; the two subspaces meet only at $0$ and span the $18$-dimensional real space.

## Summary

$M_{3}(\mathbb{C})$ is the associative unital non-commutative $\mathbb{C}$-algebra of $3\times3$ complex matrices, with the matrix units $E_{ij}$ as a basis and the product rule

$$
\boxed{\;E_{ij}E_{kl}=\delta_{jk}E_{il},\qquad \dim_{\mathbb{C}}M_{3}=9,\qquad \dim_{\mathbb{R}}M_{3}=18.\;}
$$

Its centre is $\mathbb{C}I$, and it is simple and central simple. Its trace is the unique commutator-vanishing linear functional up to scale, its determinant is multiplicative, and the two are related by the characteristic cubic and Cayley–Hamilton. The unit group is $GL_{3}(\mathbb{C})$, of complex dimension $9$, and the projective group is $PGL_{3}(\mathbb{C})=GL_{3}/\mathbb{C}^{\times}I\cong SL_{3}/\mu_{3}$, of complex dimension $8$.

| Property | Value for $M_{3}(\mathbb{C})$ |
|---|---|
| Complex dimension | $9$ |
| Real dimension | $18$ |
| Centre | $\mathbb{C}I$ |
| Simple | yes |
| Division algebra | no; $E_{12}^{2}=0$ |
| Unit group | $GL_{3}(\mathbb{C})$, $\dim_{\mathbb{C}}=9$ |
| Projective group | $PGL_{3}(\mathbb{C})$, $\dim_{\mathbb{C}}=8$ |
| Real form | $\mathfrak{u}(3)\oplus i\mathfrak{u}(3)$, $\dim_{\mathbb{R}}\mathfrak{u}(3)=9$, $\dim_{\mathbb{R}}\mathfrak{su}(3)=8$ |

The algebra is the complexification of the real vector space $\mathfrak{u}(3)$ of skew-Hermitian matrices, and the Hermitian and skew-Hermitian parts are the real and imaginary readings of one element. No quadratic form is used in the proofs of this article; the positive definite form is *The Involution and the Hermitian Structure*, and the homotopy of the unit group is *The Topology of $M_{3}(\mathbb{C})$*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M_{3}(\mathbb{C})$ | the algebra of $3\times3$ complex matrices |
| $E_{ij}$ | the matrix unit with $1$ in position $(i,j)$ |
| $I$ | the identity matrix |
| $\operatorname{tr}$, $\det$ | the trace and the determinant |
| $\chi_{A}$ | the characteristic polynomial $\det(\lambda I-A)$ |
| $GL_{3}(\mathbb{C})$ | the invertible matrices |
| $SL_{3}(\mathbb{C})$ | the matrices of determinant $1$ |
| $PGL_{3}(\mathbb{C})$ | $GL_{3}/\mathbb{C}^{\times}I$ |
| $A^{*}$ | the conjugate transpose |
| $\mathfrak{u}(3)$, $\mathfrak{su}(3)$ | the skew-Hermitian matrices, and the traceless ones |
| $\mathfrak{gl}_{3}(\mathbb{C})$ | $M_{3}$ with the commutator bracket |

## Further Reading

- [Matrix Algebras](matrix-algebras.html), for the general theory of $M_{n}(R)$ and the matrix-unit table.
- [The Element, the Coordinates and the Trace](the-element-the-coordinates-and-the-trace-of-m3c.html), for the element, its scalar and traceless parts, and the trace pairing.
- [The Involution and the Hermitian Structure](the-involution-and-the-hermitian-structure-of-m3c.html), for the star, the positive definite form and the real forms.
- [Roots of Unity and the Lagrange Idempotents](roots-of-unity-and-the-lagrange-idempotents-of-m3c.html), for the root and its idempotents.
- [The Peirce Decomposition of $M_3(\mathbb{C})$](the-peirce-decomposition-of-m3c.html), for the decomposition by the idempotents.
- [The Determinant and Alternating Forms](the-determinant-and-alternating-forms.html), for the determinant and its multiplicativity.
- [Central Simple Algebras and the Brauer Group](central-simple-algebras-and-the-brauer-group.html), for the structure theory of simple algebras.
- [The Adjoint Action of a Lie Algebra](the-adjoint-action-of-a-lie-algebra.html), for the commutator bracket.
