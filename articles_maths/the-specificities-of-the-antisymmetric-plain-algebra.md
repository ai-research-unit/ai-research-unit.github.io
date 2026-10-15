# __The Specificities of the Antisymmetric Plain Algebra__

## Introduction

Of the twelve algebraic structures that the complex space
$\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries, exactly one carries the classical
theory of a **Lie algebra**: the **antisymmetric plain multiplication**
$\tilde P\wedge\tilde Q=\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)=\vec P\times\vec Q$ of
*Introduction to the Antisymmetric Plain Algebra of Biquaternions*, the multiplication named
$\mathrm{APA}$ in *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*. Every
structural result of the block belongs to it alone — the centre and the quotient, the derived
algebra and its identification with $\mathfrak{sl}(2,\mathbb{C})$, the invariant form, the Cartan
criteria and the Casimir element, the enveloping algebra and the matrix models — and this article
states the exact reason, in one law, and then separates the twelve.

The reason is the **Leibniz identity**, the statement that the left multiplication
$L^{\star}_{\tilde X}$ is a derivation of the product for every element. For an alternating product
that identity is equivalent to the **Jacobi identity**, and the block is the only one of the twelve
structures on which it holds at every element; equivalently, the block is the only **Lie product**
among the twelve. Each of the eleven others is built from the four general products by twisting a
slot with a conjugation or by (anti)symmetrising, and the ten non-alternating structures fail the
identity directly, on a witness, the criterion of the alternating case being unavailable to them;
the one other alternating structure, $\mathrm{AQA}$, fails it because it fails the Jacobi identity
that the alternating case requires.

The consequence is the point of the article. Only in the antisymmetric plain algebra are the centre
and the quotient, the derived algebra, the Killing form, the Cartan criteria, the Casimir element,
the enveloping algebra and the matrix models available as **theorems**. Elsewhere single elements do
behave well — the zero element gives the zero operator in all twelve, and in the associative general
plain product the commutator $\mathrm{ad}_{\tilde X}=L_{\tilde X}-R_{\tilde X}$ is a derivation for
every element though $L_{\tilde X}$ is not — and no other structure carries the theory. The one
genuine boundary case is the antisymmetric quaternionic product, whose bracket is alternating but
which fails the Jacobi identity; it is *The Jacobi Failure and the Associator Defect of the
Antisymmetric Quaternionic Algebra*, and it is stated here only as the boundary of the criterion.

**Placement.** The article is the closing entry of the *Specific Theory* section of the block, after
*The Lie Algebra of the Antisymmetric Plain Algebra* and after the six Common Theory articles
*Introduction to the Antisymmetric Plain Algebra of Biquaternions*, *Norm and Invertibility in the
Antisymmetric Plain Algebra*, *Zero Divisors of the Antisymmetric Plain Algebra*, *Square Roots of
One and the Idempotents of the Antisymmetric Plain Algebra*, *Square Roots of Zero and the
Nilpotents of the Antisymmetric Plain Algebra* and *Square Roots of a General Element in the
Antisymmetric Plain Algebra*, whose results it reads back as consequences of one law. It is
the twin of *The Specificities of the Symmetric Plain Algebra*, which states commutativity with the
Jordan identity as the criterion of the other half of the plain product and proves that the
symmetric plain product alone satisfies it; the two halves of the plain product are the two unique
structures of the twelve, the symmetric plain algebra the only Jordan product and the antisymmetric
plain algebra the only Lie product.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis
$e_0,e_1,e_2,e_3$ with $e_1e_2=e_3$ and central scalar imaginary $i$. The product written $\star$ is
a generic one, its identity stated at each use. The **left multiplication** of a product $\star$ by
$\tilde X$ is $L^{\star}_{\tilde X}:\tilde Y\mapsto\tilde X\star\tilde Y$, and the **adjoint map** is
$\mathrm{ad}^{\star}_{\tilde X}\tilde Y=\tilde X\star\tilde Y-\tilde Y\star\tilde X$, so that for an
alternating product $\mathrm{ad}^{\star}_{\tilde X}=2L^{\star}_{\tilde X}$. The twelve structures are
coded as in *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*: the code has
three letters, the first $\mathrm G$, $\mathrm S$ or $\mathrm A$ for the general product or its
symmetrisation or antisymmetrisation, the second $\mathrm P$ or $\mathrm Q$ for the plain or the
quaternionic row, and the third $\mathrm A$ or $\mathrm S$ for the algebra or sesqualgebra class,
as in $\mathrm{GPA}$, $\mathrm{SPA}$, $\mathrm{APA}$.

## The Criterion

**Definition (the Leibniz identity).** Let $\star$ be a product on $\mathbb{B}$. The product
satisfies the **Leibniz identity** when
$$
L^{\star}_{\tilde X}(\tilde Y\star\tilde Z)=(L^{\star}_{\tilde X}\tilde Y)\star\tilde Z
+\tilde Y\star(L^{\star}_{\tilde X}\tilde Z)\qquad\text{for all }\tilde X,\tilde Y,\tilde Z,
$$
equivalently
$$
\tilde X\star(\tilde Y\star\tilde Z)=(\tilde X\star\tilde Y)\star\tilde Z
+\tilde Y\star(\tilde X\star\tilde Z)\qquad\text{for all }\tilde X,\tilde Y,\tilde Z .
$$
The operator $L^{\star}_{\tilde X}$ is then a **derivation** of $\star$ for every $\tilde X$.

**Theorem (the criterion).** Let $\star$ be an **alternating** product. Then $\star$ satisfies the
Leibniz identity if and only if it satisfies the Jacobi identity.

*Proof.* Write
$$
\Lambda(\tilde X,\tilde Y,\tilde Z)=\tilde X\star(\tilde Y\star\tilde Z)
-(\tilde X\star\tilde Y)\star\tilde Z-\tilde Y\star(\tilde X\star\tilde Z)
$$
for the Leibniz defect and
$$
J(\tilde X,\tilde Y,\tilde Z)=(\tilde X\star\tilde Y)\star\tilde Z
+(\tilde Y\star\tilde Z)\star\tilde X+(\tilde Z\star\tilde X)\star\tilde Y
$$
for the cyclic sum. Alternation reverses each of the last two products, so the Leibniz defect is
$$
\Lambda=-(\tilde Y\star\tilde Z)\star\tilde X-(\tilde X\star\tilde Y)\star\tilde Z
+(\tilde X\star\tilde Z)\star\tilde Y .
$$
The last summand is $-(\tilde Z\star\tilde X)\star\tilde Y$ by the alternation of the two inner
factors, $(\tilde X\star\tilde Z)=-(\tilde Z\star\tilde X)$, so the bracket is exactly
$-J(\tilde X,\tilde Y,\tilde Z)$. Hence $\Lambda$ vanishes identically if and only if $J$ does,
which is the criterion. Computed exactly on general elements of $\mathbb{Q}(i)$ coefficients and
on triples of the units.

**Corollary (the block satisfies the law).** The antisymmetric plain multiplication is alternating
and satisfies the Jacobi identity, so it satisfies the Leibniz identity: every left multiplication
of the block is a derivation,
$$
L_{\tilde X}(\tilde Y\wedge\tilde Z)=(L_{\tilde X}\tilde Y)\wedge\tilde Z
+\tilde Y\wedge(L_{\tilde X}\tilde Z),\qquad
L_{\tilde X}\tilde Y=\tilde X\wedge\tilde Y .
$$

*Proof.* The alternation and the Jacobi identity are *Introduction to the Antisymmetric Plain
Algebra of Biquaternions*; the criterion above turns them into the Leibniz identity. The direct
reason is *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*: the
adjoint $\mathrm{ad}_{\tilde X}=2L_{\tilde X}$ is a derivation because the bracket is the
half-commutator of an associative product, and the halving carries the Leibniz rule of the
associativity to the block.

## The Operator Identity and the Adjoint Representation

**Proposition (the adjoint reading).** For an alternating product $\star$ and every $\tilde X$,
$$
\mathrm{ad}^{\star}_{\tilde X}=2L^{\star}_{\tilde X},
$$
so the Leibniz identity is the statement that the adjoint maps of $\star$ are derivations of
$\star$; for the block this is the statement that the left multiplications, which are the adjoint
maps of the block's own bracket, form a representation of the bracket by derivations,
$$
\mathrm{ad}^{\wedge}_{\tilde X\wedge\tilde Y}=[\mathrm{ad}^{\wedge}_{\tilde X},\mathrm{ad}^{\wedge}_{\tilde Y}],
\qquad
\mathrm{ad}^{\wedge}_{\tilde X}(\tilde Y\wedge\tilde Z)
=\mathrm{ad}^{\wedge}_{\tilde X}\tilde Y\wedge\tilde Z+\tilde Y\wedge\mathrm{ad}^{\wedge}_{\tilde X}\tilde Z ,
\qquad
\mathrm{ad}^{\wedge}_{\tilde X}=L_{\tilde X}=\tilde X\wedge\cdot .
$$

*Proof.* For an alternating product the adjoint is twice the left multiplication,
$\mathrm{ad}^{\star}_{\tilde X}=2L^{\star}_{\tilde X}$, because
$\tilde X\star\tilde Y-\tilde Y\star\tilde X=2\,\tilde X\star\tilde Y$. The bracket's own operator
is the halved adjoint $\mathrm{ad}^{\wedge}_{\tilde X}=L_{\tilde X}$, and its two identities are
the operator form of the Jacobi identity, $[L_{\tilde X},L_{\tilde Y}]=L_{\tilde X\wedge\tilde Y}$,
and the Leibniz identity carried to the bracket. The doubled adjoint carries the factor two
throughout,
$$
\mathrm{ad}_{\tilde X\wedge\tilde Y}=\tfrac12\,[\mathrm{ad}_{\tilde X},\mathrm{ad}_{\tilde Y}],
$$
which is the identity of the source article read with the doubled adjoint. Both are
*The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*, where the two
adjoints are kept apart.

**Corollary (the kernel and the image).** The adjoint representation of the block has kernel the
centre $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ and image the inner derivations, identified with the
derived algebra $\mathrm{Vect}(\mathbb{B})\cong\mathfrak{sl}(2,\mathbb{C})$:
$$
\ker\mathrm{ad}=\mathbb{C}_{\mathbb{B}},\qquad
\operatorname{Inn}(\mathfrak{g})=\{\mathrm{ad}_{\tilde P}\}
=\{\mathrm{ad}_{\vec P}:\vec P\in\mathrm{Vect}(\mathbb{B})\}\cong\mathfrak{sl}(2,\mathbb{C}).
$$

*Proof.* An adjoint vanishes exactly when the element brackets to zero with everything, which is
the centre $\mathbb{C}_{\mathbb{B}}$ (*The Lie Algebra of the Antisymmetric Plain Algebra*,
§*The Centre of the Bracket*); the image is the inner derivations, of complex dimension three
(*The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*,
§*The Inner Derivations*).

## The Isolation among the Twelve

One law separates the block from the other eleven. The block's product is **alternating** and satisfies the **Jacobi identity**; an alternating product with the Jacobi identity is a **Lie product**, and the block is the only Lie product of the twelve.

**Theorem (the isolation).** Of the twelve structures of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, the antisymmetric plain product is the only one all of whose left multiplications are derivations, equivalently the only **Lie product**.

*Proof.* The twelve are generated from the four general products by twisting a slot with a conjugation or by (anti)symmetrising, and the three operations decide the two clauses. The ten non-alternating structures fail the Leibniz identity directly, because the criterion of the alternating case is unavailable to them; the one other alternating structure, the antisymmetric quaternionic product, is alternating and fails the Jacobi identity, so by §*The Criterion* it fails the Leibniz identity too. The block is alternating by construction and satisfies the Jacobi identity, so it alone meets both clauses.

| family | structures | alternating | Jacobi | Leibniz identity |
|---|---|---|---|---|
| the plain product and its symmetrisation | GPA, SPA | no | — | fails by non-alternation |
| the antisymmetric plain product | APA | **yes** | **yes** | **yes**, the criterion |
| the quaternionic product and its symmetrisation | GQA, SQA | no | — | fails by non-alternation |
| the antisymmetric quaternionic product | AQA | yes | no | fails by the Jacobi defect at $(e_0,e_1,e_2)$ |
| the six sesquilinear structures | GPS, SPS, APS, GQS, SQS, AQS | no | — | fails by non-alternation |

The isolation is about the **law** and not about isolated elements, and the distinction is the boundary of the claim. Single elements of the other structures do give derivations — the zero element gives the zero operator in all twelve, and in the associative general plain product the commutator $\mathrm{ad}_{\tilde X}=L_{\tilde X}-R_{\tilde X}$ is a derivation for every element — but no other structure carries the law, and the theory needs the law at every element and not a case of it. The article therefore refuses the false strengthening "no other structure has a derivation" and states the true one: only here is every left multiplication a derivation.

## What the Criterion Delivers

The whole Lie theory of the block is a consequence of the criterion. Alternation is the law that makes the square of every element vanish, and it is shared with the antisymmetric quaternionic product; it is the criterion — the Jacobi identity, equivalently the Leibniz identity — that is the block's own and that makes the bracket a Lie bracket.

- **The bracket is a Lie algebra.** The block is alternating and satisfies the Jacobi identity, so
$(\mathbb{B},\wedge)$ is a complex Lie algebra, the complexification of the cross product of
$\mathbb{R}^{3}$.
- **The centre and the quotient.** The centre is the central line $\mathbb{C}_{\mathbb{B}}$ and the
quotient is the vector subspace $\mathrm{Vect}(\mathbb{B})$, of complex dimension three
(*The Lie Algebra of the Antisymmetric Plain Algebra*).
- **The derived algebra and the identifications.** The derived algebra is $\mathrm{Vect}(\mathbb{B})$,
isomorphic to $\mathfrak{sl}(2,\mathbb{C})$, with the real form $\mathfrak{su}(2)$ on the
anti-Hermitian subspace (*The Lie Algebra of the Antisymmetric Plain Algebra*).
- **The invariant form.** The Killing form is $\kappa(\tilde P,\tilde Q)=-2\,\vec P\cdot\vec Q$,
invariant and symmetric, of radical the centre; read on it the Cartan criteria give that the
algebra is not semisimple, its radical being the centre, and that its derived algebra
$\mathfrak{sl}(2,\mathbb{C})$ is simple; the form produces the Casimir element
(*The Killing Form of the Antisymmetric Plain Algebra*).
- **The derivations and the adjoint representation.** Every adjoint is a derivation, the inner
derivations are the adjoints of the vector subspace, and the outer derivations are computed in
*The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*.
- **The enveloping algebra and the matrix models.** The universal enveloping algebra of the bracket
is *The Lie Algebra of the Antisymmetric Plain Algebra*, and the two matrix models are
*The Antisymmetric Plain Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*
and *The Antisymmetric Plain Algebra in the $4\times4$ Matrix Element Representation
$M_4(\mathbb{C})_L$*, faithful on the derived algebra and with the centre as kernel.

**Remark (alternation and the criterion).** Two different laws are in force in the block, and they
are kept apart. **Alternation** is the law that makes the square of every element vanish, and it is
what the element-theory articles of the block record: the roots of $0$ are the whole punctured
space, the idempotent set is the origin, the nilpotents are the whole space and the zero divisors
are the whole punctured space (*Norm and Invertibility in the Antisymmetric Plain Algebra* and its
companions).
**The criterion** — the Jacobi identity, equivalently the Leibniz identity — is the further law
that makes the bracket a Lie bracket, and it is what the specific theory of the block records. The
two are independent: $\mathrm{AQA}$ is alternating and not Lie, and the associative general plain
product is Lie-admissible — its commutator is a Lie bracket — while being neither alternating nor
a Lie product in the sense fixed here.

## The Boundary of the Criterion

Two statements are easily confused and are kept apart here.

1. **As a law, the Leibniz identity is exactly the threshold.** The statement that
$L^{\star}_{\tilde X}$ is a derivation for every $\tilde X$, equivalently that the product is a
Lie product in the presence of alternation, is satisfied by the antisymmetric plain product and
by no other of the twelve.
2. **As a statement about one element, the identity can hold outside the block.** An operator
$L^{\star}_{\tilde X}$ may be a derivation in a structure that is not a Lie product, because the
identity is then demanded at one element and not at all of them. The zero element gives the zero
operator, a derivation, in all twelve; in the associative general plain product the derivation is
the commutator $\mathrm{ad}_{\tilde X}=L_{\tilde X}-R_{\tilde X}$, the difference of the two
multiplications and not $L_{\tilde X}$ alone, and it exists for every element; and the derived
subalgebra $\mathrm{Vect}(\mathbb{B})$ of the antisymmetric quaternionic product is a Lie algebra
under the restriction, although the product on the whole space is not (*The Jacobi Failure and the
Associator Defect of the Antisymmetric Quaternionic Algebra*).

**Remark (the sharp form of the specificity).** The correct exclusive statement is therefore that
the antisymmetric plain algebra is the only structure of the twelve **all of whose left
multiplications are derivations**, equivalently the only Lie product; not that no other structure has
an element whose left multiplication is a derivation. This is why the centre, the derived algebra,
the Killing form, the Casimir element and the enveloping algebra are properties of the antisymmetric
plain product and are not transferable, and it is the reason the twelve are not twelve copies of one
theory but one theory with eleven deformations, the antisymmetric plain product being the Lie
deformation of the plain one.

## Summary

The antisymmetric plain multiplication is the only one of the twelve structures of the complex space
whose every left multiplication is a derivation, equivalently the only **Lie product**: the Leibniz
identity, at every element,

$$
L_{\tilde X}(\tilde Y\star\tilde Z)=(L_{\tilde X}\tilde Y)\star\tilde Z+\tilde Y\star(L_{\tilde X}\tilde Z) .
$$

For an alternating product that identity is
equivalent to the Jacobi identity, the Leibniz defect being the negative of the cyclic sum,
$\Lambda=-J$, and the block satisfies both. The criterion is the exact reason the Lie theory of the
block — the centre and the quotient, the derived algebra isomorphic to $\mathfrak{sl}(2,\mathbb{C})$,
the Killing form of radical the centre, the Cartan criteria, the Casimir element, the enveloping
algebra and the matrix models — is a theory and not a collection of examples: it holds at every
element of the block. Among the twelve it is the block alone, the ten non-alternating structures
failing the identity directly and the one other alternating structure, $\mathrm{AQA}$, through its
Jacobi defect at $(e_0,e_1,e_2)$; the isolation is a statement about the law and not about isolated
elements.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\star$ | a generic product, specified at each use |
| $L^{\star}_{\tilde X}:\tilde Y\mapsto\tilde X\star\tilde Y$ | the left multiplication of a product |
| $\mathrm{ad}^{\star}_{\tilde X}\tilde Y=\tilde X\star\tilde Y-\tilde Y\star\tilde X$ | the adjoint map, equal to $2L^{\star}_{\tilde X}$ for an alternating product |
| $\mathrm{ad}^{\wedge}_{\tilde X}=L_{\tilde X}=\tilde X\wedge\cdot$ | the adjoint of the block's own bracket, the halved adjoint |
| $L^{\star}_{\tilde X}(\tilde Y\star\tilde Z)=(L^{\star}_{\tilde X}\tilde Y)\star\tilde Z+\tilde Y\star(L^{\star}_{\tilde X}\tilde Z)$ | the Leibniz identity, the criterion |
| $\Lambda=-J$ | the Leibniz defect is the negative of the cyclic sum, for an alternating product |
| $\mathrm{GPA}\dots\mathrm{AQS}$ | the twelve structures, coded as in *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ | the kernel of the adjoint representation, the centre of the bracket |
| $\mathrm{Vect}(\mathbb{B})\cong\mathfrak{sl}(2,\mathbb{C})$ | the image of the adjoint representation, the inner derivations |

## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the left and right multiplications, the derivations and the Lie-admissible algebras.
- Nathan Jacobson, *Lie Algebras* (Interscience, 1962), for the Jacobi identity, the adjoint representation and the Killing form.
- *The Symmetric and Antisymmetric Parts of an Algebra Product* (`articles_maths/the-symmetric-and-antisymmetric-parts-of-an-algebra-product.md`), for the split of a product into its two halves and the Lie-admissibility of a commutator.
- *The Specificities of the Symmetric Plain Algebra* (`articles_maths/the-specificities-of-the-symmetric-plain-algebra.md`), the twin of this article, for the criterion of the other half of the plain product.
- *The Lie Algebra of the Antisymmetric Plain Algebra* (`articles_maths/the-lie-algebra-of-the-antisymmetric-plain-algebra.md`), for the centre, the derived algebra and the enveloping algebra the criterion delivers.
- *The Killing Form of the Antisymmetric Plain Algebra* (`articles_maths/the-killing-form-of-the-antisymmetric-plain-algebra.md`), for the invariant form, the Cartan criteria and the Casimir element.
- *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra* (`articles_maths/the-adjoint-operators-and-the-derivations-of-the-antisymmetric-plain-algebra.md`), for the adjoint maps, the inner and the outer derivations.
- *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-algebraic-structures-over-the-biquaternion-c-space.md`), for the twelve operations and the row table.
