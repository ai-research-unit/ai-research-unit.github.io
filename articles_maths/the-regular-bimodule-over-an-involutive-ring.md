# __The Regular Bimodule over an Involutive Ring__

## Introduction

An involution of a ring $A$ is an anti-automorphism of order two, and it is the same datum as an isomorphism $A \cong A^{\mathrm{op}}$. Carried to the regular bimodule it produces three structures: the twist that turns the left regular module into the right one, a symmetry of the regular bimodule with its swap through the involution, and a Hermitian form on the module with values in $A$ itself, whose isometries are the unitary elements. The left and the right regular modules, indistinguishable in general, become interchangeable, and the module over itself becomes a module with a form.

The article specialises *Modules over an Involutive Ring* to the case $M = A$: that article defines the twist $M^{\sigma}$, the dual module and the induced map on the endomorphisms for an arbitrary module, and this one reads the same three constructions on the regular object, where they acquire their ring-theoretic form. It assumes *Involutive Rings* for the definition, the fixed and the skew elements, and the opposite ring, and *The Regular Module and the Regular Bimodule* and *The Regular Representation as an Algebra of Operators* for the regular object and its operators. The forms with positivity, the Hilbert structures and the sesquilinear pairings on a general module are *Hilbert Algebras*, in Part II; here everything is algebraic and the form takes its values in $A$. The involutions of the biquaternions and their lattice are *Biquaternion Involution Lattice*, in Part VI.

Throughout, $A$ is a ring with $1 \neq 0$ and an involution $\sigma$, and $\sigma$ is written on the right of the argument or as the mark ${}^{*} = \sigma$ where no confusion arises. The fixed set is $A^{\sigma}$, the antisymmetric part is $A^{-} = \{x : \sigma(x) = -x\}$, and the left and right multiplications are $L_a(x) = ax$ and $R_a(x) = xa$. No trace, no positivity and no topology is used.

## The Twist of the Regular Module

### The twist of the left regular module

**Definition.** The twist of a left $A$-module $M$ is the same additive group with the right action $x \cdot a = \sigma(a)x$, written $M^{\sigma}$ (*Modules over an Involutive Ring*).

**Proposition.** The involution $\sigma$ is an isomorphism of right $A$-modules

$$
\sigma : ({}_AA)^{\sigma} \longrightarrow A_A , \qquad x \mapsto \sigma(x) ,
$$

where $({}_AA)^{\sigma}$ carries $x \cdot a = \sigma(a)x$ and $A_A$ carries $x \cdot a = xa$. Hence the twist of the left regular module is the right regular module up to the comparison $\sigma$, and this comparison is exactly the involution.

**Proof.** The map $\sigma$ is bijective, being an involution, and for the right actions $\sigma(x \cdot a) = \sigma(\sigma(a)x) = \sigma(x)\sigma(\sigma(a)) = \sigma(x)a = \sigma(x) \cdot a$. Additivity is the additivity of $\sigma$.

**Corollary (the commutative case).** If $A$ is commutative and $\sigma$ is any involution, the twisted action is $x \cdot a = \sigma(a)x = x\sigma(a)$, which is the ordinary right action read through $\sigma$; in particular for $\sigma$ the identity the twist fixes the regular bimodule, ${}_AA^{\sigma} = A_A$, and the real and the complex cases below are the two extremes.

### The involution is the symmetry of the bimodule

**Definition.** Let $\sigma$ be an involution of $A$. The **$\sigma$-swap** of the regular bimodule, written ${}^{\mathrm{sw}}{}_AA_A^{\sigma}$, is the same additive group with the left and the right actions interchanged and read through $\sigma$:

$$
a \cdot y = y\,\sigma(a), \qquad y \cdot b = \sigma(b)\,y .
$$

For the identity involution of a commutative ring the two actions are simply interchanged, and the $\sigma$-swap is the **swap** ${}^{\mathrm{sw}}{}_AA_A$, with $a \cdot x = xa$ and $x \cdot b = bx$. The involution is carried in the definition because over a noncommutative ring the two actions cannot be exchanged by themselves: the untwisted swap is not the target of $\sigma$.

**Proposition.** The involution $\sigma$ is an isomorphism of bimodules

$$
\sigma : {}_AA_A \longrightarrow {}^{\mathrm{sw}}{}_AA_A^{\sigma}, \qquad \sigma(axb) = \sigma(b)\sigma(x)\sigma(a) ,
$$

and conversely every bimodule isomorphism $\varphi : {}_AA_A \to {}^{\mathrm{sw}}{}_AA_A^{\sigma}$ is of the form $x \mapsto d\,\sigma(x)$ with $d$ a central unit; it is an anti-homomorphism, hence its own inverse when $\varphi(1) = 1$, precisely when $d = 1$. So an involution of $A$ is exactly a bimodule isomorphism of the regular bimodule with its $\sigma$-swap, normalised at the unit.

**Proof.** That $\sigma$ is bijective and additive is the definition of an involution. Inserting $\sigma$ into the target, $a \cdot \sigma(x) \cdot b = \bigl(\sigma(b)\sigma(x)\bigr)\sigma(a) = \sigma(b)\sigma(x)\sigma(a)$, which is the anti-multiplicativity applied to $axb$; so $\sigma$ intertwines the two structures — the left action with the swapped left action and the right action with the swapped right action. For the converse, let $\varphi : {}_AA_A \to {}^{\mathrm{sw}}{}_AA_A^{\sigma}$ be a bimodule isomorphism and put $d = \varphi(1)$. Left linearity gives $\varphi(a) = a \cdot \varphi(1) = \varphi(1)\sigma(a) = d\sigma(a)$, and right linearity gives $\varphi(a) = \varphi(1) \cdot a = \sigma(a)\varphi(1) = \sigma(a)d$; the two agree on every $a$ exactly when $d$ commutes with $\sigma(A) = A$, that is when $d$ is central, and $d$ is a unit because $\varphi$ is bijective. Then $\varphi(xy) = d\sigma(xy) = d\sigma(y)\sigma(x)$ while $\varphi(y)\varphi(x) = d\sigma(y)\,d\sigma(x) = d^2\sigma(y)\sigma(x)$, so $\varphi$ is an anti-homomorphism exactly when $d = 1$, and then it is the involution $\sigma$.

**Corollary.** An involution of $A$ is the same datum as an isomorphism $A \cong A^{\mathrm{op}}$, and the same datum as a bimodule isomorphism of the regular bimodule onto its $\sigma$-swap normalised at the unit: the involution, the opposite-ring isomorphism, and the symmetry of the regular bimodule are three names for one thing.

**Remark (why the swap must be twisted).** The plain swap is recovered from the $\sigma$-swap exactly when $\sigma = \mathrm{id}$, which forces $A$ commutative: for $\sigma \neq \mathrm{id}$ the untwisted swap is not the target of $\sigma$, as the matrix case of the worked examples shows — there $A = M_n(F)$ with $\sigma(X) = X^{*}$, and $a \cdot \sigma(x) \cdot b = \sigma(b)\sigma(x)\sigma(a)$ while the untwisted swap gives $b\,\sigma(x)\,a$, and the two differ whenever $b$ and $\sigma(x)$ fail to commute.

## A Hermitian Form on the Regular Module

### The sesquilinear forms

**Definition.** Let $M$ be a left $A$-module over a ring with involution $\sigma$. A map $h : M \times M \to A$ is **$\sigma$-sesquilinear** if it is additive in each variable and

$$
h(ax, y) = a\,h(x,y), \qquad h(x, ay) = h(x,y)\,\sigma(a) ;
$$

it is **Hermitian** if in addition $h(y,x) = \sigma\bigl(h(x,y)\bigr)$.

### The canonical form of the regular module

**Proposition.** On ${}_AA$ the formula

$$
h(x,y) = x\,\sigma(y)
$$

is a Hermitian $\sigma$-sesquilinear form with values in $A$, and it is non-degenerate: $h(x,y) = 0$ for all $y$ implies $x = 0$, and $h(x,y) = 0$ for all $x$ implies $y = 0$.

**Proof.** Additivity is the distributivity of $A$. For the two sesquilinearity laws, $h(ax,y) = ax\sigma(y) = a\,h(x,y)$ and $h(x,ay) = x\sigma(ay) = x\sigma(y)\sigma(a) = h(x,y)\sigma(a)$. Hermitianity is $\sigma(h(x,y)) = \sigma(x\sigma(y)) = \sigma(\sigma(y))\sigma(x) = y\sigma(x) = h(y,x)$, using $\sigma^2 = \mathrm{id}$. For non-degeneracy, $h(x,1) = x\sigma(1) = x$ and $h(1,y) = \sigma(y)$, so a vector killed on one side by every argument is killed at the unit and is zero.

**Remark (the two values of the form).** The form is left $A$-linear and right $\sigma$-semilinear, and it is not symmetric but Hermitian; when $A$ is commutative and $\sigma$ is the identity it is the plain product $h(x,y) = xy$, a symmetric bilinear form, and when $A$ is a field the regular form of the field is the ordinary product. Over a ring with a nontrivial involution the form is the algebraic core of the sesquilinear pairings of *Hilbert Algebras*, without their positivity.

### The associated quadratic form

**Definition.** The **associated quadratic form** of $h$ is $q(x) = h(x,x) = x\sigma(x)$.

**Proposition.** $q$ satisfies $q(ax) = a\,q(x)\,\sigma(a)$, and $q$ determines the Hermitian form by the polarisation identity

$$
h(x,y) + \sigma\bigl(h(y,x)\bigr) = q(x+y) - q(x) - q(y)
$$

whenever $2$ is invertible in $A$; for $A = M_n(F)$ over a field of characteristic not two this is the usual passage between the quadratic and the Hermitian form.

**Proof.** $q(ax) = ax\sigma(ax) = ax\sigma(x)\sigma(a) = aq(x)\sigma(a)$. For the polarisation, expand $q(x+y)$ and use $h(y,x) = \sigma(h(x,y))$, so that $h(x,y)+\sigma(h(y,x)) = 2h(x,y)$; the displayed identity is the expansion. The last statement is the matrix computation with $\sigma$ the transpose or the conjugate transpose.

### The unitary elements are the isometries

**Definition.** An element $u \in A$ is **unitary** when $u\sigma(u) = \sigma(u)u = 1$; the unitary elements form the **unitary group** $U(A)$ of the involutive ring, the group of *Involutive Rings*.

**Proposition.** The $A$-linear isometries of $h$ are exactly the right multiplications $R_u$ by the unitary elements, $u \in U(A)$; they form a group isomorphic to $U(A)$. A left multiplication $L_u$ is an isometry exactly when $u$ is a central unitary element.

**Proof.** The $A$-linear endomorphisms of ${}_AA$ are the right multiplications $R_b$, $\operatorname{End}_A({}_AA) \cong A^{\mathrm{op}}$, by *The Regular Module and the Regular Bimodule*. Now $h(xb,yb) = xb\,\sigma(yb) = xb\sigma(b)\sigma(y) = x\,b\sigma(b)\,\sigma(y)$, so $R_b$ preserves $h$ for all $x,y$ exactly when $b\sigma(b) = 1$, which for a unit $b$ is the unitary condition. For a left multiplication, $h(ux,uy) = u\,h(x,y)\,\sigma(u)$; preservation forces $u\sigma(u) = 1$ from $x = y = 1$, and then $uz\sigma(u) = z$ for every $z$ in the image of $h$, which is all of $A$ because $h(1,y) = \sigma(y)$; multiplying $uz\sigma(u) = z$ on the right by $u$ gives $uz = zu$, so $u$ is central.

**Corollary (the two readings).** The unitary elements of the involutive ring act on the regular module as the isometries of its canonical form, on the right, and the right regular representation carries the unitary group into the isometry group. A unitary element that is not central acts as an isometry through $R_u$ and not through $L_u$, so the two one-sided readings of the same element differ as soon as the ring is non-commutative.

## Examples

### The matrix algebra with the conjugate transpose

Let $F$ be a field with an involution, for instance $F = \mathbb{C}$ with complex conjugation, let $A = M_n(F)$, and let $\sigma(X) = \overline{X}^{\mathsf{T}} = X^{*}$ be the conjugate transpose. Then the symmetric elements are the Hermitian matrices and the skew elements the anti-Hermitian ones, the unitary elements are the matrices with $UU^{*} = 1$, and the canonical form is $h(X,Y) = XY^{*}$. Its $A$-linear isometries are the right multiplications by the unitary matrices, which is the natural right action of $U(n)$ on the space of matrices; the left multiplications by unitary matrices are isometries only for the scalars, since those are the central unitary elements. The form $h$ is the algebraic Hilbert–Schmidt form of the matrix algebra, and its positivity is Part II.

### The group algebra

Let $A = F[G]$ for a group $G$, with the involution $\sigma(g) = g^{-1}$ extended $F$-linearly, as in *Involutions of a Group Ring*. The symmetric elements are the group-ring elements fixed by the antipode, the skew elements those negated by it, the unitary elements are the $x$ with $x^{*}x = 1$, and these include the elements of $G$; the canonical form is $h(x,y) = x\sigma(y)$, and the right multiplications by the group elements are isometries. For $G$ finite and $F$ a field in which $|G|$ is invertible the form is the algebraic descendant of the standard orthogonality of the character table, whose positivity is Part II.

### The commutative case

If $A$ is commutative and $\sigma$ is the identity then $\sigma$ is the identity involution, the swap of the regular bimodule is the bimodule itself, the canonical form is the product $h(x,y) = xy$, symmetric and non-degenerate when $A$ is a domain, and the unitary elements are the involutions $u^2 = 1$; the $A$-linear isometries are the right multiplications by these elements, which here coincide with the left ones. The split-complex numbers and the dual numbers, whose algebras are *Split-Complex Algebra* and *Dual-Numbers Algebra*, are the two degenerate cases of the corpus, and both carry the identity involution with $A = A^{\sigma}$ and $A^{-} = 0$.

### The biquaternions

The biquaternion algebra $\mathbb{B}$ carries four natural involutions, the complex conjugation, the quaternion conjugation, the conjugate transpose and their product, and each gives its own twist, its own $\sigma$-swap isomorphism and its own Hermitian form on the regular bimodule. The lattice they form is *Biquaternion Involution Lattice*, in Part VI, where the same regular module is read through each of them; the present article supplies only the general construction.

## Summary

For a ring $A$ with an involution $\sigma$ the regular object acquires three structures. The twist of the left regular module is the right regular module up to the comparison $\sigma : ({}_AA)^{\sigma} \to A_A$, which is an isomorphism of right modules; the involution is a bimodule isomorphism of ${}_AA_A$ onto its $\sigma$-swap, $\sigma(axb) = \sigma(b)\sigma(x)\sigma(a)$, and conversely every bimodule isomorphism of the regular bimodule onto its $\sigma$-swap is $x \mapsto d\sigma(x)$ with $d$ a central unit, the involution itself being the normalised case $d = 1$; over a noncommutative ring the involution must be carried in the target, the plain swap being its commutative case. The regular module carries the canonical Hermitian $\sigma$-sesquilinear form $h(x,y) = x\sigma(y)$ with values in $A$, non-degenerate, with associated quadratic form $q(x) = x\sigma(x)$ and polarisation identity when $2$ is invertible. Its $A$-linear isometries are the right multiplications $R_u$ by the unitary elements $u\sigma(u) = 1$, forming the unitary group $U(A)$, while a left multiplication $L_u$ is an isometry only for a central unitary $u$. The matrix algebra with the conjugate transpose, the group algebra with $g^{*} = g^{-1}$ and the commutative ring with the identity involution are the three worked cases, and the positivity of the form is deferred to Part II.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma$, $A^{\sigma}$, $A^{-}$ | the involution, the symmetric and the skew elements |
| $M^{\sigma}$, $x \cdot a = \sigma(a)x$ | the twist of a left module |
| $\sigma : ({}_AA)^{\sigma} \to A_A$ | the twist of the regular left module is the right one |
| ${}^{\mathrm{sw}}{}_AA_A^{\sigma}$, $a \cdot y = y\sigma(a)$, $y \cdot b = \sigma(b)y$ | the $\sigma$-swap of the regular bimodule |
| ${}^{\mathrm{sw}}{}_AA_A$, $a \cdot x = xa$, $x \cdot b = bx$ | the plain swap, its commutative case |
| $\sigma(axb) = \sigma(b)\sigma(x)\sigma(a)$ | the involution is the bimodule $\sigma$-swap isomorphism |
| $\varphi(x) = d\,\sigma(x)$, $d$ a central unit | every bimodule $\sigma$-swap isomorphism, $d = 1$ normalised |
| $h(x,y) = x\sigma(y)$ | the canonical Hermitian form on ${}_AA$ |
| $h(ax,y) = ah(x,y)$, $h(x,ay) = h(x,y)\sigma(a)$ | $\sigma$-sesquilinearity |
| $h(y,x) = \sigma(h(x,y))$ | Hermitianity |
| $q(x) = x\sigma(x)$, $q(ax) = aq(x)\sigma(a)$ | the associated quadratic form |
| $U(A) = \{u : u\sigma(u) = 1\}$ | the unitary group |
| $R_u$ with $u \in U(A)$ | the $A$-linear isometries of $h$ |
| $L_u$ is an isometry $\iff u$ central unitary | the one-sided distinction |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for involutions, sesquilinear and Hermitian forms, and the unitary group.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the symmetric and skew elements and the structure of involutive rings.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society, 1956), for the regular module of a ring with involution and the bilinear forms on it.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for involutions, the forms they define and the unitary groups.
- Tsit-Yuen Lam, *Lectures on Modules and Rings* (Springer, 1999), for the regular module, its endomorphism ring and the sesquilinear forms over an involutive ring.
