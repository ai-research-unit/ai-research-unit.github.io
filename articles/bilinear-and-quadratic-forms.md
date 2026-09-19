
# __Bilinear and Quadratic Forms__

## Introduction

This article introduces bilinear and quadratic forms. The treatment is introductory and purely mathematical.

The goal is to explain what a bilinear form is, what a quadratic form is, and how the two are related. The correspondence between bilinear forms and quadratic forms is the central idea: every symmetric bilinear form gives rise to a quadratic form by taking the diagonal, and every quadratic form arises in this way from a unique symmetric bilinear form, provided the base ring has characteristic not equal to 2 and 2 is invertible.

We assume familiarity with modules and linear maps. No prior knowledge of bilinear forms is required.

This article treats the general theory over a **commutative ring**, without assuming finite rank. The finite-rank theory — diagonalization, signature, and classification — is developed in the article *Clifford Algebras in Finite Dimensions*, where it is used to classify Clifford algebras.

A separate article, *Bilinear and Quadratic Forms: Categorization*, gives a classification organized by ring.

A word on the base structure. The classical theory of bilinear and quadratic forms assumes that the scalars form a field. But many of the constructions and theorems carry over to the more general setting where the scalars form a **commutative ring**. This is the setting we adopt here. The main differences from the field case are:

- Modules over a commutative ring need not be free, whereas vector spaces over a field always are.
- The polarization identity requires division by 2, so we must assume that 2 is invertible in the base ring.
- Non-degeneracy of a bilinear form is defined via an isomorphism $V \to V^*$, which requires care over a general commutative ring.
- The classification of quadratic forms is much more subtle over a general commutative ring than over a field.

We indicate where these differences matter.

---

## Part I: Bilinear Forms

### The Definition

Let $M$ be a module over a commutative ring $R$. A **bilinear form** on $M$ is a function

$$
B : M \times M \to R
$$

that is **linear in each argument separately**:

1. **Linearity in the first argument:**

$$
B(u + v, w) = B(u, w) + B(v, w), \qquad B(r u, v) = r B(u, v)
$$

for all $u, v, w \in M$ and $r \in R$.

2. **Linearity in the second argument:**

$$
B(u, v + w) = B(u, v) + B(u, w), \qquad B(u, r v) = r B(u, v)
$$

for all $u, v, w \in M$ and $r \in R$.

A bilinear form is **symmetric** if

$$
B(u, v) = B(v, u)
$$

for all $u, v \in M$. In this article we consider only symmetric bilinear forms, since they are the ones that give rise to quadratic forms.

### Non-Degeneracy

A symmetric bilinear form $B$ over a commutative ring $R$ is **non-degenerate** if the induced map

$$
M \to M^*, \qquad u \mapsto B(u, -),
$$

is an isomorphism, where $M^* = \operatorname{Hom}_R(M, R)$ is the dual module.

A symmetric bilinear form is **degenerate** if the induced map is not an isomorphism. The kernel of the map is the **radical** of $B$:

$$
\mathrm{rad}(B) = \{u \in M : B(u, v) = 0 \text{ for all } v \in M\}.
$$

Over a finite-dimensional vector space, the form is non-degenerate if and only if the radical is zero. Over a general commutative ring, non-degeneracy is a stronger condition: the radical must be zero **and** the induced map must be surjective.

**Key difference from the field case.** Over a finite-dimensional vector space, the induced map $V \to V^*$ is injective if and only if it is an isomorphism, because $V$ and $V^*$ have the same finite dimension. Over a general commutative ring, this is not true: a module and its dual can have different "sizes," and injectivity does not imply surjectivity. So non-degeneracy over a ring is more delicate than over a field.

### The Matrix of a Bilinear Form

Let $M$ be a free module over a commutative ring $R$ with basis $e_1, \ldots, e_n$. A bilinear form $B$ is completely determined by its values on the basis vectors. Define

$$
M_{ij} = B(e_i, e_j).
$$

Then for any $u = \sum_i u_i e_i$ and $v = \sum_j v_j e_j$, we have

$$
B(u, v) = \sum_{i=1}^{n} \sum_{j=1}^{n} u_i v_j B(e_i, e_j) = \sum_{i=1}^{n} \sum_{j=1}^{n} M_{ij} u_i v_j.
$$

In matrix form,

$$
B(u, v) = u^T M v,
$$

where $u$ and $v$ are the column vectors of coordinates, and $M$ is the $n \times n$ matrix with entries $M_{ij}$.

If $B$ is symmetric, then the matrix $M$ is symmetric: $M_{ij} = M_{ji}$.

Over a field, the form $B$ is non-degenerate if and only if the matrix $M$ is invertible. Over a general commutative ring, the form $B$ is non-degenerate if and only if the matrix $M$ is invertible, which means its determinant is a **unit** of $R$. This is the key modification.

### Change of Basis

The matrix of a bilinear form depends on the choice of basis. If we change the basis, the matrix changes in a controlled way.

Let $\mathcal{B}$ and $\mathcal{B}'$ be two bases of $M$, and let $P$ be the change-of-basis matrix from $\mathcal{B}'$ to $\mathcal{B}$. Then for any vector $v \in M$,

$$
[v]_{\mathcal{B}} = P [v]_{\mathcal{B}'}.
$$

Substituting into the formula $B(u, v) = [u]_{\mathcal{B}}^T M [v]_{\mathcal{B}}$, we get

$$
B(u, v) = [u]_{\mathcal{B}'}^T (P^T M P) [v]_{\mathcal{B}'}.
$$

So the matrix of $B$ with respect to the new basis $\mathcal{B}'$ is

$$
M' = P^T M P.
$$

Two matrices $M$ and $M'$ related by $M' = P^T M P$ for some invertible $P$ are called **congruent**. The classification of bilinear forms up to change of basis is the classification of symmetric matrices up to congruence.

**Key difference from the field case.** Over a field, "invertible" means "nonzero determinant." Over a general commutative ring, "invertible" means "determinant is a unit." So the congruence relation is more restrictive over a general commutative ring than over a field.

---

## Part II: The Quadratic Form of a Bilinear Form

### The Diagonal

Given a symmetric bilinear form $B$ on a module $M$ over a commutative ring $R$, we define a function $Q : M \to R$ by evaluating $B$ on the diagonal:

$$
Q(v) = B(v, v).
$$

This function is called the **quadratic form associated with $B$**. It is the natural function of one variable that comes from a bilinear form of two variables.

The function $Q$ has the following property:

$$
Q(r v) = B(r v, r v) = r^2 B(v, v) = r^2 Q(v)
$$

for all $r \in R$ and $v \in M$. So $Q$ is **homogeneous of degree 2**.

### The Polarization Identity

We have seen that every symmetric bilinear form $B$ over a commutative ring $R$ gives rise to a quadratic form $Q(v) = B(v, v)$. The converse is also true, provided the ring has characteristic not equal to 2 and 2 is invertible: every quadratic form arises from a unique symmetric bilinear form.

The bridge between the two is the **polarization identity**. Let us derive it.

For any $u, v \in M$, we have

$$
Q(u + v) = B(u + v, u + v).
$$

Expanding using bilinearity and symmetry,

$$
Q(u + v) = B(u, u) + B(u, v) + B(v, u) + B(v, v) = Q(u) + 2B(u, v) + Q(v).
$$

Solving for $B(u, v)$,

$$
B(u, v) = \frac{1}{2}\bigl(Q(u + v) - Q(u) - Q(v)\bigr).
$$

This is the polarization identity. It recovers the bilinear form $B$ from the quadratic form $Q$.

The identity uses division by 2, so it requires that 2 is invertible in the ring $R$. Over $\mathbb{R}$, $\mathbb{C}$, and $\mathbb{Q}$, this is automatic. Over $\mathbb{Z}$, it is not: 2 is not a unit of $\mathbb{Z}$. So the theory over $\mathbb{Z}$ requires more care.

**Key difference from the field case.** Over a field of characteristic not equal to 2, 2 is automatically invertible. Over a general commutative ring, we must assume that 2 is a unit. This is the main hypothesis needed to extend the theory.

### The Correspondence

We have established a bijective correspondence:

$$
\left\{ \begin{array}{c} \text{symmetric bilinear} \\ \text{forms } B \text{ on } M \end{array} \right\}
\longleftrightarrow
\left\{ \begin{array}{c} \text{quadratic} \\ \text{forms } Q \text{ on } M \end{array} \right\}.
$$

The map from $B$ to $Q$ is $Q(v) = B(v, v)$. The inverse map from $Q$ to $B$ is the polarization identity.

This correspondence is the reason quadratic forms are important. They allow us to study symmetric bilinear forms — which are linear in each argument — through a single function of one variable, and vice versa.

---

## Part III: The Abstract Characterization

### The Characterization

We have seen that every symmetric bilinear form $B$ over a commutative ring $R$ gives rise to a function $Q(v) = B(v, v)$ that is homogeneous of degree 2 and whose polarization is bilinear. Conversely, every function with these two properties arises from a unique symmetric bilinear form, provided 2 is invertible in $R$.

This gives an abstract characterization of quadratic forms that does not refer to a bilinear form:

A **quadratic form** on $M$ over a commutative ring $R$ is a function $Q : M \to R$ such that:

1. **Homogeneity of degree 2:** $Q(r v) = r^2 Q(v)$ for all $r \in R$ and $v \in M$.
2. **The polarization condition:** the function $B : M \times M \to R$ defined by

$$
B(u, v) = \frac{1}{2}\bigl(Q(u + v) - Q(u) - Q(v)\bigr)
$$

is bilinear.

The second condition is exactly the condition that $Q$ arises from a symmetric bilinear form. It is not a technicality: it is the condition that ensures $Q$ is a quadratic form in the geometric sense.

### Why This Order Matters

The abstract characterization is not the most natural starting point. It is the endpoint of the construction, not the beginning. We start with a bilinear form, define the quadratic form as its diagonal, and then characterize the objects obtained in this way. The abstract definition is a *summary* of what we have built, not a *foundation*.

This order has two advantages:

1. It makes the polarization identity obvious: it is just the expansion of $B(u + v, u + v)$.
2. It makes the correspondence between bilinear and quadratic forms transparent: it is a bijection, and the two directions are given by the diagonal and the polarization identity.

---

## Part IV: Summary

Let me summarize the main points.

**A bilinear form** on a module $M$ over a commutative ring $R$ is a function $B : M \times M \to R$ that is linear in each argument separately. It is symmetric if $B(u, v) = B(v, u)$.

**The matrix of a bilinear form** with respect to a basis $e_1, \ldots, e_n$ is the matrix $M$ with entries $M_{ij} = B(e_i, e_j)$. It satisfies $B(u, v) = u^T M v$. Under a change of basis with change-of-basis matrix $P$, the matrix transforms as $M' = P^T M P$.

**A quadratic form** is the diagonal of a symmetric bilinear form: $Q(v) = B(v, v)$.

**The polarization identity** recovers the bilinear form from the quadratic form:

$$
B(u, v) = \frac{1}{2}\bigl(Q(u + v) - Q(u) - Q(v)\bigr).
$$

It requires that 2 is invertible in the ring $R$.

**The correspondence** between symmetric bilinear forms and quadratic forms is bijective, provided 2 is invertible in $R$.

**The abstract characterization** of a quadratic form is: a function $Q : M \to R$ that is homogeneous of degree 2 and whose polarization is bilinear.

**Key differences from the field case.**

- Over a field, every module is free, so every bilinear form has a matrix with respect to a basis. Over a general commutative ring, not every module is free.
- Over a finite-dimensional vector space, non-degeneracy is equivalent to the radical being zero. Over a general commutative ring, non-degeneracy requires the induced map $M \to M^*$ to be an isomorphism.
- Over a field of characteristic not equal to 2, 2 is automatically invertible. Over a general commutative ring, we must assume that 2 is a unit.
- Over a field, invertibility of a matrix is equivalent to nonzero determinant. Over a general commutative ring, invertibility requires the determinant to be a unit.

The finite-rank theory — diagonalization, signature, and classification — is developed in the article *Clifford Algebras in Finite Dimensions*. A classification of examples is given in the article *Bilinear and Quadratic Forms: Categorization*.

---

## Further Reading

- Michael Artin, *Algebra* (Prentice Hall, 1991).
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002).
- I. N. Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975).
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003).
- Nathan Jacobson, *Basic Algebra I* (Dover, 2nd ed. 2009).
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Springer, 1991).
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (AMS, 2005).

