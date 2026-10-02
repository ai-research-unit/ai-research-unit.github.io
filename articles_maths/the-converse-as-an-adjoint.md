
# __The Converse as an Adjoint__

## Introduction

For a relation $R \subseteq X \times Y$ the converse $R^{-1} \subseteq Y \times X$ is the involution
studied in *The Converse Relation as an Operator* and *Relation Algebras and the Converse*. This
article reads the converse through a **pairing** of relations and shows that it is the **adjoint** of
$R$ for that pairing: the operator "compose on the left with $R$" has, under the pairing $\langle U, V
\rangle = U^{-1} ; V$, the adjoint "compose on the left with $R^{-1}$", and the identity

$$
\langle R ; S, T \rangle = \langle S, R^{-1} ; T \rangle
$$

is the adjointness. The same converse computes the right adjoint of composition in the residuation of
*Operators on a Poset*, $R \backslash T = \overline{R^{-1} ; \overline{T}}$, and the **unit** and
**counit** of the adjunction, $R^{-1} ; R$ and $R ; R^{-1}$, measure exactly when $R$ is surjective or
functional. The article develops the pairing, the Galois reading and the unit and counit, and it is the
first article of the `- * Operator Theory` group, in which the operator itself carries the involution.

The article presupposes *Relation Algebras and the Converse* and *The Converse Relation as an
Operator*, which supply the converse, composition and their laws, and *Operators on a Poset*, for the
residuals and the Galois connections. It names no form, no norm and no topology; the Hilbert-space
adjoint, where the pairing is an inner product, is Part II and the `- * Operator Theory` group, and is
not used.

## The Pairing of Relations

**Definition.** Let $X$ and $Z$ be sets. The **pairing** of two relations $U, V \subseteq X \times Z$
is the relation

$$
\langle U, V \rangle = U^{-1} ; V \subseteq Z \times Z .
$$

**Proposition.** The pairing is additive in each variable and satisfies $\langle U, V \rangle^{-1} =
\langle V, U \rangle$; it is nondegenerate, in the sense that $\langle U, W \rangle \subseteq \langle V,
W \rangle$ for all $W$ implies $U \subseteq V$, and dually.

**Proof.** Composition distributes over unions, so the pairing is additive. The identity is
$(U^{-1};V)^{-1} = V^{-1};U = \langle V,U \rangle$ by the law of the converse. For the nondegeneracy,
take $W = Z \times Z$, the greatest relation, so that $\langle U, W \rangle = U^{-1} ; (Z \times Z)$ is
$Z \times Z$ if $U \neq \emptyset$ and $\emptyset$ if $U = \emptyset$; the inclusion for this $W$ forces
$U = \emptyset$ whenever $V = \emptyset$, and iterating over the elements of $X$ gives $U \subseteq V$.

**Theorem (adjointness).** For relations $R \subseteq X \times Y$, $S \subseteq Y \times Z$ and $T
\subseteq X \times Z$,

$$
\langle R ; S, T \rangle = \langle S, R^{-1} ; T \rangle .
$$

Hence the operator $L_R : S \mapsto R ; S$ on relations has, under the pairing, the adjoint $L_{R^{-1}}
: T \mapsto R^{-1} ; T$, and the adjoint of $L_R$ is $L_{R^{-1}}$.

**Proof.** By the law of the converse for a composite, $(R;S)^{-1} = S^{-1};R^{-1}$, so $\langle R;S, T
\rangle = (R;S)^{-1};T = S^{-1};R^{-1};T = S^{-1};(R^{-1};T) = \langle S, R^{-1};T \rangle$ by
associativity. The adjoint statement is the identity read as the definition of the adjoint operator for
the pairing.

**Corollary.** The adjoint operation on the operator layer, $L \mapsto L^{*}$ with $\langle L S, T
\rangle = \langle S, L^{*} T \rangle$, is an involution: $(L_R)^{*} = L_{R^{-1}}$ and $(L_{R^{-1}})^{*}
= L_R$. On the operators that commute with the converse it is the identity, and $L_R$ is self-adjoint
exactly when $R = R^{-1}$, that is, when $R$ is symmetric.

**Proof.** The two identities are the theorem applied twice; $L_R = L_{R^{-1}}$ means $R;S = R^{-1};S$
for all $S$, which with $S = \Delta_Y$ gives $R = R^{-1}$.

## The Galois Reading

**Theorem (residuation).** For a fixed relation $R \subseteq X \times Y$ the operator $L_R : S \mapsto R
; S$ is residuated, with right adjoint $T \mapsto R \backslash T$ where

$$
R \backslash T = \overline{R^{-1} ; \overline{T}} \subseteq Y \times Z .
$$

Its **unit** and **counit** are the inclusions

$$
S \subseteq R \backslash (R ; S), \qquad R ; (R \backslash T) \subseteq T ,
$$

which hold for all $S, T$.

**Proof.** The residual identity $R;S \subseteq T \Leftrightarrow S \subseteq R \backslash T$ is proved
in *Relation Algebras and the Converse*; the displayed formula for $R \backslash T$ follows from it
because $R^{-1};\overline{T}$ is the set of $(y,z)$ with some $(x,y) \in R$ and $(x,z) \notin T$, whose
complement is the set of $(y,z)$ with every $(x,y) \in R$ giving $(x,z) \in T$, which is $R \backslash
T$. The unit and counit are the two inclusions of the adjunction, with $S$ arbitrary in the first and
$T$ arbitrary in the second.

The formula expresses the Galois reading of the scope: the converse $R^{-1}$ is exactly what computes
the right adjoint of composition with $R$, and the adjunction is the residuation of *Operators on a
Poset*. The operator $L_{R^{-1}}$ of the previous section and the right adjoint $T \mapsto R \backslash
T$ are two different faces of the same converse: the first is the adjoint for the pairing, the second
the adjoint for the order.

## Unit and Counit

The unit $R^{-1} ; R$ and the counit $R ; R^{-1}$ of the pairing adjunction are relations on $Y$ and on
$Y$ respectively, and their comparison with the diagonal decides the nature of $R$.

**Theorem.** For a relation $R \subseteq X \times Y$:

1. $\Delta_Y \subseteq R^{-1} ; R$ if and only if $R$ is **surjective**, that is, every $y \in Y$ is
   related to some $x \in X$;
2. $R ; R^{-1} \subseteq \Delta_Y$ if and only if $R$ is a **partial function**, that is, each $y \in
   Y$ is the image of at most one $x$;
3. both hold, so that $R^{-1}$ is a two-sided adjoint of $R$, if and only if $R$ is a bijection, in
   which case $R^{-1}$ is the inverse function.

**Proof.** $(y,y') \in R^{-1};R$ means that some $x$ is related to both $y$ and $y'$; the diagonal is
contained exactly when every $y$ is related to at least one $x$, which is surjectivity. $(y,y') \in
R;R^{-1}$ means that some $z$ with $(y,z) \in R$ and $(y',z) \in R$ exists — that is, $y$ and $y'$
share an image; this is contained in the diagonal exactly when no two distinct elements share an image,
which is the partial-function condition. In that case $R$ is a partial function and $R^{-1}$ is its
partially defined inverse; with the unit as well, the function is total and its inverse is two-sided.

**Corollary.** An adjunction $R \dashv R^{-1}$ in the bicategory of relations exists exactly when $R$
is a bijection; for a general relation the unit and counit are the two defects of $R$, the failure of
surjectivity and the failure of single-valuedness.

**Proof.** The two conditions of the theorem are the unit and counit of the 2-categorical adjunction;
both hold exactly for a bijection, and each fails for the corresponding defect.

## Summary

The converse is the adjoint of a relation for the pairing $\langle U, V \rangle = U^{-1};V$: the
identity $\langle R;S, T \rangle = \langle S, R^{-1};T \rangle$ says that left composition with $R$ has,
as adjoint under the pairing, left composition with $R^{-1}$, and the adjoint operation is an involution
fixed exactly by the operators commuting with the converse.

The same converse computes the right adjoint of composition in the residuation, $R \backslash T =
\overline{R^{-1};\overline{T}}$, with unit $S \subseteq R \backslash (R;S)$ and counit $R ; (R
\backslash T) \subseteq T$. The unit $R^{-1};R$ and the counit $R;R^{-1}$ of the pairing measure
surjectivity and single-valuedness, so that $R$ and $R^{-1}$ are two-sided adjoints exactly when $R$ is
a bijection.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle U, V \rangle = U^{-1};V$ | The pairing of relations $X \to Z$ |
| $L_R : S \mapsto R;S$ | Left composition with $R$ |
| $L_{R^{-1}}$ | The adjoint of $L_R$ under the pairing |
| $R \backslash T = \overline{R^{-1};\overline{T}}$ | The right adjoint of $L_R$ in the residuation |
| $R^{-1};R$, $R;R^{-1}$ | Unit and counit; surjectivity and single-valuedness of $R$ |

## Further Reading

- Chris Brink, Wolfram Kahl and Gunther Schmidt, *Relational Methods in Computer Science* (Springer, 1997), for the pairing of relations, residuation and the converse as an adjoint.
- Gunther Schmidt and Thomas Ströhlein, *Relations and Graphs* (Springer, 1993), for the residual calculus and the adjointness of the converse.
- Michael Barr and Charles Wells, *Category Theory for Computing Science*, 3rd ed. (CRM, 1999), for adjoint functors, units and counits, and the bicategory of relations.
- Francis Borceux, *Handbook of Categorical Algebra 1* (Cambridge University Press, 1994), for adjunctions, units and counits and their duality.
