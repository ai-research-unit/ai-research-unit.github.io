# __The Hermitian Jordan Algebra of a Form__

## Introduction

The self-adjoint operators of *Self-Adjoint and Skew Operators of a Form* close under the anticommutator, and the resulting structure is a **Jordan algebra**: commutative, with the Jordan identity but without associativity. This article identifies it, computes its product and its unit, and links it to the two structures that surround it — the Lie algebra of the skew operators (*The Unitary Group of a Form and Its Lie Algebra*) and the Hermitian forms of the layer (*Polarisation and the Hermitian Square*).

Three facts are the substance. The product $T \circ S = \tfrac{1}{2}(TS + ST)$ of two self-adjoint operators is self-adjoint by the sign rule, so the self-adjoint part of the operator algebra is closed under the symmetrised product; the identity operator is the unit; the Jordan identity holds because the underlying product of the operators is associative, which makes the structure a **special** Jordan algebra, that is, one embedded in an associative algebra under the symmetrised product. The correspondence $T \mapsto Q_{T}$, $Q_{T}(x) = h(Tx,x)$, identifies the self-adjoint operators with the Hermitian forms of the shape $h(T\cdot,\cdot)$, and it is additive: the Jordan algebra of the form is a space of Hermitian forms with the anticommutator transported to the forms. And the **sandwich** $\Theta_{T}(y) = TyT^{*}$ coincides with the **quadratic representation** $U_{T}(S) = TST$ of the Jordan theory exactly when $T$ is self-adjoint, which is the identity that carries the two-sided operators of the category into the Jordan structure.

The Jordan algebra of the *elements* of a sesqualgebra — the self-adjoint elements with the symmetrised product — is *The Hermitian Jordan Algebra* and *Self-Adjoint Elements and the Positive Cone*; this article is the operator-level companion, and the positivity of the operators and the cone are Part II: *Positivity and the Hermitian Cone of a Hermitian Algebra with Hermitian Adjoint* and *Completely Positive Maps of a Hermitian Algebra with Hermitian Adjoint*. Throughout, $(A,*,h)$ is a sesqualgebra with a form with $h$ nonsingular, $2$ is invertible in the fixed ring, and the operators are the $R$-linear endomorphisms of $A$ admitting an adjoint for $h$.

## The Jordan Algebra of the Self-Adjoint Operators

**Definition.** The **symmetrised product** of two operators is $T \circ S = \tfrac{1}{2}(TS + ST)$, and the **self-adjoint part** of the operator algebra is

$$
\operatorname{Herm}(A,h) = \{T : T^{*} = T\} .
$$

**Proposition.** The self-adjoint part is closed under the symmetrised product and contains the identity; with the product $\circ$ it is a commutative algebra with unit $1$, and it satisfies the **Jordan identity**

$$
(T \circ S)\circ T^{2} = T \circ (S \circ T^{2}), \qquad T^{2} = T \circ T .
$$

**Proof.** Closure: the sign rule of *Self-Adjoint and Skew Operators of a Form* gives $(TS+ST)^{*} = TS+ST$ for self-adjoint $S, T$. Commutativity is the definition. The identity is self-adjoint and $1 \circ T = T$. The Jordan identity is the standard identity of the special Jordan algebras: it holds in every associative algebra for the symmetrised product, and the verification is the expansion of the two sides in the associative product combined with the associativity.

**Corollary.** The operator algebra with the involution $T \mapsto T^{*}$ is an associative algebra with an involution whose **hermitian part** is a Jordan algebra with the symmetrised product; the structure is special, and the general theory of the Jordan algebras with an involution is *The Hermitian Jordan Algebra* and *Hermitian and Skew-Hermitian Elements*.

## The Correspondence with the Hermitian Forms

**Proposition.** The map

$$
\operatorname{Herm}(A,h) \longrightarrow \{\text{Hermitian forms on } A\}, \qquad T \longmapsto Q_{T}, \quad Q_{T}(x) = h(Tx,x) ,
$$

is an injective $R^{\varsigma}$-linear map onto the Hermitian forms of the shape $h(T\cdot,\cdot)$ when the sesquilinear forms are determined by their diagonals — in particular over a field containing a scalar $\mathrm{i}$ with $\varsigma(\mathrm{i}) = -\mathrm{i}$; its inverse sends such a form back to its operator through the polarisation $\tfrac{1}{2}\bigl(Q(x+y) - Q(x) - Q(y)\bigr) = \tfrac{1}{2}\bigl(h(Tx,y) + h(Ty,x)\bigr)$ and the non-degeneracy of $h$.

**Proof.** The map is additive in $T$; it is valued in the Hermitian forms by the equivalence of *Self-Adjoint and Skew Operators of a Form*, and the polarisation formula is the polarisation identity of *Polarisation and the Hermitian Square* applied to $Q_{T}$. Its kernel is the set of the self-adjoint operators with $h(Tx,x) = 0$ for every $x$, which is zero under the hypothesis on the diagonal and is otherwise the part that the diagonal loses, by the remark of *The Form-Adjoint of an Operator*; the non-degeneracy of $h$ gives the injectivity on that kernel.

**Corollary.** The Jordan algebra of the self-adjoint operators is a space of Hermitian forms of the layer, and the symmetrised product corresponds to the product of the forms given by $Q_{T\circ S}(x) = \tfrac{1}{2}\bigl(h(TSx,x) + h(STx,x)\bigr)$; the compatibility of the operator product and the sesquilinearity of the form is what makes the correspondence a statement of the layer and not only of the operators.

## The Quadratic Representation and the Sandwich

**Definition.** The **quadratic representation** of an operator $T$ is $U_{T}(S) = TST$; it is an operator on the algebra of the operators.

**Proposition.** The sandwich $\Theta_{T}(y) = TyT^{*}$ of *The Form-Adjoint of the Multiplications* coincides with the quadratic representation exactly when $T$ is self-adjoint:

$$
T^{*} = T \implies \Theta_{T} = U_{T}, \qquad \text{and} \qquad \Theta_{T}(S) = TST^{*} .
$$

**Proof.** For a self-adjoint $T$ the definition of the sandwich gives $TyT^{*} = TyT$, which is the quadratic representation. The general statement is the definition of the sandwich read as an operator on the operator algebra.

**Corollary.** The quadratic representation preserves the Jordan algebra when $T$ is self-adjoint: $U_{T}$ maps $\operatorname{Herm}(A,h)$ to itself, and for invertible $T$ it is an automorphism of the Jordan structure up to the inverse, $U_{T}^{-1} = U_{T^{-1}}$; the structure group of the Jordan algebra is the group generated by the quadratic representations, and its linear part contains the unitary group acting by $S \mapsto USU^{-1}$.

**Proposition.** Let $u$ be unitary. The conjugation $S \mapsto uSu^{-1}$ is an automorphism of the Jordan algebra $\operatorname{Herm}(A,h)$, and its infinitesimal form is the derivation $S \mapsto [T,S]$ with $T$ skew-adjoint.

**Proof.** The conjugation by a unitary element is an algebra automorphism of the operators and commutes with the adjoint operation because $u^{*} = u^{-1}$; it therefore preserves the self-adjoint part and the symmetrised product. The infinitesimal statement is the derivative at $u = 1$ of the conjugation, which is the commutator, and the commutator is a derivation of the Jordan product by the associativity of the underlying product.

## Examples

### The Hermitian Matrices

On $M_n(\mathbb{C})$ with the trace form the self-adjoint operators are the Hermitian matrices and the Jordan algebra is the real vector space of the Hermitian matrices with the anticommutator $X \circ Y = \tfrac{1}{2}(XY+YX)$; the quadratic representation is $U_{X}(Y) = XYX$, the sandwich of the matrix algebra.

### The Orthogonal Case

At the trivial base involution and $* = \mathrm{id}$ the Jordan algebra is the space of the symmetric operators of the form with the anticommutator, and the derivations are the commutators with the skew operators of $\mathfrak{so}(G)$; the structure is the symmetric part of the theory of *The Orthogonal Lie Algebra*.

### The Biquaternions

On $\mathbb{B}$ with the dagger the self-adjoint operators are the Hermitian forms of the biquaternion algebra and the quadratic representation is the sandwich of *The Hermitian Sandwich in the Biquaternion Algebra with Hermitian Adjoint*; the positivity of the sandwich operators is the definite case and belongs to Part II.

## Summary

- The **self-adjoint operators** with the symmetrised product $T \circ S = \tfrac12(TS+ST)$ form a **Jordan algebra** with unit the identity, because the underlying operator product is associative; the structure is special.
- The Jordan identity holds by the associativity of the operators, and the closure under $\circ$ is the sign rule of the adjoint involution.
- The map $T \mapsto Q_{T}$, $Q_{T}(x) = h(Tx,x)$, identifies the self-adjoint operators with the Hermitian forms of the shape $h(T\cdot,\cdot)$, and it is additive and injective.
- The **quadratic representation** $U_{T}(S) = TST$ coincides with the sandwich exactly for self-adjoint $T$, and it preserves the Jordan algebra.
- The unitary group acts on the Jordan algebra by conjugation, and its infinitesimal action is the derivation $S \mapsto [T,S]$ with $T$ skew-adjoint.
- The positivity, the cone and the completely positive maps of the layer are Part II; the Jordan algebra of the elements of a sesqualgebra is *The Hermitian Jordan Algebra*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $T \circ S = \tfrac12(TS+ST)$ | the symmetrised product of the operators |
| $\operatorname{Herm}(A,h)$ | the self-adjoint operators of the form |
| $Q_{T}(x) = h(Tx,x)$ | the Hermitian form of a self-adjoint operator |
| $U_{T}(S) = TST$ | the quadratic representation |
| $\Theta_{T}(y) = TyT^{*}$ | the sandwich, equal to $U_{T}$ for self-adjoint $T$ |

## Further Reading

- Nathan Jacobson, *Structure and Representations of Jordan Algebras*, American Mathematical Society Colloquium Publications 39 (1968), for the Jordan algebra of the self-adjoint elements of an algebra with an involution and the quadratic representation.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings*, Grundlehren der mathematischen Wissenschaften 294 (Springer, 1991), for the hermitian part of an algebra with an involution.
- Kevin McCrimmon, *A Taste of Jordan Algebras*, Universitext (Springer, 2004), for the special Jordan algebras and the Jordan identity.
