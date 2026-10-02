# __The Commutator Operator__

## Introduction

The product of an algebra is not commutative in general, and the amount by which it fails to be is measured by the **commutator**

$$
[a, b] = a b - b a .
$$

Fix the first argument and let the second vary: the commutator becomes an operator on the algebra, the **adjoint action**

$$
\mathrm{ad}_a : A \longrightarrow A, \qquad \mathrm{ad}_a(x) = [a, x].
$$

This operator is the subject of the present article. It is the antisymmetrisation of the left and the right multiplication, $\mathrm{ad}_a = L(a) - R(a)$; it is a derivation of the algebra; and the assignment $a \mapsto \mathrm{ad}_a$ is a homomorphism of Lie algebras whose kernel is the centre. Each of these three statements is a reading of the same element in the operator space of $A$, and the article develops the three together.

Throughout, $k$ is a field and $A$ is a unital associative $k$-algebra, with $n = \dim_k A$ when $A$ is finite-dimensional. The operators live in $\operatorname{End}_k(A)$; the left and the right multiplications $L(a)$, $R(a)$ are those of *The Operators on an Algebra* and are treated in detail in *Left and Right Multiplication*, and the derivations are the derivations of *Automorphisms and Derivations of Algebras*. The first section collects the identities of the bracket, the second introduces the operator, the third computes its commutators with the multiplication operators, the fourth gathers the derivation theory of the operator under one heading, and the last two treat the antisymmetrisation and the examples.

## The Commutator Bracket

### Definition and Identities

**Definition.** For $a, b \in A$ the **commutator**, or **bracket**, of $a$ and $b$ is

$$
[a, b] = a b - b a .
$$

The bracket is $k$-bilinear in its two arguments, and it is **antisymmetric**,

$$
[a, b] = -[b, a], \qquad [a, a] = 0 ,
$$

the second identity following from the first when $2$ is invertible and holding in every case as written. It satisfies the **Jacobi identity**

$$
[a, [b, c]] + [b, [c, a]] + [c, [a, b]] = 0 .
$$

*Proof of the Jacobi identity.* Expand each term and collect. The first commutator is $a(bc) - a(cb) - (bc)a + (cb)a$, and the sum of the three cyclic terms is the sum of twelve monomials; each of the twelve occurs twice with opposite signs — the monomial $abc$ occurs as $a(bc)$ in the first term and as $-(ab)c + ...$: the systematic statement is that each ordered product of the three letters $a, b, c$ appears once from each of the two bracketings of the triple, with the two signs opposite. Since the product is associative and the twelve ordered products are in bijection with the six permutations of the three letters taken together with the three choices of which letter is bracketed first, the total is zero.

The two identities say that $A$, equipped with the bracket in place of the product, is a **Lie algebra**. It is written $A^{(-)}$ when the product and the bracket are both in play, and it is called the **commutator algebra** of $A$; this is the construction that passes from the associative theory to the Lie theory of *Lie Algebras*, and it is the source of the examples of that article.

**Proposition.** For every $a \in A$ the map $x \mapsto [a, x]$ is $k$-linear and satisfies the **Leibniz rule**

$$
[a, xy] = [a, x]\, y + x\, [a, y] .
$$

*Proof.* Linear in $x$ because the product is; and $a(xy) - (xy)a = (ax - xa)y + x(ay - ya)$ by associativity, the cross terms $axy$ cancelling after the expansion.

The Leibniz rule says that the map is a **derivation** of $A$. The derivations of an algebra form a Lie algebra under the commutator of operators, and the map $a \mapsto [a, \cdot]$ is the source of the **inner** ones; the general theory of this passage is in *Automorphisms and Derivations of Algebras*, and the present article uses it in the fourth section.

### The Antisymmetrisation

The commutator is the antisymmetrised product, and it is also the antisymmetrisation of the two one-sided multiplications.

**Proposition.** For all $a, x \in A$,

$$
[a, x] = L(a)(x) - R(a)(x) = (L(a) - R(a))(x),
$$

so that as operators $\mathrm{ad}_a = L(a) - R(a)$; and the antisymmetrisation of the sandwich is the bracket,

$$
[T_{a,b} - T_{b,a}](1) = ab - ba = [a, b].
$$

*Proof.* The first identity is the definition of the two multiplications. For the second, $T_{a,b}(1) = ab$ by the elementary proposition of *The Sandwich Operator on an Algebra*, and similarly $T_{b,a}(1) = ba$.

The operator identity $\mathrm{ad}_a = L(a) - R(a)$ is the reason the commutator belongs to the operator layer: the bracket is not a new operation on the algebra but the difference of the two operators that the product already provides. Its vanishing is the commutativity of $a$ with everything, and its size measures the difference between the two sides.

## The Adjoint Action

### The Operator

**Definition.** For $a \in A$ the **adjoint action**, or **inner multiplication operator**, determined by $a$ is the operator

$$
\mathrm{ad}_a \in \operatorname{End}_k(A), \qquad \mathrm{ad}_a(x) = [a, x] = ax - xa .
$$

**Proposition.** The assignment

$$
\mathrm{ad} : A \longrightarrow \operatorname{End}_k(A), \qquad a \longmapsto \mathrm{ad}_a
$$

is $k$-linear, and it satisfies

$$
[\mathrm{ad}_a, \mathrm{ad}_b] = \mathrm{ad}_{[a,b]},
$$

where the bracket on the left is the commutator of operators in $\operatorname{End}_k(A)$ and that on the right is the bracket of $A$; hence $\mathrm{ad}$ is a homomorphism of Lie algebras from the commutator algebra $A^{(-)}$ into $\operatorname{End}_k(A)$.

*Proof.* Linearity in $a$ is the bilinearity of the bracket. For the bracket identity, compute on a general $x$:

$$
\mathrm{ad}_a\mathrm{ad}_b(x) = [a, [b, x]], \qquad \mathrm{ad}_b\mathrm{ad}_a(x) = [b, [a, x]],
$$

so the difference is $[a,[b,x]] - [b,[a,x]]$, which the Jacobi identity rewrites as $[[a,b],x] = \mathrm{ad}_{[a,b]}(x)$.

### The Kernel and the Centraliser

**Proposition.** The kernel of $\mathrm{ad}$ is the **centre** $Z(A) = \{a : ax = xa \text{ for all } x\}$, and for a single element $a$ the kernel of $\mathrm{ad}_a$ is the **centraliser**

$$
C_A(a) = \{x \in A : ax = xa\}.
$$

Hence $\mathrm{ad}$ is injective exactly when $A$ is commutative, and in every case it induces an isomorphism of Lie algebras

$$
A^{(-)}/Z(A) \;\cong\; \operatorname{InnDer}_k(A)
$$

onto the space of inner derivations of *Automorphisms and Derivations of Algebras*.

*Proof.* The kernel of $\mathrm{ad}_a$ consists of the $x$ with $ax = xa$, which is the centraliser; the kernel of $\mathrm{ad}$ is the intersection of the centralisers over all $a$, which is the set of elements commuting with everything, the centre. The first isomorphism theorem for Lie algebras then gives the last display, the inner derivations being by definition the image of $\mathrm{ad}$.

The centre is thus exactly the part of the algebra that the operator $\mathrm{ad}$ cannot see, and this is the operator form of the fact — stated for rings in *Centre, Units, Zero Divisors and Division Algebras* — that the centre is the intersection of the centralisers. When $A$ is a field, $A^{(-)}$ is the zero Lie algebra and $\mathrm{ad} = 0$; when $A = M_n(k)$ the centre is the scalars, so $\operatorname{InnDer}_k(M_n(k))$ has dimension $n^2 - 1$.

### The Centraliser as an Operator Kernel

**Proposition.** For $a \in A$ the centraliser $C_A(a)$ is the kernel of $\mathrm{ad}_a$, hence a subalgebra of $A$ containing $a$ and the centre; and it is the whole of $A$ exactly when $a$ is central.

*Proof.* $C_A(a) = \ker \mathrm{ad}_a$ is a kernel of a linear map, so a subspace, and it is closed under the product because the Leibniz rule gives $[a, xy] = [a,x]y + x[a,y] = 0$ when both brackets vanish. It contains $a$ because $[a,a] = 0$, and it contains the centre because a central element commutes with everything. It is $A$ exactly when $\mathrm{ad}_a = 0$, that is when $a$ is central.

## The Commutators of the Multiplication Operators

The commutator of two multiplication operators is again a multiplication operator, and the two-sided case produces the associator. The following statements are the operator content of associativity, and they are the reason the present article sits beside *The Sandwich Operator on an Algebra*.

**Theorem.** For all $a, b \in A$,

$$
[L(a), L(b)] = L([a, b]), \qquad [R(a), R(b)] = R([b, a]) = -R([a, b]), \qquad [L(a), R(b)] = -A_{a,b},
$$

where $A_{a,b}(x) = (a, x, b)$ is the associator operator of *The Sandwich Operator on an Algebra*.

*Proof.* For the first, $L(a)L(b)(x) = a(bx) = (ab)x = L(ab)(x)$ and $L(b)L(a)(x) = L(ba)(x)$, so the difference is $L(ab - ba) = L([a,b])$. For the second, $R(a)R(b)(x) = (xb)a = x(ba) = R(ba)(x)$ and $R(b)R(a)(x) = R(ab)(x)$, so $[R(a),R(b)] = R(ba - ab) = R(-[a,b])$. The third is the theorem of the associator in *The Sandwich Operator on an Algebra*.

**Corollary.** The map $L$ is an injective homomorphism of Lie algebras $A^{(-)} \to \operatorname{End}_k(A)$, so $L(A)$ is a Lie subalgebra isomorphic to $A^{(-)}$; the map $-R$ is an injective homomorphism of Lie algebras, so $R(A)$ is a Lie subalgebra isomorphic to the opposite algebra $A^{(-)\mathrm{op}}$; and the two images commute exactly when every associator vanishes, that is for an associative algebra for all pairs.

*Proof.* The theorem shows that $L([a,b]) = [L(a),L(b)]$ and that $R([b,a]) = [R(a),R(b)]$, the second being the statement that $-R$ is a homomorphism; injectivity of $L$ and of $R$ is the statement, from *The Operators on an Algebra*, that $L(a) = 0$ or $R(a) = 0$ forces $a = 0$ in a unital algebra. Commutativity of the two images is the vanishing of $[L(a),R(b)] = -A_{a,b}$ for all $a$ and $b$, which by *The Sandwich Operator on an Algebra* is associativity.

The theorem is a compact restatement of the algebra: the left multiplications carry the product, the right multiplications carry the opposite product, and the failure of the two to commute is exactly the failure of associativity. In the associative case the two-sided picture is the one of *Left and Right Multiplication*, and the commutator of an $L$ with an $R$ vanishes, so the whole Lie algebra $L(A) + R(A)$ is the direct sum of two commuting copies.

## The Derivation Reading

**Proposition.** For every $a \in A$ the operator $\mathrm{ad}_a$ is a **derivation** of $A$, the map
$\mathrm{ad}: A^{(-)} \to \operatorname{Der}_k(A)$ is a homomorphism of Lie algebras with kernel $Z(A)$ and image the inner derivations, and the inner derivations form a Lie ideal of the Lie algebra of all derivations.

*Proof.* The Leibniz rule is the proposition of the first section, and the bracket identity is the proposition of the second; the kernel and the image are computed above. That the inner derivations form a Lie ideal follows from $[\delta, \mathrm{ad}_a] = \mathrm{ad}_{\delta(a)}$ for a derivation $\delta$, which is the statement that the adjoint action is the infinitesimal automorphism: $\delta[a,x] = [\delta a, x] + [a, \delta x]$, so $[\delta, \mathrm{ad}_a](x) = \delta[a,x] - [a, \delta x] = [\delta a, x] = \mathrm{ad}_{\delta(a)}(x)$.

**Remark.** The identity $[\delta, \mathrm{ad}_a] = \mathrm{ad}_{\delta(a)}$ says that the assignment $a \mapsto \mathrm{ad}_a$ is equivariant for the action of the derivation algebra, and it is the operator form of the fact that the inner derivations are the image of the algebra under a map that the outer derivations permute. When every derivation is inner — in particular for a central simple algebra, by *Central Simple Algebras and the Brauer Group* — the map $\mathrm{ad}$ is surjective and $\operatorname{Der}_k(A) \cong A^{(-)}/Z(A)$. This is the reading of the derivations of *Automorphisms and Derivations of Algebras* as operators on $A$, and its exponential $\exp(\mathrm{ad}_a)(x) = e^a x e^{-a}$ is the inner automorphism $\iota_{e^a}$ of that article.

## The Antisymmetric Sandwich

The commutator is the antisymmetrisation of the sandwich, and the antisymmetrisation is a systematic operation on the operator space.

**Proposition.** For all $a, b, c, d \in A$,

$$
T_{a,b}T_{c,d} - T_{c,d}T_{a,b} = T_{ac,\,db} - T_{ca,\,bd},
$$

and the right-hand side is a single sandwich exactly when the two index pairs agree, that is when $ac = ca$ and $db = bd$. In particular the antisymmetrisation vanishes for every pair on a commutative algebra.

*Proof.* The composition rule $T_{a,b}T_{c,d} = T_{ac,db}$ is the theorem of *The Sandwich Operator on an Algebra*, and subtracting the transposed product gives the display. The two terms on the right coincide exactly when the pairs $(ac, db)$ and $(ca, bd)$ are equal.

**Remark.** The commutator of two multiplications and the antisymmetrisation of the sandwich are the same operation seen twice, and the order that emerges from the two readings is the standard one of the theory of the enveloping algebra of the commutator algebra. The reading is not developed here; the tensor construction of the enveloping algebra belongs to *Tensor Products of Algebras*, and the Lie theory of the bracket to *Lie Algebras*.

## The Examples

### The Matrix Algebra

Let $A = M_n(k)$ and let $E_{ij}$ be the matrix units. Then

$$
[E_{ij}, E_{kl}] = \delta_{jk} E_{il} - \delta_{li} E_{kj},
$$

so that the bracket of two matrix units is a difference of two matrix units or vanishes, and the operator $\mathrm{ad}_{E_{ij}}$ sends $E_{kl}$ to $\delta_{jk}E_{il} - \delta_{li}E_{kj}$. The centre is $k \cdot I$, so $\operatorname{InnDer}_k(M_n(k))$ has dimension $n^2 - 1$; the elements $\mathrm{ad}_{E_{ij}}$ with $(i,j) \neq (n,n)$ span it, and $\mathrm{ad}$ is surjective because every derivation of $M_n(k)$ is inner.

### The Quaternions

Let $A = \mathbb{H}$ over $\mathbb{R}$. The centre is $\mathbb{R}$, and on the pure imaginary part the bracket of two elements is twice their cross product,

$$
[e_1, e_2] = 2e_3, \qquad [e_2, e_3] = 2e_1, \qquad [e_3, e_1] = 2e_2,
$$

with the labelling of the generators of *The Operators on an Algebra*. The operator $\mathrm{ad}_p$ for a pure imaginary $p$ is the derivation of $\mathbb{H}$ determined by $p$, and the correspondence $p \mapsto \mathrm{ad}_p$ is an isomorphism of Lie algebras $\mathbb{H}^{(-)}/\mathbb{R} \cong \mathbb{R}^3$ with the bracket twice the cross product; this is the reason the derivations of the quaternions form a three-dimensional Lie algebra.

### The Commutative Case

Let $A$ be commutative. Then $[a, b] = 0$ for all $a$ and $b$, the commutator algebra is the zero Lie algebra, the operator $\mathrm{ad}_a$ is the zero operator for every $a$, and the centre is all of $A$. The commutator operator is the measure of the failure of commutativity, and it is identically zero exactly on the commutative algebras; the algebras for which it is *not* identically zero are the noncommutative ones, and the size of its image is the size of the inner derivation algebra, $n - \dim_k Z(A)$.

## Summary

The commutator $[a,b] = ab - ba$ is a $k$-bilinear antisymmetric operation satisfying the Jacobi identity, so that $A^{(-)} = (A, [\cdot,\cdot])$ is a Lie algebra. Fixing the first argument gives the **adjoint action** $\mathrm{ad}_a(x) = [a,x]$, an operator equal to $L(a) - R(a)$ and equal, on the unit, to the antisymmetrised sandwich, $[a,b] = T_{a,b}(1) - T_{b,a}(1)$. The map $a \mapsto \mathrm{ad}_a$ is a homomorphism of Lie algebras $A^{(-)} \to \operatorname{End}_k(A)$ with $[\mathrm{ad}_a, \mathrm{ad}_b] = \mathrm{ad}_{[a,b]}$, whose kernel is the centre $Z(A)$ and whose image is the space of inner derivations; the kernel of a single $\mathrm{ad}_a$ is the centraliser $C_A(a)$, a subalgebra containing $a$ and the centre.

Each $\mathrm{ad}_a$ is a derivation, by the Leibniz rule $[a,xy] = [a,x]y + x[a,y]$, and the inner derivations form a Lie ideal of $\operatorname{Der}_k(A)$ on which the outer derivations act by $[\delta, \mathrm{ad}_a] = \mathrm{ad}_{\delta(a)}$. The commutators of the multiplication operators are $[L(a),L(b)] = L([a,b])$, $[R(a),R(b)] = -R([a,b])$ and $[L(a),R(b)] = -A_{a,b}$, the last being the associator; the left and the right multiplication spaces therefore commute exactly when the product is associative, and the two-sided operator is the sandwich of *The Sandwich Operator on an Algebra*. For $M_n(k)$ the bracket of two matrix units is a difference of two matrix units and the inner derivations have dimension $n^2 - 1$; for $\mathbb{H}$ the bracket on the pure imaginary part is twice the cross product and the derivations form a three-dimensional Lie algebra; and on a commutative algebra the operator is identically zero.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$ | the field of scalars |
| $A$ | a unital associative $k$-algebra |
| $n = \dim_k A$ | the dimension, when finite |
| $[a,b] = ab - ba$ | the commutator |
| $A^{(-)}$ | the commutator algebra, $A$ with the bracket |
| $\mathrm{ad}_a(x) = [a,x]$ | the adjoint action, or inner multiplication operator |
| $\mathrm{ad} : A \to \operatorname{End}_k(A)$ | the adjoint representation, $a \mapsto \mathrm{ad}_a$ |
| $Z(A)$ | the centre, the kernel of $\mathrm{ad}$ |
| $C_A(a)$ | the centraliser of $a$, the kernel of $\mathrm{ad}_a$ |
| $\operatorname{InnDer}_k(A)$ | the inner derivations, the image of $\mathrm{ad}$ |
| $[L(a),L(b)] = L([a,b])$ | the bracket of two left multiplications |
| $[L(a),R(b)] = -A_{a,b}$ | the bracket of a left and a right multiplication |

## Further Reading

- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the commutator algebra of an associative algebra and its relation to the Lie theory.
- I. N. Herstein, *Noncommutative Rings* (Carus Mathematical Monographs 15, Mathematical Association of America, 1968), for the centraliser, the centre and inner derivations.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the multiplication algebra and the structure of the operator space.
- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for the adjoint representation and the structure of the inner derivation algebra.
- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, second edition, 1992), for the endomorphism ring and the centraliser of the regular module.
