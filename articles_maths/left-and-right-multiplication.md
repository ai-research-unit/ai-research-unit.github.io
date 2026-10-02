# __Left and Right Multiplication__

## Introduction

The product of an algebra is a bilinear map of two arguments, and fixing one argument turns it into a linear operator of the other. Fixing the first gives the **left multiplication** $L(a)$, fixing the second the **right multiplication** $R(a)$; together the two families are the two regular representations of the algebra acting on itself. They carry the whole structure of the algebra — its product, its unit, its centre and its opposite — and the whole of the present article is the reading of the algebra off these two families of operators.

The two families are not symmetric. The left multiplications compose in the order of the product, $L(a)L(b) = L(ab)$, so $L$ is a homomorphism; the right multiplications compose against it, $R(a)R(b) = R(ba)$, so $R$ is an anti-homomorphism, and its image is a copy of the opposite algebra. The two images therefore commute exactly when the product is associative, and their failure to do so is the associator. These three statements are the skeleton of the article.

Throughout, $k$ is a field and $A$ is a unital associative $k$-algebra, with $n = \dim_k A$ when $A$ is finite-dimensional. The operators live in $\operatorname{End}_k(A)$; the definitions and the first properties of $L$ and $R$ are in *The Operators on an Algebra*, the ambient theory of the operator space is that article and *Operator Algebras*, and the two-sided product of an $L$ with an $R$ is the sandwich of *The Sandwich Operator on an Algebra*.

## The One-Sided Multiplications

### Definition

**Definition.** For $a \in A$ the **left multiplication** by $a$ is the operator

$$
L(a) : A \to A, \qquad L(a)(x) = a x,
$$

and the **right multiplication** by $a$ is the operator

$$
R(a) : A \to A, \qquad R(a)(x) = x a .
$$

Both are $k$-linear, since the product is bilinear in each argument; both are $k$-linear in $a$, since the product is bilinear in the other argument as well. The assignments $L, R : A \to \operatorname{End}_k(A)$ are therefore $k$-linear maps from the algebra into its operator space.

### Injectivity

**Proposition.** If $A$ is unital, then $L$ and $R$ are injective, and more precisely

$$
\ker L = \ker R = 0, \qquad L(a)(1) = a, \qquad R(a)(1) = a .
$$

*Proof.* From $L(a) = 0$ one gets $a = a \cdot 1 = L(a)(1) = 0$, and from $R(a) = 0$ one gets $a = 1 \cdot a = R(a)(1) = 0$. The evaluations at the unit give the two displayed identities, which show that $a$ is recovered from either operator.

**Corollary.** The spaces of left and of right multiplications,

$$
L(A) = \{L(a) : a \in A\}, \qquad R(A) = \{R(a) : a \in A\},
$$

are subspaces of $\operatorname{End}_k(A)$ of dimension $n$ each, and $L : A \to L(A)$ and $R : A \to R(A)$ are isomorphisms of $k$-modules.

The two spaces are the first two rungs of the operator ladder of *The Operators on an Algebra*, and their internal structure is settled by the multiplicative rules below.

### The Two-Sided Product

The product of a left and a right multiplication is the sandwich, and its two bracketings agree exactly when the product is associative.

**Proposition.** For all $a, b \in A$ the composites $L(a)R(b)$ and $R(b)L(a)$ are the operators

$$
L(a)R(b)(x) = a x b, \qquad R(b)L(a)(x) = a x b
$$

with the same value on $x$, so that $L(a)R(b) = R(b)L(a) = T_{a,b}$, the sandwich of *The Sandwich Operator on an Algebra*.

*Proof.* $R(b)L(a)(x) = R(b)(ax) = (ax)b$ and $L(a)R(b)(x) = L(a)(xb) = a(xb)$; associativity makes the two equal.

This is the sense in which the left and the right multiplications commute in an associative algebra: the identity $L(a)R(b) = R(b)L(a)$ is exactly the associativity of the product read on the two operators, and it holds for every pair precisely when the algebra is associative.

## The Left Multiplications

### The Homomorphism

**Theorem.** For all $a, b \in A$,

$$
L(a)L(b) = L(ab), \qquad L(1) = \mathrm{id}_A .
$$

Hence $L : A \to \operatorname{End}_k(A)$ is a homomorphism of unital $k$-algebras, its image $L(A)$ is a subalgebra of $\operatorname{End}_k(A)$, and $L$ is an isomorphism of algebras $A \to L(A)$.

*Proof.* $L(a)L(b)(x) = L(a)(bx) = a(bx) = (ab)x = L(ab)(x)$, the middle equality being associativity; $L(1)(x) = x$. A unital algebra homomorphism is injective exactly when its kernel, an ideal, is zero, and the kernel is zero by the injectivity proposition; hence $A \cong L(A)$.

The image $L(A)$ is called the **left regular representation** of $A$; it is a copy of $A$ inside $\operatorname{End}_k(A)$, and the isomorphism $L$ carries the product of $A$ to the composition of operators. The algebra and its left regular representation are therefore the same algebra up to the naming of the elements, and every statement about $A$ has a left-regular reading.

### The Linear Operators

The left multiplications are not the whole of the operators that respect the module structure, and the difference is the point of the noncommutative case.

**Proposition.** An operator $M \in \operatorname{End}_k(A)$ commutes with every left multiplication, $M L(a) = L(a) M$ for all $a$, if and only if $M$ is a right multiplication, and the correspondence is a $k$-linear isomorphism

$$
\{M : ML(a) = L(a)M \text{ for all } a\} = R(A) \cong A^{\mathrm{op}} .
$$

*Proof.* This is the theorem of *The Operators on an Algebra* that the centraliser of $L(A)$ in $\operatorname{End}_k(A)$ is exactly $R(A)$, together with the identification of $R(A)$ with the opposite algebra given below.

The proposition is the operator form of the statement that the $A$-module endomorphisms of the regular module are the right multiplications: an operator that is $A$-linear for the left action on an arbitrary module need not be a right multiplication, but on the regular module the two conditions coincide. The asymmetry between the two sides of the algebra is thus visible as the asymmetry between the centraliser and the algebra itself.

## The Right Multiplications

### The Anti-Homomorphism

**Theorem.** For all $a, b \in A$,

$$
R(a)R(b) = R(ba), \qquad R(1) = \mathrm{id}_A .
$$

Hence $R$ is an anti-homomorphism of unital algebras, and it is an isomorphism of algebras

$$
R : A^{\mathrm{op}} \longrightarrow R(A), \qquad a \longmapsto R(a),
$$

from the opposite algebra of $A$ onto the subalgebra $R(A)$ of $\operatorname{End}_k(A)$.

*Proof.* $R(a)R(b)(x) = R(a)(xb) = (xb)a = x(ba) = R(ba)(x)$, the middle equality being associativity. The order of the factors is reversed, which is exactly the definition of a homomorphism on the opposite algebra; the map is bijective onto its image and preserves products in the reversed order, hence is an isomorphism $A^{\mathrm{op}} \to R(A)$.

The contrast with the left case is the whole content of the right regular representation: $L$ is a copy of $A$ and $R$ is a copy of $A^{\mathrm{op}}$. The two copies are isomorphic as algebras exactly when $A$ is commutative, and in general they are the two opposite algebras, which is the reason the right module theory of $A$ is the left module theory of $A^{\mathrm{op}}$.

### The Two Regular Representations

**Corollary.** The pair $(L, R)$ gives a homomorphism of algebras

$$
A \otimes_k A^{\mathrm{op}} \longrightarrow \operatorname{End}_k(A), \qquad a \otimes b \longmapsto L(a)R(b) = T_{a,b},
$$

whose image is the sandwich space $\mathcal{S}(A)$ of *The Sandwich Operator on an Algebra*; equivalently, the regular bimodule ${}_A A_A$ carries a left action of $A$ and a commuting right action of $A$, and the pair of these actions is a left action of the enveloping algebra $A^{\mathrm{e}} = A \otimes_k A^{\mathrm{op}}$.

*Proof.* The left multiplications and the right multiplications commute by the two-sided product proposition, so the assignments $a \mapsto L(a)$ and $b \mapsto R(b)$ combine into a homomorphism on the tensor product, with the second factor read in the opposite order; the image is spanned by the products $L(a)R(b) = T_{a,b}$. The bimodule statement is the definition of a bimodule over $A$, and a left $A$-action commuting with a right $A$-action is a left $A^{\mathrm{e}}$-action by $(a \otimes b) \cdot x = a x b$.

## The Intersection and the Sum

### The Intersection

**Proposition.** The two spaces of one-sided multiplications meet in the multiplications by the central elements:

$$
L(A) \cap R(A) = L(Z(A)) = R(Z(A)),
$$

where $Z(A)$ is the centre of $A$. In particular the intersection contains $k \cdot 1$ and is never zero for a unital algebra, it has dimension $\dim_k Z(A)$, and it has dimension one exactly when the algebra is central, $Z(A) = k \cdot 1$.

*Proof.* Suppose $L(a) = R(b)$. Evaluating at $1$ gives $a = L(a)(1) = R(b)(1) = b$, and then $L(a) = R(a)$ says $ax = xa$ for all $x$, that is $a \in Z(A)$. Conversely a central $a$ satisfies $L(a) = R(a)$ and the element lies in both spaces. The dimension is that of $Z(A)$, because $L$ restricts to an isomorphism $Z(A) \to L(Z(A))$.

### The Sum

**Proposition.** The sum $L(A) + R(A)$ is a subalgebra of $\operatorname{End}_k(A)$, it is spanned by the left and the right multiplications, and

$$
\dim_k (L(A) + R(A)) = 2n - \dim_k Z(A) .
$$

*Proof.* Both $L(A)$ and $R(A)$ are subalgebras, and they commute by the two-sided product proposition, so their sum is closed under composition; the dimension formula is the standard one for the sum of two subspaces, $\dim(L+R) = \dim L + \dim R - \dim(L \cap R)$, with the intersection computed above.

**Remark.** The sum $L(A) + R(A)$ is a proper subspace of the sandwich space $\mathcal{S}(A) = L(A)R(A)$ in general, and of the whole operator space $\operatorname{End}_k(A)$ except in the smallest cases. For the complex numbers read as a real algebra, $\dim_k A = 2$ and $Z(A) = A$ is two-dimensional, so $L(A) = R(A)$ is two-dimensional and the sum is that space, of dimension $2 = 2\cdot 2 - 2$. For $M_n(k)$ over a field the algebra has dimension $N = n^2$ and a one-dimensional centre, so the sum has dimension $2N - 1 = 2n^2 - 1$ inside the space of dimension $N^2 = n^4$, and it is far from the whole.

## The Associator as the Obstruction

### The Identity

**Theorem.** For all $a, b \in A$,

$$
L(a)R(b) - R(b)L(a) = -A_{a,b}, \qquad \text{where} \qquad A_{a,b}(x) = (a, x, b) = (ax)b - a(xb).
$$

Hence the left and the right multiplications commute for every pair if and only if the algebra is associative; the associator is exactly the obstruction to their commutation.

*Proof.* Evaluate on $x$: $L(a)R(b)(x) - R(b)L(a)(x) = a(xb) - (ax)b = -((ax)b - a(xb)) = -A_{a,b}(x)$. The operator vanishes for all $a$, $b$ and $x$ exactly when every associator vanishes, which is associativity.

### The Consequences

The identity has three consequences, and they are the reason the associator is stated both in the algebra and in the operator space.

**Corollary.** In an associative algebra the two subalgebras $L(A)$ and $R(A)$ of $\operatorname{End}_k(A)$ commute elementwise; equivalently, their sum $L(A) + R(A)$ is a commutative subalgebra of $\operatorname{End}_k(A)$, with product $L(a)R(b) = R(b)L(a) = T_{a,b}$.

**Corollary.** The associators span the commutator space $[L(A), R(A)]$, which is the image of the operator $A_{(\cdot,\cdot)}$ and is a subspace of $\operatorname{End}_k(A)$ vanishing exactly when $A$ is associative; hence the deviation of $A$ from associativity is measured by the failure of the two one-sided multiplication algebras to commute.

**Corollary.** The map $A \otimes_k A^{\mathrm{op}} \to \operatorname{End}_k(A)$ of the two regular representations is an isomorphism onto the sandwich space exactly when that space is the whole of $\operatorname{End}_k(A)$, that is when $\dim_k \mathcal{S}(A) = n^2$; this holds for a central simple algebra, by *Central Simple Algebras and the Brauer Group*.

The three corollaries are the operator form of the statement that associativity is not a property of the product alone but of the way the two sides of the product commute. The left and the right multiplications each know only one side; the associator is what happens when the two sides are brought together.

## The Examples

### The Matrix Algebra

Let $A = M_n(k)$, of dimension $n^2$; the operators form $M_{n^2}(k)$, of dimension $n^4$. The left and the right multiplications are the operators $X \mapsto AX$ and $X \mapsto XB$ on the space of matrices, of dimension $n^2$ each; the centre is $k \cdot I$ of dimension one, so the intersection $L(A) \cap R(A)$ is one-dimensional, spanned by the identity operator, and the sum $L(A) + R(A)$ has dimension $2n^2 - 1$. For $n = 2$ this is $7$ inside a space of dimension $16$; the left multiplications and the right multiplications overlap exactly in the scalars, and together they generate a seven-dimensional subalgebra of the operator algebra. The sandwich space is larger, and it is the whole of $\operatorname{End}_k(M_n(k))$ by *The Sandwich Operator on an Algebra*, so the operator algebra is generated by the two one-sided families and their products.

### The Commutative Case

Let $A$ be commutative. Then $L(a) = R(a)$ for every $a$, the two spaces coincide, $L(A) = R(A)$ has dimension $n$, and the sum is one copy of the multiplication algebra. The left and the right multiplication are the same operator, and the associator vanishes automatically; the whole of the two-sided theory collapses to the one-sided theory of the multiplication operators, which is developed for the commutative case in *Multiplication Operators on a Commutative Algebra* of the symmetric category.

### The Quaternions

Let $A = \mathbb{H}$ over $\mathbb{R}$, of dimension $4$; the centre is $\mathbb{R}$, so the intersection $L(A) \cap R(A)$ is one-dimensional and the sum has dimension $7$ inside the space of dimension $16$. The four left multiplications and the four right multiplications are the two copies of the algebra and its opposite inside the operator space, and their products give the sandwich space, which is all of $\operatorname{End}_{\mathbb{R}}(\mathbb{H})$ because $\mathbb{H}$ is central simple over $\mathbb{R}$. The two three-dimensional pieces of the operator ladder of *The Operators on an Algebra* — the pure left multiplications and the derivations — are the further refinement of this picture.

## Summary

The left multiplication $L(a)$ and the right multiplication $R(a)$ are the two $k$-linear operators $x \mapsto ax$ and $x \mapsto xa$ on $A$; they are injective when $A$ is unital, and their images $L(A)$ and $R(A)$ are subspaces of $\operatorname{End}_k(A)$ of dimension $n$ each. The left multiplications compose as $L(a)L(b) = L(ab)$, so $L : A \to \operatorname{End}_k(A)$ is an algebra isomorphism onto $L(A)$; the right multiplications compose as $R(a)R(b) = R(ba)$, so $R$ is an anti-homomorphism, and $R : A^{\mathrm{op}} \to R(A)$ is an algebra isomorphism from the opposite algebra. The two families commute, $L(a)R(b) = R(b)L(a) = T_{a,b}$, exactly when the product is associative, and the obstruction is the associator,

$$
L(a)R(b) - R(b)L(a) = -A_{a,b}, \qquad A_{a,b}(x) = (ax)b - a(xb);
$$

equivalently $A$ is associative exactly when every left multiplication commutes with every right multiplication. The pair $(L,R)$ is a homomorphism $A \otimes_k A^{\mathrm{op}} \to \operatorname{End}_k(A)$ with image the sandwich space, and the regular module is the bimodule it makes of $A$. The two spaces meet in the multiplications by the centre, $L(A) \cap R(A) = L(Z(A))$, so their sum has dimension $2n - \dim_k Z(A)$; and the centraliser of $L(A)$ in $\operatorname{End}_k(A)$ is exactly $R(A)$. For $M_n(k)$ the left and the right multiplications meet in the scalars and their sum has dimension $2n^2 - 1$; for a commutative algebra the two sides coincide; and the two-sided product with the associator is the subject of *The Sandwich Operator on an Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$ | the field of scalars |
| $A$ | a unital associative $k$-algebra |
| $n = \dim_k A$ | the dimension, when finite |
| $L(a)$, $L(a)(x) = ax$ | the left multiplication by $a$ |
| $R(a)$, $R(a)(x) = xa$ | the right multiplication by $a$ |
| $L(A)$, $R(A)$ | the spaces of left and right multiplications |
| $A^{\mathrm{op}}$ | the opposite algebra, isomorphic to $R(A)$ |
| $A^{\mathrm{e}} = A \otimes_k A^{\mathrm{op}}$ | the enveloping algebra |
| $T_{a,b} = L(a)R(b) = R(b)L(a)$ | the sandwich, the product of the two sides |
| $(a,x,b) = (ax)b - a(xb)$ | the associator |
| $Z(A)$ | the centre, with $L(A) \cap R(A) = L(Z(A))$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the regular representations and the multiplication algebra.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society, 1956), for the left and the right multiplications and the double centraliser theorem.
- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, second edition, 1992), for the regular module, its endomorphism ring and the identification of the centraliser.
- Carl Faith, *Algebra: Rings, Modules and Categories I* (Springer, 1973), for the structure of the multiplication algebra of an associative algebra.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the associator and the identities that replace associativity.
