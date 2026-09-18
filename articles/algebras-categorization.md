
# __Algebras: Categorization__

## Introduction

This article gives a classification of algebras, organized by the **commutative ring of scalars**. For each commutative ring, we state the classification of the simplest and most important algebras over that ring.

The general theory of algebras is in the preceding article, *Algebras: A General Introduction*. We assume familiarity with the definitions given there.

We consider four commutative rings, in order of increasing complexity:

- The rational numbers $\mathbb{Q}$, a field.
- The real numbers $\mathbb{R}$, a field.
- The complex numbers $\mathbb{C}$, a field.
- The split complex numbers $\mathbb{D}$, a commutative ring with zero divisors.

For each commutative ring, we state the rank of the algebra over that ring, the properties it satisfies (associative, commutative, unital, division), and where appropriate the geometric interpretation.

A note on terminology. The first three rings are fields, so the classical theory of algebras over a field applies verbatim. The fourth ring $\mathbb{D}$ is not a field: it is a commutative ring with zero divisors. The theory of algebras over $\mathbb{D}$ is similar to the theory over a field, with the caveat that not every nonzero element is a unit, and that a division algebra over $\mathbb{D}$ is only possible in rank 1 (and even then only if the unique element is a unit). We indicate where this difference matters.

Throughout this article, we use **rank** rather than **dimension** when speaking of algebras over a general commutative ring, reserving **dimension** for the field case. When the ring is a field, the two notions coincide.

---

# Part I: Algebras over $\mathbb{Q}$

## 1. The Rational Numbers $\mathbb{Q}$ over $\mathbb{Q}$

The set of rational numbers is a **one-dimensional algebra over $\mathbb{Q}$**. The product is ordinary multiplication. It is associative, commutative, unital, and every nonzero element has an inverse. It is a field.

## 2. The Field $\mathbb{Q}[\sqrt{2}]$ over $\mathbb{Q}$

The set of numbers of the form $a + b\sqrt{2}$ with $a, b \in \mathbb{Q}$ is a **two-dimensional algebra over $\mathbb{Q}$**, with basis $\{1, \sqrt{2}\}$ and the relation $(\sqrt{2})^2 = 2$. It is associative, commutative, unital, and a division algebra over $\mathbb{Q}$. It is a field extension of $\mathbb{Q}$ of degree 2.

## 3. The Quaternion Algebra over $\mathbb{Q}$

The quaternions with rational coefficients form a **four-dimensional algebra over $\mathbb{Q}$**, with the same relations as $\mathbb{H}$ but with coefficients in $\mathbb{Q}$. It is associative and unital over $\mathbb{Q}$, and a division algebra over $\mathbb{Q}$. It is not commutative.

## 4. The Algebra $M_n(\mathbb{Q})$ over $\mathbb{Q}$

The set of $n \times n$ matrices with rational entries is an **$n^2$-dimensional algebra over $\mathbb{Q}$**. The product is matrix multiplication. It is associative and unital over $\mathbb{Q}$. It is not commutative for $n \geq 2$. It is not a division algebra.

---

# Part II: Algebras over $\mathbb{R}$

## 5. The Real Numbers $\mathbb{R}$ over $\mathbb{R}$

The set of real numbers is a **one-dimensional algebra over $\mathbb{R}$**. The product is ordinary multiplication. It is associative, commutative, unital, and every nonzero element has an inverse. It is a field.

## 6. The Complex Numbers $\mathbb{C}$ over $\mathbb{R}$

The set of complex numbers is a **two-dimensional algebra over $\mathbb{R}$**, with basis $\{1, i\}$ and the relation $i^2 = -1$. A general element is $a + bi$ with $a, b \in \mathbb{R}$, and the product is

$$
(a + bi)(c + di) = (ac - bd) + (ad + bc)i.
$$

It is associative, commutative, unital, and every nonzero element has an inverse. It is a field, and a field extension of $\mathbb{R}$ of degree 2.

## 7. The Quaternions $\mathbb{H}$ over $\mathbb{R}$

The set of quaternions is a **four-dimensional algebra over $\mathbb{R}$**, with basis $\{e_0, e_1, e_2, e_3\}$ and the relations

$$
e_0 = 1, \quad e_1^2 = e_2^2 = e_3^2 = -e_0,
$$

$$
e_1 e_2 = e_3, \quad e_2 e_3 = e_1, \quad e_3 e_1 = e_2,
$$

$$
e_2 e_1 = -e_3, \quad e_3 e_2 = -e_1, \quad e_1 e_3 = -e_2.
$$

A general quaternion is $q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ with $q_\mu \in \mathbb{R}$. The quaternions are associative and unital over $\mathbb{R}$, and every nonzero element has an inverse. They are not commutative. So they form a **division algebra over $\mathbb{R}$** but not a field.

By the Frobenius theorem (Part V below), the quaternions are one of only three finite-dimensional associative real division algebras, the others being $\mathbb{R}$ and $\mathbb{C}$.

## 8. The Split Complex Numbers $\mathbb{D}$ over $\mathbb{R}$

The set of split complex numbers is a **two-dimensional algebra over $\mathbb{R}$**, with basis $\{1, e\}$ and the relation $e^2 = +1$. A general element is $a + be$ with $a, b \in \mathbb{R}$, and the product is

$$
(a + be)(c + de) = (ac + bd) + (ad + bc)e.
$$

It is associative, commutative, and unital over $\mathbb{R}$, but it is **not a division algebra**: it has zero divisors. For example, $(1 + e)(1 - e) = 0$.

## 9. The Dual Numbers over $\mathbb{R}$

The **dual numbers** are a **two-dimensional algebra over $\mathbb{R}$**, with basis $\{1, \epsilon\}$ and the relation $\epsilon^2 = 0$. A general element is $a + b\epsilon$ with $a, b \in \mathbb{R}$, and the product is

$$
(a + b\epsilon)(c + d\epsilon) = ac + (ad + bc)\epsilon.
$$

They are associative, commutative, and unital over $\mathbb{R}$, but not a division algebra: $\epsilon$ is nilpotent and has no inverse.

## 10. The Algebra $M_n(\mathbb{R})$ over $\mathbb{R}$

The set of $n \times n$ matrices with real entries is an **$n^2$-dimensional algebra over $\mathbb{R}$**. The product is matrix multiplication. It is associative and unital over $\mathbb{R}$. It is not commutative for $n \geq 2$. It is not a division algebra: a matrix with vanishing determinant is nonzero but has no inverse.

## 11. The Polynomial Algebra $\mathbb{R}[x]$ over $\mathbb{R}$

The set of polynomials in one variable with real coefficients is an **infinite-dimensional algebra over $\mathbb{R}$**. The product is ordinary multiplication of polynomials. It is associative, commutative, and unital over $\mathbb{R}$. It is not a division algebra.

## 12. The Exterior Algebra $\Lambda(V)$ over $\mathbb{R}$

Let $V$ be a real vector space of dimension $n$. The **exterior algebra** $\Lambda(V)$ is a **$2^n$-dimensional algebra over $\mathbb{R}$**, generated by $V$ subject to the relation $v \wedge v = 0$. It is associative and unital over $\mathbb{R}$. It is not commutative for $n \geq 2$. It is not a division algebra.

## 13. The Cross Product Algebra on $\mathbb{R}^3$ over $\mathbb{R}$

The set $\mathbb{R}^3$ with the cross product is a **three-dimensional algebra over $\mathbb{R}$**. It is bilinear and antisymmetric over $\mathbb{R}$, but **not associative**. It satisfies the Jacobi identity, so it is a Lie algebra over $\mathbb{R}$.

## 14. The Tensor Algebra $T(V)$ over $\mathbb{R}$

Let $V$ be a real vector space. The **tensor algebra** $T(V)$ is an **infinite-dimensional algebra over $\mathbb{R}$**, the free associative unital algebra on $V$. It satisfies no relations beyond bilinearity and associativity.

## 15. The Clifford Algebra $Cl(V, Q)$ over $\mathbb{R}$

Let $V$ be a real vector space with a quadratic form $Q$. The **Clifford algebra** $Cl(V, Q)$ is a **$2^n$-dimensional algebra over $\mathbb{R}$**, generated by $V$ subject to the relation $v^2 = Q(v) \cdot 1$. It is associative and unital over $\mathbb{R}$. It includes the real numbers, the complex numbers, and the quaternions as special cases.

---

# Part III: Algebras over $\mathbb{C}$

## 16. The Complex Numbers $\mathbb{C}$ over $\mathbb{C}$

The set of complex numbers is a **one-dimensional algebra over $\mathbb{C}$**. The product is multiplication of complex numbers. It is associative, commutative, unital, and a division algebra over $\mathbb{C}$. It is a field.

## 17. The Biquaternions $\mathbb{H} \otimes \mathbb{C}$ over $\mathbb{C}$

The **biquaternions** are the tensor product $\mathbb{H} \otimes_\mathbb{R} \mathbb{C}$, viewed as a **four-dimensional algebra over $\mathbb{C}$**, with basis $\{1, i, j, k\}$ and the same relations as the quaternions, with coefficients in $\mathbb{C}$. They are associative and unital over $\mathbb{C}$, but not commutative. They are **not a division algebra**: they have zero divisors. As a complex algebra, they are isomorphic to $M_2(\mathbb{C})$.

## 18. The Algebra $M_n(\mathbb{C})$ over $\mathbb{C}$

The set of $n \times n$ matrices with complex entries is an **$n^2$-dimensional algebra over $\mathbb{C}$**. The product is matrix multiplication. It is associative and unital over $\mathbb{C}$. It is not commutative for $n \geq 2$. It is not a division algebra.

## 19. The Polynomial Algebra $\mathbb{C}[x]$ over $\mathbb{C}$

The set of polynomials in one variable with complex coefficients is an **infinite-dimensional algebra over $\mathbb{C}$**. It is associative, commutative, and unital over $\mathbb{C}$. It is not a division algebra.

## 20. The Complex Cross Product Algebra on $\mathbb{C}^3$ over $\mathbb{C}$

The set $\mathbb{C}^3$ with the complex cross product is a **three-dimensional algebra over $\mathbb{C}$**. It is bilinear and antisymmetric over $\mathbb{C}$, but not associative. It satisfies the Jacobi identity, so it is a Lie algebra over $\mathbb{C}$.

---

# Part IV: Algebras over $\mathbb{D}$

The split complex numbers $\mathbb{D}$ are not a field in the strict sense: they form a commutative ring with zero divisors. But the theory of algebras over $\mathbb{D}$ is similar to the theory over a field, with the caveat that not every nonzero element has an inverse.

## 21. The Split Complex Numbers $\mathbb{D}$ over $\mathbb{D}$

The set of split complex numbers is a **one-dimensional algebra over $\mathbb{D}$**. The product is multiplication of split complex numbers. It is associative, commutative, and unital over $\mathbb{D}$. It is not a division algebra over $\mathbb{D}$, because $\mathbb{D}$ itself has zero divisors.

## 22. The Split Quaternions over $\mathbb{D}$

The **split quaternions** are the tensor product $\mathbb{H} \otimes_\mathbb{R} \mathbb{D}$, viewed as a **four-dimensional algebra over $\mathbb{D}$**, with basis $\{1, i, j, k\}$ and the same relations as the quaternions, with coefficients in $\mathbb{D}$. They are associative and unital over $\mathbb{D}$, but not commutative. They are not a division algebra.

---

# Part V: The Frobenius Theorem

The classification of algebras over $\mathbb{R}$ is governed by a classical theorem that singles out the three division algebras $\mathbb{R}$, $\mathbb{C}$, and $\mathbb{H}$. This section states the theorem, explains the field to which it applies, discusses the consequences, and computes the tensor products of the three algebras.

## 23. The Statement of the Theorem

**Frobenius's theorem.** Let $A$ be a finite-dimensional associative algebra over the field $\mathbb{R}$ with no zero divisors. Then $A$ is isomorphic to one of the following three algebras:

1. $\mathbb{R}$, of dimension $1$ over $\mathbb{R}$.
2. $\mathbb{C}$, of dimension $2$ over $\mathbb{R}$.
3. $\mathbb{H}$, of dimension $4$ over $\mathbb{R}$.

Each of these three algebras is a division algebra over $\mathbb{R}$, and they are pairwise non-isomorphic.

The theorem was proved by Ferdinand Georg Frobenius in 1878. It is one of the foundational results of the theory of real algebras.

## 24. The Field in the Theorem

The field in the theorem is $\mathbb{R}$, the real numbers. The theorem is a statement about **algebras over $\mathbb{R}$**. It does not apply to algebras over $\mathbb{Q}$, $\mathbb{C}$, or any other field or ring. The reader should keep in mind throughout this section that the base field is $\mathbb{R}$.

This is worth emphasizing because the Frobenius theorem is often stated in the literature without making the field explicit, and it is easy to conflate it with statements about other fields. The theorem is specifically about real algebras. Over $\mathbb{Q}$, for example, there are infinitely many quaternion algebras, and the classification is much more complicated. Over $\mathbb{C}$, the only finite-dimensional associative division algebra is $\mathbb{C}$ itself, because $\mathbb{C}$ is algebraically closed. So the Frobenius theorem is a distinctively real phenomenon.

## 25. Why the Theorem Matters

The theorem tells us that the passage from $\mathbb{R}$ to $\mathbb{C}$ to $\mathbb{H}$ exhausts the finite-dimensional associative real division algebras. There is no four-dimensional real division algebra other than $\mathbb{H}$, and there is no real division algebra of any dimension greater than $4$ if we require associativity.

If we drop associativity, the **Cayley–Dickson construction** allows us to continue the doubling procedure one more step, to the **octonions** $\mathbb{O}$, of dimension $8$ over $\mathbb{R}$. The octonions are a non-associative division algebra. Beyond the octonions, the construction produces algebras with zero divisors (the sedenions and beyond), so the doubling stops there for division algebras.

The Frobenius theorem is therefore the precise statement that the classical number systems $\mathbb{R}$, $\mathbb{C}$, and $\mathbb{H}$ are the only associative real division algebras. It is the algebraic counterpart of the geometric fact that the only finite-dimensional real normed division algebras are $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$, and $\mathbb{O}$ (the last being non-associative).

## 26. The Tensor Products

The Frobenius theorem is complemented by the computation of the tensor products of the three algebras over $\mathbb{R}$. These show that the tensor product of two division algebras over $\mathbb{R}$ need not be a division algebra. All tensor products below are over $\mathbb{R}$.

**$\mathbb{R} \otimes_\mathbb{R} \mathbb{R} \cong \mathbb{R}$.** Dimension $1$. A division algebra.

**$\mathbb{R} \otimes_\mathbb{R} \mathbb{C} \cong \mathbb{C}$.** Dimension $2$. A division algebra.

**$\mathbb{R} \otimes_\mathbb{R} \mathbb{H} \cong \mathbb{H}$.** Dimension $4$. A division algebra.

**$\mathbb{C} \otimes_\mathbb{R} \mathbb{C} \cong \mathbb{C} \oplus \mathbb{C}$.** Dimension $4$. Not a division algebra: it has zero divisors. The idempotents $e_1 = \tfrac{1}{2}(1 \otimes 1 + i \otimes j)$ and $e_2 = \tfrac{1}{2}(1 \otimes 1 - i \otimes j)$ satisfy $e_1 e_2 = 0$.

**$\mathbb{C} \otimes_\mathbb{R} \mathbb{H} \cong \mathbb{B} \cong M_2(\mathbb{C})$.** Dimension $8$. Here $\mathbb{B} = \mathbb{H} \otimes_\mathbb{R} \mathbb{C}$ is the **biquaternion algebra**. It is not a division algebra: it has zero divisors. As a complex algebra, it is isomorphic to $M_2(\mathbb{C})$.

**$\mathbb{H} \otimes_\mathbb{R} \mathbb{H} \cong M_4(\mathbb{R})$.** Dimension $16$. Not a division algebra: it has zero divisors. It is the algebra of $4 \times 4$ real matrices.

The pattern is clear: the tensor product of two division algebras over $\mathbb{R}$ is a division algebra if and only if at least one factor is $\mathbb{R}$. As soon as both factors are non-trivial, the tensor product has zero divisors.

This phenomenon is governed by the **Brauer group** of $\mathbb{R}$, which is isomorphic to $\mathbb{Z}/2\mathbb{Z}$. The two elements are represented by $\mathbb{R}$ (the identity) and $\mathbb{H}$ (the non-trivial element). The complex numbers $\mathbb{C}$ are not a central simple algebra over $\mathbb{R}$, because they are commutative, and their tensor products split as direct sums of copies of $\mathbb{C}$. The tensor product $\mathbb{H} \otimes_\mathbb{R} \mathbb{H} \cong M_4(\mathbb{R})$ is the statement that $\mathbb{H}$ has order $2$ in the Brauer group of $\mathbb{R}$.

## 27. Summary

**The field is $\mathbb{R}$.** The Frobenius theorem is a statement about finite-dimensional associative division algebras over $\mathbb{R}$. The three algebras are $\mathbb{R}$, $\mathbb{C}$, and $\mathbb{H}$, of dimensions $1$, $2$, and $4$ over $\mathbb{R}$.

**The tensor products are over $\mathbb{R}$.** There are six tensor products of the three algebras, and only the three involving $\mathbb{R}$ as a factor are division algebras. The other three have zero divisors.

**No other field is involved.** The theorem and the tensor products are entirely about the field $\mathbb{R}$.

**The theorem is sharp.** There are no other finite-dimensional associative real division algebras. If associativity is dropped, the octonions are the only additional example.

---

# Summary

Let me summarize the classification in a table.

| Algebra | Ring | Rank | Associative | Commutative | Unital | Division |
|---|---|---|---|---|---|---|
| $\mathbb{Q}$ | $\mathbb{Q}$ | 1 | yes | yes | yes | yes |
| $\mathbb{Q}[\sqrt{2}]$ | $\mathbb{Q}$ | 2 | yes | yes | yes | yes |
| $\mathbb{H}(\mathbb{Q})$ | $\mathbb{Q}$ | 4 | yes | no | yes | yes |
| $M_n(\mathbb{Q})$ | $\mathbb{Q}$ | $n^2$ | yes | no | yes | no |
| $\mathbb{R}$ | $\mathbb{R}$ | 1 | yes | yes | yes | yes |
| $\mathbb{C}$ | $\mathbb{R}$ | 2 | yes | yes | yes | yes |
| $\mathbb{H}$ | $\mathbb{R}$ | 4 | yes | no | yes | yes |
| $\mathbb{D}$ | $\mathbb{R}$ | 2 | yes | yes | yes | no |
| dual numbers | $\mathbb{R}$ | 2 | yes | yes | yes | no |
| $M_n(\mathbb{R})$ | $\mathbb{R}$ | $n^2$ | yes | no | yes | no |
| $\mathbb{R}[x]$ | $\mathbb{R}$ | $\infty$ | yes | yes | yes | no |
| $\Lambda(V)$ | $\mathbb{R}$ | $2^n$ | yes | no | yes | no |
| $\mathbb{R}^3$ cross | $\mathbb{R}$ | 3 | no | no | no | no |
| $T(V)$ | $\mathbb{R}$ | $\infty$ | yes | no | yes | no |
| $Cl(V, Q)$ | $\mathbb{R}$ | $2^n$ | yes | no | yes | no |
| $\mathbb{C}$ | $\mathbb{C}$ | 1 | yes | yes | yes | yes |
| $\mathbb{H} \otimes \mathbb{C}$ | $\mathbb{C}$ | 4 | yes | no | yes | no |
| $M_n(\mathbb{C})$ | $\mathbb{C}$ | $n^2$ | yes | no | yes | no |
| $\mathbb{C}[x]$ | $\mathbb{C}$ | $\infty$ | yes | yes | yes | no |
| $\mathbb{C}^3$ cross | $\mathbb{C}$ | 3 | no | no | no | no |
| $\mathbb{D}$ | $\mathbb{D}$ | 1 | yes | yes | yes | no |
| $\mathbb{H} \otimes \mathbb{D}$ | $\mathbb{D}$ | 4 | yes | no | yes | no |

The pattern is clear: the ring of scalars determines the structure of the algebra. The rational numbers give rise to arithmetic versions of the classical algebras. The real numbers give rise to the classical division algebras $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$, and the split and degenerate versions $\mathbb{D}$ and the dual numbers. The complex numbers give rise to the biquaternions and matrix algebras. The split complex numbers give rise to the split versions, which have zero divisors and are not division algebras.

**Key differences from the field case.** Over the fields $\mathbb{Q}$, $\mathbb{R}$, and $\mathbb{C}$, the theory is the classical theory of algebras over a field. Over the commutative ring $\mathbb{D}$, the theory is similar but with the following caveats:

- Not every nonzero element of $\mathbb{D}$ is a unit, so a $\mathbb{D}$-algebra can fail to be a division algebra even if it has no zero divisors of its own.
- The rank of a $\mathbb{D}$-algebra is well-defined only if the algebra is free as a $\mathbb{D}$-module.
- The classical theorems (Frobenius, Wedderburn) do not apply over $\mathbb{D}$, because $\mathbb{D}$ is not a field.

---

## Further Reading

- Michael Artin, *Algebra* (Prentice Hall, 1991).
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002).
- I. N. Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975).
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003).
- Nathan Jacobson, *Basic Algebra I* and *II* (Dover, 2nd ed. 2009).
- David S. Dummit and Richard M. Foote, *Abstract Algebra* (Wiley, 3rd ed. 2004).
- Richard S. Pierce, *Associative Algebras* (Springer, 1982).
- I. R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995).
- I. M. Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968).
- F. Catoni, R. Cannata, V. Catoni, E. Nichelatti, P. Zampetti, *The Mathematics of Minkowski Space-Time* (Birkhäuser, 2008).

