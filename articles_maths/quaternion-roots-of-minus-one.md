
# __Quaternion Roots of Minus One__

## Introduction

The equation $\xi^2 = -1$ has, in the quaternion algebra, not two solutions but a whole two-dimensional family: the pure unit quaternions. This article determines that family, describes it as a single conjugacy class and as a homogeneous space of the unit group, relates it to the complex structures that the algebra places on its underlying real vector space, solves the companion equation $\xi^2 = +1$, and compares the answer with the biquaternion and split-quaternion cases. It is the article of the quaternion family that owns the square roots of $-1$; the unit group itself is from *Quaternion Norm and Invertibility*, and the adjoint action that realises the conjugacy class is from *Quaternion Rotations and Reflections*.

The single fact on which everything rests is the absence of zero divisors: since a product in $\mathbb{H}$ vanishes only when a factor vanishes, the equation $(\tilde q-1)(\tilde q+1) = 0$ forces $\tilde q = \pm 1$, and a companion argument forces the roots of $-1$ to be pure. Both the smallness of the root set of $+1$ and the roundness of the root set of $-1$ are consequences of the same property, and both fail as soon as the coefficient field is enlarged.

The corpus's default base is a commutative ring with identity, and the algebra is defined there by its presentation. The results below are stated over $\mathbb{R}$, where the norm form is positive definite and the algebra is a division algebra; the reduction of the equation and the classification of the roots hold over any field of characteristic not $2$ in which the norm form is anisotropic, and the topological descriptions of the root sets are the statements over $\mathbb{R}$.

Throughout, $\mathbb{H}$ is the quaternion algebra with basis $e_0 = 1, e_1, e_2, e_3$ and $e_k^2 = -e_0$, a quaternion is $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ with scalar part $q_0$ and vector part $\mathbf{q}\in\operatorname{Im}\mathbb{H}$, the conjugate is $\bar{\tilde q} = q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3$, the norm form is $N(\tilde q) = \tilde q\bar{\tilde q}$, the unit group is $\mathbb{H}^{\times} = \mathbb{H}\setminus\{0\}$, and the unit sphere is $Sp(1) = \{\tilde q : N(\tilde q) = 1\} = S^3$.

## The Problem and Its Reduction

### Statement

**Theorem.** A quaternion $\tilde q\in\mathbb{H}$ satisfies $\tilde q^2 = -1$ if and only if $\tilde q$ is a pure imaginary quaternion of norm one,

$$
\tilde q\in\operatorname{Im}\mathbb{H}\cap Sp(1) = \{x\in\operatorname{Im}\mathbb{H} : N(x) = 1\}.
$$

*Proof.* Write $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ with $q_0\in\mathbb{R}$ and $\mathbf{q}\in\operatorname{Im}\mathbb{H}$. The square is

$$
\tilde q^2 = q_0^2 - N(\mathbf{q}) + 2q_0\mathbf{q},
$$

because the product of two pure imaginaries is $\mathbf{p}\mathbf{q} = -\langle\mathbf{p},\mathbf{q}\rangle + \mathbf{p}\times\mathbf{q}$, so that $\mathbf{q}^2 = -N(\mathbf{q})$. Hence $\tilde q^2 = -1$ is the pair of equations

$$
2q_0\mathbf{q} = 0, \qquad q_0^2 - N(\mathbf{q}) = -1 .
$$

If $q_0\neq 0$ the first equation gives $\mathbf{q} = 0$, and the second gives $q_0^2 = -1$, which has no real solution. Therefore $q_0 = 0$, and the second equation becomes $N(\mathbf{q}) = 1$. Conversely a pure imaginary of norm one plainly has square $-N(\mathbf{q}) = -1$. $\square$

### Vector-Part Decomposition

The reduction shows that the square of a quaternion separates into a scalar equation and a vector equation, with the vector equation linear in $\mathbf{q}$ and the scalar equation quadratic. The scalar equation is an equation for the scalar part and the modulus of the vector part together; the vector equation constrains the direction of $\mathbf{q}$ relative to $q_0$.

### The Pure Roots

**Corollary.** The solutions of $\xi^2 = -1$ in $\mathbb{H}$ are exactly the unit vectors of the imaginary subspace.

*Proof.* By the theorem the solutions are precisely the elements of $\operatorname{Im}\mathbb{H}$ of norm one. $\square$

**Proposition.** The solution set $\Sigma = \{\xi\in\mathbb{H} : \xi^2 = -1\}$ is the unit sphere $\operatorname{Im}\mathbb{H}\cap Sp(1)$, a two-dimensional sphere $S^2$ embedded in $\mathbb{H}\cong\mathbb{R}^4$ and contained in the unit sphere $S^3$.

*Proof.* The imaginary subspace is a three-dimensional real vector subspace of $\mathbb{H}$, and the solutions are its unit vectors; the unit sphere of a three-dimensional Euclidean space is $S^2$. $\square$

Thus the quaternion algebra has a two-sphere of square roots of $-1$, where the complex numbers have two, $\pm i$. The excess is not an accident of notation: it is the same excess that makes the quaternion algebra non-commutative, and it is the reason the exponential and the polar form are many-to-one on the real points of $Sp(1)$.

## The Classification

### Statement of the Theorem

**Theorem.** The root set $\Sigma = \{\xi : \xi^2 = -1\}$ is a single conjugacy class of the unit group $\mathbb{H}^{\times}$ under the adjoint action, and the map $\tilde q\mapsto \tilde q e_1\tilde q^{-1}$ is a surjection $Sp(1)\to\Sigma$ with fibres the cosets of the stabiliser $U(1)$ of $e_1$.

*Proof.* The adjoint action $\operatorname{Ad}_q(x) = qxq^{-1}$ of a unit quaternion on the imaginary subspace is an orthogonal isometry of $\operatorname{Im}\mathbb{H}$ by *Quaternion Rotations and Reflections*; it preserves the norm form and hence carries $\Sigma$ to itself, and since it acts on $\operatorname{Im}\mathbb{H}\cong\mathbb{R}^3$ as the full rotation group $SO(3)$ it acts transitively on the unit sphere $\Sigma$. Hence $\Sigma$ is one orbit, that is, one conjugacy class. The stabiliser of $e_1$ is the set of units with $qe_1\tilde q^{-1} = e_1$, namely the units commuting with $e_1$; the commutant of $e_1$ in $\mathbb{H}$ is the two-dimensional plane $\mathbb{R}\oplus\mathbb{R}e_1$, whose unit circle is $U(1) = \{e^{e_1\theta}\}$. The orbit is therefore $Sp(1)/U(1)$ as a set with a transitive action, and the fibres of the orbit map are the cosets of $U(1)$. $\square$

### The Homogeneous Space

**Theorem.** There is a canonical bijection of homogeneous spaces

$$
\Sigma \cong Sp(1)/U(1) \cong SO(3)/SO(2),
$$

and $\Sigma$ is diffeomorphic to the two-sphere $S^2$.

*Proof.* The orbit–stabiliser theorem gives $\Sigma\cong Sp(1)/U(1)$ as a homogeneous space of $Sp(1)$, and the identification $Sp(1)/\{\pm1\}\cong SO(3)$ of *Quaternion Rotations and Reflections* identifies it with $SO(3)/SO(2)$ because $U(1)$ contains $\{\pm1\}$. The quotient of the compact group $SO(3)$ by the one-parameter subgroup $SO(2)$ is the two-sphere, the classical transitive action of $SO(3)$ on $S^2$. $\square$

### Verification

The statement can be checked in coordinates. The unit vectors of the imaginary subspace are the triples $u = (u_1,u_2,u_3)$ with $u_1^2+u_2^2+u_3^2 = 1$, and the rotation group acts on triples faithfully; conjugating $e_1$ by a unit quaternion produces the vector $R_q e_1$, where $R_q$ is the matrix of the adjoint action, and as $\tilde q$ ranges over $Sp(1)$ the vector $R_qe_1$ ranges over the whole unit sphere because $SO(3)$ acts transitively on it. So the two descriptions of $\Sigma$ agree.

### Status of the Roots

Each root $\xi\in\Sigma$ is a unit quaternion, hence invertible, with $\xi^{-1} = \bar\xi = -\xi$. It generates a subalgebra $\mathbb{R}\oplus\mathbb{R}\xi\cong\mathbb{C}$ inside $\mathbb{H}$, and the square of $\xi$ is the scalar $-1$; this is the sense in which each root gives a copy of the complex numbers inside the quaternions. Distinct roots $\xi\neq\eta$ generate distinct, but conjugate, copies: there is a unit quaternion carrying one onto the other, although no quaternion commutes with two distinct roots except a real number.

## The Relation to the Complex Structures on $\mathbb{R}^4$

**Definition.** A **complex structure** on the real vector space $\mathbb{H}$ is a real-linear map $J : \mathbb{H}\to\mathbb{H}$ with $J^2 = -\mathrm{id}$. A complex structure $J$ is **compatible with the quaternion structure** if it is left multiplication by a root, $J = L_\xi$ with $\xi^2 = -1$, where $L_\xi(x) = \xi x$.

**Theorem.** For every $\xi\in\Sigma$ the operator $L_\xi$ of left multiplication by $\xi$ is a complex structure on $\mathbb{H}$, and the assignment $\xi\mapsto L_\xi$ is a bijection from $\Sigma$ onto the set of complex structures on $\mathbb{H}$ compatible with the quaternion structure.

*Proof.* Left multiplication is real-linear, and $L_\xi^2 = L_{\xi^2} = L_{-1} = -\mathrm{id}$ because $\xi^2 = -1$. Conversely, if $L_\xi = L_\eta$ then $\xi = L_\xi(1) = L_\eta(1) = \eta$, so the map is injective. $\square$

**Proposition.** The three elements $e_1,e_2,e_3$ give three complex structures $I_1,I_2,I_3$ satisfying the quaternion relations

$$
I_1^2 = I_2^2 = I_3^2 = -1, \qquad I_1I_2 = I_3, \quad I_2I_3 = I_1, \quad I_3I_1 = I_2 ,
$$

and the whole two-sphere $\Sigma$ of roots is the family of complex structures spanned by them.

*Proof.* The relations are the images of the algebra relations $e_k^2 = -e_0$ and $e_1e_2 = e_3$ under the injective algebra map $L$. A general root is $\xi = u_1e_1+u_2e_2+u_3e_3$ with $u_1^2+u_2^2+u_3^2 = 1$, and $L_\xi = u_1I_1+u_2I_2+u_3I_3$. $\square$

The family $\{I_1,I_2,I_3\}$ is a **quaternionic structure** on $\mathbb{H}$: a triple of anticommuting complex structures, whose span is the two-sphere $\Sigma$, and whose existence is the same statement as the non-commutativity of the algebra. The complex line spanned by $1$ and $\xi$ is a complex structure in the algebraic sense — a subalgebra isomorphic to $\mathbb{C}$ — while $L_\xi$ is a complex structure in the linear sense.

## The Roots of Plus One

**Theorem.** The solutions of $\eta^2 = 1$ in $\mathbb{H}$ are exactly $\eta = \pm 1$.

*Proof.* The identity $\eta^2-1 = (\eta-1)(\eta+1)$ holds by distributivity, and $\mathbb{H}$ has no zero divisors, so $\eta^2 = 1$ implies $\eta-1 = 0$ or $\eta+1 = 0$. The two values both satisfy the equation. $\square$

**Corollary.** The set of roots of $+1$ has two elements, and it is the centre of the unit sphere: $\{\pm1\} = Z(Sp(1))$.

*Proof.* The centre of $Sp(1)$ consists of the units commuting with every quaternion, which are the norm-one elements of the centre $\mathbb{R}$, namely $\pm1$. $\square$

**Remark.** The contrast between the two equations is complete. The root set of $+1$ is discrete and realizes the centre; the root set of $-1$ is a two-sphere and realizes a single conjugacy class, the class of $e_1$, and it is as far from central as a conjugacy class can be: only the trivial class is smaller in the quotient. The equation $\eta^2 = 1$ has as many solutions as an algebra with no zero divisors permits — exactly the two central ones — and it has no solution outside $\mathbb{R}$.

## Comparison with the Biquaternion and Split-Quaternion Cases

The root set of $-1$ grows as soon as the coefficient field is enlarged, and the enlargement is the measure of how far the algebra has moved from the division case.

**Proposition.** In the split quaternion algebra $\mathbb{H}_{\mathrm{s}}$, with basis $1,e_1,e_2,e_3$, $e_1^2 = -1$, $e_2^2 = +1$, $e_3 = e_1e_2$, the solutions of $\xi^2 = -1$ are the points of the two-sheeted hyperboloid

$$
x_1^2 - x_2^2 - x_3^2 = 1, \qquad \xi = x_1e_1+x_2e_2+x_3e_3 ,
$$

a two-dimensional surface rather than a sphere.

*Proof.* Writing $\xi = x_0 + x_1e_1+x_2e_2+x_3e_3$ and using $e_1^2 = -1$, $e_2^2 = e_3^2 = +1$ and the vanishing of the anticommutators, one has $v^2 = -x_1^2+x_2^2+x_3^2$ for the vector part $v = x_1e_1+x_2e_2+x_3e_3$, so $\xi^2 = x_0^2 - x_1^2+x_2^2+x_3^2 + 2x_0v$. Setting $\xi^2 = -1$ gives $x_0v = 0$ and $x_0^2-x_1^2+x_2^2+x_3^2 = -1$; if $x_0\neq0$ then $v = 0$ and $x_0^2 = -1$, impossible, so $x_0 = 0$ and $x_1^2-x_2^2-x_3^2 = 1$. $\square$

| Algebra | Roots of $-1$ | Roots of $+1$ |
|---|---|---|
| $\mathbb{H}$ | the sphere $S^2$ of pure units | $\{\pm1\}$ |
| $\mathbb{H}_{\mathrm{s}}$ | the two-sheeted hyperboloid $x_1^2-x_2^2-x_3^2 = 1$ (in $x_0 = 0$) | the one-sheeted hyperboloid $x_2^2+x_3^2-x_1^2 = 1$ (in $x_0 = 0$), together with $\pm1$ |
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | a two-sphere together with further complex sheets | the roots $\xi i$ obtained from those of $-1$, including $\pm\mu i$ for a pure unit $\mu$ |

The biquaternion root set is computed in *Biquaternion Roots of Minus One*; it contains the pure sphere but also roots with complex coordinates, from which the non-trivial idempotents $\tfrac{1}{2}(1+\xi i)$ are built. The presence of those extra roots is the failure of division: in a division algebra the factorisation argument of the roots-of-$+1$ theorem is available and the root set is small, while in $\mathbb{H}_{\mathrm{s}}$ and in $\mathbb{B}$ the same factorisation fails.

## Summary

A quaternion satisfies $\xi^2 = -1$ exactly when it is a pure imaginary quaternion of norm one, so the root set is the unit sphere $\Sigma = \operatorname{Im}\mathbb{H}\cap Sp(1)\cong S^2$, a two-dimensional family in place of the two roots $\pm i$ of the complex case. The square of a general quaternion splits into the scalar equation $q_0^2-N(\mathbf{q}) = -1$ and the vector equation $2q_0\mathbf{q} = 0$, and the pair forces $q_0 = 0$ and $N(\mathbf{q}) = 1$.

The root set is a single conjugacy class of the unit group under the adjoint action, and the orbit–stabiliser theorem identifies it with the homogeneous space $Sp(1)/U(1)\cong SO(3)/SO(2)\cong S^2$, the stabiliser of $e_1$ being the circle of units commuting with $e_1$. Each root gives a complex structure $L_\xi$ on the underlying real space $\mathbb{H}\cong\mathbb{R}^4$, and the three roots $e_1,e_2,e_3$ give the anticommuting triple $I_1,I_2,I_3$ of a quaternionic structure whose span is the whole two-sphere of roots.

The companion equation $\eta^2 = 1$ has only the two solutions $\pm1$, because the factorisation $(\eta-1)(\eta+1) = 0$ together with the absence of zero divisors forces $\eta$ to be central; the root set of $+1$ is the centre of the unit sphere $Sp(1)$. In the split quaternion algebra the roots of $-1$ fill a two-sheeted hyperboloid rather than a sphere, and in the biquaternion algebra they include further complex sheets, from which the non-trivial idempotents are built; in both cases the extra roots are bought with the loss of the division property.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | The quaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ | General quaternion, scalar part $q_0$, vector part $\mathbf{q}$ |
| $\bar{\tilde q} = q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3$ | Quaternion conjugate |
| $N(\tilde q) = \tilde q\bar{\tilde q}$ | Norm form |
| $\operatorname{Im}\mathbb{H}$ | Pure imaginary quaternions, $\cong\mathbb{R}^3$ |
| $\Sigma = \{\xi : \xi^2 = -1\} = \operatorname{Im}\mathbb{H}\cap Sp(1)$ | Root sphere, $\cong S^2$ |
| $Sp(1) = \{\tilde q : N(\tilde q) = 1\} = S^3$ | Unit quaternions |
| $U(1) = \{e^{e_1\theta}\}$ | Stabiliser of $e_1$, the commutant unit circle |
| $\Sigma\cong Sp(1)/U(1)\cong SO(3)/SO(2)$ | Root set as a homogeneous space |
| $L_\xi(x) = \xi x$ | Complex structure of left multiplication by a root |
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
