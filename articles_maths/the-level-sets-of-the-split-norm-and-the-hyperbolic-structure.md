# __The Level Sets of the Split Norm and the Hyperbolic Structure__

## Introduction

The split norm $N(Q)=a^2-b^2$ is a quadratic form of signature $(1,1)$, and its level sets are the hyperbolas of the hyperbolic plane. This article describes them: the two branches of a positive level, the two of a negative one, the four components of a level of fixed magnitude, and the pair of lines at the value zero. It then reads the hyperbolic structure: the group of norm-one elements acts on the plane, transitively on each branch, so each branch is an orbit and the quotient of the plane by the group is the set of branches with the value of the norm as its coordinate. The null pair of lines is the common boundary, and the comparison with the circles of the complex plane closes the article.

The claim is that the level sets are the orbits, and that the orbit structure is what the indefiniteness produces. Over $\mathbb{C}$ the level sets of the modulus are circles, compact and connected, and each is a single orbit of the circle group; here each level set is a pair of non-compact branches and each branch is a single orbit of a group isomorphic to $\mathbb{R}^\times$. The two pictures are the two faces of the definiteness of the form.

The norm is *The Two Forms and the Two Algebraic Norms of the Split-Complex Space*; the cone and its two components are *The Hermitian Form, the Double Cone and the Reversed Cauchy-Schwarz Inequality*; the zero divisors that form the null set are *Zero Divisors of the Split-Complex Algebra*; the hyperbolic geometry of the plane is *Hyperbolic Rotations*.

## The Level Sets

### The Definition and the Two Signs

**Definition.** The **level set** of the split norm at the value $c$ is

$$
\Sigma_c=\{Q : N(Q)=c\}=\{a+jb : a^2-b^2=c\} .
$$

The set is empty for no value of $c$: every real $c$ is attained, since $N(a)=a^2$ runs over $\mathbb{R}_{\ge0}$ and $N(bj)=-b^2$ over $\mathbb{R}_{\le0}$.

### The Positive Level and Its Two Branches

For $c>0$ the level set is the hyperbola with vertices at $\pm\sqrt{c}$ on the real axis and asymptotes the two null lines,

$$
\Sigma_c=\{a=\pm\sqrt{c+b^2}\} ,
$$

and it has two branches, the right branch $a\ge\sqrt{c}$ and the left branch $a\le-\sqrt{c}$. Each branch is a copy of the real line, parametrised by $b$, and the two branches are exchanged by the conjugation and by the multiplication by $-1$.

### The Negative Level and Its Two Branches

For $c<0$ the level set is the hyperbola opened on the split imaginary axis,

$$
\Sigma_c=\{b=\pm\sqrt{a^2-c}\} ,
$$

with an upper branch $b\ge\sqrt{-c}$ and a lower branch $b\le-\sqrt{-c}$, each a copy of the real line parametrised by $a$. The two branches are exchanged by the conjugation.

### The Four Components of a Level of Fixed Magnitude

The two signs of the value give two hyperbolas, and each has two branches, so a level set of fixed **magnitude** $\lvert N\rvert=c\neq0$ has four components:

$$
\{N=c\}_+\cup\{N=c\}_-\cup\{N=-c\}_+\cup\{N=-c\}_- ,
$$

the two branches of the timelike hyperbola and the two branches of the spacelike one. A fixed non-zero value has two components; a fixed non-zero magnitude has four. The distinction is the one between a level set and the union of two level sets; it matters for the count of the components and it is the reason the article speaks of branches as well as of values.

## The Null Level and the Cone

### The Two Lines at Zero

At $c=0$ the level set degenerates into the pair of lines

$$
\Sigma_0=\{a^2=b^2\}=\mathbb{R}\Pi_+\cup\mathbb{R}\Pi_- ,
$$

the two isotropic lines of the form. They are the asymptotes of every hyperbola of the family, and the level sets of both signs approach them as $\lvert c\rvert\to0$.

### The Common Boundary

**Theorem.** The null pair of lines is the common boundary of all the level sets: every branch of $\Sigma_c$ for $c>0$ has the two rays $\mathbb{R}_{>0}\Pi_\pm$ as its asymptotic boundary, and every branch of $\Sigma_c$ for $c<0$ has the two rays $\mathbb{R}\Pi_\pm$ likewise.

**Proof.** On the right branch of $\Sigma_c$ the coordinate $a=\sqrt{c+b^2}$ tends to $\lvert b\rvert$ as $\lvert b\rvert\to\infty$, so the branch approaches the two rays $b=\pm a$ without meeting them; the other branches are the same computation reflected.

The null lines are therefore the boundary of every level set and the set where the level sets of the two signs are separated. The cone of the form is the union of the level sets of the non-negative values, and its boundary is $\Sigma_0$; the exterior is the union of the negative ones.

## The Hyperbolic Rotations

### The Group

**Definition.** The **hyperbolic rotations** are the multiplications by the elements of norm one,

$$
X\mapsto uX, \qquad N(u)=1 ,
$$

with matrix $\begin{pmatrix}u_1&u_2\\u_2&u_1\end{pmatrix}$ and $u_1^2-u_2^2=1$.

**Proposition.** The hyperbolic rotations preserve the norm and the polar form, they form a group isomorphic to $\mathbb{R}^\times$, and the identity component is parametrised by the hyperbolic angle,

$$
u=(\cosh t,\sinh t), \qquad t\in\mathbb{R} .
$$

**Proof.** $N(uX)=N(u)N(X)=N(X)$, and the polar form is preserved because the quadratic form is. The parametrisation is the hyperbola $u_1^2-u_2^2=1$ with $u_1>0$, and the addition formula $\cosh(s+t)=\cosh s\cosh t+\sinh s\sinh t$ is the multiplication of the two elements.

### Transitivity on a Level Set

**Theorem.** The group acts transitively on each level set of non-zero value, and its identity component acts transitively on each branch of such a level set.

**Proof.** Let $A$ and $C$ have the same non-zero norm. Then $u=C/A$ is defined and $N(u)=N(C)/N(A)=1$, so $u$ is in the group and $uA=C$. When $A$ and $C$ lie on the same branch their idempotent coordinates have the same sign pattern, so $u_+=C_+/A_+>0$ and $u$ lies in the identity component; when they lie on opposite branches $u_+<0$ and $u$ lies in the other component.

The two branches of one level set are therefore one orbit, exchanged by the element $-1$ of the group, and the identity component preserves each branch and moves within it.

### The Orbit of One

**Theorem.** The level set of norm one is the orbit of $1$ under the group, $\Sigma_1=\{u\cdot1 : N(u)=1\}$.

**Proof.** $u\cdot1=u$, so the orbit of $1$ is the group itself, and the group is $\Sigma_1$ by definition.

The level set $\Sigma_1$ is therefore a group acting on itself by left multiplication, and its two branches are the two components of the group. The same holds for every non-zero value up to a scaling: $\Sigma_c=c\,\Sigma_1$ for $c>0$, and $\Sigma_c=\lvert c\rvert\,j\,\Sigma_1$ for $c<0$, since $N(j)=-1$.

### The Angle and the Absence of a Period

The parameter $t$ of the identity component is the hyperbolic angle, and it is a coordinate of the branch: each branch is a copy of $\mathbb{R}$ with $t$ as its coordinate. There is no period. Over $\mathbb{C}$ the corresponding parameter is an angle modulo $2\pi$, because the level set there is a circle; here it is an angle modulo nothing, because the level set is a line.

## The Quotient

### The Invariant

The norm is invariant under the group, and off zero it is a complete invariant: two elements of the same non-zero norm are in the same orbit. At zero it is not complete, and the refinement is the whole of the singular structure.

**Proposition.** The orbits of the group are the level sets $\Sigma_c$ for $c\neq0$, the two punctured null lines $\mathbb{R}^\times\Pi_+$ and $\mathbb{R}^\times\Pi_-$, and the origin.

**Proof.** Transitivity on a level set of non-zero value gives the first family. On the null set, $u\cdot t\Pi_+=(u_+t)\Pi_+$ and $u_+$ runs over $\mathbb{R}^\times$, so the orbit of $t\Pi_+$ is the whole punctured line; the two lines are not in one orbit, because a product of two null elements of different lines is zero; and the origin is fixed.

### The Quotient

The quotient of the plane by the group is the set of orbits, and it is the real line with the value zero replaced by three points: the two punctured null lines and the origin. Away from zero the norm is a coordinate of the quotient, one point per non-zero value; at zero the coordinate collapses and three orbits sit over it.

So the quotient is not a manifold, and the failure is exactly at the value of the norm that separates the units from the zero divisors. The norm is a complete invariant on the units and on nothing else, which is the quotient form of the statement that the zero divisors are where the ring's structure degenerates.

## The Comparison with the Complex Case

### The Circles

Over $\mathbb{C}$ the level sets of the modulus are circles: $\{A : A\bar A=r^2\}$ is the circle of radius $r$, one component, compact, and a single orbit of the circle group. Each circle is the orbit of $r$ under the unitary group. There is no second branch and no asymptote, and the level set at $r=0$ is the origin alone, not a pair of lines.

### Compactness and Periodicity

The circle is compact and the hyperbola is not, and the difference is the signature of the form: a definite form of signature $(2,0)$ has compact level sets, an indefinite form of signature $(1,1)$ has non-compact ones. The group acting is the compact $S^1$ there and the non-compact $\mathbb{R}^\times$ here, and the parameter has a period there and none here. The four components of a level of fixed magnitude here have no complex counterpart: over $\mathbb{C}$ the magnitude fixes the level set and the level set is connected.

### What the Two Pictures Have in Common

In both cases the level sets are the orbits of the group of norm-one elements and the norm is the invariant. The difference is in the shape of one orbit: a circle there, a branch of a hyperbola here. The whole of the hyperbolic structure is that one substitution, and everything else, the two branches, the asymptotes, the absence of a period, the non-compactness, follows from it.

## Summary

The level sets of the split norm are the hyperbolas $a^2-b^2=c$: two branches for $c>0$, two for $c<0$, and the pair of null lines at $c=0$. A level of fixed magnitude has four components, the two branches of each of the two signs, and the null pair of lines is the common boundary of all of them, the asymptotes of every hyperbola.

The hyperbolic rotations, the multiplications by elements of norm one, form a group isomorphic to $\mathbb{R}^\times$ whose identity component is parametrised by the hyperbolic angle with no period. The group acts transitively on each level set of non-zero value and its identity component on each branch, so the orbits are the non-zero level sets, the two punctured null lines and the origin, and the level set of norm one is the orbit of $1$. The quotient is the real line with three orbits over the value zero, and the norm is a complete invariant exactly on the units.

Over $\mathbb{C}$ the level sets are circles, compact, connected, one per value, and each a single orbit of the circle group. The split level sets are non-compact, in two branches, and their four components per magnitude have no complex counterpart; the difference is the signature of the form, and the whole of the hyperbolic structure is that difference.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Sigma_c=\{N=c\}$ | The level set of the split norm at the value $c$ |
| $a^2-b^2=c$ | The hyperbola, with the two null lines as asymptotes |
| $\Sigma_0=\mathbb{R}\Pi_+\cup\mathbb{R}\Pi_-$ | The null level, the common boundary |
| $c>0$, two branches | The timelike hyperbola, right and left |
| $c<0$, two branches | The spacelike hyperbola, upper and lower |
| four components | The two branches of $N=c$ and of $N=-c$ |
| $N(u)=1$ | The hyperbolic rotations, $\cong\mathbb{R}^\times$ |
| $(\cosh t,\sinh t)$ | The identity component, $t$ the hyperbolic angle |
| the branches | The components of the level sets; the orbits are the level sets themselves |

## Further Reading

- Barrett O'Neill, *Semi-Riemannian Geometry with Applications to Relativity* (Academic Press, 1983), for hyperboloids, causal structure and the level sets of a form of signature $(1,1)$.
- John Stillwell, *Geometry of Surfaces* (Springer, Universitext, 1992), for the hyperbolic plane, its hyperbolas and the hyperbolic angle.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for isotropic vectors, hyperbolas and the classification of forms in dimension two.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the level sets of the split norm and their asymptotes.
- János Bognár, *Indefinite Inner Product Spaces* (Springer, Ergebnisse der Mathematik 78, 1974), for the orbit structure of an indefinite form under its isometry group.
