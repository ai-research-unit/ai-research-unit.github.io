# __The Hermitian Form, the Double Cone and the Reversed Cauchy-Schwarz Inequality__

## Introduction

The Hermitian form $H(A,C)=A\bar C$ is indefinite, and everything in this article follows from that one fact. The set where $H$ is non-negative is a double cone, not a half-space and not the plane; the two idempotent lines are totally isotropic; the sign of the form on a pair of causal vectors is forced, and it forces a Cauchy-Schwarz inequality with the inequality reversed. The cone then defines an order, and the norm-one elements form a group with two branches.

The claim is that the indefiniteness is not a defect to be repaired but the structure itself. It is what makes the ring a partial order, what makes two idempotent lines isotropic, and what makes the unitary group of rank one non-compact; all three are one property, seen three times. The comparison with the complex field, where the form is definite, gives the contrast at each step.

The form is *The Two Forms and the Two Algebraic Norms of the Split-Complex Space*; the isotropic lines are *The Involutions, the Subspaces and the Idempotent Lines of the Split-Complex Space*; the level sets are *The Level Sets of the Split Norm and the Hyperbolic Structure*; the group of units is *Norm and Invertibility in the General Split-Complex Algebra*.

## The Cone of $H$-Positivity

### The Definition

**Definition.** The **cone of $H$-positivity** is the set of elements whose Hermitian square is non-negative,

$$
\mathcal{C}=\{Q : H(Q,Q)\ge0\}=\{Q : N(Q)\ge0\} .
$$

On the coordinates $N(Q)=a^2-b^2$, so the cone is

$$
\mathcal{C}=\{a+jb : a^2\ge b^2\} ,
$$

the **double cone** of the hyperbolic metric: the union of the two opposite cones $\{a\ge\lvert b\rvert\}$ and $\{a\le-\lvert b\rvert\}$, glued at the origin.

### The Two Components

The double cone has two components, and they are the two signs of the coordinate $a$:

$$
\mathcal{C}_+=\{a\ge\lvert b\rvert\}, \qquad \mathcal{C}_-=\{a\le-\lvert b\rvert\} ,
$$

the **forward** and the **backward** cone. In idempotent coordinates the two components are the two sets where the coordinates have a common sign, since $N=Q_+Q_-$:

$$
\mathcal{C}_+=\{Q_+\ge0,\ Q_-\ge0\}, \qquad \mathcal{C}_-=\{Q_+\le0,\ Q_-\le0\} .
$$

Each component is closed, convex, closed under addition and under multiplication by non-negative scalars, and pointed: $\mathcal{C}_+\cap(-\mathcal{C}_+)=\{0\}$.

### The Interior and the Boundary

**Theorem.** The interior of the cone is the set of units of positive norm, and its boundary is the set of zero divisors with the origin adjoined.

**Proof.** An element is interior to $\mathcal{C}$ when $N(Q)>0$, and $N(Q)\neq0$ is the criterion of invertibility. The boundary is the set where $N(Q)=0$, which is the union of the two null lines; those lines are the union of the two families $\mathbb{R}^\times\Pi_\pm$ of zero divisors and the origin (*Zero Divisors of the Split-Complex Algebra*).

So the cone is a picture of the ring's classification: the two open regions inside it are the timelike units, its boundary is the singular set, and its exterior is the set of the elements of negative norm, which are units too, on the spacelike side. The group of units is therefore the interior together with the exterior, and the cone alone is not it. The double cone is not the set of units and its complement is not the set of zero divisors; the boundary is.

## The Vanishing on the Idempotent Lines

### The Two Lines Are Totally Isotropic

**Theorem.** $H$ vanishes on each of the two idempotent lines,

$$
H(\lambda\Pi_+,\mu\Pi_+)=0, \qquad H(\lambda\Pi_-,\mu\Pi_-)=0 \qquad(\lambda,\mu\in\mathbb{R}),
$$

so both lines are **totally isotropic**.

**Proof.** $\overline{\Pi_+}=\Pi_-$ and $\Pi_+\Pi_-=0$ give $H(\lambda\Pi_+,\mu\Pi_+)=\lambda\mu\Pi_+\Pi_-=0$, and the other line is the same computation.

A line is totally isotropic when the form vanishes on it, not merely when some vector of it is isotropic. The two idempotent lines are the extreme case: every vector of each is isotropic, and the form vanishes on every pair of them. The two isotropic lines are the two components of the boundary of the cone, which is why the boundary is a pair of straight lines and not a curve.

### The Algebra Is Not a Hilbert Algebra

**Definition.** A **Hilbert algebra** is an algebra with an involution $\dagger$ and a positive definite Hermitian form with $\langle xy,z\rangle=\langle y,x^{\dagger}z\rangle$.

**Theorem.** $\mathbb{C}_{\mathrm{spl}}$ with $H$ satisfies the adjoint axiom and fails the positivity, so it is not a Hilbert algebra.

**Proof.** $H(QX,Y)=QX\bar Y$ and $H(X,\bar QY)=X\overline{\bar QY}=XQ\bar Y$, so the axiom holds with $Q^{\dagger}=\bar Q$. The form is not positive definite, since $H(\Pi_+,\Pi_+)=0$ with $\Pi_+\neq0$, and it is not even positive semi-definite, since $H$ takes both signs.

The adjoint axiom is satisfied, so the algebra is a **$\ast$-algebra with a Hermitian form** and not a Hilbert algebra. The gap is positivity, and positivity is exactly what the two isotropic lines destroy. Over the complex field the same construction is a Hilbert algebra: $A\bar C$ is definite there and the adjoint axiom holds.

## The Reversed Cauchy-Schwarz Inequality

### The Statement

**Theorem (reversed Cauchy-Schwarz).** Let $A$ and $C$ lie in the same component of the cone. Then

$$
g(A,C)\ \ge\ \sqrt{N(A)\,N(C)} ,
$$

where $g(A,C)=ac-bd$ is the polar form. On the whole double cone the inequality holds with the sign dropped,

$$
g(A,C)^2\ \ge\ N(A)\,N(C) .
$$

### The Proof

**Proof.** Work in the idempotent coordinates, where $g(A,C)=\tfrac12(A_+C_-+A_-C_+)$ and $N(A)=A_+A_-$. Both coordinates of both elements are non-negative in one component, so

$$
A_+C_-+A_-C_+\ \ge\ 2\sqrt{A_+C_-\,A_-C_+}=2\sqrt{N(A)N(C)}
$$

by the inequality $x+y\ge2\sqrt{xy}$ for non-negative $x,y$. Halving gives the first statement. For the second, apply the first to $A$ and to $-C$ if they lie in opposite components; the left side changes sign and the right side multiplies by $-1$, so the squared form holds throughout.

The proof is the whole of the matter: on a definite form the argument runs with $x+y\ge2\sqrt{xy}$ reversed, and the reversal of the sign of the form reverses the inequality. Over $\mathbb{C}$ the Cauchy-Schwarz inequality for $A\bar C$ is $\lvert g(A,C)\rvert\le\lvert A\rvert\lvert C\rvert$, with the inequality pointing the other way.

### The Equality Case

Equality holds exactly when the two elements are proportional with a non-negative factor:

$$
g(A,C)=\sqrt{N(A)N(C)} \iff A=\lambda C\ \text{or}\ C=\lambda A\ \text{with}\ \lambda\ge0 .
$$

**Proof.** Equality in $x+y\ge2\sqrt{xy}$ needs $x=y$, that is $A_+C_+=A_-C_-$; with all four coordinates non-negative this forces the two pairs to be proportional, and the factor to be non-negative.

On the same component the reversed inequality is therefore an equality on the rays of the cone and strict elsewhere, exactly as the ordinary one is an equality on the lines of the plane.

## The Reversed Triangle Inequality

### The Statement and the Proof

**Theorem.** For $A$ and $C$ in the same component of the cone,

$$
\sqrt{N(A+C)}\ \ge\ \sqrt{N(A)}+\sqrt{N(C)} .
$$

**Proof.** $N(A+C)=N(A)+N(C)+2g(A,C)$, and the reversed Cauchy-Schwarz bounds $g$ from below, so

$$
N(A+C)\ \ge\ N(A)+N(C)+2\sqrt{N(A)N(C)}=\bigl(\sqrt{N(A)}+\sqrt{N(C)}\bigr)^2 .
$$

The square root is monotone on the non-negative reals, and $A+C$ is in the same component, so $N(A+C)\ge0$ and the inequality follows.

The inequality points the other way from the ordinary triangle inequality: the sum of two causal vectors is longer than the sum of their lengths. This is the reverse triangle inequality of the hyperbolic metric, and it is the reason the distance defined by the norm is a hyperbolic distance and not a Euclidean one.

### The Failure Across Components

The inequality fails when the two elements lie in opposite components. On $A=\Pi_+$ and $C=-\Pi_-$ both norms vanish and $A+C=j$ has norm $-1$, so the right side is $0$ and the left is not defined. Even the weaker statement fails: $\sqrt{N(A+C)}$ is not real there. The reversed inequality is a statement about one component, and it must be stated as such.

## The Order the Cone Defines

### The Order

**Definition.** For $A,C$ in the plane, $A\succeq C$ when $A-C\in\mathcal{C}_+$.

**Theorem.** $\succeq$ is a partial order, and it is the product of the two orders of the idempotent coordinates:

$$
A\succeq C \iff A_+\ge C_+ \ \text{and}\ A_-\ge C_- .
$$

**Proof.** $A-C\in\mathcal{C}_+$ reads $(A-C)_+\ge0$ and $(A-C)_-\ge0$, which is the two inequalities displayed. The order is reflexive, transitive and antisymmetric because each of the two coordinate orders is.

### Partial, Not Total

The order is not total. The two idempotents are incomparable: $\Pi_+-\Pi_-=j$ has norm $-1$ and $\Pi_--\Pi_+$ has norm $-1$, so neither difference lies in the cone. So there are pairs of elements of which neither is above the other, and the order is a partial order in the strict sense.

The double cone alone does not give an order: it is not convex, since the sum of a vector of one component and a vector of the other can leave the cone, and it is not pointed, since $\mathcal{C}\cap(-\mathcal{C})=\mathcal{C}$. The order comes from one component, and the choice of the forward one is the choice of a time direction.

### Monotonicity of the Product

**Proposition.** If $A\succeq0$ and $C\succeq0$ then $AC\succeq0$.

**Proof.** The coordinates multiply, $A_\pm C_\pm\ge0$, and an element with both coordinates non-negative is in $\mathcal{C}_+$.

The order is compatible with the multiplication on the positive cone, which is the statement that the cone is closed under multiplication. It is not compatible with the whole ring: the product of two elements of negative norm has positive norm, so the sign of the order is not multiplicative on the units.

## The Unitary Group

### The Group of Norm-One Elements

**Definition.** The **unitary group** of the module of rank one is

$$
U_1=\{u : H(u,u)=1\}=\{u : N(u)=1\} .
$$

**Theorem.** $U_1$ is a group under the plain product, isomorphic to $\mathbb{R}^\times$ by $u\mapsto u_+$.

**Proof.** $N(uv)=N(u)N(v)$, so the set is closed under multiplication; $N(1)=1$; and $N(u)=1$ gives $u^{-1}=\bar u$ with $N(\bar u)=1$. In idempotent coordinates $N(u)=u_+u_-=1$, so $u_-=1/u_+$ and the map $u\mapsto u_+$ is a bijection onto $\mathbb{R}^\times$ carrying the product to the product.

### The Two Branches

The hyperbola $a^2-b^2=1$ has two branches, $a>0$ and $a<0$, and they are the two components of $U_1$: the identity component $\{u_+=u_->0\}$ and its opposite. Each branch is a copy of the real line,

$$
u=(\cosh t,\sinh t)\quad\text{or}\quad u=-(\cosh t,\sinh t), \qquad t\in\mathbb{R},
$$

and the second branch is $(-1)$ times the first. The group is therefore $\mathbb{Z}/2\times\mathbb{R}$ as a space and $\mathbb{R}^\times$ as a group: two branches, one identity component, no period.

### The Action

The group acts on the plane by multiplication, and it preserves the norm and the cone, hence the order. On a level set of non-zero norm it is transitive on each branch; on the level set of norm one it is transitive on the whole set, since $u\cdot1=u$. The identity component preserves each branch and acts on it simply transitively, which is the statement that the hyperbolic angle is a coordinate of the branch. The element $-1$ of the group exchanges the two branches and reverses the order, and the reflections of the plane add the other two components of the isometry group of $g$.

## The Comparison with the Complex Case

### The Ray There

Over $\mathbb{C}$ the Hermitian square $A\bar A$ takes its values in the ray $\mathbb{R}_{\ge0}$, and the set of elements with non-negative square is the whole plane. There is no cone, no component and no boundary: the analogue of the double cone is the ray of the values, and the analogue of its two components does not exist.

### The Compact Group There

Over $\mathbb{C}$ the unitary group of the module of rank one is the circle $S^1$, compact, connected, with a period. Here it is $\mathbb{R}^\times$, disconnected, with two branches and no period. The difference is the signature: a definite form of signature $(2,0)$ gives a compact group, an indefinite one of signature $(1,1)$ gives a non-compact group with two components. The compact part of the isometry group of $g$ is $\{\pm\mathrm{id},\pm\bar\cdot\}$, of order four, which is the shadow of the circle that the definite case has in full.

### The Isotropic Lines There

Over $\mathbb{C}$ no non-zero vector is isotropic, and no line is totally isotropic. Here two lines are, and they are the boundary of the cone. This is the sharpest form of the difference: a definite form has no isotropic vector, an indefinite form of signature $(1,1)$ has two isotropic lines, and everything in this article, the cone, the reversed inequalities, the order and the two branches, is a consequence of those two lines.

## Summary

The Hermitian form $H(A,C)=A\bar C$ is indefinite of signature $(1,1)$, and the set where it is non-negative is the double cone $a^2\ge b^2$, with two components, the interior of units and the boundary of zero divisors. The form vanishes on both idempotent lines, which are therefore totally isotropic; the adjoint axiom holds and positivity fails, so the algebra is a $\ast$-algebra with a Hermitian form and not a Hilbert algebra.

Indefiniteness reverses the two inequalities. On one component of the cone, $g(A,C)\ge\sqrt{N(A)N(C)}$ and $\sqrt{N(A+C)}\ge\sqrt{N(A)}+\sqrt{N(C)}$, with equality on the rays and failure across components. The forward cone defines a partial order, the product of the two orders of the idempotent coordinates, not total because the two idempotents are incomparable, and compatible with the multiplication on the positive cone.

The unitary group of rank one is the group of norm-one elements, isomorphic to $\mathbb{R}^\times$, with the two branches of the hyperbola and no period. Over $\mathbb{C}$ the Hermitian square takes its values in the ray $\mathbb{R}_{\ge0}$, the unitary group is the circle and no vector is isotropic; the cone, the reversed inequalities, the order and the second branch are all consequences of the two isotropic lines of the split case.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $H(A,C)=A\bar C$ | The Hermitian form of signature $(1,1)$ |
| $\mathcal{C}=\{N\ge0\}$ | The double cone, the cone of $H$-positivity |
| $\mathcal{C}_\pm$ | The forward and the backward cone, the two components |
| $g(A,C)=ac-bd$ | The polar form, the real part of $H$ |
| $N(Q)=Q_+Q_-=a^2-b^2$ | The split norm |
| $\mathbb{R}\Pi_\pm$ | The two totally isotropic lines, the boundary of the cone |
| $\succeq$ | The order $A-C\in\mathcal{C}_+$ |
| $U_1=\{N=1\}$ | The unitary group of rank one, $\cong\mathbb{R}^\times$ |
| $\{\pm\mathrm{id},\pm\bar\cdot\}$ | The compact part of the isometry group of $g$ |

## Further Reading

- János Bognár, *Indefinite Inner Product Spaces* (Springer, Ergebnisse der Mathematik 78, 1974), for indefinite forms, isotropic subspaces and the reversed inequalities.
- Barrett O'Neill, *Semi-Riemannian Geometry with Applications to Relativity* (Academic Press, 1983), for causal vectors, the reverse triangle inequality and the two time orientations.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for isotropic vectors, hyperbolic planes and the classification of forms in dimension two.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, Colloquium Publications 44, 1998), for the adjoint axiom and algebras with a Hermitian form.
- John B. Conway, *A Course in Functional Analysis* (Springer, Graduate Texts in Mathematics 96, 2nd ed. 1990), for the Cauchy-Schwarz inequality, its equality case and the positive definite setting it requires.
