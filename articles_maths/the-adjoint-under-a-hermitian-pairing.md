
# __The Adjoint under a Hermitian Pairing__

## Introduction

A Hermitian pairing on a vector space over a field with an involution assigns to every linear operator $T$ an **adjoint** $T^{\dagger}$, the operator characterised by the identity $h(Tx,y) = h(x,T^{\dagger}y)$; in a basis the adjoint is the conjugate transpose of the matrix sandwiched between the matrix of the pairing and its inverse, $T^{\dagger} = H^{-1}T^{*}H$, so the adjoint is a **two-sided operator with adjoint**, built from the pairing by a sandwich. The article develops the adjoint in this layer of the corpus: the pairing is the datum, the adjoint is the operator it induces on the algebra of the operators, and the **self-adjoint elements**, the operators equal to their own adjoints, are the Hermitian elements of the geometry. The two involutions of the corpus are kept apart: the involution on the **elements** is the field conjugation with which the pairing is sesquilinear, and the adjoint on the **operators** is the structure of the present article, induced by the pairing; they agree only in the unitary case, and the article proves where.

The article develops the Hermitian pairing and the existence and the uniqueness of the adjoint, its explicit matrix form and its properties, the self-adjoint and the skew-adjoint elements with their decomposition, the unitary elements and the group they form, the adjoint as the two-sided sandwich $H^{-1}(\cdot)^{*}H$ with its relation to the algebra involution, and the standard examples. The spectral theory of the self-adjoint operators is *Self-Adjoint Operators and the Spectral Theorem*, and the geometry of the unitary group is *Unitary Geometry over a Field with Involution*; the article owns the adjoint construction and its algebraic properties.

The article assumes *Unitary Geometry over a Field with Involution* for the field with an involution, the Hermitian forms and the unitary group; *Bilinear Forms* and *Quadratic Forms and Polarisation* of Part II for the pairings and their nondegeneracy; *The Operators on an Algebra* of Part III for the two-sided operators and the sandwich; and *Linear Maps and Matrices* and *Vector Spaces* of Part I for the linear operators and the matrices. The spectral theory of the self-adjoint operators and the analytic adjoint on a Hilbert space are Part III and later in this Part, named as forward references. No distance and no physics is invoked.

## The Hermitian Pairing and the Adjoint

### The Pairing

**Definition.** Let $V$ be a finite-dimensional vector space over a field $K$ with an involution $c$, written with a bar, and let $h$ be a **nondegenerate Hermitian pairing**, that is, a sesquilinear form with $h(x,y) = \overline{h(y,x)}$ and with the radical zero; in a basis the pairing has the matrix $H$ with $H^{*} = H$, and the pairing is the datum of the geometry.

**Proposition.** A nondegenerate pairing induces an isomorphism $V \to V^{*}$, $y \mapsto h(\cdot,y)$, and its inverse; the pairing identifies the space with its dual in a conjugate-linear way, and the algebra of the operators carries the structure of a **ring with involution**, whose involution is the adjoint of the next subsection. The pairing is two-sided: it pairs the left argument linearly and the right argument conjugate-linearly, and this asymmetry is the source of the conjugate-linearity of the adjoint.

**Proof.** The nondegeneracy is the invertibility of the map to the dual; the sesquilinearity gives the linearity in the left argument and the conjugate-linearity in the right, and the Hermitian condition makes the induced map conjugate-linear. The statement is the standard duality of a sesquilinear form, in *Bilinear Forms* and *Unitary Geometry over a Field with Involution*.

### The Adjoint

**Definition.** Let $T \in \operatorname{End}_K(V)$. The **adjoint** of $T$ with respect to $h$ is the operator $T^{\dagger}$ defined by

$$
h(Tx, y) = h(x, T^{\dagger}y) \qquad \text{for all } x, y \in V ;
$$

it exists and is unique because the pairing is nondegenerate.

**Theorem.** The adjoint exists and is unique, it is an operator of $\operatorname{End}_K(V)$, and in a basis it has the matrix

$$
T^{\dagger} = H^{-1}\, T^{*}\, H , \qquad T^{*} = \overline{T}^{\mathsf T} ,
$$

where $H$ is the matrix of the pairing and the star is the conjugate transpose; the adjoint is therefore the **two-sided sandwich** of the conjugate transpose between the matrix of the pairing and its inverse, and it is the unique operator with the defining identity.

**Proof.** The map $y \mapsto h(Tx,y)$ is a linear form on the first argument, so the nondegeneracy gives a unique vector $T^{\dagger}x$ representing it, and the assignment is linear in $x$; in the coordinates the identity is $x^{*}HTy = (Tx)^{*}Hy = x^{*}T^{*}Hy = h(x, T^{\dagger}y) = x^{*}H T^{\dagger}y$, and cancelling the nondegenerate form gives $HT = T^{*}H$, which is the displayed formula after the multiplication by $H^{-1}$. The statement is the standard matrix form of the adjoint, in *Linear Maps and Matrices*.

## Properties of the Adjoint

### The Involution on the Operators

**Theorem.** The adjoint has the following properties for all $S, T \in \operatorname{End}_K(V)$ and $\lambda \in K$:

$$
(S T)^{\dagger} = T^{\dagger} S^{\dagger}, \qquad (S + T)^{\dagger} = S^{\dagger} + T^{\dagger}, \qquad (\lambda T)^{\dagger} = \bar{\lambda}\, T^{\dagger}, \qquad (T^{\dagger})^{\dagger} = T ,
$$

so the adjoint is a **conjugate-linear anti-automorphism of order two** of the algebra of the operators: it reverses the order of the product, it is additive, it is conjugate-linear over the scalars, and it is an involution. The adjoint is the involution of the algebra $\operatorname{End}_K(V)$ induced by the pairing, and it depends on the pairing and not on the algebra alone.

**Proof.** The anti-multiplicativity is $h(STx,y) = h(Tx,S^{\dagger}y) = h(x,T^{\dagger}S^{\dagger}y)$, so $(ST)^\dagger = T^\dagger S^\dagger$; the additivity is the linearity of the pairing; the conjugate-linearity is $h(\lambda Tx,y) = \lambda h(Tx,y) = \lambda h(x,T^\dagger y) = h(x,\bar\lambda T^\dagger y)$, so $(\lambda T)^\dagger = \bar\lambda T^\dagger$; the involution property is the Hermitian symmetry $h(Tx,y) = \overline{h(y,Tx)} = \overline{h(T^\dagger y,x)} = h(x,T^\dagger y)$ applied twice. The statement is in *The Operators on an Algebra* and *Hilbert Algebras*.

**Remark (the two involutions).** The involution on the **elements** of $V$ is the field conjugation extended to the coefficients, and the adjoint on the **operators** is the involution of the previous theorem; the two are different structures, and the adjoint is defined only after the pairing is chosen. Two pairings give two adjoints on the same algebra, the transpose with respect to a bilinear pairing and the Hermitian adjoint with respect to a Hermitian one being the standard example; when the two coincide the representation is a $*$-representation, and the agreement is proved and not assumed.

### The Self-Adjoint and the Skew-Adjoint Elements

**Definition.** An operator $T$ is **self-adjoint** or **Hermitian** when $T^{\dagger} = T$, **skew-adjoint** or **skew-Hermitian** when $T^{\dagger} = -T$, and **unitary** when $T^{\dagger}T = T T^{\dagger} = \mathrm{id}$; the sets of the Hermitian and the skew-Hermitian operators are written $\operatorname{Herm}(V,h)$ and $\operatorname{Skew}(V,h)$.

**Theorem.** When $2$ is invertible in $K$ the algebra of the operators decomposes as the direct sum

$$
\operatorname{End}_K(V) = \operatorname{Herm}(V,h) \oplus \operatorname{Skew}(V,h), \qquad T = \tfrac12(T + T^{\dagger}) + \tfrac12(T - T^{\dagger}) ,
$$

the Hermitian part and the skew-Hermitian part; the Hermitian operators form a $K_0$-vector space of the dimension $n^2$ over $K_0$ in the quadratic case, and the skew-Hermitian operators form the complement; the trace of a self-adjoint operator lies in the fixed field $K_0$, and the trace of a skew-adjoint operator lies in the trace-zero part of $K$ over $K_0$.

**Proof.** The two summands are the eigenspaces of the adjoint involution for the eigenvalues $+1$ and $-1$, and an involution of order two over a field in which $2$ is invertible decomposes the algebra as the direct sum of its fixed parts; the dimensions are the number of the independent entries of a Hermitian matrix and its complement. The statement is the elementary decomposition of an algebra with involution, in *Hilbert Algebras* and *Involutive Bilinear Algebras*.

**Proposition.** The Hermitian operators of a Hermitian space over the real or the complex field have real eigenvalues, and the skew-Hermitian operators have purely imaginary eigenvalues; the Hermitian operators are diagonalisable in an orthonormal basis, and the eigenvalues of a Hermitian form are the eigenvalues of its matrix with respect to the standard pairing. The spectral theory is *Self-Adjoint Operators and the Spectral Theorem*.

**Proof.** For a self-adjoint $T$ and an eigenvector $x$ with eigenvalue $\lambda$ the identity $\lambda h(x,x) = h(Tx,x) = \overline{h(x,Tx)} = \bar\lambda h(x,x)$ gives $\lambda = \bar\lambda$, so the eigenvalue lies in the fixed field; the diagonalisation is the spectral theorem over $\mathbb{R}$ and $\mathbb{C}$. The statement is in *Self-Adjoint Operators and the Spectral Theorem*.

## The Unitary Elements and the Group

**Definition.** The **unitary elements** of $\operatorname{End}_K(V)$ are the operators with $T^{\dagger}T = \mathrm{id}$; they form the **unitary group** $U(V,h)$ of the pairing, and they are exactly the isometries of the form, $h(Tx,Ty) = h(x,y)$ for all $x,y$.

**Theorem.** The unitary elements form a group under the composition, equal to the group of the isometries of $h$; the determinant of a unitary element has norm one, $N(\det T) = 1$ in the nontrivial case, and the special unitary group is the subgroup of determinant one. The self-adjoint and the skew-adjoint elements are the tangent spaces of the unitary group at the identity,

$$
\mathfrak{u}(V,h) = \operatorname{Skew}(V,h) ,
$$

the Lie algebra of the unitary group, and the exponential of a skew-adjoint operator is unitary.

**Proof.** The isometry condition is $h(Tx,Ty) = h(x,y)$ for all $x,y$, which is $T^{\dagger}T = \mathrm{id}$ after the identity $h(Tx,Ty) = h(x,T^\dagger T y)$; the norm-one determinant is the computation of the previous articles; the Lie algebra is the derivative of the condition $T^\dagger T = \mathrm{id}$ at the identity, which gives $X^\dagger + X = 0$, that is, the skew-adjoint operators. The statement is in *Unitary Geometry over a Field with Involution* and *Lie Algebras*.

**Remark (the unitary group as the fixed group).** The unitary group is the group of the fixed elements of the antiautomorphism $T \mapsto (T^{\dagger})^{-1}$ of the general linear group, and it is the group of the isometries of the pairing; the adjoint involution and the unitary group are the operator-layer structures of the Hermitian geometry, while the self-adjoint elements are the elements of the Lie algebra of the group and the fixed elements of the involution.

## The Adjoint as a Two-Sided Operator

**Definition.** The **adjoint map** is the map of the algebra of the operators

$$
\mathrm{ad}_h : \operatorname{End}_K(V) \longrightarrow \operatorname{End}_K(V), \qquad \mathrm{ad}_h(T) = T^{\dagger} = H^{-1}\,T^{*}\,H ,
$$

the sandwich of the conjugate transpose between the matrix $H$ of the pairing and its inverse.

**Theorem.** The adjoint map is the composite of the conjugate transpose and the two-sided sandwich by $H$; it is a two-sided operator with the two parameters $H^{-1}$ and $H$, its fixed elements are the self-adjoint operators, its fixed elements up to the sign are the skew-adjoint ones, and the composite $\mathrm{ad}_h^2 = \mathrm{id}$; the adjoint map is the operator-layer involution that the corpus pairs with the element-layer involution of the field, and it is the archetype of the group `- * Operator Theory`.

**Proof.** The map is the composition of the conjugate transpose, an anti-automorphism, with the conjugation by $H$, an inner automorphism; the fixed points are $T^\dagger = T$ by definition, and the square is the identity because the conjugate transpose and the inner automorphism each square to the identity and they commute up to the automorphism. The statement is the definition of the adjoint involution, in *The Operators on an Algebra* and *Hilbert Algebras*.

**Remark (the agreement with the element involution).** When the pairing is the standard one, $H = I$, the adjoint is the conjugate transpose itself, $\mathrm{ad}_h(T) = T^{*}$, and it acts on the operators in the same way that the field involution acts on the scalars; the two involutions then agree and the algebra is a $*$-algebra in the strict sense. For a general pairing the adjoint is the conjugate transpose twisted by the sandwich of $H$, and the two involutions differ; the difference is measured by the matrix $H$ and vanishes exactly when $H$ is scalar.

## Examples

**Example (the matrix algebra and the standard pairing).** Let $V = K^n$ and $h$ the standard pairing, $H = I$; the adjoint is the conjugate transpose $T^{\dagger} = T^{*}$, the self-adjoint operators are the Hermitian matrices, the skew-adjoint are the skew-Hermitian matrices, and the unitary group is the classical unitary group $U(n)$ over $\mathbb{C}$ or the orthogonal group $O(n)$ over $\mathbb{R}$ with the trivial involution.

**Example (the hyperbolic pairing).** Let $\dim V = 2$ and let $h$ have the matrix of the hyperbolic plane; then the adjoint of $T = \begin{pmatrix} a & b \\ c & d\end{pmatrix}$ is $T^{\dagger} = H^{-1}T^{*}H$ with the sign on the off-diagonal entries reversed, and the skew-adjoint operators of the hyperbolic plane form a real Lie algebra isomorphic to $\mathfrak{su}(1,1)$, which is isomorphic to $\mathfrak{sl}_2(\mathbb{R})$. The hyperbolic pairing is the local model of the unitary group of signature $(1,1)$.

**Example (the finite field).** Let $K = \mathbb{F}_{q^2}$ with the Frobenius involution and the standard Hermitian pairing on $K^n$; the adjoint is the conjugate transpose, the self-adjoint operators are the Hermitian matrices over the finite field, and the unitary group is the finite group $GU(n,q)$ of *Unitary Geometry over a Field with Involution*. The example shows that the adjoint construction is algebraic and needs no order and no topology.

## Summary

A nondegenerate Hermitian pairing $h$ induces on the algebra of the operators the **adjoint** $T^{\dagger}$, the unique operator with $h(Tx,y) = h(x,T^{\dagger}y)$; in a basis it is the two-sided sandwich $T^{\dagger} = H^{-1}T^{*}H$ of the conjugate transpose between the matrix of the pairing and its inverse. The adjoint is a conjugate-linear anti-automorphism of order two, $(ST)^\dagger = T^\dagger S^\dagger$, $(\lambda T)^\dagger = \bar\lambda T^\dagger$, $(T^\dagger)^\dagger = T$; when $2$ is invertible the algebra decomposes into the self-adjoint and the skew-adjoint operators, the eigenspaces of the involution, and the self-adjoint operators have their trace in the fixed field. The unitary elements, those with $T^\dagger T = \mathrm{id}$, are exactly the isometries of the pairing and form the unitary group, whose Lie algebra is the space of the skew-adjoint operators; the self-adjoint operators are the fixed elements of the adjoint map and the elements of the tangent space under the identification by the pairing. The adjoint map is the two-sided operator $H^{-1}(\cdot)^{*}H$ with the parameters $H^{-1}$ and $H$, the archetype of the operator-layer involution, and it agrees with the element-layer involution exactly when the pairing is standard.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(K,c)$, $\bar{x}$ | Field with involution and its conjugation |
| $h(x,y)$, $h(x,y) = \overline{h(y,x)}$ | Nondegenerate Hermitian pairing |
| $H$, $H^{*} = H$ | Matrix of the pairing |
| $T^{\dagger}$ | Adjoint, $h(Tx,y) = h(x,T^{\dagger}y)$ |
| $T^{\dagger} = H^{-1}T^{*}H$ | Matrix form of the adjoint |
| $T^{*} = \overline{T}^{\mathsf T}$ | Conjugate transpose |
| $\operatorname{Herm}(V,h)$, $\operatorname{Skew}(V,h)$ | Self-adjoint and skew-adjoint operators |
| $T^{\dagger} = T$, $T^{\dagger} = -T$ | Self-adjoint and skew-adjoint conditions |
| $U(V,h) = \{T : T^{\dagger}T = \mathrm{id}\}$ | Unitary group, the isometries |
| $\mathfrak{u}(V,h) = \operatorname{Skew}(V,h)$ | Lie algebra of the unitary group |
| $\mathrm{ad}_h(T) = H^{-1}T^{*}H$ | Adjoint map, the two-sided involution |
| $N(\det T) = 1$ | Norm-one determinant of a unitary element |

## Further Reading

- Nathan Jacobson, *Lectures in Abstract Algebra*, vol. 2 (Van Nostrand, 1953), for the adjoint and the algebras with involution.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the adjoint involutions and the unitary groups.
- Paul R. Halmos, *Finite-Dimensional Vector Spaces*, 2nd ed. (Van Nostrand, 1958), for the adjoint of a linear transformation and the spectral theorem.
- Jean Dieudonné, *La géométrie des groupes classiques* (Springer, 1955), for the unitary groups and their Lie algebras.
- Serge Lang, *Algebra*, 3rd ed. (Springer, 2002), for the sesquilinear forms, the Hermitian matrices and the classical groups.
