
# __Two-Sided Operators on a Clifford Algebra__

## Introduction

Every operator used in the geometric layer of a Clifford algebra dresses an element of the algebra between two factors built from a single element, one on the left and one on the right. The reflection and the rotation of *The Clifford, Pin and Spin Groups with Signed Inner Conjugation* are the members of that family in which the right factor is the inverse. The other members are used elsewhere in the corpus, so the family is set up here once, with the properties that hold for all of its members, before any single member is singled out.

The family has five members, indexed by the right factor: the **inner conjugation** $x\,y\,x^{-1}$ and the **signed inner conjugation** $\alpha(x)\,y\,x^{-1}$, both defined on the units; the **reversion sandwich** $x\,y\,x^{r}$ and the **conjugation sandwich** $x\,y\,x^{\natural}$, both defined on the whole algebra; and the **Hermitian sandwich** $x\,y\,x^{\dagger}$, defined when the base carries an involution. The first two are the members used by the groups, the middle two need no invertibility, and the last belongs to the involutive theory.

The Clifford algebra, the fundamental relation and the parity grading are from *Clifford Algebras*; the grade involution $\alpha$, reversion $x^{r}$ and Clifford conjugation $x^{\natural}=\alpha(x^{r})$ are from the same entry and from *Clifford Algebras in Finite Dimensions*; the Clifford group $\Gamma(V,q)$, the Clifford norm $N(x)=x x^{\natural}$ and the signed inner conjugation action are from *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*; the dagger, its involution of the base and the Hermitian sandwich are from *Hilbert Algebras*. Nothing owned by those entries is re-derived. The base is a field $F$ of characteristic not $2$, with $q$ a non-degenerate quadratic form on the finite-dimensional space $V$ and $B$ its polar form.

## The General Operator

### Definition

**Definition.** Let $\theta$ be an automorphism of $\mathrm{Cl}(V,q)$ and let $c$ be an anti-automorphism, so that $c(xz)=c(z)c(x)$ and $c(1)=1$. For $x\in\mathrm{Cl}(V,q)$ the **two-sided operator** attached to the pair $(\theta,c)$ is the map

$$
\Phi^{\theta,c}_x:\mathrm{Cl}(V,q)\longrightarrow\mathrm{Cl}(V,q),\qquad \Phi^{\theta,c}_x(y)=\theta(x)\,y\,c(x).
$$

The left factor carries the element and the right factor carries its conjugate. The pairing of the two factors is what makes the family closed under composition.

**Remark.** Let $L_a(y)=ay$ and $R_b(y)=yb$ be left and right multiplication. These commute, and

$$
\Phi^{\theta,c}_x=L_{\theta(x)}\circ R_{c(x)}.
$$

Every member of the family is thus the product of a left translation and a right translation, and each is an $F$-linear endomorphism of the algebra.

### Multiplicativity

**Proposition.** Let $\theta$ be an automorphism and $c$ an anti-automorphism. Then $\Phi^{\theta,c}_{xz}=\Phi^{\theta,c}_x\circ\Phi^{\theta,c}_z$ for all $x,z\in\mathrm{Cl}(V,q)$.

**Proof.** Evaluating the composition on $y$ and using the two defining properties of the pair,

$$
\Phi^{\theta,c}_x\bigl(\Phi^{\theta,c}_z(y)\bigr)=\theta(x)\bigl(\theta(z)\,y\,c(z)\bigr)c(x)=\theta(xz)\,y\,\bigl(c(z)c(x)\bigr)=\theta(xz)\,y\,c(xz).
$$

**Remark.** The assignment $x\mapsto\Phi^{\theta,c}_x$ is a homomorphism from the multiplicative monoid of $\mathrm{Cl}(V,q)$ to the endomorphisms of $\mathrm{Cl}(V,q)$. When the right factor is the inverse the assignment is defined on the units and is a homomorphism of the unit group. It is the multiplicativity that lets a composite of two operators be read off from the product of the two elements: it is why the product of two reflections is computed from the product of the two reflecting vectors, and why the image of the unit group is a group of isometries.

### The Value at the Unit

The members are told apart by their value on the algebra unit and by their behaviour on the parity.

**Proposition.** For every $x$ one has $\Phi^{\theta,c}_x(1)=\theta(x)\,c(x)$. In particular, for the members of the family,

| member | $\Phi_x(1)$ |
|---|---|
| inner conjugation | $1$ |
| signed inner conjugation | $+1$ on $\mathrm{Cl}^0$, $-1$ on $\mathrm{Cl}^1$ |
| reversion sandwich | $x\,x^{r}$ |
| conjugation sandwich | $x\,x^{\natural}=N(x)$ |

**Proof.** Immediate from the definition, since $1$ is the identity and $c(1)=1$; for the signed inner conjugation $\alpha(x)x^{-1}$ equals $x\,x^{-1}=1$ when $x$ is even and $-x\,x^{-1}=-1$ when $x$ is odd; for the conjugation sandwich $x\,x^{\natural}$ is the Clifford norm.

**Remark.** The inner conjugation is the only member that fixes the unit identically. The signed inner conjugation fixes it on the even part and negates it on the odd part, which is the same parity sign that distinguishes the two actions of *Versors, Rotors and the Sandwich Action with Signed Inner Conjugation*. The anti-involution sandwiches return an element that measures the size of $x$: reversion returns $x\,x^{r}$ and Clifford conjugation returns the Clifford norm.

### The Parity

**Proposition.** Each member of the family preserves the parity grading: $\Phi^{\theta,c}_x(\mathrm{Cl}^0)\subseteq\mathrm{Cl}^0$ and $\Phi^{\theta,c}_x(\mathrm{Cl}^1)\subseteq\mathrm{Cl}^1$.

**Proof.** The maps $\mathrm{id}$ and $\alpha$ preserve the grading, and so do the anti-involutions $r$ and $\bar\cdot$ because their signs on a blade depend only on the degree. A product of two factors of the same parity is even.

## The Members of the Family

### The Table

The family is indexed by the right factor, the left factor being the element itself except in the graded case, where it is its image under the grade involution.

| name | left factor | right factor | operator | defined for |
|---|---|---|---|---|
| inner conjugation | $x$ | $x^{-1}$ | $x\,y\,x^{-1}$ | the units |
| signed inner conjugation | $\alpha(x)$ | $x^{-1}$ | $\alpha(x)\,y\,x^{-1}$ | the units |
| reversion sandwich | $x$ | $x^{r}$ | $x\,y\,x^{r}$ | every $x$ |
| conjugation sandwich | $x$ | $x^{\natural}$ | $x\,y\,x^{\natural}$ | every $x$ |
| Hermitian sandwich | $x$ | $x^{\dagger}$ | $x\,y\,x^{\dagger}$ | every $x$ |

The right factors of the last three rows are the standard anti-involutions of the Clifford algebra, and the table carries the first structural fact: invertibility is required by the inverse alone. The first two operators are defined only where the inverse exists, that is on the unit group; the other three are defined on the whole algebra.

### The Inverse Sandwiches

The two members with the inverse to the right are the ones that act on the quadratic space by isometries.

The **inner conjugation** $y\mapsto x\,y\,x^{-1}$ is defined on the unit group and is the conjugation by $x$. On the even units it acts on the vectors as a rotation, and on the whole algebra it is the inner automorphism attached to $x$.

The **signed inner conjugation** $y\mapsto \alpha(x)\,y\,x^{-1}$ is defined on the unit group and differs from the inner conjugation by the grade involution in the left factor. On a vector $u$ with $q(u)\neq0$ it reproduces the reflection $\rho_u(v)=v-2B(v,u)q(u)^{-1}u=-uvu^{-1}$, and the elements $x$ for which it preserves the space of vectors are by definition the elements of the Clifford group $\Gamma(V,q)$.

**Remark.** The two differ exactly on the odd part: for even $x$ the factors $\alpha(x)$ and $x$ coincide, and the two operators agree. This is why a rotation, carried by an even element, is described by either one, while a reflection, carried by an odd element, requires the graded form.

**Remark (the general automorphism and the name).** The definition of the family allows an arbitrary automorphism $\theta$ as the left factor's map, and with the inverse to the right the general member is

$$
y\longmapsto \theta(x)\,y\,x^{-1},
$$

the **graded inner conjugation**. The inner conjugation is the case $\theta=\mathrm{id}$ and the signed inner conjugation is the case $\theta=\alpha$; the name *signed* records that $\alpha$ is the sign character, equal to $-1$ on the odd part, and it is precisely that minus that makes an odd element give the reflection $\rho_u$ instead of its negative. The general member with an arbitrary $\theta$ is not used by the geometric layer, and the two cases above are the ones the corpus carries; the specialisation to $\theta=\alpha$ is the subject of *Two-Sided Operators on a Clifford Algebra with Signed Inner Conjugation*.

### The Anti-Involution Sandwiches

The two members with an anti-involution to the right are the ones that need no invertibility.

The **reversion sandwich** $y\mapsto x\,y\,x^{r}$ is defined for every $x$, because reversion is defined on the whole algebra. It fixes the vectors: on $u\in V$ one has $u^{r}=u$. It is the member whose right factor is the identity on $V$.

The **conjugation sandwich** $y\mapsto x\,y\,x^{\natural}$ is defined for every $x$. It negates the vectors, since $u^{\natural}=-u$ for $u\in V$, and its value on the unit is the Clifford norm, $\Phi(1)=x x^{\natural}=N(x)$.

**Proposition.** The reversion sandwich and the conjugation sandwich agree on the even part of the algebra and differ on the odd part by a sign. On the elements of the Clifford group the conjugation sandwich is the inner conjugation scaled by the norm.

**Proof.** For the first statement, $x^{\natural}=\alpha(x^{r})$ and $\alpha$ is the identity on $\mathrm{Cl}^0$; on an odd element $\alpha$ contributes the sign $-1$. The second statement is the scaling proposition of the next section.

### The Involutive Member

The **Hermitian sandwich** $y\mapsto x\,y\,x^{\dagger}$ has the dagger to the right. This is the one member that is not available in the general theory: the dagger requires an involution of the base, which is a structure the base need not carry. The member, its definition, its Hermitian forms and the unitary slice on which the dagger is the inverse are treated in *Hilbert Algebras*, and nothing of that theory is used here; with the trivial involution the member reduces to the conjugation sandwich.

## Preservation of the Quadratic Space

### The Condition

A two-sided operator acts on the whole algebra, and the ones that carry geometric information are those that send the subspace of vectors into itself,

$$
\Phi^{\theta,c}_x(V)\subseteq V.
$$

For the signed inner conjugation this condition is the definition of the Clifford group, and once it holds the restriction to $V$ is an isometry up to the scale that the Clifford norm measures.

### The Scaling by the Norm

**Proposition.** Let $x\in\Gamma(V,q)$ and let $N(x)=x x^{\natural}$ be its Clifford norm. Then $x^{\natural}=N(x)\,x^{-1}$ and

$$
x\,y\,x^{\natural}=N(x)\,\bigl(x\,y\,x^{-1}\bigr)
$$

for every $y\in\mathrm{Cl}(V,q)$. The conjugation sandwich on $\Gamma$ is thus the inner conjugation scaled by the norm.

**Proof.** The norm of an element of $\Gamma$ is a scalar, so $x x^{\natural}=N(x)$, and multiplication on the right by $x^{-1}$ gives $x^{\natural}=N(x)\,x^{-1}$. Substituting this expression for $x^{\natural}$ and moving the scalar $N(x)$ to the front gives the identity.

**Remark.** The scale separates two facts that the inverse sandwich carries at once. On the elements of $\Gamma$ with $N(x)=\pm1$ the conjugation sandwich and the inner conjugation coincide, the restriction to $V$ is an isometry, and the odd and the even elements give the reflections and the rotations. That is the content of *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*.

### The Scale Must Be a Scalar

Preservation of $V$ does not follow from the weaker requirement that the scale be central.

**Example.** In $\mathrm{Cl}_{3,0}$ the volume element $\omega=e_1e_2e_3$ is central, and for $x=1+\omega$ one has

$$
x x^{\natural}=2\omega,
$$

which is central and not a scalar, while $x\,e_1\,x^{\natural}=2e_2e_3$ is a bivector. Such an $x$ does not preserve $V$ and is not in the Clifford group. The scale must therefore be tested for being a scalar, and the scalar hypothesis on $N(x)$ for $x\in\Gamma$ is not a convenience.

## Worked Cases

### An Odd Element

Let $x=e_1+e_2$ in $\mathrm{Cl}_{3,0}$. Then $x$ is odd, $x^{r}=x$, $x^{\natural}=-x$, and

$$
N(x)=x x^{\natural}=-2, \qquad x^{-1}=\tfrac{1}{2}(e_1+e_2).
$$

The four defined members act on the vector $e_1$ as follows.

| member | $x\,e_1\,c(x)$ | $\Phi_x(1)$ |
|---|---|---|
| inner conjugation | $e_2$ | $1$ |
| signed inner conjugation | $-e_2$ | $-1$ |
| reversion sandwich | $2e_2$ | $2$ |
| conjugation sandwich | $-2e_2$ | $-2$ |

The two inverse sandwiches send $e_1$ to $\pm e_2$, which is the reflection in the line $x^{\perp}$ up to the sign that the twist supplies; the two anti-involution sandwiches send it to the same vector scaled by $\pm N(x)=\mp2$, in agreement with the scaling proposition. The value at the unit separates the two inverse members ($1$ and $-1$, the parity sign of the odd element) and the two anti-involution members ($2$ and $-2$, that is $x\,x^{r}$ and the norm).

### An Even Element

For the unit rotor $R=e_1e_2$ one has $N(R)=1$, so the norm-one slice applies: the inner conjugation, the reversion sandwich and the conjugation sandwich send $e_1$ to $-e_1$, all three agreeing, because $R^{r}=\bar R=R^{-1}$ on a norm-one even element. For the volume element $\omega=e_1e_2e_3$, which is even but has $N(\omega)=-1$, the reversion sandwich sends $e_1$ to $e_1$ while the conjugation sandwich sends it to $-e_1$; the two differ by the sign of the grade involution, as the proposition states.

## Summary

A **two-sided operator** on a Clifford algebra is the map $\Phi^{\theta,c}_x(y)=\theta(x)\,y\,c(x)$ attached to an automorphism $\theta$ and an anti-automorphism $c$. It is the product of a left translation and a right translation, it is $F$-linear in $y$, and it satisfies the composition law $\Phi_{xz}=\Phi_x\circ\Phi_z$, so that $x\mapsto\Phi_x$ is a homomorphism of the multiplicative monoid on the algebra and of the unit group on the units. Each member preserves the parity grading.

The family has five members, indexed by the right factor. The **inner conjugation** $x\,y\,x^{-1}$ and the **signed inner conjugation** $\alpha(x)\,y\,x^{-1}$ are defined on the units and are the members that act on the quadratic space by isometries; they agree on the even part and differ on the odd part, which is why a reflection needs the graded form while a rotation does not. The **reversion sandwich** $x\,y\,x^{r}$ and the **conjugation sandwich** $x\,y\,x^{\natural}$ are defined on the whole algebra, need no invertibility, fix and negate the vectors respectively, and agree on the even part; the value of the conjugation sandwich at the unit is the Clifford norm. The **Hermitian sandwich** $x\,y\,x^{\dagger}$ requires an involution of the base and belongs to *Hilbert Algebras*.

The members differ at the unit by a parity sign and a norm: the inner conjugation fixes $1$, the signed inner conjugation gives $\pm1$ according to parity, the reversion sandwich gives $x\,x^{r}$, and the conjugation sandwich gives $N(x)$. The operators that carry geometry are those with $\Phi_x(V)\subseteq V$, which for the signed inner conjugation is the defining condition of the Clifford group. On $\Gamma$ the conjugation sandwich is the inner conjugation scaled by the norm, $x\,y\,x^{\natural}=N(x)\,(x\,y\,x^{-1})$, so on the slice $N(x)=\pm1$ the two coincide and the odd and even elements give the reflections and the rotations. The scale must be a scalar and not merely central: in $\mathrm{Cl}_{3,0}$ the element $x=1+\omega$ has $x x^{\natural}=2\omega$ central and sends $e_1$ to the bivector $2e_2e_3$, so it is not in the Clifford group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\theta$ | Automorphism of $\mathrm{Cl}(V,q)$, the left factor's map |
| $c$ | Anti-automorphism, $c(xz)=c(z)c(x)$, $c(1)=1$ |
| $\Phi^{\theta,c}_x(y)=\theta(x)\,y\,c(x)$ | Two-sided operator |
| $L_a$, $R_b$ | Left and right translation, $\Phi^{\theta,c}_x=L_{\theta(x)}R_{c(x)}$ |
| $x\,y\,x^{-1}$ | Inner conjugation, defined on the units |
| $\alpha(x)\,y\,x^{-1}$ | Signed inner conjugation, defined on the units |
| $x\,y\,x^{r}$ | Reversion sandwich, defined for every $x$ |
| $x\,y\,x^{\natural}$ | Conjugation sandwich, defined for every $x$ |
| $x\,y\,x^{\dagger}$ | Hermitian sandwich, needs an involution of the base |
| $\Gamma(V,q)$ | Clifford group, the $x$ with $\Phi_x(V)\subseteq V$ |
| $N(x)=x x^{\natural}$ | Clifford norm, the value of the conjugation sandwich at $1$ |
| $\rho_u$ | Reflection in $u^{\perp}$, a value of the signed inner conjugation |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the sandwich operators and their action on vectors.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the signed inner conjugation and the generation of the orthogonal group.
- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras*, Collected Works vol. 2 (Springer, 1997), for the original algebraic construction of the graded action.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the signed inner conjugation action and the Clifford group in the geometric setting.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the anti-involutions of a Clifford algebra and the Hermitian member.
