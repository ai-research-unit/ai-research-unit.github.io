
# __Complex Regular Element Representation__

## Introduction

The complex algebra $\mathbb{C}$ is two-dimensional over $\mathbb{R}$ and one-dimensional over itself. This article presents its **regular representation**, the algebra acting on itself on the left, and the $2 \times 2$ real matrix of that action in the basis $1$, $i$. The matrix is the Cayley matrix of complex multiplication, and its image is the algebra of conformal $2 \times 2$ real matrices, the matrices of the shape $aI + a'J$. The article is the base case of the representation group of the tensor family: it sits below the $2 \times 2$ representation of the quaternions $\mathbb{H}$ and the $4 \times 4$ regular representation of the biquaternions $\mathbb{B}$, which is assembled from it by a tensor product.

The conventions are those of *Complex Algebra*: basis $1$, $i$ with $i^2 = -1$, a general element $A = a + i a'$, norm $N(A) = A\bar A = a^2+a'^2$, and complex conjugation $\bar A$. The word *representation* is used in both senses, as in the biquaternion companion: the concrete realization of the algebra by matrices, and the technical action of the algebra on a vector space. The article owns the left matrix, its multiplicativity, the identification with the conformal matrices, the determinant and the trace, and the relation to the quaternion and biquaternion regular representations; the complex-linear one-dimensional representation and the classification of the modules over a field are the subject of *Complex Element Representations* and are cited once.

## The Left Regular Representation

**Definition.** The **left regular representation** of $\mathbb{C}$ is the map

$$
\rho_L : \mathbb{C} \longrightarrow \operatorname{End}_{\mathbb{R}}(\mathbb{C}), \qquad \rho_L(A)(B) = A B .
$$

For each $A$, the map $B \mapsto AB$ is $\mathbb{R}$-linear because multiplication is bilinear, so $\rho_L(A)$ is an $\mathbb{R}$-linear endomorphism of the two-dimensional real space $\mathbb{C}$. Writing each endomorphism as a matrix in the basis $1, i$, the same symbol $\rho_L(A)$ denotes the matrix acting on the column $(b, b')^{\mathsf{T}}$ of $B = b + i b'$.

**Proposition (the regular matrix is the Cayley matrix).** In the basis $1, i$,

$$
\rho_L(A) = \begin{pmatrix} a & -a' \\ a' & a \end{pmatrix} = a I + a' J, \qquad J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \qquad J^2 = -I .
$$

**Proof.** The columns are the images $\rho_L(A)(e_m) = A e_m$ expressed in the basis. For $m = 0$, $A\cdot 1 = A = a + i a'$, giving the first column $(a, a')^{\mathsf{T}}$. For $m = 1$, $A i = (a+i a') i = a i + i^2 a' = -a' + i a$, giving the second column $(-a', a)^{\mathsf{T}}$. The basis element $i$ therefore acts by $J$, and $J^2 = -I$ is the matrix form of $i^2 = -1$.

The matrix has only two independent entries, the two real coordinates of $A$; it is the **Cayley matrix** of complex multiplication. The identity matrix is $\rho_L(1)$, and multiplication by $i$ is $\rho_L(i) = J$, the **complex structure** of the plane.

**Example.** For $A = 3+4i$ the Cayley matrix is

$$
\rho_L(A) = \begin{pmatrix} 3 & -4 \\ 4 & 3 \end{pmatrix}, \qquad \rho_L(A)\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 3 \\ 4 \end{pmatrix},
$$

so the column of $1$ is the column of $A$ itself. For the pair $A = 3+4i$ and $B = 1-2i$ the two matrices are

$$
\rho_L(A) = \begin{pmatrix} 3 & -4 \\ 4 & 3 \end{pmatrix}, \qquad \rho_L(B) = \begin{pmatrix} 1 & 2 \\ -2 & 1 \end{pmatrix}.
$$

**Multiplicativity.** The matrix product is

$$
\rho_L(A)\rho_L(B) = \begin{pmatrix} 3 & -4 \\ 4 & 3 \end{pmatrix}\begin{pmatrix} 1 & 2 \\ -2 & 1 \end{pmatrix}
= \begin{pmatrix} 3+8 & 6-4 \\ 4-6 & 8+3 \end{pmatrix} = \begin{pmatrix} 11 & 2 \\ -2 & 11 \end{pmatrix} = \rho_L(AB),
$$

the matrix of the product $AB = 11-2i$; the reversed order gives $\rho_L(B)\rho_L(A) = \rho_L(AB)$ as well, the concrete form of commutativity.

**Determinant and trace.** $\det \rho_L(A) = 3\cdot 3 - (-4)\cdot 4 = 25 = N(A)$ and $\operatorname{tr}\rho_L(A) = 6 = 2\operatorname{Re} A$; likewise $\det \rho_L(B) = 1\cdot 1 - 2\cdot(-2) = 5 = N(B)$ and $\operatorname{tr}\rho_L(B) = 2 = 2\operatorname{Re} B$.

**The unit factor.** $\rho_L(u) = \tfrac15 \rho_L(A) = \begin{pmatrix} 0.6 & -0.8 \\ 0.8 & 0.6 \end{pmatrix}$ has determinant $0.36+0.64 = 1$ and lies in $SO(2)$, the rotation through $\theta = \arctan(4/3)$; the factorisation $\rho_L(A) = 5\,\rho_L(u)$ is the polar decomposition of the conformal matrix $\rho_L(A)$ into a scalar and a rotation.

**Transposition.** $\rho_L(A)^{\mathsf{T}} = \begin{pmatrix} 3 & 4 \\ -4 & 3 \end{pmatrix} = \rho_L(\bar A)$, since $\bar A = 3-4i$; more generally $\rho_L(A)^{\mathsf{T}} = \rho_L(\bar A)$, the matrix form of the involution.

## The Left Representation Is a Homomorphism

**Theorem (multiplicativity).** For all $A, B \in \mathbb{C}$,

$$
\rho_L(A)\,\rho_L(B) = \rho_L(AB).
$$

Hence $\rho_L$ is an $\mathbb{R}$-algebra homomorphism and the space $\mathbb{C}$ is a left $\mathbb{C}$-module under it. It is **faithful**: if $\rho_L(A) = 0$ then $A = \rho_L(A)(1) = 0$.

**Proof.** Both sides are $\mathbb{R}$-linear in the second factor and are computed on the basis. For every $m$, associativity gives

$$
\rho_L(A)\bigl(\rho_L(B)(e_m)\bigr) = A(B e_m) = (AB) e_m = \rho_L(AB)(e_m),
$$

so the two matrices agree on a basis.

**Example (a concrete check).** For $A = 3+4i$ and $B = 1-2i$ the product is $AB = 11-2i$, and

$$
\rho_L(A)\rho_L(B) = \begin{pmatrix} 3 & -4 \\ 4 & 3 \end{pmatrix}\begin{pmatrix} 1 & 2 \\ -2 & 1 \end{pmatrix} = \begin{pmatrix} 11 & 2 \\ -2 & 11 \end{pmatrix} = \rho_L(AB),
$$

the reversed order giving the same matrix, as the algebra is commutative.

## The Right Regular Representation and Commutativity

**Definition.** The **right regular representation** of $\mathbb{C}$ is the map

$$
\rho_R : \mathbb{C} \longrightarrow \operatorname{End}_{\mathbb{R}}(\mathbb{C}), \qquad \rho_R(A)(B) = B A .
$$

**Proposition.** $\rho_R = \rho_L$.

**Proof.** The algebra is commutative, so $BA = AB$ for all $B$, hence the two endomorphisms agree on every element.

The right regular representation therefore carries no information beyond the left one, and it is not a second realization. This is the first place where the commutative base case differs structurally from the biquaternion algebra: there the left and right regular representations are distinct, the right one is an anti-homomorphism, the naive identity $\rho_R(\tilde{Q}) = \rho_L(\tilde{Q})^{\mathsf{T}}$ is false, and the difference vanishes exactly on the centre. None of that apparatus exists here. The slot is empty because the algebra is commutative, and the emptiness is the statement.

## Transposition and Conjugation

**Proposition.** For every complex number $A$,

$$
\rho_L(A)^{\mathsf{T}} = \rho_L(\bar A),
$$

where the transpose is taken in the basis $1, i$.

**Proof.** Transposing $\rho_L(A) = \begin{pmatrix} a & -a' \\ a' & a \end{pmatrix}$ gives $\begin{pmatrix} a & a' \\ -a' & a \end{pmatrix}$, which is $\rho_L(a - i a') = \rho_L(\bar A)$.

Transposition is therefore complex conjugation in the matrix picture: it is the matrix form of the involution, and the antisymmetric matrix $\rho_L(A) - \rho_L(\bar A)$ changes sign under it. This is the placement, in the two-dimensional case, of the biquaternion identity $\rho_L(\tilde{Q})^{\mathsf{T}} = \rho_L(\tilde{Q}^{\natural})$, where the transpose corresponds to quaternion conjugation; the same theorem holds here with the single involution of the field.

## The Module Structure: Irreducibility

The regular representation is the algebra acting on itself, and over $\mathbb{C}$ the module $\mathbb{C}$ is one-dimensional. Since $\mathbb{C}$ is a field, its only submodules are $\{0\}$ and $\mathbb{C}$ itself:

**Proposition.** The regular module is **simple** (irreducible), and the regular representation has no proper nonzero invariant subspace.

**Proof.** A submodule is a left ideal of the field $\mathbb{C}$, and a field has no proper nonzero ideals. Equivalently, $\rho_L(B)$ spans the whole module for every nonzero $B$.

This is the largest structural difference from the biquaternion algebra. There the regular module is $\mathbb{B} = I_1 \oplus I_2$, the direct sum of two minimal left ideals, and the regular representation is reducible, $\rho_L \cong V \oplus V$ with $V = \mathbb{C}^2$ the simple module. Here the algebra is a field, its regular module is simple, and there is no Peirce decomposition, no idempotent splitting and no centralizer larger than the image itself. The endomorphism algebra of the regular module is $\operatorname{End}_{\mathbb{C}}(\mathbb{C}) = \mathbb{C}$, the image of $\rho_L$, which is the commutative shadow of the double-centralizer statement $\operatorname{End}_{\mathbb{B}}(\mathbb{B}) = \rho_R(\mathbb{B})$ of the biquaternion article.

## The Determinant and the Trace

**Proposition.** For $A = a+i a'$,

$$
\det \rho_L(A) = a^2 + a'^2 = N(A), \qquad \operatorname{tr}\rho_L(A) = 2a = 2 \operatorname{Re} A .
$$

**Proof.** $\det\rho_L(A) = a\cdot a - (-a')\cdot a' = a^2 + a'^2$, and $\operatorname{tr}\rho_L(A) = a + a = 2a$.

The determinant is the norm, and the trace is twice the real part, which is also the algebra trace $\operatorname{Tr}(A)$ of $\mathbb{C}$ over $\mathbb{R}$. This is a genuine difference from the biquaternion regular representation, where the determinant is the **square** of the norm, $\det\rho_L(\tilde{Q}) = N(\tilde{Q})^2$. The square appears there because the biquaternion regular module is the direct sum of two copies of the simple module, so its determinant is the product of two norms; here the regular module is one-dimensional over $\mathbb{C}$ and the determinant is the norm itself. The determinant also shows that $\rho_L(A)$ is invertible exactly when $A \neq 0$, matching the invertibility criterion of *Complex Norm and Invertibility*.

**Corollary.** $\rho_L(A)$ is orientation-preserving for $A \neq 0$, since $\det\rho_L(A) = N(A) > 0$.

## The Images of the Distinguished Subspaces

The two distinguished subspaces $\mathbb{R}_{\mathbb{C}}$ and $i\mathbb{R}_{\mathbb{C}}$ of the algebra have the following images under $\rho_L$:

| subspace | image | matrix characterization |
|---|---|---|
| $\mathbb{R}_{\mathbb{C}}$ | scalar matrices | $\rho_L(a) = a I$, $a \in \mathbb{R}$ |
| $i\mathbb{R}_{\mathbb{C}}$ | traceless skew-symmetric matrices | $\rho_L(i a') = a' J$, $a' \in \mathbb{R}$, $\rho_L(ia')^{\mathsf{T}} = -\rho_L(ia')$ |

The real subspace is the line of scalar matrices, a copy of $\mathbb{R}$ inside $M_2(\mathbb{R})$; the imaginary subspace is the line of skew-symmetric matrices, and $J^2 = -I$ is the matrix form of $i^2 = -1$. The image of $\mathbb{R}_{\mathbb{C}}$ is closed under matrix multiplication; the image of $i\mathbb{R}_{\mathbb{C}}$ is not, since the product of the two multiples $(a'J)(cJ) = -a'c\,I$ of $J$ is a scalar matrix, mirroring $(ia')(ic) = -a'c$ in the algebra. Under the transpose the two lines are distinguished: $\rho_L(A)^{\mathsf{T}} = \rho_L(\bar A)$ negates the imaginary subspace and fixes the real one.

## The Identification with the Conformal Matrices

The image of the regular representation is the algebra

$$
\rho_L(\mathbb{C}) = \left\{ \begin{pmatrix} a & -a' \\ a' & a \end{pmatrix} : a, a' \in \mathbb{R} \right\} = \{ aI + a'J : a, a' \in \mathbb{R} \},
$$

the set of real matrices of the shape $aI + a'J$.

**Proposition.** The matrices of the shape $aI + a'J$ are exactly the real $2 \times 2$ matrices commuting with $J$, equivalently the $\mathbb{R}$-linear maps $\mathbb{R}^2 \to \mathbb{R}^2$ that are complex-linear under the identification $\mathbb{R}^2 \cong \mathbb{C}$. They form a field isomorphic to $\mathbb{C}$ under $\rho_L$, and the nonzero ones are the **conformal** or **similarity** matrices of the plane: each is the composition of a scaling by $r = \sqrt{N(A)} > 0$ and a rotation by $\theta = \arg A$.

**Proof.** A matrix $M = \begin{pmatrix} p & q \\ s & t \end{pmatrix}$ commutes with $J$ exactly when $s = -q$ and $p = t$, which is the shape $aI+a'J$; this is the condition that it be the real matrix of a $\mathbb{C}$-linear map. The map $\rho_L$ is an injective algebra homomorphism by multiplicativity and faithfulness, and its image is therefore a field isomorphic to $\mathbb{C}$. In the polar form $A = re^{i\theta}$ with $r>0$, the matrix factors as

$$
\rho_L(A) = r \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix},
$$

a positive scalar times an element of $SO(2)$; that is, a similarity of ratio $r$ and angle $\theta$.

The image $\rho_L(\mathbb{C})$ is the field of conformal matrices, and its group of nonzero elements is the group of orientation-preserving similarities of the plane fixing the origin; it is isomorphic to $\mathbb{C}^\times \cong \mathbb{R}_{>0} \times SO(2)$. The determinant is the square of the ratio and the trace is twice the real part of the complex number, so the polar decomposition $A = ru$ is the polar decomposition of the conformal matrix into a scalar and a rotation, as developed in *Complex Polar Element Representation* and *Rotations and Reflections in the Complex Plane*.

## The Image of the Unit Circle

**Proposition.** The image of the unit circle under $\rho_L$ is the rotation group of the plane. For $u = e^{i\theta} \in U(1)$,

$$
\rho_L(u) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} = R_\theta, \qquad \det R_\theta = \cos^2\theta + \sin^2\theta = 1, \qquad \operatorname{tr} R_\theta = 2\cos\theta,
$$

and $R_\theta$ is orthogonal, $R_\theta^{\mathsf{T}}R_\theta = I$, with determinant $+1$. The map $u \mapsto \rho_L(u)$ is an isomorphism of Lie groups $U(1) \to SO(2)$.

**Proof.** Substituting $A = e^{i\theta}$ into $\rho_L(A) = aI+a'J$ with $a = \cos\theta$, $a' = \sin\theta$ gives the display, and orthogonality with determinant $+1$ is immediate from it. The map is a homomorphism by multiplicativity, $\rho_L(uv) = \rho_L(u)\rho_L(v)$, it is injective by faithfulness, and it is surjective because every element of $SO(2)$ is such a matrix for exactly one $\theta \in \mathbb{R}/2\pi\mathbb{Z}$.

The rotation matrix is therefore the matrix form of multiplication by a unit, and the product rule $R_\theta R_\varphi = R_{\theta+\varphi}$ is multiplicativity read on the circle. Because $\rho_L(i) = J$, the regular representation carries the exponential of the algebra to the exponential of matrices,

$$
\exp(\theta J) = \sum_{n \ge 0} \frac{\theta^n J^n}{n!} = \cos\theta\, I + \sin\theta\, J = R_\theta,
$$

so the skew-symmetric matrices $\theta J$ form the one-dimensional abelian Lie algebra $\mathrm{SO}(2) \cong \mathbb{R}$ and $\exp : \mathrm{SO}(2) \to SO(2)$ is surjective with kernel $2\pi\mathbb{Z}$. The determinant of a rotation is $N(u) = 1$ and its trace is $2\operatorname{Re} u$, the specialisation of the determinant and trace formulas to the unit circle.

The reflections are the other coset. Since $\rho_L(A)^{\mathsf{T}} = \rho_L(\bar A)$, the transpose realises the involution, and the matrix of the reflection $S_u(A) = u\bar A$ in the basis $\{1, i\}$ is the product $\rho_L(u)E$ with $E = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ the matrix of complex conjugation; with $u = e^{2i\alpha}$ it is

$$
\rho_L(u) E = \begin{pmatrix} \cos 2\alpha & \sin 2\alpha \\ \sin 2\alpha & -\cos 2\alpha \end{pmatrix},
$$

of determinant $-1$, trace $0$ and eigenvalues $+1$ and $-1$, on the fixed line and the perpendicular line of the reflection. The reflection matrices therefore exhaust the nontrivial coset $\rho_L(U(1))E$ of $SO(2)$ in $O(2) = \rho_L(U(1)) \cup \rho_L(U(1))E$.

## The Relation to the Quaternion and Biquaternion Representations

The regular representation of $\mathbb{C}$ is the base factor of a tensor product. For real algebras $A$ and $B$, left multiplication by $c \otimes d$ on $A \otimes_{\mathbb{R}} B$ is the tensor product of the left multiplications,

$$
\rho_{A \otimes B}(c \otimes d) = \rho_A(c) \otimes \rho_B(d),
$$

because $(c \otimes d)(a \otimes b) = ca \otimes db$. Taking $A = \mathbb{C}$ and $B = \mathbb{H}$, so that $A \otimes B = \mathbb{B}$, the regular representation of the biquaternions is the tensor product of the two-dimensional real regular representation of $\mathbb{C}$ and the four-dimensional real regular representation of $\mathbb{H}$:

$$
\rho_L^{\mathbb{B}} = \rho_L^{\mathbb{C}} \otimes_{\mathbb{R}} \rho_L^{\mathbb{H}}, \qquad \dim_{\mathbb{R}} = 2 \times 4 = 8,
$$

which is the $4 \times 4$ complex regular representation of $\mathbb{B}$ read over $\mathbb{R}$. Equivalently, writing an element of $\mathbb{B}$ as $\sum_\mu Q_\mu e_\mu$ with $Q_\mu \in \mathbb{C}$, the complex Cayley factor $\rho_L^{\mathbb{C}}$ acts on each coefficient and the quaternion Cayley factor $\rho_L^{\mathbb{H}}$ acts on the index $\mu$; the two combine into the Cayley matrix of *Biquaternion 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$*.

The lower end of the same hierarchy is the $2 \times 2$ complex representation of the quaternions. Since $\mathbb{H} \otimes_{\mathbb{R}} \mathbb{C} \cong M_2(\mathbb{C})$, the quaternion regular representation, of real dimension $4$, complexifies to the $2 \times 2$ complex representation

$$
\rho^{\mathbb{H}} : \mathbb{H} \longrightarrow M_2(\mathbb{C}), \qquad q = q_0 + q_1 e_1 + q_2 e_2 + q_3 e_3 \longmapsto \begin{pmatrix} q_0 + i q_1 & q_2 + i q_3 \\ -q_2 + i q_3 & q_0 - i q_1 \end{pmatrix},
$$

with determinant $N_{\mathbb{H}}(q) = q_0^2+q_1^2+q_2^2+q_3^2$. The three cases form the chain

| algebra | dimension over $\mathbb{R}$ | regular matrix | determinant |
|---|---|---|---|
| $\mathbb{C}$ | $2$ | $2 \times 2$ real, Cayley | $N_{\mathbb{C}}(A) = a^2+a'^2$ |
| $\mathbb{H}$ | $4$ | $4 \times 4$ real, or $2 \times 2$ complex | $N_{\mathbb{H}}(q)^2$ over $\mathbb{R}$, $N_{\mathbb{H}}(q)$ over $\mathbb{C}$ |
| $\mathbb{B}$ | $8$ | $4 \times 4$ complex, Cayley, reducible | $N_{\mathbb{B}}(\tilde{Q})^2$ |

The complex case is the bottom of the chain in two senses: its regular representation is the smallest Cayley matrix, and its module is simple, whereas the quaternion and biquaternion regular modules are sums of copies of a smaller simple module once the algebra is complexified.

## Summary

The left regular representation of $\mathbb{C}$, defined by $\rho_L(A)(B) = AB$, is the algebra acting on itself on the left, and in the basis $1, i$ its matrix is the Cayley matrix

$$
\rho_L(A) = \begin{pmatrix} a & -a' \\ a' & a \end{pmatrix} = aI + a'J, \qquad J^2 = -I .
$$

It is a faithful $\mathbb{R}$-algebra homomorphism, $\rho_L(A)\rho_L(B) = \rho_L(AB)$; its transpose is the matrix of the conjugate, $\rho_L(A)^{\mathsf{T}} = \rho_L(\bar A)$; its determinant is the norm and its trace is twice the real part. The image is the field of conformal $2 \times 2$ real matrices, the nonzero elements of which are the orientation-preserving similarities of the plane, and the polar decomposition of $A$ is the decomposition of its matrix into a scalar and a rotation. On the distinguished subspaces the image is the line of scalar matrices for $\mathbb{R}_{\mathbb{C}}$ and the line of skew-symmetric matrices for $i\mathbb{R}_{\mathbb{C}}$, and on the unit circle it is the rotation group: $\rho_L$ carries $U(1)$ isomorphically onto $SO(2)$, $u = e^{i\theta}$ to the rotation matrix $R_\theta$, and the reflections $S_u(A) = u\bar A$ to the coset $\rho_L(U(1))E$ of $SO(2)$ in $O(2)$.

Because the algebra is commutative, the right regular representation coincides with the left and the left-right apparatus of the biquaternion case is empty. Because the algebra is a field, the regular module is simple: the biquaternion reduction $\rho_L \cong V \oplus V$ into two minimal left ideals, the determinant $N^2$, and the nontrivial centralizer all have no analogue here, and their absence is the commutativity and the divisibility of $\mathbb{C}$. The complex regular representation is the tensor factor of the biquaternion one, $\rho_L^{\mathbb{B}} = \rho_L^{\mathbb{C}} \otimes_{\mathbb{R}} \rho_L^{\mathbb{H}}$, and the base of the chain whose other members are the $2 \times 2$ complex representation of $\mathbb{H}$ and the reducible $4 \times 4$ complex representation of $\mathbb{B}$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{C}$ | the complex algebra, basis $1$, $i$, $i^2 = -1$ |
| $A = a + i a'$ | a complex number |
| $\rho_L(A)(B) = AB$ | the left regular representation |
| $\rho_R(A)(B) = BA$ | the right regular representation, equal to $\rho_L$ |
| $\rho_L(A) = aI + a'J$ | the Cayley matrix of $A$ |
| $J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ | the complex structure, $J^2 = -I$ |
| $N(A) = a^2+a'^2$ | the norm, $\det\rho_L(A) = N(A)$ |
| $\operatorname{tr}\rho_L(A) = 2\operatorname{Re}A$ | the trace of the regular matrix |
| $\rho_L(\mathbb{C})$ | the image, the field of conformal matrices $\cong \mathbb{C}$ |
| $\mathbb{R}_{\mathbb{C}}, i\mathbb{R}_{\mathbb{C}}$ | the distinguished subspaces, imaged as the scalar and the skew-symmetric matrices |
| $U(1) = \{u : \lvert u\rvert = 1\}$ | the unit circle, imaged as the rotation group |
| $R_\theta = \rho_L(e^{i\theta})$ | the rotation matrix, the image of a unit |
| $E = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ | the matrix of complex conjugation; the reflections are $\rho_L(U(1))E$ |
| $SO(2)$ | the rotation factor of the conformal group |
| $S_u(A) = u\bar A$, $u \in U(1)$ | a reflection of the plane, matrix $\rho_L(u)E$ |
| $O(2) = \rho_L(U(1)) \cup \rho_L(U(1))E$ | the orthogonal group, rotations and reflections |
| $\mathrm{SO}(2) \cong \mathbb{R}$ | the skew-symmetric matrices $\theta J$, the Lie algebra of $SO(2)$ |
| $\rho_L^{\mathbb{C}} \otimes_{\mathbb{R}} \rho_L^{\mathbb{H}}$ | the biquaternion regular representation as a tensor product |

## Further Reading

- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the regular representation of an algebra and its endomorphism algebra.
- Charles B. Curtis and Irving Reiner, *Representation Theory of Finite Groups and Associative Algebras* (Interscience, 1962), for the regular module and its decomposition into minimal left ideals.
- Frank B. Anderson and Kent R. Fuller, *Rings and Categories of Modules*, 2nd edition (Springer, 1992), for the regular module over a field and the simplicity of the regular representation of a division ring.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the Cayley matrix of multiplication and its transpose.
- John Voight, *Quaternion Algebras*, Graduate Texts in Mathematics 288 (Springer, 2021), for the regular representation of a quaternion algebra and its complexification.
- Tristan Needham, *Visual Complex Analysis* (Oxford University Press, 1997), for the conformal-matrix reading of multiplication by a complex number.
