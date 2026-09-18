
# __Orthogonal Transformations categorization__

## Introduction

This article gives the low-rank examples of orthogonal transformations, organized by commutative ring and, where applicable, by signature.

The general theory is in the preceding article, *Orthogonal Transformations*. We assume familiarity with the definitions given there.

We treat the fields $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$, and the commutative ring $\mathbb{D}$. The part on $\mathbb{R}$ contains the signature and the classification by signature, because the signature is specific to the real numbers. The part on $\mathbb{C}$ is developed in some detail, because the complex case is where the classical number systems appear most clearly.

A word on terminology. The first three rings are fields, so the classical theory of orthogonal transformations over a field applies verbatim. The fourth ring $\mathbb{D}$ is not a field: it is a commutative ring with zero divisors. The theory of orthogonal transformations over $\mathbb{D}$ is similar to the theory over a field, with the caveat that not every nonzero element is a unit, and that the determinant condition "invertible if and only if determinant is nonzero" becomes "invertible if and only if determinant is a unit of $\mathbb{D}$". We indicate where this difference matters.

Throughout this article, we use **rank** rather than **dimension** when speaking of orthogonal transformations over a general commutative ring, reserving **dimension** for the field case. When the ring is a field, the two notions coincide.

---

# Part I: The Field $\mathbb{Q}$

## 1. Rank 1

The module is $\mathbb{Q}$, with basis vector $e$. The quadratic form is $Q(e) = \lambda$ for some nonzero $\lambda \in \mathbb{Q}$.

The orthogonal group $O(1, \mathbb{Q})$ consists of the linear transformations $z \mapsto az$ with $a \in \mathbb{Q}$ satisfying $a^2 = 1$. The solutions are $a = \pm 1$. So

$$
O(1, \mathbb{Q}) = \{+1, -1\}.
$$

The rotation group $SO(1, \mathbb{Q})$ is the trivial group.

## 2. Rank 2

The module is $\mathbb{Q}^2$, with basis $e_1, e_2$. The quadratic form is determined by $Q(e_1)$, $Q(e_2)$, and $B(e_1, e_2)$.

For example, the form $x^2 + y^2$ has orthogonal group $O(2, \mathbb{Q})$ consisting of the matrices with rational entries that preserve the form. This is a discrete group, because $\mathbb{Q}$ is discrete.

The classification over $\mathbb{Q}$ requires arithmetic invariants, which we do not develop here.

---

# Part II: The Field $\mathbb{R}$

## 3. The Signature

The **signature** of a real quadratic form $Q$ is the pair $(p, q)$ of positive and negative squares in a diagonal basis, as defined in the article *Bilinear and Quadratic Forms*. The rank of the module is $p + q$ for a non-degenerate form.

The signature determines the structure of the orthogonal group:

- **Positive definite** signature $(n, 0)$: the orthogonal group is compact, and $SO(n)$ is connected.
- **Indefinite** signature $(p, q)$ with $p, q > 0$: the orthogonal group is non-compact, and $SO(p, q)$ may have more than one connected component.

This is the reason the examples over $\mathbb{R}$ are organized by signature.

## 4. Rank 1

The module is $\mathbb{R}$, with $Q(x) = x^2$. The signature is $(1, 0)$.

The orthogonal group $O(1)$ has two elements: the identity and the reflection $x \mapsto -x$. The rotation group $SO(1)$ is the trivial group.

## 5. Rank 2, Positive Definite

The module is $\mathbb{R}^2$, with $Q(x, y) = x^2 + y^2$. The signature is $(2, 0)$.

The rotation group $SO(2)$ consists of the rotations by arbitrary angles:

$$
R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}.
$$

This is the matrix of multiplication by the complex number $e^{i\theta}$:

$$
(x + iy) \mapsto e^{i\theta}(x + iy).
$$

So the rotation group $SO(2)$ is isomorphic to the circle group $S^1$:

$$
SO(2) \cong U(1) \cong S^1.
$$

## 6. Rank 2, Indefinite

The module is $\mathbb{R}^2$, with $Q(x, y) = x^2 - y^2$. The signature is $(1, 1)$.

The rotation group $SO(1, 1)$ consists of the hyperbolic transformations

$$
H_t = \begin{pmatrix} \cosh t & \sinh t \\ \sinh t & \cosh t \end{pmatrix}, \qquad t \in \mathbb{R}.
$$

The group $SO(1, 1)$ has two connected components. The identity component is isomorphic to the group of split complex numbers of norm $1$ with positive real part, which is a hyperbola.

## 7. Rank 3, Positive Definite

The module is $\mathbb{R}^3$, with $Q(x, y, z) = x^2 + y^2 + z^2$. The signature is $(3, 0)$.

The rotation group $SO(3)$ consists of the rotations about arbitrary axes. It is three-dimensional, and it is isomorphic to the group of unit quaternions modulo $\pm 1$:

$$
SO(3) \cong SU(2) / \{\pm 1\}.
$$

## 8. Rank 3, Indefinite

The module is $\mathbb{R}^3$, with $Q(x, y, z) = x^2 + y^2 - z^2$. The signature is $(2, 1)$.

The rotation group $SO(2, 1)$ is three-dimensional. It is not compact, and it has two connected components. It is isomorphic to a quotient of the group of unit split quaternions.

## 9. Rank 4

The two cases are:

**$Q(x_1, x_2, x_3, x_4) = x_1^2 + x_2^2 + x_3^2 + x_4^2$.** Signature $(4, 0)$. The rotation group is

$$
SO(4) \cong (SU(2) \times SU(2)) / \{\pm 1\}.
$$

**$Q(x_1, x_2, x_3, x_4) = x_1^2 + x_2^2 - x_3^2 - x_4^2$.** Signature $(2, 2)$. The rotation group is

$$
SO(2, 2) \cong (SL(2, \mathbb{R}) \times SL(2, \mathbb{R})) / \{\pm 1\}.
$$

## 10. Summary for the Field $\mathbb{R}$

| Module | Quadratic form | Signature | Rotation group |
|---|---|---|---|
| $\mathbb{R}$ | $x^2$ | $(1, 0)$ | trivial |
| $\mathbb{R}^2$ | $x^2 + y^2$ | $(2, 0)$ | $SO(2) = S^1$ |
| $\mathbb{R}^2$ | $x^2 - y^2$ | $(1, 1)$ | $SO(1, 1)$, $2$ components |
| $\mathbb{R}^3$ | $x^2 + y^2 + z^2$ | $(3, 0)$ | $SO(3) = SU(2)/\{\pm 1\}$ |
| $\mathbb{R}^3$ | $x^2 + y^2 - z^2$ | $(2, 1)$ | $SO(2, 1)$, $2$ components |
| $\mathbb{R}^4$ | $x_1^2 + x_2^2 + x_3^2 + x_4^2$ | $(4, 0)$ | $SO(4) = (SU(2) \times SU(2))/\{\pm 1\}$ |
| $\mathbb{R}^4$ | $x_1^2 + x_2^2 - x_3^2 - x_4^2$ | $(2, 2)$ | $SO(2, 2) = (SL(2, \mathbb{R}) \times SL(2, \mathbb{R}))/\{\pm 1\}$ |

---

# Part III: The Field $\mathbb{C}$

## 11. Classification over $\mathbb{C}$

Over $\mathbb{C}$, every non-degenerate quadratic form of rank $n$ is isomorphic to the standard form. There is only one case up to isomorphism. There is no signature.

The reason is that over $\mathbb{C}$, we can rescale a basis vector by a complex scalar to change the sign of its coefficient. If a coefficient is $\lambda \neq 0$, we can write $\lambda = \mu^2$ for some $\mu \in \mathbb{C}^\times$, and then rescale the basis vector by $\mu$ to make the coefficient $1$.

So over $\mathbb{C}$, there is only one isomorphism class of non-degenerate quadratic forms in each rank. The orthogonal group is a complex Lie group, and its structure is different from the real case.

## 12. Rank 1

The module is $\mathbb{C}$, with $Q(z) = z^2$.

The orthogonal group $O(1, \mathbb{C})$ consists of the linear transformations $z \mapsto az$ with $a \in \mathbb{C}$ satisfying $a^2 = 1$. The solutions are $a = \pm 1$. So

$$
O(1, \mathbb{C}) = \{+1, -1\}.
$$

The rotation group $SO(1, \mathbb{C})$ is the trivial group.

## 13. Rank 2

The module is $\mathbb{C}^2$, with basis $e_1, e_2$. The quadratic form is

$$
Q(z_1, z_2) = z_1^2 + z_2^2
$$

after rescaling, so $Q(e_1) = +1$ and $Q(e_2) = +1$, with $B(e_1, e_2) = 0$.

The Clifford algebra associated with this quadratic form is $\mathbb{C}l_2$, which is isomorphic to the biquaternions:

$$
\mathbb{C}l_2 \cong \mathbb{H} \otimes \mathbb{C} \cong M_2(\mathbb{C}).
$$

The orthogonal group $O(2, \mathbb{C})$ consists of the complex linear transformations that preserve the form. The rotation group $SO(2, \mathbb{C})$ is the subgroup with determinant $+1$.

The structure of these groups is more subtle than over $\mathbb{R}$, because $\mathbb{C}$ is algebraically closed. We do not develop the details here.

## 14. Rank 3

The module is $\mathbb{C}^3$, with basis $e_1, e_2, e_3$. The quadratic form is

$$
Q(z_1, z_2, z_3) = z_1^2 + z_2^2 + z_3^2
$$

after rescaling. There is only one case up to isomorphism.

The Clifford algebra associated with this quadratic form is $\mathbb{C}l_3$, which is isomorphic to the direct sum of two copies of the biquaternions:

$$
\mathbb{C}l_3 \cong M_2(\mathbb{C}) \oplus M_2(\mathbb{C}).
$$

The orthogonal group $O(3, \mathbb{C})$ is a complex Lie group. We do not develop the details here.

## 15. Summary for the Field $\mathbb{C}$

| Rank | Quadratic form | Clifford algebra | Rotation group |
|---|---|---|---|
| 0 | — | $\mathbb{C}$ | trivial |
| 1 | $z^2$ | $\mathbb{C} \oplus \mathbb{C}$ | trivial |
| 2 | $z_1^2 + z_2^2$ | $\mathbb{H} \otimes \mathbb{C}$ (biquaternions) | complex orthogonal group |
| 3 | $z_1^2 + z_2^2 + z_3^2$ | $M_2(\mathbb{C}) \oplus M_2(\mathbb{C})$ | complex orthogonal group |

The complex case is where the biquaternions appear naturally: they are the Clifford algebra of the two-dimensional complex quadratic form.

---

# Part IV: The Commutative Ring $\mathbb{D}$

## 16. A Caveat

The split complex numbers $\mathbb{D}$ are not a field in the strict sense: they form a commutative ring with zero divisors. The orthogonal group over $\mathbb{D}$ is defined as the set of $\mathbb{D}$-linear transformations that preserve the quadratic form, with the caveat that the determinant condition "invertible if and only if determinant is nonzero" becomes "invertible if and only if determinant is a unit of $\mathbb{D}$".

## 17. Rank 1

The module is $\mathbb{D}$, with $Q(z) = z^2$.

The orthogonal group $O(1, \mathbb{D})$ consists of the linear transformations $z \mapsto az$ with $a \in \mathbb{D}$ satisfying $a^2 = 1$. The solutions are $a = \pm 1$. So

$$
O(1, \mathbb{D}) = \{+1, -1\}.
$$

The rotation group $SO(1, \mathbb{D})$ is the trivial group.

## 18. Rank 2

The module is $\mathbb{D}^2$, with basis $e_1, e_2$. In an orthogonal basis, the quadratic form is determined by $Q(e_1)$ and $Q(e_2)$.

**$Q(e_1) = +1$, $Q(e_2) = +1$.** The rotation group $SO(2, \mathbb{D})$ consists of the transformations of the form

$$
\begin{pmatrix} \cosh t & \sinh t \\ \sinh t & \cosh t \end{pmatrix}
$$

with $t \in \mathbb{D}$. These are the hyperbolic transformations over $\mathbb{D}$.

**$Q(e_1) = +1$, $Q(e_2) = -1$.** The rotation group is analogous, with the roles of the two generators exchanged.

**$Q(e_1) = -1$, $Q(e_2) = -1$.** The rotation group is again the group of hyperbolic transformations.

The details depend on the zero divisors of $\mathbb{D}$, which make the group structure more subtle than over $\mathbb{R}$.

---

# Part V: Summary

Let me summarize the examples in a table.

| Module | Quadratic form | Ring | Rotation group |
|---|---|---|---|
| $\mathbb{Q}$ | $x^2$ | $\mathbb{Q}$ | trivial |
| $\mathbb{Q}^2$ | $x^2 + y^2$ | $\mathbb{Q}$ | discrete orthogonal group |
| $\mathbb{R}$ | $x^2$ | $\mathbb{R}$ | trivial |
| $\mathbb{R}^2$ | $x^2 + y^2$ | $\mathbb{R}$ | $SO(2) = S^1$ |
| $\mathbb{R}^2$ | $x^2 - y^2$ | $\mathbb{R}$ | $SO(1, 1)$, $2$ components |
| $\mathbb{R}^3$ | $x^2 + y^2 + z^2$ | $\mathbb{R}$ | $SO(3) = SU(2)/\{\pm 1\}$ |
| $\mathbb{R}^3$ | $x^2 + y^2 - z^2$ | $\mathbb{R}$ | $SO(2, 1)$, $2$ components |
| $\mathbb{R}^4$ | $x_1^2 + x_2^2 + x_3^2 + x_4^2$ | $\mathbb{R}$ | $SO(4) = (SU(2) \times SU(2))/\{\pm 1\}$ |
| $\mathbb{R}^4$ | $x_1^2 + x_2^2 - x_3^2 - x_4^2$ | $\mathbb{R}$ | $SO(2, 2) = (SL(2, \mathbb{R}) \times SL(2, \mathbb{R}))/\{\pm 1\}$ |
| $\mathbb{C}$ | $z^2$ | $\mathbb{C}$ | $\{+1, -1\}$ |
| $\mathbb{C}^2$ | $z_1^2 + z_2^2$ | $\mathbb{C}$ | complex orthogonal group |
| $\mathbb{C}^3$ | $z_1^2 + z_2^2 + z_3^2$ | $\mathbb{C}$ | complex orthogonal group |
| $\mathbb{D}$ | $z^2$ | $\mathbb{D}$ | $\{+1, -1\}$ |
| $\mathbb{D}^2$ | $z_1^2 + z_2^2$ | $\mathbb{D}$ | hyperbolic transformations over $\mathbb{D}$ |

The pattern is clear: the ring of scalars and, over $\mathbb{R}$, the signature, determine the structure of the orthogonal group.

**Key differences from the field case.**

- Over a field, every module is free, so the orthogonal group is a matrix group. Over a general commutative ring, the module need not be free.
- Over a field, invertibility is equivalent to nonzero determinant. Over a general commutative ring, invertibility requires the determinant to be a unit.
- Over a field of characteristic not equal to 2, the equation $\det(T)^2 = 1$ has exactly two solutions. Over a general commutative ring, it may have more.
- The classification of orthogonal groups over a general commutative ring is much more subtle than over a field, and requires the theory of quadratic forms over rings.

---

## Further Reading

- Michael Artin, *Algebra* (Prentice Hall, 1991).
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002).
- I. N. Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975).
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003).
- Nathan Jacobson, *Basic Algebra I* (Dover, 2nd ed. 2009).
- Jean Dieudonné, *La géométrie des groupes classiques* (Springer, 1971).
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Springer, 1991).

