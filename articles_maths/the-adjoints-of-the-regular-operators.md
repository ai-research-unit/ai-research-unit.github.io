# __The Adjoints of the Regular Operators__

## Introduction

An involution on a ring, together with a trace it leaves invariant, puts a Hermitian form on the regular module, and a Hermitian form puts an adjoint on the operators. The left and the right regular representations then become representations that carry the involution to the adjoint, $L_a^{\dagger} = L_{a^{*}}$ and $R_b^{\dagger} = R_{b^{*}}$, the two-sided operations $L_aR_b$ have adjoint $L_{a^{*}}R_{b^{*}}$, the commutant of the left representation is the conjugate of the right one, and the self-adjoint, the normal and the unitary elements of the ring become operators of the same kind. This article is the ${}^{*}$-operator layer of the regular object: where *The Regular Module and the Regular Bimodule* reads the ring as a module and *The Regular Representation as an Algebra of Operators* reads it as an algebra of operators, this one reads the involution of the ring as the adjoint of those operators.

The article assumes *The Regular Representation as an Algebra of Operators* for the representation, the commutant and the bicommutant, *The Regular Bimodule over an Involutive Ring* for the twist, the swap and the canonical form, *Involutive Rings* for the involution and its symmetric and skew elements, *The Adjoint of the Left Multiplication on a Ring*, in the category Rings, for the ring-level computation of the same adjoint, and *Involutions of the Endomorphism Ring*, *The Adjoint of an Endomorphism* and *Unitary Endomorphisms* for the adjoint involution a pairing defines on an endomorphism algebra. The positivity of the form, the Hilbert space it completes and the operator theory that needs a norm are *Hilbert Algebras* and Part II; here everything is algebraic and finite-dimensional where a trace is used. The star-derivations attached to the involution are *Star-Derivations and the Skew Derivations*.

Throughout, $A$ is a ring with $1 \neq 0$ and an involution $\sigma$, written $a^{*} = \sigma(a)$, and $\tau$ is a trace on $A$ that is $\sigma$-invariant in the sense $\tau(\sigma(x)) = \tau(x)$. When $A$ is a finite-dimensional algebra over a field $F$, $F$ carries the induced involution and $\operatorname{End}_F(A)$ is the operator algebra. The left and right multiplications are $L_a(x) = ax$ and $R_a(x) = xa$, and the operator adjoint is written ${}^{\dagger}$, as in *Conventions in Mathematics*.

## The Form and the Adjoint Involution

### The trace pairing

**Definition.** The **trace pairing** of the involutive ring is

$$
\beta(x,y) = \tau\bigl(x\,\sigma(y)\bigr) = \tau(x\,y^{*}) .
$$

**Proposition.** $\beta$ is a Hermitian form on the regular module: it is additive in each variable, $F$-linear in the first and $\sigma$-semilinear in the second,

$$
\beta(ax, y) = a\,\beta(x,y), \qquad \beta(x, ay) = \beta(x,y)\,\sigma(a),
$$

and $\beta(y,x) = \sigma(\beta(x,y))$; it is non-degenerate when the trace pairing is, and for $A = M_n(F)$ with the matrix trace it is the trace form $\beta(X,Y) = \operatorname{tr}(XY^{*})$.

**Proof.** Additivity and the two sesquilinearity laws are the linearity of $\tau$ and the trace property $\tau(uv) = \tau(vu)$, together with the anti-multiplicativity of $\sigma$; Hermitianity is $\sigma$-invariance of $\tau$, $\sigma(\tau(xy^{*})) = \tau(\sigma(x)\sigma(y^{*})) = \tau(\sigma(x)y) = \tau(y\sigma(x)) = \beta(y,x)$, using the cyclicity of the trace. The matrix statement is the definition.

### The adjoint involution

**Definition.** For $T \in \operatorname{End}_F(A)$ the **adjoint** $T^{\dagger}$ is the operator, when it exists, with

$$
\beta(Tx, y) = \beta(x, T^{\dagger}y) \qquad (x, y \in A).
$$

**Proposition (the adjoint is an involution of the operator algebra).** If $\beta$ is non-degenerate then $T^{\dagger}$ exists for every $T$ and is unique; the assignment $T \mapsto T^{\dagger}$ is additive, of order two, and reverses composition,

$$
(S T)^{\dagger} = T^{\dagger} S^{\dagger}, \qquad (T^{\dagger})^{\dagger} = T, \qquad (\lambda T)^{\dagger} = \sigma(\lambda)\, T^{\dagger} ,
$$

so it is the adjoint involution of *Involutions of the Endomorphism Ring* carried to the operator algebra, $\sigma$-semilinear when $\sigma$ is not the identity.

**Proof.** Uniqueness and existence are the non-degeneracy of $\beta$, as in *The Adjoint of an Endomorphism*. Additivity and order two are the two linearities of $\beta$. For the reversal, $\beta(STx,y) = \beta(Tx, S^{\dagger}y) = \beta(x, T^{\dagger}S^{\dagger}y)$, so $(ST)^{\dagger} = T^{\dagger}S^{\dagger}$. The scalar law is the $\sigma$-semilinearity of $\beta$ in the second variable.

## The Regular Representation Is a ${}^{*}$-Representation

### The definition

**Definition.** Let $A$ be an algebra with involution over a field with involution and let $V$ carry a non-degenerate Hermitian form with adjoint ${}^{\dagger}$. A representation $\pi : A \to \operatorname{End}(V)$ is a **${}^{*}$-representation** if

$$
\pi(ab) = \pi(a)\pi(b), \qquad \pi(a^{*}) = \pi(a)^{\dagger} .
$$

**Remark.** The first law says that $\pi$ is a representation, the second that it carries the involution of the algebra to the adjoint of the operators; the two together are what makes the pair of an involutive algebra and a formed module into a ${}^{*}$-object. When no form is present the adjoint is undefined and the notion collapses to the representation.

### The left and the right regular representations

**Theorem.** With respect to the trace pairing $\beta$, the left and the right regular representations are ${}^{*}$-representations of $A$ on the regular module:

$$
(L_a)^{\dagger} = L_{a^{*}}, \qquad (R_b)^{\dagger} = R_{b^{*}} .
$$

Equivalently, $L : A \to \operatorname{End}_F(A)$ is a ${}^{*}$-homomorphism from $A$ with its involution to the operator algebra with its adjoint, and so is $R$ read through the opposite ring.

**Proof.** For the left multiplication, $\beta(L_a x, y) = \tau(a x y^{*}) = \tau(x y^{*} a)$ by the cyclicity of $\tau$, and $\beta(x, L_{a^{*}}y) = \tau(x\,(a^{*}y)^{*}) = \tau(x\,y^{*}a)$ because $(a^{*}y)^{*} = y^{*}\,a$. The two agree, so $(L_a)^{\dagger} = L_{a^{*}}$ by uniqueness. For the right multiplication, $\beta(R_b x, y) = \tau(x b y^{*}) = \tau(x y^{*} b)$ and $\beta(x, R_{b^{*}}y) = \tau(x\,(y b^{*})^{*}) = \tau(x\, b\, y^{*})$, so $(R_b)^{\dagger} = R_{b^{*}}$; the computation is the same with the sides exchanged, and it is the representation-theoretic form of the twisted-pairing statement of *The Adjoint of the Left Multiplication on a Ring*.

**Corollary (the two-sided operators).** $(L_aR_b)^{\dagger} = R_{b^{*}}L_{a^{*}} = L_{a^{*}}R_{b^{*}}$, because the two representations commute.

**Proof.** Apply the theorem and the reversal of composition, then commute the two factors by $L_aR_b = R_bL_a$.

### The two adjoints of one module

**Remark (the contrast with the symmetric pairing).** The regular module carries two natural pairings, the symmetric one $\beta_0(x,y) = \tau(xy)$ of *The Adjoint of the Left Multiplication on a Ring* and the Hermitian one $\beta(x,y) = \tau(xy^{*})$. With respect to $\beta_0$ the adjoint of the left multiplication is the right multiplication, $L_a^{*} = R_a$, and the left regular representation is not a ${}^{*}$-representation but a representation whose adjoint exchanges the two sides; with respect to $\beta$ the adjoint of the left multiplication is the left multiplication by the image, $(L_a)^{\dagger} = L_{a^{*}}$, and the representation is a ${}^{*}$-representation. The two statements are not in conflict: they are the adjoints for two different forms, and the involution is precisely the isomorphism between the two pairings.

## The Operator Dictionary

### Self-adjoint, normal and unitary elements

**Proposition.** For the involution $\sigma$ and an element $a \in A$, the left regular operator $L_a$ satisfies

$$
L_a^{\dagger} = L_{a} \iff a = a^{*}, \qquad L_aL_a^{\dagger} = L_a^{\dagger}L_a \iff aa^{*} = a^{*}a, \qquad L_a^{\dagger}L_a = \mathrm{id} \iff a^{*}a = 1 ,
$$

and the same three statements hold for $R_a$. Hence the self-adjoint elements of $A$ become self-adjoint operators, the normal elements become normal operators, and the unitary elements become unitary operators, the last with the one-sided condition made two-sided by invertibility.

**Proof.** By the theorem $L_a^{\dagger} = L_{a^{*}}$, and $L$ is injective, so each identity reduces to the corresponding identity in $A$: $L_a = L_{a^{*}}$ is $a = a^{*}$, $L_aL_{a^{*}} = L_{a^{*}}L_a$ is $aa^{*} = a^{*}a$, and $L_{a^{*}}L_a = L_{a^{*}a} = \mathrm{id}$ is $a^{*}a = 1$, the unitary condition. The statements for $R$ are identical.

**Corollary (the centre of the operator algebra).** The scalar operators correspond to the central elements, and the operators that are images of central self-adjoint elements are the self-adjoint operators in the centre of $\operatorname{End}_F(A)$; the central unitary elements give the unitary scalar-type operators, as in *The Regular Bimodule over an Involutive Ring*.

**Proof.** The centre of the image is the image of the centre by the corollary of *The Regular Representation as an Algebra of Operators*, and a central element is self-adjoint or unitary according to the same conditions on $a$.

### The commutant is the conjugate of the representation

**Proposition.** For every $a \in A$ the right multiplication is the $\sigma$-conjugate of a left multiplication,

$$
R_a = \sigma\,L_{a^{*}}\,\sigma ,
$$

so the commutant $L(A)' = R(A)$ is the conjugate of the representation, and it is stable under the adjoint. Consequently the adjoint maps $L(A)$ into itself, $R(A)$ into itself, and the commutant of a ${}^{*}$-stable subalgebra is ${}^{*}$-stable.

**Proof.** $\sigma L_{a^{*}}\sigma(x) = \sigma(a^{*}\sigma(x)) = \sigma(\sigma(x))\,\sigma(a^{*}) = x a$, which is $R_a$, using $\sigma^2 = \mathrm{id}$ and $\sigma(a^{*}) = a$. Since $L(A)$ and $R(A)$ are each carried into themselves by ${}^{\dagger}$, and since the operator $T \mapsto T^{\dagger}$ is an involution, an operator commuting with all of $L(A)$ has an adjoint commuting with all of $L(A)$, so the commutant is stable as well.

**Remark (the representation is self-adjoint in the commutant).** The left regular representation has commutant the conjugate of the right one, $L(A)' = R(A) = \sigma L(A)\sigma$, so the two halves of the regular bimodule are exchanged by the involution. Without the involution the two halves are the opposite algebras $A$ and $A^{\mathrm{op}}$; with it they become isomorphic and the representation and its commutant are the same algebra up to $\sigma$, which is the operator-level form of $A \cong A^{\mathrm{op}}$ in *Involutive Rings*.

### The star-closure of the image

**Corollary.** $L(A)$ and $R(A)$ are ${}^{*}$-subalgebras of $\operatorname{End}_F(A)$ for the adjoint involution of the trace pairing, and $L : A \to L(A)$ is an isomorphism of involutive algebras.

**Proof.** The theorem gives $L(A)^{\dagger} = L(A)$ and $R(A)^{\dagger} = R(A)$; the second statement is that $L$ is bijective and $L_{a^{*}} = L_a^{\dagger}$.

## Examples

### The matrix algebra

Let $A = M_n(\mathbb{C})$ with $X^{*} = \overline{X}^{\mathsf{T}}$ and $\tau$ the matrix trace, so that $\beta(X,Y) = \operatorname{tr}(XY^{*})$ is the Hilbert–Schmidt form. The adjoint of $T \in \operatorname{End}_\mathbb{C}(M_n(\mathbb{C}))$ is its conjugate transpose for the Hilbert–Schmidt form, the left regular operators satisfy $(L_X)^{\dagger} = L_{X^{*}}$, and the self-adjoint, the normal and the unitary matrices give self-adjoint, normal and unitary operators. The left regular representation embeds $M_n(\mathbb{C})$ as a ${}^{*}$-subalgebra of the operators on the $n^2$-dimensional space of matrices; its positivity and its completion into an operator algebra are Part II.

### The group algebra

Let $A = F[G]$ with $g^{*} = g^{-1}$ and let $\tau$ be the coefficient of the identity, which is $\sigma$-invariant since the involution permutes the group basis. Then $\beta(x,y)$ is the coefficient of the identity in $x\sigma(y)$, and on the group basis $\beta(g,h) = 1$ for $g = h$ and $\beta(g,h) = 0$ otherwise: the group basis is orthonormal. The regular representation is unitary, $(L_g)^{\dagger} = L_{g^{-1}}$, and the unitary elements of $A$ include the group elements, in agreement with the group picture of *Unitary Endomorphisms* and with the orthogonal basis of the regular representation of a finite group.

### The commutative case with the identity involution

If $A$ is commutative and $\sigma$ is the identity then $a^{*} = a$, the trace pairing is symmetric, the adjoint involution of the operator algebra is the transpose in the sense of *The Transpose as an Adjoint*, the left and the right regular representations coincide, and every multiplication operator is self-adjoint: the regular representation of a commutative ring is a representation by self-adjoint operators, which is the algebraic statement whose spectral theory belongs to Part III.

## Summary

An involution $\sigma$ on a ring $A$ together with a $\sigma$-invariant trace $\tau$ defines the Hermitian form $\beta(x,y) = \tau(xy^{*})$ on the regular module, and this form defines the adjoint $T \mapsto T^{\dagger}$ on the operator algebra $\operatorname{End}_F(A)$, additive, of order two and reversing composition, $\sigma$-semilinear in the scalar. With respect to it the left and the right regular representations are ${}^{*}$-representations, $(L_a)^{\dagger} = L_{a^{*}}$ and $(R_b)^{\dagger} = R_{b^{*}}$, and the two-sided operators satisfy $(L_aR_b)^{\dagger} = L_{a^{*}}R_{b^{*}}$. The same module carries the symmetric pairing $\beta_0(x,y) = \tau(xy)$, for which the adjoint of $L_a$ is $R_a$ and the representation is not a ${}^{*}$-representation; the involution is the isomorphism between the two pairings, and the two statements are the two adjoints of one module. The self-adjoint, the normal and the unitary elements of $A$ are carried to operators of the same kind, the commutant $L(A)' = R(A)$ is the conjugate of the representation and stable under the adjoint, and $L(A)$, $R(A)$ are ${}^{*}$-subalgebras with $L$ an isomorphism of involutive algebras. The matrix algebra with the conjugate transpose is the ${}^{*}$-algebra case, the group algebra with the orthonormal basis of the regular representation is the unitary case, and the commutative ring with the identity involution is the case in which every multiplication operator is self-adjoint. The positivity of the form and the operator theory it completes are Part II.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma$, $a^{*} = \sigma(a)$ | the involution of the ring |
| $\tau$ | a $\sigma$-invariant trace |
| $\beta(x,y) = \tau(x\sigma(y))$ | the trace pairing on the regular module, Hermitian |
| $T^{\dagger}$ | the adjoint of an operator, $\beta(Tx,y) = \beta(x,T^{\dagger}y)$ |
| $(ST)^{\dagger} = T^{\dagger}S^{\dagger}$ | the adjoint involution of the operator algebra |
| $(L_a)^{\dagger} = L_{a^{*}}$, $(R_b)^{\dagger} = R_{b^{*}}$ | the regular representations are ${}^{*}$-representations |
| $(L_aR_b)^{\dagger} = L_{a^{*}}R_{b^{*}}$ | the adjoint of a two-sided operator |
| $a = a^{*} \Rightarrow L_a^{\dagger} = L_a$ | self-adjoint elements give self-adjoint operators |
| $R_a = \sigma L_{a^{*}}\sigma$ | the commutant is the conjugate of the representation |
| $L(A)$, $R(A)$ ${}^{*}$-subalgebras | the images are stable under the adjoint |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for sesquilinear and Hermitian forms, the adjoint of an endomorphism and the unitary group.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the symmetric and skew elements and the adjoint properties of the regular operators.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society, 1956), for the adjoint involution of an endomorphism ring and the regular representation.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the involutions, the forms they define and the unitary groups.
- Tsit-Yuen Lam, *Lectures on Modules and Rings* (Springer, 1999), for the sesquilinear forms over an involutive ring and the endomorphism ring of the regular module.
