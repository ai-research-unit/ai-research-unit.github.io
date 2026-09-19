
# __Bilinear and Quadratic Forms: Categorization__

## Introduction

This article gives a classification of bilinear and quadratic forms, organized by the **commutative ring of scalars**. For each commutative ring, we state the classification of the simplest and most important forms.

The general theory is in the preceding article, *Bilinear and Quadratic Forms*. We assume familiarity with the definitions given there.

We consider four commutative rings, in order of increasing complexity:

- The rational numbers $\mathbb{Q}$, a field.
- The real numbers $\mathbb{R}$, a field.
- The complex numbers $\mathbb{C}$, a field.
- The split complex numbers $\mathbb{D}$, a commutative ring with zero divisors.

For each commutative ring, we classify the standard bilinear forms and the associated quadratic forms. We describe each class in elementary terms: whether it is definite or indefinite, whether it is degenerate or non-degenerate, and whether it has isotropic vectors.

A note on terminology. The first three rings are fields, so the classical theory of bilinear and quadratic forms over a field applies verbatim. The fourth ring $\mathbb{D}$ is not a field: it is a commutative ring with zero divisors. The theory of forms over $\mathbb{D}$ is similar to the theory over a field, with the caveat that the forms may take values in a ring with zero divisors, and that non-degeneracy is more delicate. We indicate where this difference matters.

Throughout this article, we use **rank** rather than **dimension** when speaking of forms over a general commutative ring, reserving **dimension** for the field case. When the ring is a field, the two notions coincide.

---

# Part I: Forms over $\mathbb{Q}$

## 1. The Standard Form over $\mathbb{Q}$

On $\mathbb{Q}^n$, the **standard bilinear form** is

$$
B(u, v) = u_1 v_1 + u_2 v_2 + \cdots + u_n v_n.
$$

The associated quadratic form is

$$
Q(v) = v_1^2 + v_2^2 + \cdots + v_n^2.
$$

Over $\mathbb{Q}$, this form is **positive definite** with respect to the usual order on $\mathbb{Q}$. It is non-degenerate. It is **anisotropic** for $n \leq 3$: the equation $x_1^2 + \cdots + x_n^2 = 0$ has no nonzero rational solution.

## 2. The Form $x^2 + y^2$ over $\mathbb{Q}$

On $\mathbb{Q}^2$, the form

$$
Q(x, y) = x^2 + y^2
$$

is positive definite and anisotropic. The equation $x^2 + y^2 = 0$ has no nonzero rational solution.

## 3. The Form $x^2 - 2y^2$ over $\mathbb{Q}$

On $\mathbb{Q}^2$, the form

$$
Q(x, y) = x^2 - 2y^2
$$

is indefinite over $\mathbb{R}$. Over $\mathbb{Q}$, it is anisotropic: the equation $x^2 = 2y^2$ has no nonzero rational solution, because $\sqrt{2}$ is irrational.

## 4. The Form $x^2 + 2y^2$ over $\mathbb{Q}$

On $\mathbb{Q}^2$, the form

$$
Q(x, y) = x^2 + 2y^2
$$

is positive definite over $\mathbb{R}$. Over $\mathbb{Q}$, it is anisotropic. It is not isomorphic over $\mathbb{Q}$ to the standard form $x^2 + y^2$, even though the two forms have the same definiteness over $\mathbb{R}$. This shows that definiteness is not the only invariant over $\mathbb{Q}$.

## 5. The Sum of Four Squares over $\mathbb{Q}$

On $\mathbb{Q}^4$, the form

$$
Q(x_1, x_2, x_3, x_4) = x_1^2 + x_2^2 + x_3^2 + x_4^2
$$

is positive definite. By **Lagrange's four-square theorem**, every non-negative rational number is a sum of four rational squares. So this form represents every non-negative rational number. In particular, the equation $Q(v) = 0$ has only the trivial solution, so the form is anisotropic.

---

# Part II: Forms over $\mathbb{R}$

## 6. The Euclidean Form over $\mathbb{R}$

On $\mathbb{R}^n$, the **Euclidean bilinear form** is the dot product:

$$
B(u, v) = u \cdot v = u_1 v_1 + u_2 v_2 + \cdots + u_n v_n.
$$

The associated quadratic form is

$$
Q(v) = v_1^2 + v_2^2 + \cdots + v_n^2.
$$

This is the **Euclidean length squared**. The form is positive definite, non-degenerate, and anisotropic. It has no isotropic vectors.

## 7. The Minkowski Form over $\mathbb{R}$

On $\mathbb{R}^4$, the **Minkowski bilinear form** is

$$
B(u, v) = u_0 v_0 - u_1 v_1 - u_2 v_2 - u_3 v_3.
$$

The associated quadratic form is

$$
Q(v) = v_0^2 - v_1^2 - v_2^2 - v_3^2.
$$

This is the **Minkowski interval**. The form is indefinite and non-degenerate. It has isotropic vectors: the **null vectors** of relativity, such as $v = (1, 1, 0, 0)$, satisfy $Q(v) = 1 - 1 = 0$.

## 8. The Split Form over $\mathbb{R}$

On $\mathbb{R}^2$, the **split bilinear form** is

$$
B(u, v) = u_1 v_1 - u_2 v_2.
$$

The associated quadratic form is

$$
Q(v) = v_1^2 - v_2^2.
$$

The form is indefinite and non-degenerate. It has isotropic vectors: $v = (1, 1)$ satisfies $Q(v) = 1 - 1 = 0$. The isotropic vectors form the two **isotropic lines** $v_1 = v_2$ and $v_1 = -v_2$.

## 9. The Hyperbola over $\mathbb{R}$

The set of vectors $v$ with $Q(v) = 1$ for the split form is

$$
v_1^2 - v_2^2 = 1.
$$

This is a **hyperbola** in the plane. It has two connected components: the branch with $v_1 > 0$ and the branch with $v_1 < 0$. The equation $Q(v) = -1$ gives the conjugate hyperbola, with two more components.

This hyperbola is the geometric picture of the split form. The hyperbolic transformations of $\mathbb{R}^2$ (the analogue of rotations for the split form) move points along these hyperbolas.

## 10. The Indefinite Form over $\mathbb{R}$

On $\mathbb{R}^{p+q}$, the **indefinite form** is

$$
Q(v) = v_1^2 + \cdots + v_p^2 - v_{p+1}^2 - \cdots - v_{p+q}^2.
$$

The form is non-degenerate. It is:

- Positive definite if $q = 0$.
- Negative definite if $p = 0$.
- Indefinite if $p > 0$ and $q > 0$.

If $p > 0$ and $q > 0$, the form has isotropic vectors.

## 11. The Frobenius Form over $\mathbb{R}$

On the space $M_n(\mathbb{R})$ of $n \times n$ real matrices, the **Frobenius bilinear form** is

$$
B(A, C) = \operatorname{tr}(A^T C).
$$

The associated quadratic form is

$$
Q(A) = \operatorname{tr}(A^T A) = \sum_{i,j} A_{ij}^2.
$$

This is the **Frobenius norm squared** of the matrix $A$. The form is positive definite and anisotropic.

## 12. The Determinant Form over $\mathbb{R}$

On the space $M_2(\mathbb{R})$ of $2 \times 2$ real matrices, the **determinant** is a quadratic form:

$$
Q(A) = \det(A) = A_{11} A_{22} - A_{12} A_{21}.
$$

The associated bilinear form is

$$
B(A, C) = \tfrac{1}{2} \bigl(\det(A + C) - \det(A) - \det(C)\bigr).
$$

The form is indefinite and non-degenerate. It has isotropic vectors: the singular matrices satisfy $\det(A) = 0$.

---

# Part III: Forms over $\mathbb{C}$

## 13. The Standard Form over $\mathbb{C}$

On $\mathbb{C}^n$, the **standard bilinear form** is

$$
B(u, v) = u_1 v_1 + u_2 v_2 + \cdots + u_n v_n.
$$

The associated quadratic form is

$$
Q(v) = v_1^2 + v_2^2 + \cdots + v_n^2.
$$

Over $\mathbb{C}$, this form takes complex values. The notions of definiteness do not apply, because there is no total order on $\mathbb{C}$.

## 14. All Non-Degenerate Forms Are Isomorphic over $\mathbb{C}$

The key fact over $\mathbb{C}$ is that every non-degenerate quadratic form of dimension $n$ is isomorphic to the standard form $z_1^2 + \cdots + z_n^2$.

The reason is that over $\mathbb{C}$, we can rescale a basis vector by a complex scalar to change the sign of its coefficient. If a coefficient is $\lambda \neq 0$, we can write $\lambda = \mu^2$ for some $\mu \in \mathbb{C}^\times$, and then rescale the basis vector by $1/\mu$ to make the coefficient $1$.

So over $\mathbb{C}$, there is only one isomorphism class of non-degenerate quadratic forms in each dimension.

## 15. The Complex Indefinite Form over $\mathbb{C}$

On $\mathbb{C}^{p+q}$, the form

$$
Q(v) = v_1^2 + \cdots + v_p^2 - v_{p+1}^2 - \cdots - v_{p+q}^2
$$

is isomorphic to the standard form $z_1^2 + \cdots + z_n^2$. The reason is that over $\mathbb{C}$, we can rescale the basis vectors $v_{p+1}, \ldots, v_{p+q}$ by $i$ to change the signs of the negative coefficients.

So over $\mathbb{C}$, the distinction between positive and negative coefficients is not an invariant. There is only the dimension $n$.

## 16. The Complex Determinant Form over $\mathbb{C}$

On the space $M_2(\mathbb{C})$ of $2 \times 2$ complex matrices, the determinant is a quadratic form over $\mathbb{C}$. It is isomorphic to the standard form $z_1^2 + z_2^2 + z_3^2 + z_4^2$.

## 17. Isotropic Vectors over $\mathbb{C}$

Every non-degenerate quadratic form of dimension at least 2 over $\mathbb{C}$ has isotropic vectors. For example, the standard form $Q(z_1, z_2) = z_1^2 + z_2^2$ has $Q(1, i) = 1 + i^2 = 1 - 1 = 0$.

So over $\mathbb{C}$, isotropic vectors always exist in dimension at least 2.

---

# Part IV: Forms over $\mathbb{D}$

The split complex numbers $\mathbb{D}$ are not a field in the strict sense: they form a commutative ring with zero divisors. But the theory of bilinear and quadratic forms over $\mathbb{D}$ is similar to the theory over a field, with the caveat that the forms may take values in a ring with zero divisors.

## 18. The Standard Form over $\mathbb{D}$

On $\mathbb{D}^n$, the **standard bilinear form** is

$$
B(u, v) = u_1 v_1 + u_2 v_2 + \cdots + u_n v_n.
$$

The associated quadratic form is

$$
Q(v) = v_1^2 + v_2^2 + \cdots + v_n^2.
$$

Over $\mathbb{D}$, this form takes values in $\mathbb{D}$, which has zero divisors.

## 19. The Split Form over $\mathbb{D}$

On $\mathbb{D}$ itself, viewed as a two-dimensional algebra over $\mathbb{R}$, the **split form** is

$$
Q(a + be) = a^2 - b^2.
$$

This is the form that defines the split complex numbers as a **quadratic algebra**. The isotropic vectors are the elements with $a^2 = b^2$, i.e., $a = \pm b$. These are the **isotropic lines** $1 + e$ and $1 - e$, which are the zero divisors of $\mathbb{D}$.

## 20. The Hyperbola over $\mathbb{D}$

The set of elements of $\mathbb{D}$ with $Q(z) = 1$ is

$$
a^2 - b^2 = 1.
$$

This is a **hyperbola** in the $(a, b)$-plane. It has two connected components: the branch with $a > 0$ and the branch with $a < 0$. The group of units of $\mathbb{D}$ with norm $1$ is exactly this hyperbola.

## 21. The Split Quaternions and Forms over $\mathbb{D}$

The split quaternions $\mathbb{H} \otimes \mathbb{D}$ are a four-dimensional algebra over $\mathbb{D}$ and an eight-dimensional algebra over $\mathbb{R}$. The norm form

$$
N(q) = q \bar{q}
$$

takes values in $\mathbb{D}$. Over $\mathbb{D}$, the structure is more subtle because $\mathbb{D}$ has zero divisors.

---

# Summary

Let me summarize the classification in a table.

| Form | Ring | Rank | Definite | Degenerate | Isotropic vectors |
|---|---|---|---|---|---|
| standard form | $\mathbb{Q}$ | $n$ | yes | no | no for $n \leq 3$ |
| $x^2 + 2y^2$ | $\mathbb{Q}$ | 2 | yes | no | no |
| $x^2 - 2y^2$ | $\mathbb{Q}$ | 2 | no | no | no |
| four-square form | $\mathbb{Q}$ | 4 | yes | no | no |
| Euclidean form | $\mathbb{R}$ | $n$ | yes | no | no |
| Minkowski form | $\mathbb{R}$ | 4 | no | no | yes |
| split form | $\mathbb{R}$ | 2 | no | no | yes |
| indefinite form | $\mathbb{R}$ | $p + q$ | no | no | yes if $p, q > 0$ |
| Frobenius form | $\mathbb{R}$ | $n^2$ | yes | no | no |
| determinant form | $\mathbb{R}$ | 4 | no | no | yes |
| standard form | $\mathbb{C}$ | $n$ | — | no | yes if $n \geq 2$ |
| complex determinant | $\mathbb{C}$ | 4 | — | no | yes |
| standard form | $\mathbb{D}$ | $n$ | — | no | no |
| split form | $\mathbb{D}$ | 2 | no | no | yes |

The pattern is clear: the ring of scalars determines the classification of quadratic forms. Over $\mathbb{R}$, the forms are classified by their definiteness and their isotropic vectors. Over $\mathbb{C}$, there is only one non-degenerate form per dimension, and every form of dimension at least 2 has isotropic vectors. Over $\mathbb{Q}$, the situation is more subtle, and arithmetic invariants are needed. Over $\mathbb{D}$, the situation is analogous to $\mathbb{R}$ but with zero divisors.

**Key differences from the field case.**

- Over a field, every module is free, so every form has a matrix with respect to a basis. Over a general commutative ring, not every module is free.
- Over a field, non-degeneracy is equivalent to the radical being zero. Over a general commutative ring, non-degeneracy requires the induced map $M \to M^*$ to be an isomorphism.
- Over a field of characteristic not equal to 2, 2 is automatically invertible. Over a general commutative ring, we must assume that 2 is a unit.
- Over a field, invertibility of a matrix is equivalent to nonzero determinant. Over a general commutative ring, invertibility requires the determinant to be a unit.
- The classification of quadratic forms over a general commutative ring is much more subtle than over a field. In particular, the classification over $\mathbb{Q}$ requires arithmetic invariants (Hasse–Minkowski, Hilbert symbol), and the classification over $\mathbb{D}$ requires care because $\mathbb{D}$ has zero divisors.

---

## Further Reading

- Michael Artin, *Algebra* (Prentice Hall, 1991).
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002).
- I. N. Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975).
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003).
- Nathan Jacobson, *Basic Algebra I* (Dover, 2nd ed. 2009).
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Springer, 1991).
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (AMS, 2005).
- I. M. Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968).
- F. Catoni, R. Cannata, V. Catoni, E. Nichelatti, P. Zampetti, *The Mathematics of Minkowski Space-Time* (Birkhäuser, 2008).

