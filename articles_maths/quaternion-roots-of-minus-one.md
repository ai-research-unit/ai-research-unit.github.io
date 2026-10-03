
# __Quaternion Roots of Minus One__

## Introduction

The equation $\xi^2 = -1$ has, in the quaternion algebra, not two solutions but a whole two-dimensional family: the pure unit quaternions. This article determines that family, describes it as a single conjugacy class and as a homogeneous space of the unit group, relates it to the complex structures that the algebra places on its underlying real vector space, solves the companion equation $\xi^2 = +1$, and compares the answer with the biquaternion and split-quaternion cases. It is the article of the quaternion family that owns the square roots of $-1$; the unit group itself is from *Quaternion Norm and Invertibility*, and the adjoint action that realises the conjugacy class is from *Quaternion Rotations and Reflections*.

The single fact on which everything rests is the absence of zero divisors: since a product in $\mathbb{H}$ vanishes only when a factor vanishes, the equation $(\tilde q-1)(\tilde q+1) = 0$ forces $\tilde q = \pm 1$, and a companion argument forces the roots of $-1$ to be pure. Both the smallness of the root set of $+1$ and the roundness of the root set of $-1$ are consequences of the same property, and both fail as soon as the coefficient field is enlarged.

The corpus's default base is a commutative ring with identity, and the algebra is defined there by its presentation. The results below are stated over $\mathbb{R}$, where the algebra is a division algebra; the reduction of the equation and the classification of the roots hold over any field of characteristic not $2$ in which the algebra is a division algebra, and the identification of the root sets with level sets of the central product is the statement over $\mathbb{R}$.

Throughout, $\mathbb{H}$ is the quaternion algebra with basis $e_0 = 1, e_1, e_2, e_3$ and $e_k^2 = -e_0$, a quaternion is $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ with scalar part $q_0$ and vector part $\mathbf{q}\in\operatorname{Im}\mathbb{H}$, the conjugate is $\tilde{q}^{\natural} = q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3$, and the quaternion norm $N$, the unit group $\mathbb{H}^{\times} = \mathbb{H}\setminus\{0\}$ and the unit sphere $Sp(1) = S^3$ are those of *Quaternion Norm and Invertibility*, named here and not defined again.

## The Problem and Its Reduction

### Statement

**Theorem.** A quaternion $\tilde q\in\mathbb{H}$ satisfies $\tilde q^2 = -1$ if and only if $\tilde q$ is a pure imaginary quaternion with $N = 1$,

$$
\tilde q\in\operatorname{Im}\mathbb{H}\cap Sp(1) = \{\tilde q\in\operatorname{Im}\mathbb{H} : N(\tilde q) = 1\}.
$$

*Proof.* Write $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ with $q_0\in\mathbb{R}$ and $\mathbf{q}\in\operatorname{Im}\mathbb{H}$. The square is

$$
\tilde q^2 = q_0^2 - N(\mathbf{q}) + 2q_0\mathbf{q},
$$

because the square of a pure imaginary is the real number $\mathbf{q}^2 = -N(\mathbf{q})$, as in *Quaternion Norm and Invertibility*. Hence $\tilde q^2 = -1$ is the pair of equations

$$
2q_0\mathbf{q} = 0, \qquad q_0^2 - N(\mathbf{q}) = -1 .
$$

If $q_0\neq 0$ the first equation gives $\mathbf{q} = 0$, and the second gives $q_0^2 = -1$, which has no real solution. Therefore $q_0 = 0$, and the second equation becomes $N(\mathbf{q}) = 1$. Conversely a pure imaginary element with $N = 1$ plainly has square $-N(\mathbf{q}) = -1$.

### Vector-Part Decomposition

The reduction shows that the square of a quaternion separates into a scalar equation and a vector equation, with the vector equation linear in $\mathbf{q}$ and the scalar equation quadratic. The scalar equation is an equation for the scalar part and the central product $N(\mathbf{q})$ of the vector part together; the vector equation constrains the direction of $\mathbf{q}$ relative to $q_0$.

### The Pure Roots

**Corollary.** The solutions of $\xi^2 = -1$ in $\mathbb{H}$ are exactly the unit vectors of the imaginary subspace.

*Proof.* By the theorem the solutions are precisely the elements of $\operatorname{Im}\mathbb{H}$ with $N = 1$.

**Proposition.** The solution set $\Sigma = \{\xi\in\mathbb{H} : \xi^2 = -1\}$ is the set $\operatorname{Im}\mathbb{H}\cap Sp(1)$ of elements of the imaginary subspace with $N = 1$; it has real dimension two in $\mathbb{H}\cong\mathbb{R}^4$, is contained in the level set $\{N = 1\}$, and its topological properties are those of *Quaternion Topology*.

*Proof.* The imaginary subspace is a three-dimensional real vector subspace of $\mathbb{H}$ and the solutions are its elements with $N = 1$, so $\Sigma$ has real dimension two; that the level set $\{N = 1\}$ of a three-dimensional real space has dimension two is the standard identification quoted from *Quaternion Norm and Invertibility*.

Thus the quaternion algebra has a two-dimensional family of square roots of $-1$, where the complex numbers have two, $\pm i$. The excess is not an accident of notation: it is the same excess that makes the quaternion algebra non-commutative, and it is the reason the exponential and the polar form are many-to-one on the real points of $Sp(1)$.

## The Classification

### Statement of the Theorem

**Theorem.** The root set $\Sigma = \{\xi : \xi^2 = -1\}$ is a single conjugacy class of the unit group $\mathbb{H}^{\times}$ under the adjoint action, and the map $\tilde q\mapsto \tilde q e_1\tilde q^{-1}$ is a surjection $Sp(1)\to\Sigma$ with fibres the cosets of the stabiliser $U(1)$ of $e_1$.

*Proof.* The adjoint action $\operatorname{Ad}_{\tilde q}(\tilde p) = \tilde q\tilde p\tilde q^{-1}$ of a unit quaternion preserves the imaginary subspace and the quaternion norm, hence carries $\Sigma$ to itself, and it is transitive on $\Sigma$: the transitivity of the adjoint action on the imaginary subspace is in *Quaternion Rotations and Reflections*. Hence $\Sigma$ is one orbit, that is, one conjugacy class. The stabiliser of $e_1$ is the set of units with $\tilde q e_1\tilde q^{-1} = e_1$, namely the units commuting with $e_1$; the commutant of $e_1$ in $\mathbb{H}$ is the two-dimensional plane $\mathbb{R}\oplus\mathbb{R}e_1$, whose unit circle is $U(1) = \{e^{e_1\theta}\}$. The orbit is therefore $Sp(1)/U(1)$ as a set with a transitive action, and the fibres of the orbit map are the cosets of $U(1)$.

### The Homogeneous Space

**Theorem.** There is a canonical bijection of homogeneous spaces

$$
\Sigma \cong Sp(1)/U(1) \cong SO(3)/SO(2),
$$

and under these identifications $\Sigma$ has real dimension two.

*Proof.* The orbit–stabiliser theorem gives $\Sigma\cong Sp(1)/U(1)$ as a homogeneous space of $Sp(1)$, and the identification $Sp(1)/\{\pm1\}\cong SO(3)$ of *Quaternion Rotations and Reflections* identifies it with $SO(3)/SO(2)$ because $U(1)$ contains $\{\pm1\}$. That $SO(3)/SO(2)$ has real dimension two, and with it the identification of $\Sigma$ with $SO(3)/SO(2)$, is the classical statement quoted from *Quaternion Topology*.

### Verification

The statement can be checked in coordinates. A root is $\xi = u_1e_1+u_2e_2+u_3e_3$ with $u_1^2+u_2^2+u_3^2 = 1$, and conjugating $e_1$ by the unit quaternion $\tilde q = q_0+q_1e_1+q_2e_2+q_3e_3$ produces the root $\tilde q e_1\tilde q^{-1}$, whose coordinates are the entries of the matrix of the adjoint action applied to $e_1$; as $\tilde q$ ranges over $Sp(1)$ these conjugate roots fill the whole of $\Sigma$, by the transitivity quoted above. So the two descriptions of $\Sigma$ agree.

### Status of the Roots

Each root $\xi\in\Sigma$ is a unit quaternion, hence invertible, with $\xi^{-1} = \bar\xi = -\xi$. It generates a subalgebra $\mathbb{R}\oplus\mathbb{R}\xi\cong\mathbb{C}$ inside $\mathbb{H}$, and the square of $\xi$ is the scalar $-1$; this is the sense in which each root gives a copy of the complex numbers inside the quaternions. Distinct roots $\xi\neq\eta$ generate distinct, but conjugate, copies: there is a unit quaternion carrying one onto the other, although no quaternion commutes with two distinct roots except a real number.

## The Relation to the Complex Structures on $\mathbb{R}^4$

**Definition.** A **complex structure** on the real vector space $\mathbb{H}$ is a real-linear map $J : \mathbb{H}\to\mathbb{H}$ with $J^2 = -\mathrm{id}$. A complex structure $J$ is **compatible with the quaternion structure** if it is left multiplication by a root, $J = L_\xi$ with $\xi^2 = -1$, where $L_\xi(\tilde q) = \xi\tilde q$.

**Theorem.** For every $\xi\in\Sigma$ the operator $L_\xi$ of left multiplication by $\xi$ is a complex structure on $\mathbb{H}$, and the assignment $\xi\mapsto L_\xi$ is a bijection from $\Sigma$ onto the set of complex structures on $\mathbb{H}$ compatible with the quaternion structure.

*Proof.* Left multiplication is real-linear, and $L_\xi^2 = L_{\xi^2} = L_{-1} = -\mathrm{id}$ because $\xi^2 = -1$. Conversely, if $L_\xi = L_\eta$ then $\xi = L_\xi(1) = L_\eta(1) = \eta$, so the map is injective.

**Proposition.** The three elements $e_1,e_2,e_3$ give three complex structures $I_1,I_2,I_3$ satisfying the quaternion relations

$$
I_1^2 = I_2^2 = I_3^2 = -1, \qquad I_1I_2 = I_3, \quad I_2I_3 = I_1, \quad I_3I_1 = I_2 ,
$$

and the whole two-dimensional set $\Sigma$ of roots is the family of complex structures spanned by them.

*Proof.* The relations are the images of the algebra relations $e_k^2 = -e_0$ and $e_1e_2 = e_3$ under the injective algebra map $L$. A general root is $\xi = u_1e_1+u_2e_2+u_3e_3$ with $u_1^2+u_2^2+u_3^2 = 1$, and $L_\xi = u_1I_1+u_2I_2+u_3I_3$.

The family $\{I_1,I_2,I_3\}$ is a **quaternionic structure** on $\mathbb{H}$: a triple of anticommuting complex structures, whose span is the two-dimensional set $\Sigma$, and whose existence is the same statement as the non-commutativity of the algebra. The complex line spanned by $1$ and $\xi$ is a complex structure in the algebraic sense — a subalgebra isomorphic to $\mathbb{C}$ — while $L_\xi$ is a complex structure in the linear sense.

## The Roots of Plus One

**Theorem.** The solutions of $\eta^2 = 1$ in $\mathbb{H}$ are exactly $\eta = \pm 1$.

*Proof.* The identity $\eta^2-1 = (\eta-1)(\eta+1)$ holds by distributivity, and $\mathbb{H}$ has no zero divisors, so $\eta^2 = 1$ implies $\eta-1 = 0$ or $\eta+1 = 0$. The two values both satisfy the equation.

**Corollary.** The set of roots of $+1$ has two elements, and it is the centre of the group $\{N = 1\}$: $\{\pm1\} = Z(Sp(1))$.

*Proof.* The centre of $Sp(1)$ consists of the units commuting with every quaternion, which are the elements of the centre $\mathbb{R}$ with $N = 1$, namely $\pm1$.

**Remark.** The contrast between the two equations is complete. The root set of $+1$ is discrete and realizes the centre; the root set of $-1$ has real dimension two and realizes a single conjugacy class, the class of $e_1$, and it is as far from central as a conjugacy class can be: only the trivial class is smaller in the quotient. The equation $\eta^2 = 1$ has as many solutions as an algebra with no zero divisors permits — exactly the two central ones — and it has no solution outside $\mathbb{R}$.

## Comparison with the Biquaternion and Split-Quaternion Cases

The root set of $-1$ grows as soon as the coefficient field is enlarged, and the enlargement is the measure of how far the algebra has moved from the division case.

**Proposition.** In the split quaternion algebra $\mathbb{H}_{\mathrm{s}}$, with basis $1,e_1,e_2,e_3$, $e_1^2 = -1$, $e_2^2 = +1$, $e_3 = e_1e_2$, the solutions of $\xi^2 = -1$ are the points of the level set $N = 1$

$$
q_1^2 - q_2^2 - q_3^2 = 1, \qquad \xi = q_1e_1+q_2e_2+q_3e_3 ,
$$

a set of dimension two rather than a surface of higher dimension.

The derivation is in *Split-Quaternion Roots of Minus One*, where the split quaternion algebra is treated; only the comparison is recorded here.

| Algebra | Roots of $-1$ | Roots of $+1$ |
|---|---|---|
| $\mathbb{H}$ | the pure elements with $N = 1$ | $\{\pm1\}$ |
| $\mathbb{H}_{\mathrm{s}}$ | the level set $q_1^2-q_2^2-q_3^2 = 1$ (in $q_0 = 0$) | the level set $q_2^2+q_3^2-q_1^2 = 1$ (in $q_0 = 0$), together with $\pm1$ |
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | a two-dimensional family together with further complex sheets | the roots $\xi i$ obtained from those of $-1$, including $\pm\mu i$ for a pure unit $\mu$ |

The biquaternion root set is computed in *Biquaternion Square Roots of Minus One, Zero and Plus One*; it contains the pure roots but also roots with complex coordinates, from which the non-trivial idempotents $\tfrac{1}{2}(1+\xi i)$ are built. The presence of those extra roots is the failure of division: in a division algebra the factorisation argument of the roots-of-$+1$ theorem is available and the root set is small, while in $\mathbb{H}_{\mathrm{s}}$ and in $\mathbb{B}$ the same factorisation fails.

## Summary

A quaternion satisfies $\xi^2 = -1$ exactly when it is a pure imaginary quaternion with $N = 1$, so the root set is $\Sigma = \operatorname{Im}\mathbb{H}\cap Sp(1)$, the level set $\{N = 1\}$, a two-dimensional family in place of the two roots $\pm i$ of the complex case. The square of a general quaternion splits into the scalar equation $q_0^2-N(\mathbf{q}) = -1$ and the vector equation $2q_0\mathbf{q} = 0$, and the pair forces $q_0 = 0$ and $N(\mathbf{q}) = 1$.

The root set is a single conjugacy class of the unit group under the adjoint action, and the orbit–stabiliser theorem identifies it with the homogeneous space $Sp(1)/U(1)\cong SO(3)/SO(2)$, the stabiliser of $e_1$ being the circle of units commuting with $e_1$. Each root gives a complex structure $L_\xi$ on the underlying real space $\mathbb{H}\cong\mathbb{R}^4$, and the three roots $e_1,e_2,e_3$ give the anticommuting triple $I_1,I_2,I_3$ of a quaternionic structure whose span is the whole two-dimensional set of roots.

The companion equation $\eta^2 = 1$ has only the two solutions $\pm1$, because the factorisation $(\eta-1)(\eta+1) = 0$ together with the absence of zero divisors forces $\eta$ to be central; the root set of $+1$ is the centre of $Sp(1)$. In the split quaternion algebra the roots of $-1$ fill a set with two components rather than one, and in the biquaternion algebra they include further complex sheets, from which the non-trivial idempotents are built; in both cases the extra roots are bought with the loss of the division property.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | The quaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ | General quaternion, scalar part $q_0$, vector part $\mathbf{q}$ |
| $\tilde{q}^{\natural} = q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3$ | Quaternion conjugate |
| $N$ | Quaternion norm, from *Quaternion Norm and Invertibility* |
| $\operatorname{Im}\mathbb{H}$ | Pure imaginary quaternions, $\cong\mathbb{R}^3$ |
| $\Sigma = \{\xi : \xi^2 = -1\} = \operatorname{Im}\mathbb{H}\cap Sp(1)$ | Root set, the level set $\{N = 1\}$ in $\operatorname{Im}\mathbb{H}$ |
| $Sp(1) = \{N = 1\}$ | The group $\{N = 1\}$ of units, from *Quaternion Norm and Invertibility* |
| $U(1) = \{e^{e_1\theta}\}$ | Stabiliser of $e_1$, the commutant unit circle |
| $\Sigma\cong Sp(1)/U(1)\cong SO(3)/SO(2)$ | Root set as a homogeneous space |
| $L_\xi(\tilde q) = \xi\tilde q$ | Complex structure of left multiplication by a root |
| $I_1,I_2,I_3$ | Complex structures $L_{e_1},L_{e_2},L_{e_3}$, a quaternionic structure |
| $\mathbb{H}_{\mathrm{s}}$ | Split quaternion algebra, for contrast |
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra, for contrast |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the origin of the imaginary units and the sphere of square roots of $-1$.
- Edmund Hlawka, "Zur Theorie der Quaternionen", *Archiv der Mathematik* **2** (1949/50) 194–199, for the geometry of the quaternion sphere and its isometries.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the roots of $-1$, the unit groups and the comparison with the other normed division algebras.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the complex structures and the quaternionic structure on $\mathbb{R}^4$.
- Simon Salamon, *Riemannian Geometry and Holonomy Groups* (Longman, 1989), for the relation between the sphere of complex structures and the quaternionic structure of a manifold.
- Garret Sobczyk, "The hyperbolic number plane", *The College Mathematics Journal* **26** (1995) 268–280, for the two-dimensional hyperbolic analogue whose unit circle is a hyperbola, against which the split and hyperbolic root sets are read.
