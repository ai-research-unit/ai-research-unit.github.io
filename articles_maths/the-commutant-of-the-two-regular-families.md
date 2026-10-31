# __The Commutant of the Two Regular Families__

## Introduction

**The subject.** The left and the right regular operators are two copies of the algebra inside the operator space, one for each side. *The Left Regular Operators on the Biquaternion Algebra* and *The Right Regular Operators on the Biquaternion Algebra* study the two families separately. This article studies them together, and answers the one question that the two separate articles cannot answer: which operators commute with which family.

**What the article proves.** Three statements, and they are exact. Every left multiplication commutes with every right multiplication, $L_{\tilde Q}R_{\tilde P}=R_{\tilde P}L_{\tilde Q}$. The commutant of the left copy is the right copy, $L(\mathbb{B})'=R(\mathbb{B})$, and the commutant of the right copy is the left copy, $R(\mathbb{B})'=L(\mathbb{B})$. The two copies meet in the scalars, $L(\mathbb{B})\cap R(\mathbb{B})=\mathbb{C}\cdot\mathrm I_4$.

**What the article does not do.** It contains no two-sided operator $T_{\tilde Q,\tilde P}$, no adjoint, no form and no example. The generation statement for the two-sided family, with its proof, is *Two-Sided Operators on the Biquaternion Algebra*; the association of the two families with the plain form is *The Four Adjoints of the Biquaternion Algebra in Examples*. This article is exactly its title: the commutant, and nothing else.

**The letters.** The left operator is $L_{\tilde Q}$, the right operator is $R_{\tilde P}$, and the argument is $X$. The prime is the commutant: for a set $\mathcal{S}$ of operators, $\mathcal{S}'=\{T:TS=ST\ \text{for every}\ S\in\mathcal{S}\}$. The conventions of the four letters and the set names are *Operator Family Conventions*.

**Boundaries.** The algebra and its centre are *The Biquaternion Algebra*; the two families are *The Left Regular Operators on the Biquaternion Algebra* and *The Right Regular Operators on the Biquaternion Algebra*; the matrix displays are the two $M_4(\mathbb{C})$ representation articles; the set names are *Operator Family Conventions*.

## The Commutation $L_{\tilde Q}R_{\tilde P}=R_{\tilde P}L_{\tilde Q}$

### The Identity

**Theorem (the commutation).** For all $\tilde Q,\tilde P\in\mathbb{B}$,

$$
L_{\tilde Q}R_{\tilde P}=R_{\tilde P}L_{\tilde Q}.
$$

*Proof.* For every $X$, $(L_{\tilde Q}R_{\tilde P})(X)=L_{\tilde Q}(X\tilde P)=\tilde QX\tilde P$, and $(R_{\tilde P}L_{\tilde Q})(X)=R_{\tilde P}(\tilde QX)=\tilde QX\tilde P$. The two values are equal by associativity.

**The reading.** The identity is associativity and nothing else. The left multiplication acts on the left factor, the right multiplication on the right factor, and the two actions do not interfere. The same computation gives $L_{\tilde Q}L_{\tilde P}=L_{\tilde Q\tilde P}$ and $R_{\tilde Q}R_{\tilde P}=R_{\tilde P\tilde Q}$; the three laws together say that the two copies generate a bimodule structure on the algebra, with the left copy acting on the left and the right copy on the right.

**The two copies centralise each other.** The identity says that every element of $L(\mathbb{B})$ commutes with every element of $R(\mathbb{B})$. In the language of commutants, $L(\mathbb{B})\subseteq R(\mathbb{B})'$ and $R(\mathbb{B})\subseteq L(\mathbb{B})'$. The next section proves that the two inclusions are equalities.

### What It Implies for Products

**The order of a mixed product.** A product of a left and a right operator can be written in either order, $L_{\tilde Q}R_{\tilde P}=R_{\tilde P}L_{\tilde Q}$. The product is therefore determined by the pair $(\tilde Q,\tilde P)$ and not by the order of the two factors, and a display that writes one order is not making a choice.

**The closure of the products.** A product of two left operators is a left operator, a product of two right operators is a right operator, and a mixed product can be regrouped but not reduced to one side. The set of products is closed under composition in the sense that every product of two products is again a product, with the parameters composed on each side; the span of the products and its dimension are the subject of *Two-Sided Operators on the Biquaternion Algebra*, where the generation theorem is proved. This article uses only the commutation, not the generation.

**The bimodule reading.** The algebra is a left module over the left copy and a right module over the right copy, and the two actions commute. The identity is the module axiom, read on the two copies; it is the reason the two-sided family can be built from the pair without a compatibility condition between the two parameters.

## The Two Centralisers

### $L(\mathbb{B})'=R(\mathbb{B})$

**Theorem (the first centraliser).** An operator $T\in\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ commutes with every left multiplication exactly when it is a right multiplication:

$$
L(\mathbb{B})'=R(\mathbb{B}).
$$

*Proof.* If $T=R_{\tilde P}$, then $TL_{\tilde Q}=R_{\tilde P}L_{\tilde Q}=L_{\tilde Q}R_{\tilde P}=L_{\tilde Q}T$ by the commutation, so $R(\mathbb{B})\subseteq L(\mathbb{B})'$.

Conversely, let $T$ commute with every $L_{\tilde Q}$. For every $\tilde Q$,

$$
T(\tilde Q)=T(L_{\tilde Q}e_t)=L_{\tilde Q}T(e_t)=\tilde Q\,T(e_t).
$$

Put $\tilde P=T(e_t)$. Then $T(\tilde Q)=\tilde Q\tilde P=R_{\tilde P}(\tilde Q)$ for every $\tilde Q$, so $T=R_{\tilde P}$. Hence $L(\mathbb{B})'\subseteq R(\mathbb{B})$, and the two inclusions give the equality.

**The proof read once.** The unit is the probe: an operator that commutes with all left multiplications is determined by its value at $e_t$, and that value is a right multiplier. The same argument with the roles exchanged gives the second centraliser.

**The exactness.** The equality is exact, not a containment up to a scalar. Every operator in the commutant is a right multiplication, and every right multiplication is in the commutant; there is no extra operator and no missing one.

### $R(\mathbb{B})'=L(\mathbb{B})$

**Theorem (the second centraliser).** An operator $T\in\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ commutes with every right multiplication exactly when it is a left multiplication:

$$
R(\mathbb{B})'=L(\mathbb{B}).
$$

*Proof.* If $T=L_{\tilde Q}$, then $TR_{\tilde P}=L_{\tilde Q}R_{\tilde P}=R_{\tilde P}L_{\tilde Q}=R_{\tilde P}T$, so $L(\mathbb{B})\subseteq R(\mathbb{B})'$.

Conversely, let $T$ commute with every $R_{\tilde P}$. For every $\tilde P$,

$$
T(\tilde P)=T(R_{\tilde P}e_t)=R_{\tilde P}T(e_t)=T(e_t)\tilde P.
$$

Put $\tilde Q=T(e_t)$. Then $T(\tilde P)=\tilde Q\tilde P=L_{\tilde Q}(\tilde P)$ for every $\tilde P$, so $T=L_{\tilde Q}$. Hence $R(\mathbb{B})'\subseteq L(\mathbb{B})$, and the two inclusions give the equality.

**The symmetry.** The two proofs are the same proof with the two sides exchanged. The left copy is the commutant of the right copy, and the right copy is the commutant of the left copy; neither is larger than the other, and the pair is a pair of mutual centralisers.

## The Intersection $L(\mathbb{B})\cap R(\mathbb{B})=\mathbb{C}\cdot\mathrm I_4$

### The Proof

**Theorem (the intersection).** An operator that is both a left multiplication and a right multiplication is a scalar multiple of the identity:

$$
L(\mathbb{B})\cap R(\mathbb{B})=\mathbb{C}\cdot\mathrm I_4.
$$

*Proof.* Let $L_{\tilde Q}=R_{\tilde P}$. Evaluate at the unit:

$$
\tilde Q=L_{\tilde Q}(e_t)=R_{\tilde P}(e_t)=\tilde P .
$$

So $\tilde Q=\tilde P$, and the operator is $L_{\tilde Q}=R_{\tilde Q}$. Then, for every $X$,

$$
\tilde QX=X\tilde Q,
$$

so $\tilde Q$ is central. The centre of the biquaternion algebra is $\mathbb{C}$, by *The Biquaternion Algebra*, §*The Scalars Are the Centre*: a central element is a complex multiple of $e_t$. Hence $\tilde Q=\lambda e_t$ and $L_{\tilde Q}=\lambda\,\mathrm I_4$.

Conversely, every $\lambda\,\mathrm I_4$ is $L_{\lambda e_t}$ and also $R_{\lambda e_t}$, so the line $\mathbb{C}\cdot\mathrm I_4$ is contained in the intersection. The two inclusions give the equality.

**The three steps.** The proof has three steps, and each is a different statement: equality at the unit gives $\tilde Q=\tilde P$; the equality of the two operators then gives the centrality of $\tilde Q$; the centre of the algebra gives the scalar. The first step evaluates both operators at the unit, the second uses the definition of the two operators, and the third the structure of the algebra.

### The Scalar as the Only Freedom

**The one-dimensional intersection.** The intersection is the line spanned by $\mathrm I_4$. It is complex one-dimensional, and its complex dimension is the complex dimension of the centre of the algebra. The scalar is the only freedom: an operator that is both a left and a right multiplication is a scalar, and every scalar is such an operator.

**The two copies are incomparable.** For a noncentral $\tilde Q$, the left multiplication $L_{\tilde Q}$ is not a right multiplication, and the right multiplication $R_{\tilde Q}$ is not a left multiplication, by the theorem. Neither copy contains the other, and their intersection is the scalar line. The two copies are therefore distinct except at the centre, and the distinction is the noncommutativity of the algebra.

**The same scalar on both sides.** The scalar operator $\lambda\mathrm I_4$ is $L_{\lambda e_t}$ and $R_{\lambda e_t}$; the parameter is the central element $\lambda e_t$, not an arbitrary element. The freedom is one complex number, and it is the same number on both sides.

## Summary

The two regular families commute element by element, $L_{\tilde Q}R_{\tilde P}=R_{\tilde P}L_{\tilde Q}$, and the identity is associativity. The commutant of the left copy is the right copy, $L(\mathbb{B})'=R(\mathbb{B})$, and the commutant of the right copy is the left copy, $R(\mathbb{B})'=L(\mathbb{B})$; the proofs evaluate a commuting operator at the unit and read the multiplier. The two copies meet in the scalars, $L(\mathbb{B})\cap R(\mathbb{B})=\mathbb{C}\cdot\mathrm I_4$: equality at the unit gives the same parameter, the equality of the two operators gives a central element, and the centre of the algebra is $\mathbb{C}$.

The two copies are therefore mutual centralisers and incomparable; their only common operators are the scalars. The products of the two families, their span and the generation theorem are *Two-Sided Operators on the Biquaternion Algebra*; the association of the two families with the plain form is *The Four Adjoints of the Biquaternion Algebra in Examples*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L(\mathbb{B})$ | The set of the left regular operators, the left copy |
| $R(\mathbb{B})$ | The set of the right regular operators, the right copy |
| $\mathcal{S}'$ | The commutant of the set $\mathcal{S}$ |
| $L(\mathbb{B})'=R(\mathbb{B})$ | The first centraliser |
| $R(\mathbb{B})'=L(\mathbb{B})$ | The second centraliser |
| $L(\mathbb{B})\cap R(\mathbb{B})=\mathbb{C}\cdot\mathrm I_4$ | The intersection, the scalar line |
| $\mathbb{C}\cdot e_t$ | The centre of $\mathbb{B}$, the parameter of the scalars |

## Further Reading

- [The Left Regular Operators on the Biquaternion Algebra](the-left-regular-operators-on-the-biquaternion-algebra.html), for the left family and its injectivity.
- [The Right Regular Operators on the Biquaternion Algebra](the-right-regular-operators-on-the-biquaternion-algebra.html), for the right family and its injectivity.
- [$M_4(\mathbb{C})$ Representation : The Left Regular Operators on the Biquaternion Algebra](m4c-representation-the-left-regular-operators-on-the-biquaternion-algebra.html), for the left matrix.
- [$M_4(\mathbb{C})$ Representation : The Right Regular Operators on the Biquaternion Algebra](m4c-representation-the-right-regular-operators-on-the-biquaternion-algebra.html), for the right matrix.
- [The Biquaternion Algebra](the-biquaternion-algebra.html), for the centre.
- [Two-Sided Operators on the Biquaternion Algebra](two-sided-operators-on-the-biquaternion-algebra.html), for the products and the generation theorem.
- [Operator Family Conventions](conventions-of-the-operator-families.html), for the letters and the set names.
