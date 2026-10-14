# __The General Quaternionic Algebra in the 4×4 Matrix Element Representation $M_4(\mathbb{R})_L$__

## Introduction

The left regular representation of $\mathbb{H}$ is the map that sends a quaternion to the matrix of left multiplication by it in the basis $e_0,e_1,e_2,e_3$. On that image the **quaternionic product** of the block is the matrix product with the transpose in the first slot, the **quaternionic form** is a quarter of the trace pairing with the transpose in the second slot, the invariants are the trace $4q_0$ and the determinant $N(\tilde q)^2$, and the centraliser of the image is the second, commuting copy of the algebra, the right regular representation of the opposite. This article reads the objects of the block in that model and compares with the plain block and with the complex case; the complex matrix model is *The General Quaternionic Algebra in the 2×2 Matrix Element Representation $M_2(\mathbb{C})$*, above this article in this category; the product is *Introduction to the General Quaternionic Algebra of Quaternions*, above this article in this category; the form is *The Isotropic Structure of the General Quaternionic Algebra*, above this article in this category; the operators are *Two-Sided Operators on the General Quaternionic Algebra of Quaternions*, above this article in this category; and the shell is *The Pin and Spin Groups of the General Quaternionic Algebra of Quaternions*, above this article in this category.

**Conventions of the block.** The quaternionic product is written with the star, $\tilde p \star \tilde q = \tilde p^{\natural}\tilde q$, and the plain product by juxtaposition; the basis is $e_0,e_1,e_2,e_3$ with $e_0$ the unit; the generic element is $\tilde q$; the conjugation is ${}^{\natural}$, negating $e_1,e_2,e_3$; the two forms are the quaternionic form $N(\tilde p,\tilde q) = \mathrm{Sc}(\tilde p\tilde q^{\natural})$ of signature $(4,0)$ and the plain form $\mathrm B(\tilde p,\tilde q) = \mathrm{Sc}(\tilde p\tilde q)$ of signature $(1,3)$; the products of the block are the plain product $\tilde p\tilde q$ and the quaternionic product $\tilde p \star \tilde q$, and none other; $L_{\tilde a}$ and $R_{\tilde b}$ are the plain left and right multiplications; $\tilde a[\,]\tilde b$ is the sandwich $\tilde q \mapsto \tilde a\tilde q\tilde b$ of the plain block, and its quaternionic companion is the transposed sandwich $\tilde q \mapsto \tilde a^{\natural}\tilde q\tilde b$. Each name is used in one sense only.

*Remark.* The conventions are collected here because the article is the last of the block and uses the whole apparatus: a reader who meets a symbol above reads its fixed sense here. The list is a convention and not a mathematical result. The bracket $[\,]$ is never the generic product of this block; where it occurs it is the commutator.

## The Left Regular Representation

**Definition.** The **left regular representation** is the map

$$
\mathsf M_4(\tilde q) : \tilde r \mapsto \tilde q\tilde r , \qquad (\mathsf M_4(\tilde q))_{ij} = \text{the } e_i\text{-coordinate of } \tilde q e_j ,
$$

the matrix of the plain left multiplication $L_{\tilde q}$ in the basis $e_0,e_1,e_2,e_3$.

**Theorem.** $\mathsf M_4$ is an injective algebra homomorphism, $\mathsf M_4(\tilde p\tilde q) = \mathsf M_4(\tilde p)\mathsf M_4(\tilde q)$, with four-dimensional image; the image is a subalgebra of $M_4(\mathbb{R})$ isomorphic to $\mathbb{H}$, with the identity matrix for unit. $\mathsf M_4(e_1)$ and $\mathsf M_4(e_2)$ are the matrices of the companion reading of the plain algebra, and $\mathsf M_4(e_3) = \mathsf M_4(e_1)\mathsf M_4(e_2)$, $\mathsf M_4(e_0) = \mathrm I_4$.

*Proof.* $L_{\tilde p}L_{\tilde q} = L_{\tilde p\tilde q}$ and the matrix of a composite is the product of the matrices; injectivity is $L_{\tilde q}(e_0) = \tilde q$; the four basis matrices are linearly independent because their first columns are the four basis vectors.

## The Quaternionic Product

**Theorem (the product in the model).** On the image the quaternionic product is the **transposed product**

$$
\mathsf M_4(\tilde p \star \tilde q) = \mathsf M_4(\tilde p^{\natural}\tilde q) = \mathsf M_4(\tilde p)^{\mathsf T}\,\mathsf M_4(\tilde q) ,
$$

the matrix product with the transpose taken in the first factor.

*Proof.* The transposition relation $\mathsf M_4(\tilde q)^{\mathsf T} = \mathsf M_4(\tilde q^{\natural})$, which is the theorem of the companion reading of the plain algebra, together with the multiplicativity of $\mathsf M_4$, gives $\mathsf M_4(\tilde p^{\natural}\tilde q) = \mathsf M_4(\tilde p^{\natural})\mathsf M_4(\tilde q) = \mathsf M_4(\tilde p)^{\mathsf T}\mathsf M_4(\tilde q)$.

**Corollary (the square and the norm).** For every element,

$$
\mathsf M_4(\tilde q \star \tilde q) = \mathsf M_4(\tilde q)^{\mathsf T}\mathsf M_4(\tilde q) = N(\tilde q)\,\mathrm I_4 ,
$$

the Gram matrix of the coordinate vector of $\tilde q$; it is positive semidefinite, and it is the identity exactly on the shell $N = 1$.

*Proof.* $\mathsf M_4(\tilde q^{\natural}\tilde q) = \mathsf M_4(N(\tilde q)e_0) = N(\tilde q)\mathrm I_4$, and $X^{\mathsf T}X$ has the squared coordinates on the diagonal.

**Corollary (the transpose-sandwich family).** The two-sided operators of the quaternionic product are the transposed sandwiches,

$$
\mathsf M_4\bigl(\tilde a^{\natural}\tilde x\tilde b\bigr) = \mathsf M_4(\tilde a)^{\mathsf T}\,\mathsf M_4(\tilde x)\,\mathsf M_4(\tilde b) ,
$$

so the operator family of *Two-Sided Operators on the General Quaternionic Algebra of Quaternions*, above this article in this category, is the family $X \mapsto A^{\mathsf T}XB$ in the regular model, where the plain family reads $X \mapsto AXB$.

*Proof.* Multiplicativity of $\mathsf M_4$ on both slots and the transposition relation.

## The Form

**Theorem (the form in the model).** The quaternionic form is a quarter of the trace pairing with the transpose,

$$
N(\tilde p,\tilde q) = \mathrm{Sc}(\tilde p\tilde q^{\natural}) = \tfrac14\operatorname{tr}\bigl(\mathsf M_4(\tilde p)\mathsf M_4(\tilde q)^{\mathsf T}\bigr) .
$$

*Proof.* $\operatorname{tr}\mathsf M_4(\tilde q) = 4q_0$, because the diagonal entry $(\mathsf M_4(\tilde q))_{ii}$ is the $e_i$-coordinate of $\tilde qe_i$ and the vector contributions cancel pairwise; hence $\operatorname{tr}(\mathsf M_4(\tilde p\tilde q^{\natural})) = 4\,\mathrm{Sc}(\tilde p\tilde q^{\natural})$.

**Theorem (the coefficient Gram matrix).** In the basis $e_0,e_1,e_2,e_3$,

$$
G_{\mu\nu} = \tfrac14\operatorname{tr}\bigl(\mathsf M_4(e_\mu)\mathsf M_4(e_\nu)^{\mathsf T}\bigr) = \mathbb{1}_4 ,
$$

of signature $(4,0)$, the identity matrix, and not the diagonal $D$ of the plain block.

*Proof.* $\operatorname{tr}\mathsf M_4(e_0) = 4$ gives the scalar entry $1$; $\mathsf M_4(e_k)^{\mathsf T} = -\mathsf M_4(e_k)$ by the transposition relation, so $\operatorname{tr}(\mathsf M_4(e_k)\mathsf M_4(e_k)^{\mathsf T}) = -\operatorname{tr}\mathsf M_4(e_k^2) = -\operatorname{tr}(-\mathrm I_4) = 4$; and the cross traces vanish because $\operatorname{tr}\mathsf M_4(e_ke_l) = 0$ for $k \neq l$.

**Corollary (the two forms compared).** The plain form is a quarter of the trace pairing without the transpose, $\mathrm B(\tilde p,\tilde q) = \tfrac14\operatorname{tr}(\mathsf M_4(\tilde p)\mathsf M_4(\tilde q))$, with Gram matrix $D = \operatorname{diag}(1,-1,-1,-1)$ of signature $(1,3)$; the quaternionic form is the same pairing with the transpose in the second slot, with Gram matrix $\mathbb{1}_4$ of signature $(4,0)$. The transpose is the matrix form of the conjugation, and it is the whole difference of the two forms.

## The Two Commuting Copies

**Definition.** The **right regular representation** is $\mathsf R_4(\tilde q) : \tilde r \mapsto \tilde r\tilde q$, the matrix of the plain right multiplication; it is an anti-homomorphism, $\mathsf R_4(\tilde p\tilde q) = \mathsf R_4(\tilde q)\mathsf R_4(\tilde p)$.

**Theorem.** The two images commute, $\mathsf M_4(\tilde p)\mathsf R_4(\tilde q) = \mathsf R_4(\tilde q)\mathsf M_4(\tilde p)$, and the centraliser of the image of $\mathsf M_4$ in $M_4(\mathbb{R})$ is the image of $\mathsf R_4$, of dimension four; the two images generate $M_4(\mathbb{R})$ and the bicommutant of either is itself.

*Proof.* The commutativity is $L_{\tilde p}R_{\tilde q} = R_{\tilde q}L_{\tilde p}$; for the centraliser, an operator commuting with every left multiplication is a right multiplication, by the double centraliser computation of the block, which is *One-Sided Operators on the General Quaternionic Algebra of Quaternions*, above this article in this category; the two copies generate the sixteen-dimensional enveloping algebra because $\operatorname{span}(\mathcal L \cup \mathcal R)$ together with its products gives all of $\operatorname{End}_\mathbb{R}(\mathbb{H})$.

**Corollary.** The quaternionic product uses the transpose inside the left regular copy alone, and the two commuting copies are those of the plain block; the enveloping algebra of the block is $M_4(\mathbb{R})$, as in the plain reading.

## The Invariants and the Shell

**Theorem (trace and determinant).** For every $\tilde q$,

$$
\operatorname{tr}\mathsf M_4(\tilde q) = 4q_0 , \qquad \det\mathsf M_4(\tilde q) = N(\tilde q)^2 .
$$

*Proof.* The trace is above. For the determinant, the operator $L_{\tilde q}$ has the complex eigenvalues $\alpha$ and $\overline{\alpha}$ with multiplicity two, where $\alpha = q_0 + |\vec q|i$ is a root of $\alpha^2 - 2q_0\alpha + N(\tilde q) = 0$, so $\det L_{\tilde q} = \alpha^2\overline{\alpha}^2 = N(\tilde q)^2$.

**Corollary (the units).** $\mathsf M_4(\tilde q)$ is invertible exactly when $\tilde q \neq 0$, with positive determinant; the image of the unit group is the group of invertible matrices in the image, isomorphic to $\mathbb{H}^{\times}$.

**Theorem (the shell).** The shell $N = 1$ corresponds to the orthogonal matrices of the image:

$$
\mathsf M_4(\tilde q)^{\mathsf T}\mathsf M_4(\tilde q) = \mathrm I_4 \iff N(\tilde q) = 1 ,
$$

so that the image of $\mathbb{H}^1$ is the intersection of the image with the special orthogonal group $SO(4)$; it is the pin and spin group of the quaternionic form by *The Pin and Spin Groups of the General Quaternionic Algebra of Quaternions*, above this article in this category, and the left regular representation is its orthogonal matrix model.

*Proof.* $\mathsf M_4(\tilde q)^{\mathsf T}\mathsf M_4(\tilde q) = \mathsf M_4(\tilde q^{\natural}\tilde q) = N(\tilde q)\mathrm I_4$ by the transposed product and the transposition relation, so orthogonality is $N(\tilde q) = 1$; the determinant of such a matrix is $N(\tilde q)^2 = 1$, so the matrices are in $SO(4)$, and conversely.

## Comparison with the Plain Block and with the Complex Case

**Proposition (the two blocks in the model).**

| feature | plain block | quaternionic block |
|---|---|---|
| product | $\mathsf M_4(\tilde p\tilde q) = \mathsf M_4(\tilde p)\mathsf M_4(\tilde q)$ | $\mathsf M_4(\tilde p \star \tilde q) = \mathsf M_4(\tilde p)^{\mathsf T}\mathsf M_4(\tilde q)$ |
| form | $\tfrac14\operatorname{tr}(XY)$, Gram $D$, signature $(1,3)$ | $\tfrac14\operatorname{tr}(XY^{\mathsf T})$, Gram $\mathbb{1}_4$, signature $(4,0)$ |
| square | $\det = N(\tilde q)^2$ | $\mathsf M_4(\tilde q \star \tilde q) = N(\tilde q)\mathrm I_4$ |
| shell | the unit sphere, read in $SO(4)$ | the same sphere, read in $SO(4)$ |
| centraliser | the right regular copy $\cong \mathbb{H}^{\mathrm{op}}$ | the same |

## Summary

The left regular representation $\mathsf M_4$ with $\mathsf M_4(\tilde q)(\tilde r) = \tilde q\tilde r$ is an injective real-algebra homomorphism of $\mathbb{H}$ into $M_4(\mathbb{R})$ with four-dimensional image. On it the quaternionic product is the transposed product $\mathsf M_4(\tilde p \star \tilde q) = \mathsf M_4(\tilde p)^{\mathsf T}\mathsf M_4(\tilde q)$, so the quaternionic square of an element is the positive scalar matrix $N(\tilde q)\mathrm I_4$; the quaternionic form is $\tfrac14\operatorname{tr}(\mathsf M_4(\tilde p)\mathsf M_4(\tilde q)^{\mathsf T})$ with Gram matrix the identity of signature $(4,0)$; the invariants are $\operatorname{tr}\mathsf M_4(\tilde q) = 4q_0$ and $\det\mathsf M_4(\tilde q) = N(\tilde q)^2$; the shell is the intersection of the image with $SO(4)$, the orthogonal matrix model of the unit sphere.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathsf M_4(\tilde q)$ | left regular matrix of $\tilde q$, $\tilde r \mapsto \tilde q\tilde r$ |
| $\mathsf R_4(\tilde q)$ | right regular matrix, $\tilde r \mapsto \tilde r\tilde q$, generating the centraliser |
| $\mathsf M_4(\tilde p \star \tilde q) = \mathsf M_4(\tilde p)^{\mathsf T}\mathsf M_4(\tilde q)$ | the quaternionic product in the model |
| $N(\tilde p,\tilde q) = \tfrac14\operatorname{tr}(\mathsf M_4(\tilde p)\mathsf M_4(\tilde q)^{\mathsf T})$ | the quaternionic form in the model |
| $\mathbb{1}_4$ | the Gram matrix of $N$, signature $(4,0)$ |
| $\mathsf M_4(\tilde q)^{\mathsf T} = \mathsf M_4(\tilde q^{\natural})$ | the transposition relation, the matrix form of the conjugation |
| $N(\tilde q) = 1$ | the shell, the image intersected with $SO(4)$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the regular representations, the trace pairing and the double centraliser theorem.
- Israel Nathan Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for the left and right regular representations of a division ring and their commutants.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for the bicommutant and the structure of matrix algebras over a division ring.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the regular matrices of the quaternion multiplication and the unit sphere.
