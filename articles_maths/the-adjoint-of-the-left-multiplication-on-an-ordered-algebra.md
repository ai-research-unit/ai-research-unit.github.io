
# __The Adjoint of the Left Multiplication on an Ordered Algebra__

## Introduction

The **left multiplication** $L_a : x\mapsto ax$ of an ordered involutive algebra has, for the trace form, the adjoint

$$
(L_a)^{*} = L_{a^{*}} ,
$$

and its right-handed companion satisfies $(R_a)^{*} = R_{a^{*}}$; the article develops the consequences of this single computation. The two-sided **multiplication operator** $T_{a,b} = L_aR_b$, which sends $x$ to $axb$, has the adjoint $(T_{a,b})^{*} = T_{b^{*},a^{*}}$, so the adjoint of a two-sided multiplication is again a two-sided multiplication, with the parameters interchanged and conjugated. The **inner derivation** $\delta_a = L_a - R_a$ has the adjoint $\delta_a^{*} = \delta_{a^{*}}$, so an inner derivation is **self-adjoint** exactly when the deriving element is self-adjoint; and the derivation property is preserved by the adjoint involution. In all of this the order is the quadratic order of *Self-Adjoint Elements and the Order*: an element is positive if and only if its left multiplication is a positive operator, and the adjoint is order preserving, so the **adjoint and the order** are compatible in every form in which the one-sided multiplications appear.

The map $a\mapsto L_a$ is a **\*-homomorphism** of the algebra into the algebra of operators, and $a\mapsto R_a$ is a **\*-anti-homomorphism**; their combination produces the two-sided structure, the derivations, and the **multiplication algebra** $\{L_aR_b\}$. The article states these maps, computes their adjoints, and identifies the order-theoretic content: the positive cone of the algebra is carried isomorphically onto the cone of the positive one-sided multiplications, and the symmetrised combinations $L_a + R_a$ are the self-adjoint operators of the multiplication algebra.

The adjoint and the positivity are *The Adjoint of a Positive Operator*; the order of the self-adjoint elements is *Self-Adjoint Elements and the Order*; the positive functionals are *Positive Functionals and Self-Adjointness*; the involution on the automorphisms is *The Involution on the Order Automorphisms*; the signed adjoints are *The Signed Adjoint Sandwich on an Ordered Algebra*, *The Signed Adjoint of the Reflection on an Ordered Algebra* and *The Signed Adjoint of the Left Multiplication on an Ordered Algebra*; the graded action is *The Graded Adjoint Action on a Module over an Ordered Algebra*; the forms are *Positive Definite Forms and the Order*; the ordered involution is *Ordered Involutive Algebras*; and the Jordan order is *The Jordan Algebra of Self-Adjoint Elements*. The operator-algebraic models are *Operator Algebras* and *The Theory of von Neumann Algebras* of Part II.

## The Adjoints of the One- and Two-Sided Multiplications

**Proposition (the one-sided multiplications).** With the adjoints taken for the trace form,

$$
(L_a)^{*} = L_{a^{*}}, \qquad (R_a)^{*} = R_{a^{*}} ,
$$

so the left multiplications form a **\*-homomorphism** $a\mapsto L_a$ with $L_{ab} = L_aL_b$ and $L_{a^{*}} = (L_a)^{*}$, and the right multiplications form a **\*-anti-homomorphism** $a\mapsto R_a$ with $R_{ab} = R_bR_a$ and $R_{a^{*}} = (R_a)^{*}$.

*Proof.* $\langle L_ax,y\rangle = \operatorname{tr}((ax)^{*}y) = \operatorname{tr}(x^{*}a^{*}y) = \langle x,L_{a^{*}}y\rangle$ and $\langle R_ax,y\rangle = \operatorname{tr}((xa)^{*}y) = \operatorname{tr}(a^{*}x^{*}y) = \operatorname{tr}(x^{*}ya^{*}) = \langle x,R_{a^{*}}y\rangle$. The homomorphism and anti-homomorphism properties are the associativity, $L_{ab} = L_aL_b$ and $R_{ab} = R_bR_a$, together with the adjoint identities.

**Proposition (the two-sided multiplications).** For $a,b\in A$ let $T_{a,b} = L_aR_b$, $T_{a,b}(x) = axb$; then

$$
(T_{a,b})^{*} = T_{b^{*},a^{*}} ,
$$

so the two-sided multiplications form a **bimodule** under the adjoint, the map $(a,b)\mapsto T_{a,b}$ is bilinear, and the identity $T_{a,b}T_{c,d} = T_{ac,db}$ holds by associativity; consequently the adjoint of a two-sided multiplication is again a two-sided multiplication, and the **self-adjoint** two-sided multiplications are the $T_{a,a^{*}}$ and their sums.

*Proof.* $\langle T_{a,b}x,y\rangle = \operatorname{tr}((axb)^{*}y) = \operatorname{tr}(b^{*}x^{*}a^{*}y) = \operatorname{tr}(x^{*}a^{*}yb^{*}) = \langle x,T_{b^{*},a^{*}}y\rangle$, which is the adjoint formula; the composition identity is associativity, and the self-adjointness statement is the fixed-point condition $T_{a,b} = T_{b^{*},a^{*}}$.

**Corollary (the symmetrised two-sided multiplication).** The operator $L_a + R_a$, the **symmetrised two-sided multiplication**, is self-adjoint exactly when $a$ is self-adjoint, $(L_a + R_a)^{*} = L_{a^{*}} + R_{a^{*}}$, and it is the operator $x\mapsto ax + xa$; the **Jordan multiplication** of the algebra is its restriction to the self-adjoint part.

*Proof.* The adjoint formula is the sum of the two adjoint identities; the self-adjointness condition is immediate; the identification with the Jordan multiplication is the definition $\{a,x\} = \frac12(ax + xa)$.

## The Inner Derivations

**Definition.** The **inner derivation** of $a$ is $\delta_a = L_a - R_a$, the operator $\delta_a(x) = ax - xa = [a,x]$.

**Proposition (the adjoint of an inner derivation).** The adjoint of an inner derivation is

$$
(\delta_a)^{*} = \delta_{a^{*}} ,
$$

so $\delta_a$ is self-adjoint exactly when $a$ is self-adjoint, and it is **skew-adjoint**, $(\delta_a)^{*} = -\delta_a$, exactly when $a$ is **skew-adjoint**, $a^{*} = -a$; the inner derivations form a Lie subalgebra of the operators, $[\delta_a,\delta_b] = \delta_{[a,b]}$, closed under the adjoint.

*Proof.* The adjoint formula is the difference of the one-sided adjoints. The skew-adjointness condition is $\delta_{a^{*}} = -\delta_a = \delta_{-a}$, which is $a^{*} = -a$. The Lie-algebra statement is the Jacobi-type identity $[\delta_a,\delta_b] = \delta_{[a,b]}$, which is the derivation property computed on the generators.

**Proposition (the Leibniz rule and the order).** Every inner derivation **derives** the multiplication, $\delta_a(xy) = \delta_a(x)y + x\delta_a(y)$, and the adjoint of a derivation is a derivation; the map $a\mapsto\delta_a$ is linear, its kernel is the centre of the algebra, and the positive elements of the centre give the vanishing inner derivations, so the order of the derivation algebra is the order of the central elements.

*Proof.* The Leibniz rule is the associativity $a(xy) - (xy)a = (ax - xa)y + x(ay - ya)$; the adjoint of a derivation is a derivation because the adjoint of the Leibniz rule is the Leibniz rule for the adjoint; the kernel statement is the definition of the centre, and the order statement is the restriction of the quadratic order to the centre.

## The Adjoint and the Order

**Theorem (the order of the multiplications).** The map $a\mapsto L_a$ is an **order isomorphism** of the ordered involutive algebra onto the subalgebra of the left multiplications, and

$$
a\geq0 \iff L_a\geq0 \iff R_a\geq0 \iff T_{a,b}\geq0 \ \text{ for every } b\geq0 ,
$$

so the positive cone of the algebra is carried isomorphically onto the cone of the positive multiplications; the adjoint of a positive multiplication is positive, and the adjoint is therefore an **order automorphism** of the multiplication algebra.

*Proof.* The first two equivalences are the theorem of *Self-Adjoint Elements and the Order*; the third is the two-sided statement $T_{a,b}(A_+) = L_aR_b(A_+)\subseteq L_a(A_+)\subseteq A_+$ for $a,b\geq0$, with the converse from the choice $b = 1$; the positivity of the adjoint is *The Adjoint of a Positive Operator*, and the order-automorphism statement is its consequence.

**Corollary (the symmetrised multiplications and the order unit).** The symmetrised two-sided multiplication $L_a + R_a$ is positive if and only if $a\geq0$, and the **order unit** of the multiplication algebra is $L_1 = I$; the positive elements of the multiplication algebra are generated by the $L_aR_b$ with $a,b\geq0$, and the order interval at the identity is the set of the multiplications $T_{a,b}$ with $0\leq a,b$ and $T_{a,b}\leq I$.

*Proof.* The positivity of $L_a + R_a$ reduces to the positivity of $L_a$ and $R_a$, hence to $a\geq0$; the order unit is the identity multiplication; the generation statement is the additive closure of the cone; the interval statement is the definition of the order interval.

## Worked Cases

### The Matrix Algebra

Let $A = M_n(\mathbb{C})$ with the trace form. The left multiplication is $L_A(X) = AX$, its adjoint is the multiplication by $A^{*}$, and the inner derivation is $\delta_A(X) = AX - XA$ with adjoint $\delta_{A^{*}}$; the skew-adjoint derivations are the $\delta_A$ with $A$ skew-Hermitian, which are the infinitesimal generators of the unitary conjugations. The positivity of $L_A$ is the positivity of $A$ in the Loewner order. This is the finite-dimensional model.

### The Self-Adjoint Operators

Let $A$ be a von Neumann algebra with the trace form. The left and right multiplications, the two-sided multiplications and the inner derivations are the standard operators of the algebra; the derivations with self-adjoint deriving elements are self-adjoint, and the derivations with skew-adjoint elements are skew-adjoint and generate the group of the inner \*-automorphisms. The positivity of the multiplications is the positivity of the elements in the order of the algebra.

### The Continuous Functions

Let $A = C(X,\mathbb{C})$ with the pointwise order and the $L^{2}$ trace form. The left multiplication $L_f$ is the multiplication by $f$, its adjoint is the multiplication by $\bar f$, and the inner derivation $\delta_f$ is the multiplication by $f - \bar f\cdot$ in the commutative case the derivations vanish on the self-adjoint part, and the adjoint of $L_f$ is $L_{\bar f}$; the positivity of $L_f$ is the pointwise nonnegativity of $f$. The commutative case shows that the derivation structure disappears and the adjoint reduces to the complex conjugation.

## Summary

The **left multiplication** $L_a : x\mapsto ax$ has the adjoint $(L_a)^{*} = L_{a^{*}}$ for the trace form, the **right multiplication** has $(R_a)^{*} = R_{a^{*}}$, and $a\mapsto L_a$ (resp. $a\mapsto R_a$) is a **\*-homomorphism** (resp. a **\*-anti-homomorphism**). The **two-sided multiplication** $T_{a,b} = L_aR_b$ has $(T_{a,b})^{*} = T_{b^{*},a^{*}}$, so it is self-adjoint for the parameters $(a,a^{*})$; the **symmetrised** $L_a + R_a$ is self-adjoint exactly for the self-adjoint $a$ and is the Jordan multiplication. The **inner derivation** $\delta_a = L_a - R_a = [a,\cdot]$ has $(\delta_a)^{*} = \delta_{a^{*}}$, is self-adjoint exactly for the self-adjoint $a$ and skew-adjoint exactly for the skew-adjoint $a$, satisfies the **Leibniz rule**, and its kernel is the centre. The **order** is transported: $a\geq0\iff L_a\geq0\iff R_a\geq0\iff T_{a,b}\geq0$ for every $b\geq0$, the adjoint of a positive multiplication is positive, and the adjoint is an **order automorphism** of the multiplication algebra, whose order unit is $L_1 = I$ and whose interval at the identity is the set of the multiplications $T_{a,b}$ below $I$. The adjoint and the positivity are *The Adjoint of a Positive Operator*; the order is *Self-Adjoint Elements and the Order*; the functionals are *Positive Functionals and Self-Adjointness*; the automorphisms are *The Involution on the Order Automorphisms*; the signed adjoints are *The Signed Adjoint Sandwich on an Ordered Algebra*, *The Signed Adjoint of the Reflection on an Ordered Algebra* and *The Signed Adjoint of the Left Multiplication on an Ordered Algebra*; the graded action is *The Graded Adjoint Action on a Module over an Ordered Algebra*; the forms are *Positive Definite Forms and the Order*; and the ordered involution is *Ordered Involutive Algebras*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_a x = ax$, $R_a x = xa$ | Left and right multiplications |
| $(L_a)^{*} = L_{a^{*}}$, $(R_a)^{*} = R_{a^{*}}$ | Adjoints |
| $T_{a,b} = L_aR_b$, $T_{a,b}(x) = axb$ | Two-sided multiplication |
| $(T_{a,b})^{*} = T_{b^{*},a^{*}}$ | Adjoint of a two-sided multiplication |
| $L_a + R_a$ | Symmetrised, self-adjoint for self-adjoint $a$ |
| $\delta_a = L_a - R_a = [a,\cdot]$ | Inner derivation |
| $(\delta_a)^{*} = \delta_{a^{*}}$ | Adjoint of a derivation |
| $a\geq0\iff L_a\geq0$ | Order isomorphism of the multiplications |

## Further Reading

- Richard Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for the left and right multiplications, the derivations and the order.
- Gert K. Pedersen, *C\*-Algebras and their Automorphism Groups* (Academic Press, 1979), for the inner derivations, the Leibniz rule and the automorphism groups.
- Jacques Dixmier, *Les algèbres d'opérateurs dans l'espace hilbertien* (Gauthier-Villars, 1969), for the multiplication algebra, the derivations and the order of a von Neumann algebra.
- Charalambos D. Aliprantis and Owen Burkinshaw, *Positive Operators* (Academic Press, 1985), for the positive multiplications, the quadratic order and the order-isomorphism of the multiplication algebra.
- Shoichiro Sakai, *C\*-Algebras and W\*-Algebras* (Springer, 1971), for the derivations, the inner automorphisms and the order of the operator algebras.
