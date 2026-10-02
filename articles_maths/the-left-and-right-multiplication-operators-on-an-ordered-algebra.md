
# __The Left and Right Multiplication Operators on an Ordered Algebra__

## Introduction

An **ordered algebra** is an algebra whose underlying vector space is ordered by a cone that the multiplication respects: the product of two positive elements is positive. This is the structure on which every one-sided operator of the category is written. The **left multiplication** $L_a$ and the **right multiplication** $R_a$,

$$
L_a x = ax, \qquad R_a x = xa ,
$$

are the elementary operators of the structure: they are linear in $x$, they are positive as soon as $a$ is positive, they commute with each other by associativity, and together they produce the **multiplication algebra** of $A$. The assignment $a\mapsto L_a$ is the left regular representation; it is an algebra homomorphism, it is injective when $A$ is unital, and — this is the point of the ordered setting — it is an **order isomorphism** onto its image, because a left multiplication by $a$ is positive exactly when $a$ is positive, the identity being available to evaluate it.

The article states these facts and organises the multiplication algebra. It is the base of the operator theory of the category: the sandwich articles add a second parameter and a grade involution to the two-sided multiplication, the reflection articles read the reflections of the algebra as two-sided operators, the signed left multiplication article twists this one-sided action by the grade involution, and the graded-action article carries the action to a module. The order and the order unit are *Ordered Vector Spaces and the Order Unit*; the positivity and the operator order are *Positive Operators on an Ordered Space* and *The Cone of Positive Operators*; the function algebra $C(X)$ and the matrix algebra are the instances of *Jordan Algebras and the Positive Cone* and of the algebra articles of Part II; the sandwich operator of an unordered algebra is *The Sandwich Operator on an Algebra*, and the graded structures and the grade involution are *Superalgebras and Graded Structures*, both of Part I. The involution on the algebra is *Ordered Involutive Algebras* later in this category, and the adjoints of the one-sided multiplications are the * Operator Theory articles at the end of the category.

## Ordered Algebras

### The Structure

**Definition.** An **ordered algebra** over $\mathbb{R}$ is an associative algebra $A$ together with a positive cone $A_+$ that is a cone of the underlying ordered vector space and is closed under multiplication:

$$
A_+\cdot A_+\subseteq A_+ .
$$

It is **unital** when it has an identity $1$, and an **ordered algebra with order unit** when $1$ is an order unit of the underlying ordered vector space. The order is $a\leq b$ when $b-a\in A_+$, and the algebra is **Archimedean** when the underlying order is.

**Proposition (the order is compatible with the multiplication).** In an ordered algebra the multiplication is **positive bilinear**: for $a,b\geq0$ and $x\leq y$,

$$
ax\leq ay, \qquad xa\leq ya, \qquad ab\geq0 ,
$$

and more generally $a\leq b$ implies $ax\leq bx$ and $xa\leq xb$ for $x\geq0$.

*Proof.* The cone is closed under products, so $a(y-x)\in A_+$ and $(y-x)a\in A_+$ when $a\geq0$ and $y-x\geq0$; this is the two inequalities, and $ab\in A_+$ for positive $a,b$ is the defining closure.

**Example.** The algebra $C_{\mathbb{R}}(X)$ of continuous real functions on a compact space, with the cone of nonnegative functions, is a commutative ordered algebra with order unit $1$. The matrix algebra $M_n(\mathbb{R})$ with the Loewner cone of positive semidefinite matrices is an ordered algebra, because a product of two positive semidefinite matrices is not symmetric in general but the **symmetrised** product cone is the one that is closed; the correct ordered algebra in the matrix case is therefore the Jordan algebra of *Jordan Algebras and the Positive Cone*, and this is the reason the category separates the associative and the Jordan orders. The polynomials with a real positivity cone are not an ordered algebra in an obvious way, which is one of the reasons the theory is carried by the function and the matrix instances.

### The One-Sided Multiplications

**Definition.** For $a\in A$ the **left multiplication** and the **right multiplication** are the operators

$$
L_a : A\to A, \quad L_a x = ax , \qquad R_a : A\to A, \quad R_a x = xa .
$$

**Proposition (linearity and positivity).** $L_a$ and $R_a$ are linear in $x$. In a unital ordered algebra, for every $a$,

$$
L_a\geq0 \iff a\geq0 \iff R_a\geq0 ,
$$

so the maps $a\mapsto L_a$ and $a\mapsto R_a$ are **order isomorphisms** from $A$ onto their images, and each is an isomorphism of ordered vector spaces when $A$ is Archimedean.

*Proof.* Linearity is the distributivity and the compatibility of the scalars. If $a\geq0$ then $ax\geq0$ and $xa\geq0$ for $x\geq0$ by the positive bilinearity; conversely $L_a\geq0$ evaluated at $1\geq0$ gives $a = L_a1\geq0$, and $R_a\geq0$ gives $a = R_a1\geq0$. The order isomorphism statement is the two implications, and the Archimedean statement is the remark that no further relation is imposed on the cone.

**Example (the commutative case).** When $A$ is commutative, $L_a = R_a$ for every $a$, and the one-sided multiplications are the single multiplication operators of the algebra. For $A = C(X)$ the operator $L_f = R_f$ is the multiplication by $f$, positive exactly when $f\geq0$, which is the operator of *Multiplication Operators on an $L^1$ Function* of Part II read on the continuous functions.

### The Regular Representation and the Commutation

**Theorem (the left and right regular representations).** The map

$$
L : A\to L(A), \qquad L(a) = L_a ,
$$

is an injective **algebra homomorphism** in a unital algebra,

$$
L_aL_b = L_{ab}, \qquad L_{a+b} = L_a+L_b, \qquad L_{\lambda a} = \lambda L_a, \qquad L_1 = I ,
$$

the map $R : a\mapsto R_a$ is an injective **anti-homomorphism**,

$$
R_aR_b = R_{ba} ,
$$

and the two images **commute**:

$$
L_aR_b = R_bL_a \qquad \text{for all } a,b\in A ,
$$

because both sides send $x$ to $axb$.

*Proof.* For the composition, $L_aL_bx = a(bx) = (ab)x = L_{ab}x$; the additive and scalar claims are the bilinearity of the multiplication; $L_1 = I$ is the identity axiom. For the anti-homomorphism, $R_aR_bx = (xb)a = x(ba) = R_{ba}x$. The commutation is $a(xb) = (ax)b$, which is associativity.

**Corollary (the multiplication algebra).** The algebra generated by the $L_a$ and the $R_a$ is the image of the homomorphism

$$
A\otimes A^{\mathrm{op}} \to L(A), \qquad a\otimes b\mapsto L_aR_b ,
$$

it contains the identity when $A$ is unital, and it is the **multiplication algebra** of $A$. When $A$ is commutative it is the image of $A\otimes A$, and when $A$ is a division algebra it is a tensor product of two copies of the structure.

*Proof.* The stated map is well defined and is a homomorphism by the two representation theorems and the commutation; its image is generated by the two families by definition; the remaining statements follow from the identification of the opposite algebra in the commutative case.

## The Multipliers

**Definition.** A **double centralizer**, or **multiplier**, of $A$ is a pair $(S,T)$ of linear maps with

$$
x\,S(y) = T(x)\,y \qquad \text{for all } x,y\in A .
$$

**Proposition.** For every $a\in A$ the pair $(L_a,R_a)$ is a double centralizer, and the map $a\mapsto(L_a,R_a)$ is injective in a unital algebra; the double centralizers form an algebra under the componentwise operations, containing the image of $A$ as a two-sided ideal, the **multiplier algebra** $M(A)$.

*Proof.* The centralizer equation for $(L_a,R_a)$ is $x(ay) = (xa)y$, which is associativity; injectivity is $L_a1 = a$. The componentwise operations make the centralizers an algebra, and for $a\in A$ and a centralizer $(S,T)$ the products $L_a(S,T) = (L_aS, \cdot)$ and $(S,T)L_a$ are again centralizers, so the image of $A$ is an ideal.

**Proposition (positivity of the multipliers).** In a unital ordered algebra a double centralizer $(S,T)$ with $S\geq0$ and $T\geq0$ is a positive pair, and the multiplier algebra is ordered by the cone of the positive pairs; when $A$ is an ordered algebra with order unit and the multipliers are bounded for the order-unit norm, $M(A)$ is an ordered algebra with order unit $(L_1,R_1) = (I,I)$.

*Proof.* The positivity of the pair is the positivity of its two components, and the operations of the multiplier algebra preserve it by the positive bilinearity of the multiplication; the order unit statement is that $I\geq0$ and that every centralizer is between multiples of $(I,I)$ when it is bounded, which is the order-unit estimate of *Positive Operators on an Ordered Space*.

## The Order and the Norm

### The Regular Representation is an Order Isomorphism

**Theorem.** In a unital ordered algebra the left regular representation is an isomorphism of ordered algebras from $A$ onto $L(A)$ with the pointwise order: it preserves the order, the products and the identity in both directions. The same holds for the right regular representation onto $R(A)$ with the anti-multiplication.

*Proof.* The order statement is the proposition on positivity: $a\geq0$ iff $L_a\geq0$. The product and identity statements are the representation theorem.

### The Operator Norm of a Multiplication

**Definition.** On a unital ordered algebra define

$$
\lVert a\rVert_L = \lVert L_a\rVert ,
$$

the operator norm of the left multiplication for the order-unit norm, when the latter is finite.

**Proposition.** The assignment $a\mapsto\lVert a\rVert_L$ is a submultiplicative algebra norm,

$$
\lVert ab\rVert_L\leq\lVert a\rVert_L\,\lVert b\rVert_L, \qquad \lVert 1\rVert_L = 1 ,
$$

and the left regular representation is isometric for it. In an ordered Banach algebra with a monotone norm the two norms agree on the positive cone.

*Proof.* Submultiplicativity is $\lVert L_{ab}\rVert = \lVert L_aL_b\rVert\leq\lVert L_a\rVert\lVert L_b\rVert$ and the identity is $\lVert L_1\rVert = \lVert I\rVert = 1$. Isometry is the definition. Monotonicity of the norm gives $\lVert a\rVert = \lVert L_a1\rVert\leq\lVert L_a\rVert$ and the reverse follows from the order-unit estimate, so the two agree.

## Worked Cases

### The Continuous Functions

For $A = C(X)$ with $X$ compact every multiplication is commutative, $L_f = R_f$ is the multiplication operator by $f$, and the left regular representation is the isometric isomorphism of $C(X)$ onto the algebra of multiplication operators on itself. The algebra is unital, so its multiplier algebra is itself; the double centralizer condition is automatic by commutativity, and a multiplier is positive exactly when its function is nonnegative.

### The Triangular Matrices

For $A = T_n(\mathbb{R})$ the upper triangular matrices with the cone of entrywise nonnegative matrices, the left and right multiplications by a nonnegative matrix are positive, and they do not commute with each other except through the centre, which for $T_n$ is the span of the identity. The multiplier algebra is $T_n$ itself, since the algebra is unital. This is the smallest noncommutative example in which $L(A)$ and $R(A)$ are genuinely different, and it shows that the commutation $L_aR_b = R_bL_a$ is a statement about the two families and not about the elements.

### The Matrix Algebra Revisited

For $A = M_n(\mathbb{R})$ with the **cone of symmetric positive semidefinite matrices inside the self-adjoint part**, the left and right multiplications preserve the cone of $A$ when $a$ is a positive semidefinite matrix, but the product of two positive semidefinite matrices need not be self-adjoint; the ordered algebra of the associative product is therefore the **symmetrised** structure, and the one-sided multiplications of the associative algebra are used together with the Jordan product of *Jordan Algebras and the Positive Cone* to recover the positive cone. This is the reason the later articles of the category distinguish the one-sided from the sandwich action.

## Summary

An **ordered algebra** is an associative algebra whose cone is closed under multiplication, so that the multiplication is positive bilinear and the order is compatible with it. The **left and right multiplications** $L_a x = ax$ and $R_a x = xa$ are linear, they are **positive exactly when $a$ is positive** in a unital ordered algebra, so that $a\mapsto L_a$ and $a\mapsto R_a$ are order isomorphisms onto their images. The left multiplication is an **algebra homomorphism** $L_{ab} = L_aL_b$ with $L_1 = I$, the right multiplication is an **anti-homomorphism** $R_{ab} = R_bR_a$, and the two families **commute**, $L_aR_b = R_bL_a$, by associativity. They generate the **multiplication algebra**, the image of $A\otimes A^{\mathrm{op}}$, and the **double centralizers** extend it to the **multiplier algebra**. The operator norm $\lVert a\rVert_L = \lVert L_a\rVert$ is a submultiplicative algebra norm for which the left regular representation is isometric. The order and the order unit are *Ordered Vector Spaces and the Order Unit*; the positivity and the operator order are *Positive Operators on an Ordered Space* and *The Cone of Positive Operators*; the sandwich operator of an unordered algebra is *The Sandwich Operator on an Algebra*; the graded structures are *Superalgebras and Graded Structures*; and the involution version and the adjoints are *Ordered Involutive Algebras* and the * Operator Theory articles of this category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A_+\cdot A_+\subseteq A_+$ | Defining closure of the cone of an ordered algebra |
| $L_a x = ax$, $R_a x = xa$ | Left and right multiplication operators |
| $L_a\geq0\iff a\geq0$ | Positivity of the one-sided multiplications in a unital algebra |
| $L_{ab} = L_aL_b$, $R_{ab} = R_bR_a$ | Regular representations, homomorphism and anti-homomorphism |
| $L_aR_b = R_bL_a$ | Commutation by associativity |
| $A\otimes A^{\mathrm{op}}$ | Multiplication algebra of the one-sided multiplications |
| $(S,T)$, $xS(y) = T(x)y$ | Double centralizer, multiplier |
| $M(A)$ | Multiplier algebra |
| $\lVert a\rVert_L = \lVert L_a\rVert$ | Operator norm of the left multiplication |

## Further Reading

- Richard Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for the left and right regular representations and the multiplier algebra.
- Bruce Blackadar, *Operator Algebras: Theory of C*-Algebras and von Neumann Algebras* (Springer, 2006), for the multiplier algebra as the double centralizer algebra.
- Charalambos D. Aliprantis and Owen Burkinshaw, *Positive Operators* (Academic Press, 1985), for the positivity of the one-sided multiplications in an ordered algebra.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1956), for the multiplication algebra and the regular representations of an associative algebra.
