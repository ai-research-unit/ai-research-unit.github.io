# __Units and the Unitary Elements__

## Introduction

A unit is an element with a two-sided inverse, and the invertible elements of an algebra form a group under the product. In an algebra with an involution a second kind of unit singles itself out: one whose inverse is its conjugate. These are the **unitary elements**, the algebraic counterpart of the elements that preserve a sesquilinear structure, and they are the group whose Lie algebra is carried by the skew-Hermitian elements.

Throughout, $A$ is an associative $R$-algebra with a unit $1$ and a $\varsigma$-semilinear involution $*$, so that $*$ is additive, $*^{2} = \mathrm{id}$, anti-multiplicative $(xy)^{*} = y^{*}x^{*}$, and $(\lambda x)^{*} = \varsigma(\lambda)x^{*}$. The derived operation $x \star y = xy^{*}$ of *Sesquilinear Algebras* makes $(A,\star)$ a sesquilinear algebra, and it is that structure which the unitary elements respect. The group of the units is written $A^{\times}$, and the Hermitian and the skew-Hermitian elements $H(A)$ and $S(A)$ are those of *Hermitian and Skew-Hermitian Elements*. Associativity is assumed from the start here, where *Sesquilinear Algebras* did not assume it, because the group structure of the units and the multiplicativity of the inner maps both need it.

What is added here: the unit and its Hermitian property, the definition of the unitary elements and their identification with the units whose inverse is the conjugate, the group structure, the stability under the involution and the inverse, the Hermitian unitary elements, the inner $*$-automorphisms that the unitaries induce, and the worked cases $M_n(\mathbb{C})$, $\mathbb{H}$, the commutative algebras and $\mathbb{B}$.

## The Unit

### The Unit is Hermitian

**Proposition.** The unit of $A$ is Hermitian: $1^{*} = 1$.

**Proof.** Since $1$ is a right unit, $1^{*}1 = 1^{*}$. Applying the involution and using that it is anti-multiplicative and of order two gives $(1^{*}1)^{*} = 1^{*}(1^{*})^{*} = 1^{*}1$, while the left hand side is also $(1^{*})^{*} = 1$. Hence $1^{*}1 = 1$, and combining this with $1^{*}1 = 1^{*}$ gives $1^{*} = 1$. $\square$

**Remark.** The unit is fixed by the involution, and the proof needs only the unit axiom, the anti-multiplicativity and $*^{2} = \mathrm{id}$. An idempotent is not fixed in the same way: in $R \times R$ with the involution that exchanges the two factors the element $(1,0)$ is a central idempotent, and its conjugate is $(0,1)$, so it is not Hermitian. What singles the unit out is that it is the unit.

**Remark.** The unit belongs to the underlying algebra, and it is not in general a unit of the derived operation. By *Sesquilinear Algebras* the element $1$ is always a right $\star$-unit, $x \star 1 = x1^{*} = x$, while a left $\star$-unit exists only when $* = \mathrm{id}$, and then $\star$ is the original product. The unit is therefore the unit of the algebra, and the sesquilinear structure is what the unitary elements preserve rather than what supplies the unit.

## The Unitary Elements

### Definition

**Definition.** An element $u \in A$ is **unitary** when

$$
u u^{*} = u^{*} u = 1 .
$$

The set of the unitary elements is written $U(A)$.

**Proposition.** An element is unitary if and only if it is a unit with $u^{*} = u^{-1}$. Equivalently $U(A) = \{ u \in A^{\times} : u^{-1} = u^{*} \}$, and in particular $U(A) \subseteq A^{\times}$.

**Proof.** If $u u^{*} = u^{*}u = 1$ then $u$ is invertible with two-sided inverse $u^{*}$, so $u \in A^{\times}$ and $u^{-1} = u^{*}$. Conversely if $u \in A^{\times}$ and $u^{-1} = u^{*}$ then $uu^{*} = uu^{-1} = 1$ and $u^{*}u = u^{-1}u = 1$. $\square$

**Remark.** The definition imposes both equations, and neither is redundant. In $M_n(\mathbb{C})$ they are equivalent, since a square matrix with a one-sided inverse has a two-sided one, and it is that equivalence which lets the unitary group there be defined by the single equation $uu^{*} = 1$. In a general algebra the two are separate conditions, and the involution exchanges the one on the left with the one on the right.

### The Group Structure

**Theorem.** $U(A)$ is a group under the product, it is a subgroup of $A^{\times}$, and it contains $1$.

**Proof.** The element $1$ is unitary because $1^{*} = 1$ and $11 = 1$. For $u, v \in U(A)$ the product $uv$ is a unit with $(uv)^{-1} = v^{-1}u^{-1} = v^{*}u^{*} = (uv)^{*}$, so $uv$ is unitary by the proposition, and the product in $U(A)$ is the product of $A$, which is associative. For $u \in U(A)$ the inverse $u^{-1} = u^{*}$ satisfies $(u^{-1})^{-1} = u = (u^{-1})^{*}$, since $(u^{*})^{*} = u$, so $u^{-1} \in U(A)$. Hence $U(A)$ is closed under the product and the inverse and contains $1$, and it is a subgroup of $A^{\times}$. $\square$

**Remark.** The proof uses the involution twice, once to exchange the two halves of the condition and once for the inverse, and both uses are instances of $(uv)^{*} = v^{*}u^{*}$ and $*^{2} = \mathrm{id}$. In a commutative algebra the condition collapses to the single equation $uu^{*} = 1$.

## Stability and Inner Automorphisms

### The Involution and the Inverse

**Proposition.** If $u$ is unitary then $u^{*}$ is unitary, and the restriction of the involution to $U(A)$ is the inversion map:

$$
u^{*} = u^{-1} \quad \text{for every } u \in U(A) .
$$

Consequently the restriction of $*$ to $U(A)$ is an involutive anti-automorphism of the group $U(A)$, and it is an automorphism exactly when $U(A)$ is abelian.

**Proof.** For $u \in U(A)$ one has $(u^{*})^{*} = u$, so $u^{*}(u^{*})^{*} = u^{*}u = 1$ and $(u^{*})^{*}u^{*} = uu^{*} = 1$; hence $u^{*} \in U(A)$. The identity $u^{*} = u^{-1}$ is the proposition above. The map $u \mapsto u^{*}$ is of order two, and on $U(A)$ it is inversion, which reverses the product; hence it is an anti-automorphism, and an anti-automorphism of a group is an automorphism exactly when the group is abelian. $\square$

**Definition.** A unitary element is **Hermitian unitary** when $u = u^{*}$.

**Proposition.** The Hermitian unitary elements are exactly the elements $u \in A$ with $u^{2} = 1$ and $u^{*} = u$; they form the set $U(A) \cap H(A)$, and every such $u$ satisfies $u = u^{-1}$.

**Proof.** If $u$ is Hermitian and unitary then $u^{2} = uu = uu^{*} = 1$. Conversely if $u^{2} = 1$ and $u = u^{*}$ then $uu^{*} = u^{2} = 1$ and $u^{*}u = u^{2} = 1$, so $u$ is unitary, and $u = u^{*}$ says it is Hermitian. The last statement is $u^{-1} = u^{*} = u$. $\square$

### Inner $*$-Automorphisms

**Proposition.** Let $u \in U(A)$. Then the map $\alpha_u : A \to A$ given by $\alpha_u(x) = uxu^{*}$ is a $*$-automorphism of $A$, with inverse $\alpha_{u^{*}} = \alpha_{u}^{-1}$. It carries $H(A)$ to $H(A)$ and $S(A)$ to $S(A)$.

**Proof.** The map is additive and multiplicative, since $\alpha_u(xy) = uxyu^{*} = (uxu^{*})(uyu^{*})$, and it is $R$-linear. It respects the involution, because

$$
\alpha_u(x)^{*} = (u x u^{*})^{*} = (u^{*})^{*} x^{*} u^{*} = u x^{*} u^{*} = \alpha_u(x^{*}) ,
$$

using $(uv)^{*} = v^{*}u^{*}$ and $*^{2} = \mathrm{id}$, and it fixes $1$ since $uu^{*} = 1$. Its inverse is $\alpha_{u^{*}}$, because $\alpha_{u^{*}}(\alpha_u(x)) = u^{*}uxu^{*}(u^{*})^{*} = x$. An element $h$ is Hermitian exactly when $h^{*} = h$, and then $\alpha_u(h)^{*} = \alpha_u(h^{*}) = \alpha_u(h)$, so $\alpha_u(h)$ is Hermitian; the same computation with the minus sign carries $S(A)$ to itself. $\square$

**Proposition.** If $u, v \in U(A)$ then $\alpha_u(v) = uvu^{*}$ is unitary, so each $\alpha_u$ restricts to an automorphism of the group $U(A)$.

**Proof.** Since $(uvu^{*})^{*} = uv^{*}u^{*}$, one has

$$
(uvu^{*})(uvu^{*})^{*} = uvu^{*}uv^{*}u^{*} = uvv^{*}u^{*} = uu^{*} = 1 ,
$$

using $u^{*}u = 1$ and $vv^{*} = 1$; the computation with the factors in the other order gives $(uvu^{*})^{*}(uvu^{*}) = 1$ as well, so $uvu^{*}$ is unitary. $\square$

**Remark.** The unitary elements act on the algebra by the inner $*$-automorphisms $x \mapsto uxu^{*}$, and the assignment $u \mapsto \alpha_u$ is a homomorphism of $U(A)$ into the $*$-automorphism group of $A$ whose kernel is the set of the central unitary elements, since $\alpha_u$ is the identity exactly when $u$ commutes with every element. The conjugation is the algebraic form of the change of basis under which the Hermitian elements are preserved, and it is the congruence $c \mapsto x^{*}cx$ of *Hermitian Squares and the Algebraic Positive Cone* taken at $x = u^{*}$, since $\alpha_u(c) = (u^{*})^{*}c\,u^{*}$; for a unitary $u$ that congruence is an automorphism, whereas for a general $x$ it is only additive.

**Remark.** The skew-Hermitian elements are the ones that generate the Lie structure attached to this group, the bracket of two of them being again skew-Hermitian, and they are the subject of *The Unitary Lie Algebra*.

## Worked Cases

### The Matrix Algebra

**Proposition.** Let $A = M_n(\mathbb{C})$ with the conjugate transpose. Then $U(A)$ is the unitary group $U(n)$: the complex matrices $u$ with $u u^{*} = u^{*}u = I$, equivalently $u^{-1} = u^{*}$. The Hermitian unitary elements are the unitary matrices that are Hermitian, equivalently the unitary involutions $u^{2} = I$.

**Proof.** This is the definition of $U(n)$ read in the algebra, and the Hermitian unitary elements are the fixed points of the involution inside $U(n)$, which by the proposition above are the unitary elements with $u^{2} = I$, that is the unitary involutions. $\square$

**Remark.** The unitary matrices are exactly the elements that preserve the pairing $\langle x, y \rangle = x^{*}y$ defined by the conjugate transpose, which is the precise sense in which the unitary elements preserve the sesquilinear structure: $u$ is unitary if and only if $\langle ux, uy \rangle = \langle x, y \rangle$ for all $x, y$, since

$$
\langle ux, uy \rangle = (ux)^{*}(uy) = x^{*}u^{*}uy .
$$

When $u^{*}u = I$ this is $x^{*}y$, and conversely the equality for all $x$ and $y$, read on the basis vectors, gives $(u^{*}u)_{ij} = \delta_{ij}$, that is $u^{*}u = I$; a square matrix with a one-sided inverse being invertible, $uu^{*} = I$ follows as well and $u$ is unitary.

### The Quaternions

**Proposition.** Let $A = \mathbb{H}$ over $R = \mathbb{R}$ with $*$ the quaternion conjugation. Then $\bar q q = q \bar q = \nu(q)1$, where $\nu(q)$ is the sum of the squares of the four coordinates of $q$, and $U(\mathbb{H})$ is the set of the unit quaternions, the elements with $\bar q q = 1$. This group is isomorphic to $\mathrm{SU}(2)$.

**Proof.** The conjugate satisfies $\bar q q = q\bar q = \nu(q)1$ by the multiplication table of the units, so $q^{*}q = qq^{*} = \nu(q)1$ and $q$ is unitary exactly when $\nu(q) = 1$. The unit quaternions are closed under the product because $\nu$ is multiplicative, and the identification with $\mathrm{SU}(2)$ is the isomorphism that sends $q = w + zj$, where $w$ and $z$ are the two complex coordinates of $q$ in the basis $1, j$, to the matrix

$$
\begin{pmatrix} w & z \\ -\bar z & \bar w \end{pmatrix} .
$$

This map is multiplicative and its determinant is $\nu(q)$, so it carries the unit quaternions onto the unitary matrices of determinant $1$, that is onto $\mathrm{SU}(2)$. $\square$

**Remark.** The two cases differ in what the units are. The algebra $\mathbb{H}$ is a division algebra, so every nonzero element is a unit, and every unit is a real multiple of a unitary element: for $q \neq 0$ one has $\nu(q) \neq 0$, and $q = \sqrt{\nu(q)}\,u$ with $u = q/\sqrt{\nu(q)}$ unitary. In $M_n(\mathbb{C})$ this fails, since an element equal to $\lambda u$ with $u$ unitary satisfies $(\lambda u)(\lambda u)^{*} = \lambda \varsigma(\lambda) I$, a multiple of the identity, and the diagonal matrix with entries $2$ and $1$ is not of that form.

### The Commutative Case

**Proposition.** If $A$ is commutative then $U(A) = \{ u : uu^{*} = 1 \}$, this group is abelian, and the involution restricts to the inversion, which is an automorphism of $U(A)$. In particular $A = \mathbb{C}$ with $*$ the conjugation gives $U(\mathbb{C}) = \{ u : u\bar u = 1 \}$.

**Proof.** In a commutative algebra $uu^{*} = u^{*}u$, so the two halves of the condition coincide and a single equation remains; the group is abelian because $A$ is, and an anti-automorphism of an abelian group is an automorphism. For $\mathbb{C}$ the product $u\bar u$ is the sum of the squares of the two coordinates in the basis $1, i$, so that $u\bar u = 1$ says $a^{2} + b^{2} = 1$ for $u = a + bi$. $\square$

### The Biquaternion Algebra

**Proposition.** Let $A = \mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ with $*$ the Hermitian conjugation, the composite of the quaternion conjugation and the conjugation of the coefficients. Then $U(\mathbb{B})$ consists of the elements $P$ with $PP^{*} = P^{*}P = 1$. Under the identification of $\mathbb{B}$ with $M_2(\mathbb{C})$ for which the Hermitian conjugation is the conjugate transpose, $U(\mathbb{B})$ is the unitary group $U(2)$.

**Proof.** The first statement is the definition read in $\mathbb{B}$. For the second, the identification carries $\mathbb{B}$ onto $M_2(\mathbb{C})$ as algebras with involution, the Hermitian conjugation being the composite of the quaternion conjugation and the conjugation of the coefficients, and this composite corresponds to the conjugate transpose of the matrix; the unitary elements are then the unitary $2 \times 2$ matrices. $\square$

**Remark.** The algebra $\mathbb{B}$ has zero divisors, so $U(\mathbb{B})$ is a proper part of the units: the element $2$ is invertible with inverse $\tfrac12$, and it is not unitary since $2 \cdot 2^{*} = 4$. The difference from the previous case is the difference between a division algebra and a full matrix algebra of size two over $\mathbb{C}$, which is what the identification with $M_2(\mathbb{C})$ makes visible.

## Summary

In an associative $R$-algebra with a unit $1$ and a $\varsigma$-semilinear involution $*$, the unit is Hermitian, $1^{*} = 1$, and it is a unit of the derived operation only as a right unit, since a left $\star$-unit exists exactly when $* = \mathrm{id}$. The unitary elements $U(A) = \{u : uu^{*} = u^{*}u = 1\}$ are exactly the units with $u^{*} = u^{-1}$, they form a group under the product containing $1$, and they are stable under the involution and the inverse, the involution restricting to the inversion, an involutive anti-automorphism of $U(A)$ that is an automorphism exactly when $U(A)$ is abelian. The Hermitian unitary elements are the elements with $u^{2} = 1$ and $u = u^{*}$, and every unitary $u$ induces the inner $*$-automorphism $x \mapsto uxu^{*}$, which preserves the Hermitian and the skew-Hermitian elements and restricts to an automorphism of the group $U(A)$. The worked cases are the unitary group $U(n)$ of $M_n(\mathbb{C})$ with the conjugate transpose, the unit quaternions of $\mathbb{H}$ with the quaternion conjugation, the elements with $uu^{*} = 1$ in a commutative algebra, which for $\mathbb{C}$ are those with $u\bar u = 1$, and the group $U(2)$ of the biquaternion algebra with the Hermitian conjugation.

## Summary of Notation

| symbol | meaning |
|---|---|
| $1^{*} = 1$ | the unit is Hermitian |
| $U(A) = \{u : uu^{*} = u^{*}u = 1\}$ | the unitary elements |
| $U(A) = \{u \in A^{\times} : u^{-1} = u^{*}\}$ | the unitaries among the units |
| $u^{*} = u^{-1}$ on $U(A)$ | the involution restricts to the inversion |
| $U(A) \cap H(A) = \{u : u^{2} = 1, u = u^{*}\}$ | the Hermitian unitary elements |
| $\alpha_u(x) = uxu^{*}$ | the inner $*$-automorphism induced by a unitary $u$ |
| $c \mapsto x^{*}cx$ at $x = u^{*}$ | the inner $*$-automorphism $\alpha_u$ as a congruence |
| $U(n)$, $\mathrm{SU}(2)$, $U(2)$ | the worked cases |

## Further Reading

- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the units, the Hermitian elements and the unitary elements of a ring with involution.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the unitary groups and the involutions that define them.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the Hermitian and the unitary elements that generate the Jordan and the Lie structures of an algebra with involution.
- Richard S. Pierce, *Associative Algebras* (Graduate Texts in Mathematics 88, Springer, 1982), for the group of units and the inner automorphisms of an associative algebra.
