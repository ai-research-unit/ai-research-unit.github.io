# __The Specificities of the Symmetric Quaternionic Algebra__

## Introduction

The symmetric quaternionic bilinear product $\tilde Q_1\bullet\tilde Q_2=\tfrac12(\tilde Q_1^{\natural}\tilde Q_2+\tilde Q_2^{\natural}\tilde Q_1)$ is governed by one formula, proved in *Introduction to the Symmetric Quaternionic Algebra* and read throughout the block,

$$
\tilde Q_1\bullet\tilde Q_2=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}\,e_t,\qquad
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2),
$$

in which $\langle\cdot,\cdot\rangle_{\natural}$ is the quaternion form, symmetric, non-degenerate, of Gram matrix the identity on the basis. The formula makes the algebra element-theoretically the poorest of the twelve: it is commutative with vanishing commutator, its image is the central line $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$, it has no unit, its radical is $\{0\}$ because the form is non-degenerate, and its idempotents are $0$ and $e_t$ alone (*The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*).

Its **operator** theory is nevertheless exactly computable, and again in one line, because the value of the product reads its two arguments only through the form: the left multiplication is the rank-one operator $L_{\tilde Q_1}:\tilde Q_2\mapsto \langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$, and its square is

$$
L_{\tilde Q_1}^{2}=X_t\,L_{\tilde Q_1},
$$

with $X_t$ the scalar coordinate of $\tilde Q_1$. This article reads the two consequences. The elements whose left multiplication is a **projector** are those of the affine hyperplane $X_t=1$, together with the origin: the first are pairwise distinct rank-one projections onto the central line, the second is the zero operator. The elements whose left multiplication is **square-zero** are those of the hyperplane $X_t=0$, which is the vector subspace $\mathrm{Vect}(\mathbb{B})$, the orthogonal complement of the central line; the nonzero ones have rank one, and the zero elements of this family are distinct from the square-zero elements of the algebra, which are the isotropic cone.

The article states and proves the exclusive law of the block on the same model as the articles that began the family: the **scalar law**, which demands that the product be commutative and that its values be central, is satisfied by the block and by no other operation of the twelve, and the classification of the block's operators is read from it. The projectors do not come from isolated elements and not from the unit: they come from a hyperplane, they are indexed by that hyperplane and not by the idempotents of the algebra, and even the element $e_t$ gives the projection onto the central line and not the identity, because the algebra has no unit. The algebra therefore produces a full family of projectors and disowns all but one of their indices, exactly as the general quaternionic product does; the difference is the size and the shape of the family.

## The Exclusive Law of the Block

The family of specificities articles states, for each block, one law that the block has and the other eleven do not, and proves it (*The Biquaternion Algebra and Its Vector Spaces*, *The Specificities of the General Quaternionic Algebra*). The law of the symmetric quaternionic block is the following.

**Definition (the scalar law).** Let $\circ$ be a product on $\mathbb{B}$. The product satisfies the **scalar law** when

1. it is **commutative**, $\tilde Q_1\circ\tilde Q_2=\tilde Q_2\circ\tilde Q_1$ for all $\tilde Q_1,\tilde Q_2$; and
2. its **values are central**, $\tilde Q_1\circ\tilde Q_2\in\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$ for all $\tilde Q_1,\tilde Q_2$.

**Theorem (the equivalent form).** A product $\circ$ satisfies the scalar law if and only if there is a symmetric $\mathbb{C}$-bilinear form $\beta$ on $\mathbb{B}$ with

$$ \boxed{\; \tilde Q_1\circ\tilde Q_2=\beta(\tilde Q_1,\tilde Q_2)\,e_t\qquad\text{for all }\tilde Q_1,\tilde Q_2 \;}. $$

**Proof.** If $\circ$ satisfies the scalar law, its value is central, so it reads $\beta(\tilde Q_1,\tilde Q_2)e_t$ with $\beta$ the scalar coefficient; the bilinearity of the product gives the bilinearity of $\beta$, and its commutativity gives the symmetry. Conversely a product of the displayed shape has central values by construction and is commutative because $\beta$ is symmetric.

**Theorem (the block is the only structure with the scalar law).** The symmetric quaternionic product satisfies the scalar law, with $\beta=N$; and among the twelve operations of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* it is the only one that does.

**Proof.** The product is $\tilde Q_1\star\tilde Q_2=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$ with $\langle\cdot,\cdot\rangle_{\natural}$ symmetric, bilinear and central-valued by *Introduction to the Symmetric Quaternionic Algebra*, so the law holds; the uniqueness is §*The Isolation among the Twelve*, where each other operation is exhibited with a witness of the failure of clause 1 or of clause 2.

**Theorem (the operator reading).** The left multiplications of the block obey the composition law

$$ \boxed{\; L_{\tilde Q_1}L_{\tilde Q_3}=\mathrm{Sc}(\tilde Q_1)\,L_{\tilde Q_3}\qquad\text{for all }\tilde Q_1,\tilde Q_3 \;}, $$

where $\mathrm{Sc}(\tilde Q_1)=X_t$ is the scalar coordinate; and no other one of the twelve operations admits a law of the form $L^{\circ}_{\tilde Q_1}L^{\circ}_{\tilde Q_3}=\ell(\tilde Q_1)L^{\circ}_{\tilde Q_3}$ with $\ell$ depending on the first factor alone.

**Proof.** The law of the block is the composition law of *The Multiplication Operators of the Symmetric Quaternionic Algebra*, $L_{\tilde Q_5}L_{\tilde Q_4}=\langle\tilde Q_5,e_t\rangle_{\natural}L_{\tilde Q_4}$, with $\langle\tilde Q_5,e_t\rangle_{\natural}=\mathrm{Sc}(\tilde Q_5)$; its specialisation at $\tilde Q_1$ is $L_{\tilde Q_1}^2=X_tL_{\tilde Q_1}$ of §*The Operator Identity*. The failures of the other eleven are in §*The Isolation among the Twelve*.

**Remark (why the two forms of the law are kept).** The element form and the operator form are not the same statement in general, and the article keeps both. The operator form is the one the block's whole operator theory reads, and it is the form in which the four columns of the projectors and the square-zero operators are computed; the element form is the one the pairs of basis elements settle, because its two clauses are decided there. The block is the unique structure that passes both.

## The Left Multiplication Is Rank One

**Theorem (the shape of the operator).** For all $\tilde Q_1,\tilde Q_2$,

$$ \boxed{\; L_{\tilde Q_1}(\tilde Q_2)=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}\,e_t \;}. $$

For $\tilde Q_1\neq0$ the operator has image the central line $\mathbb{C}e_t$, kernel the hyperplane $\langle\tilde Q_1,\cdot\rangle_{\natural}=0$, and rank one; it is the zero operator exactly at $\tilde Q_1=0$.

**Proof.** The display is the governing formula read as an operator identity. The form $\langle\cdot,\cdot\rangle_{\natural}$ is non-degenerate, so for $\tilde Q_1\neq0$ the functional $\langle\tilde Q_1,\cdot\rangle_{\natural}$ is nonzero and its kernel is a hyperplane; the image is the span of $e_t$, of complex dimension one. For $\tilde Q_1=0$ the functional vanishes and the operator is $0$; conversely $L_{\tilde Q_1}=0$ gives $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=0$ for every $\tilde Q_2$ and hence $\tilde Q_1=0$ by non-degeneracy.

**Corollary (the map of elements is faithful).** $L_{\tilde Q_1}=L_{\tilde Q_3}$ if and only if $\tilde Q_1=\tilde Q_3$.

**Proof.** The operators agree exactly when the functionals $\langle\tilde Q_1,\cdot\rangle_{\natural}$ and $\langle\tilde Q_3,\cdot\rangle_{\natural}$ agree, that is when $\langle\tilde Q_1-\tilde Q_3,\cdot\rangle_{\natural}=0$, that is when $\tilde Q_1-\tilde Q_3=0$ by non-degeneracy.

The corollary is what makes the operator theory exact: an operator identity of $\bullet$ is an element identity of the space, and no information is lost. It is the analogue of the faithfulness of the plain left multiplications, and it is the property the two sesquilinear members of the symmetric family do not have.

**Remark (the operator is one for the whole hyperplane, not for the line).** The image of $L_{\tilde Q_1}$ is the central line and never a proper subspace of it, so the operators are as small as a nonzero operator can be: rank one, by the smallest possible argument. The algebra is a rank-one pairing, and its whole operator theory is the theory of the nonzero linear functionals on the space, read with a fixed value $e_t$.

## The Operator Identity

**Theorem (the square of the left multiplication).** For every $\tilde Q_1$,

$$
L_{\tilde Q_1}^{2}=X_t\,L_{\tilde Q_1}.
$$

**Proof.** $L_{\tilde Q_1}^{2}(\tilde Q_2)=L_{\tilde Q_1}\bigl(\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t\bigr)=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}L_{\tilde Q_1}(e_t)=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}\langle\tilde Q_1,e_t\rangle_{\natural}e_t$, and $\langle\tilde Q_1,e_t\rangle_{\natural}=X_t$; so the composite is $X_t\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t=X_tL_{\tilde Q_1}(\tilde Q_2)$.

The theorem is the specialisation of the composition law $L^{\bullet}_{\tilde Q_5}L^{\bullet}_{\tilde Q_4}=\langle\tilde Q_5,e_t\rangle_{\natural}L^{\bullet}_{\tilde Q_4}$ of *The Multiplication Operators of the Symmetric Quaternionic Algebra* to the single element $\tilde Q_1$, and it is stated here as the identity the whole article reads. It is the exact replacement of the criterion of *The Biquaternion Algebra and Its Vector Spaces*, which in this algebra would read $L_{\tilde Q_1}^{2}=L_{\tilde Q_1\bullet\tilde Q_1}$; the two are not the same, and the comparison is made at §*The Criterion Fails Here*.

**Corollary (the monoid law).** $L_{\tilde Q_1}L_{\tilde Q_3}=X_t\,L_{\tilde Q_3}$ for all $\tilde Q_1,\tilde Q_3$, so the family of left multiplications is stable under composition, it is a monoid with the reversed convention of composition, and every element of scalar coordinate $1$ is a left identity of the monoid.

**Proof.** The composite of the identity of the theorem with an arbitrary $L_{\tilde Q_3}$ gives the display, and at $X_t=1$ it reads $L_{\tilde Q_1}L_{\tilde Q_3}=L_{\tilde Q_3}$: such an $L_{\tilde Q_1}$ is a left identity.

**Remark (the monoid is not the algebra).** The multiplication of the algebra is commutative and has no unit, and the monoid of its left multiplications is non-commutative as soon as both factors have nonzero scalar coordinate ($L_{\tilde Q_1}L_{\tilde Q_3}=X_tL_{\tilde Q_3}$ against $L_{\tilde Q_3}L_{\tilde Q_1}=Z_tL_{\tilde Q_1}$) and has left identities only. The passage from the algebra to its operators therefore changes both the commutativity and the unit, which is the sharpest illustration of the theme of the family: the element structure and the operator structure of these products are different objects.

## The Projectors

**Theorem (the classification).** The operator $L_{\tilde Q_1}$ is a projector if and only if $\tilde Q_1=0$ or $X_t=1$.

**Proof.** By §*The Operator Identity* the condition is $(X_t-1)L_{\tilde Q_1}=0$. If $X_t=1$ it holds. If $X_t\neq1$ then $L_{\tilde Q_1}=0$, and by the faithfulness of §*The Left Multiplication Is Rank One* this is $\tilde Q_1=0$, whose scalar coordinate is $0\neq1$; so the two cases are disjoint and cover the condition.

**Corollary (the family and its shape).** The projectors are the operators $L_{\tilde Q_1}$ with $X_t=1$, one for each point of the affine hyperplane $\{X_t=1\}$, together with the zero operator at $\tilde Q_1=0$. Each is the projection onto the central line $\mathbb{C}e_t$ along the hyperplane $\ker \langle\tilde Q_1,\cdot\rangle_{\natural}$, it fixes $e_t$ and kills that kernel, the family is of complex dimension three, and its members are pairwise distinct.

**Proof.** At $X_t=1$ the operator is idempotent by the theorem, its image is $\mathbb{C}e_t$ and its kernel is a hyperplane by §*The Left Multiplication Is Rank One*, and the two are complementary because $\langle\tilde Q_1,e_t\rangle_{\natural}=X_t=1$ does not vanish on the image: the operator is the projection onto $\mathbb{C}e_t$ along the kernel, and it fixes $e_t$. The distinctness is the faithfulness of §*The Left Multiplication Is Rank One*, and the hyperplane has complex dimension three.

**Remark (the projection is onto the line, not onto the element's own span).** Every member of the family is a projection of rank one onto the **same** line $\mathbb{C}e_t$, and the members differ only in the direction along which they project, which is the kernel of $L_{\tilde Q_1}$. The family is therefore a projective space of directions rather than a family of subspaces: the kernels $\langle\tilde Q_1,\cdot\rangle_{\natural}=0$, that is the points of the dual projective space $\mathrm{PG}(3,\mathbb{C})^{*}$ whose hyperplane does not contain the central line, the index $\tilde Q_1$ ranging over the affine chart $X_t=1$. The hyperplanes that do contain the central line form the projective plane $X_t=0$ inside that dual space, and they are exactly the kernels excluded here.

**Remark (the algebra disowns its projectors).** The idempotents of the algebra are $0$ and $e_t$ alone, and the projectors are indexed by the hyperplane $X_t=1$ and by the origin. The overlap of the two descriptions is one element, besides the origin: $e_t$. Even there the coincidence is misleading, because $L_{e_t}$ is not the identity: it is the projection $E:\tilde Q_2\mapsto Y_te_t$ onto the central line, the identity being unavailable since the algebra has no unit. The family is thus indexed by elements that are not idempotents of the algebra, and it is a full three-parameter family all the same.

**Remark (the parallel with the general quaternionic product).** In the general quaternionic algebra the projectors are the plain left multiplications indexed by the plain idempotents, a family of complex dimension two (*The Specificities of the General Quaternionic Algebra*). Here the family is indexed by the hyperplane $X_t=1$, of complex dimension three, and by itself: the index set and the family have the same dimension. In both cases the algebra disowns its projectors, the element idempotents being far fewer than the operator ones, and in both cases the disjunction has one source, that the operator reads the element only through a pairing and so cannot see the idempotent equation.

## The Square-Zero Operators

**Theorem (the classification).** The operator $L_{\tilde Q_1}$ is square-zero if and only if $X_t=0$.

**Proof.** By §*The Operator Identity* $L_{\tilde Q_1}^{2}=X_tL_{\tilde Q_1}$, which vanishes when $X_t=0$. Conversely if $L_{\tilde Q_1}^{2}=0$ and $X_t\neq0$ then $L_{\tilde Q_1}=0$, hence $\tilde Q_1=0$ by faithfulness, and $0$ has scalar coordinate $0$, a contradiction.

**Corollary (the set and its shape).** The square-zero operators are the operators $L_{\tilde Q_1}$ with $X_t=0$, that is with $\tilde Q_1$ in the vector subspace $\mathrm{Vect}(\mathbb{B})=\mathbb{C}\vec e_x+\mathbb{C}\vec e_y+\mathbb{C}\vec e_z$, which is the orthogonal complement of the central line and is of complex dimension three; the operator is zero at $\tilde Q_1=0$ and of rank one elsewhere, and it is a two-step flag $\{0\}\subseteq\mathbb{C}e_t\subseteq\ker \langle\tilde Q_1,\cdot\rangle_{\natural}$.

**Proof.** The vanishing of $X_t$ is the vanishing of the scalar coordinate, that is membership in the vector subspace; the rank statement is §*The Left Multiplication Is Rank One*, and the flag is the image inside the kernel, which is the shape of a square-zero operator.

**Remark (the two meanings of square-zero).** The square-zero **elements** of the algebra are the isotropic ones, the cone $\langle\tilde Q_1,\tilde Q_1\rangle_{\natural}=0$ of complex dimension three (*The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*), and the square-zero **operators** are the elements of the vector subspace, also of complex dimension three. The two sets are different: the isotropic cone contains $\vec e_x+i\vec e_y$, whose scalar coordinate is $0$ and which therefore does belong to both, and it contains $e_t+\vec e_x$, whose scalar coordinate is $1$ and whose operator is a projector rather than a square-zero one. The coincidence of the dimensions is arithmetic and the two sets are not equal.

**Remark (the sharp asymmetry between the two halves).** The theorem and the classification before it split the space by the scalar coordinate alone, and the split is the whole operator theory: $X_t=1$ gives the projectors, $X_t=0$ the square-zero ones, and every other element gives an operator that is neither. The property of being a projector is therefore not an algebraic property of the element in this algebra but the single scalar equation $X_t=1$, which is why the family is a hyperplane and why the algebra's own idempotent equation meets it in one element.

## The Criterion Fails Here

The criterion of *The Biquaternion Algebra and Its Vector Spaces* reads $L_{\tilde Q_1}^{2}=L_{\tilde Q_1\bullet\tilde Q_1}$ and characterises the left-alternative products. In this algebra the two sides are $X_tL_{\tilde Q_1}$ and, by §*The Operator Identity* read at the element $\tilde Q_1\bullet\tilde Q_1=\langle\tilde Q_1,\tilde Q_1\rangle_{\natural}e_t$,

$$
L_{\tilde Q_1\bullet\tilde Q_1}=\langle\tilde Q_1,\tilde Q_1\rangle_{\natural}\,L_{e_t}=\langle\tilde Q_1,\tilde Q_1\rangle_{\natural}\,E,\qquad E:\tilde Q_2\mapsto Y_te_t ,
$$

so the criterion would demand $X_t\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\langle\tilde Q_1,\tilde Q_1\rangle_{\natural}Y_t$ for every $\tilde Q_2$, that is the pair of conditions $X_t^{2}=\langle\tilde Q_1,\tilde Q_1\rangle_{\natural}$ and $X_tX_k=0$ for $k=x,y,z$. The conditions fail at the first vector, where the two sides of the alternativity law are

$$
\vec e_x\bullet(\vec e_x\bullet e_t)=0,\qquad (\vec e_x\bullet \vec e_x)\bullet e_t=e_t ,
$$

since $\vec e_x\bullet e_t=\langle \vec e_x,e_t\rangle_{\natural}e_t=0$ while $\vec e_x\bullet \vec e_x=\langle \vec e_x,\vec e_x\rangle_{\natural}e_t=e_t$. The algebra is not left-alternative, the criterion is not available, and the classification above is not an instance of it: it is read from the identity of §*The Operator Identity*, which holds for the algebra's own reason, the rank-one shape of the product.

## The Isolation among the Twelve

The family of specificities articles states, for each block, one law that the block has and the other eleven do not, proves it, and reads the block's theory from it. The law of this block is the **scalar law** of §*The Exclusive Law of the Block*: commutative with central values, equivalently $\tilde Q_1\circ\tilde Q_2=\beta(\tilde Q_1,\tilde Q_2)e_t$ for a symmetric bilinear form $\beta$.

**Theorem (the isolation).** Of the twelve structures of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, the symmetric quaternionic product is the only one that satisfies the scalar law.

*Proof.* The twelve are generated from the four general products by symmetrising or antisymmetrising. The four general products are non-commutative, so they fail the first clause; the four antisymmetrisations are non-commutative as well. Among the four symmetrisations, the symmetric plain product is commutative and not central-valued, the vector part of the plain product surviving the symmetrisation; the symmetric plain sesquilinear product is central-valued and not commutative, its conjugation conjugating a scalar; and the symmetric quaternionic sesquilinear product fails both. The symmetric quaternionic product is commutative and central-valued by the governing formula, and it alone meets both clauses.

| family | structures | commutative | central values | the scalar law |
|---|---|---|---|---|
| the four general products | GPA, GQA, GPS, GQS | no | no | no |
| the symmetric parts | SPA | yes | no | no |
| | **SQA** | **yes** | **yes** | **yes** |
| | SPS | no | yes | no |
| | SQS | no | no | no |
| the antisymmetric parts | APA, AQA, APS, AQS | no | no | no |

The operator reading of the law, $L^{\circ}_{\tilde Q_1}L^{\circ}_{\tilde Q_3}=\ell(\tilde Q_1)L^{\circ}_{\tilde Q_3}$ with $\ell$ depending on the first factor alone, fails for the other eleven as well. The three bilinear structures away from the block that carry a one-sided unit — the plain product, the general quaternionic product and the symmetric plain product — fail at $\tilde Q_3=e_t$, where $L^{\circ}_{e_t}$ is the identity, so a law of that form would make $L^{\circ}_{\tilde Q_1}$ a scalar multiple of the identity, which it is not. The two alternating products carry no unit and fail the reading at the pair $(\tilde Q_1,\tilde Q_3)=(\vec e_x,\vec e_x)$, where the two sides are not proportional. The six sesquilinear structures fail by parity: their left multiplication is conjugate-linear in its argument while a composite is $\mathbb{C}$-linear, so a linear operator equal to a conjugate-linear one vanishes, and the composite is not always zero. The block satisfies the reading with $\ell(\tilde Q_1)=X_t$ by §*The Operator Identity*.

**Remark (the four symmetric products).** The four symmetric products behave alike at the element level — no unit, few idempotents — and differently at the operator level. The symmetric plain product recovers only the identity operator, from its unit; the two symmetric sesquilinear products recover only the zero operator, their left multiplications being conjugate-linear and hence, if idempotent, zero; this block recovers the affine hyperplane $X_t=1$ of rank-one projections onto the central line, together with the zero operator. The block is the one member whose operator family is a hyperplane, and the reason is the rank-one shape $L_{\tilde Q_1}\tilde Q_2=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$ of its left multiplication, which the other three do not have.

## Summary

The symmetric quaternionic product satisfies the **scalar law** — it is commutative and its values lie in the centre, equivalently $\tilde Q_1\bullet\tilde Q_2=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$ for a symmetric bilinear form — and it is the only one of the twelve operations that does: the two other symmetrisations that survive one clause each fail the other (the symmetric plain product is commutative and not central, the symmetric plain sesquilinear product central and not commutative), and the four general products and the four antisymmetrisations fail both. Its left multiplication is the rank-one operator $L_{\tilde Q_1}\tilde Q_2=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$, faithful in $\tilde Q_1$ because the form is non-degenerate, and the single identity $L_{\tilde Q_1}^{2}=X_tL_{\tilde Q_1}$ classifies everything: the operator is a projector exactly when $\tilde Q_1=0$ or $X_t=1$, and square-zero exactly when $X_t=0$; the operator reading $L_{\tilde Q_1}L_{\tilde Q_3}=X_tL_{\tilde Q_3}$ likewise fails for the other eleven, for the six sesquilinear ones by the parity obstruction and for the rest on explicit witnesses. The projectors are the affine hyperplane $X_t=1$ together with the zero operator, a family of complex dimension three of pairwise distinct rank-one projections onto the central line, indexed by the hyperplane and not by the idempotents of the algebra, which are $0$ and $e_t$ alone; even the element $e_t$ gives the projection onto the central line and not the identity, since the algebra has no unit. The square-zero operators are the vector subspace $X_t=0$, which is not the isotropic cone of the square-zero elements, the two coinciding only on the intersection. Among the four symmetric products the block is the only one with a hyperplane of projectors, and the law that isolates it among the twelve is the scalar law of §*The Isolation among the Twelve*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\bullet$, $\star$ | the symmetric quaternionic product $\tfrac12(\tilde Q_1^{\natural}\tilde Q_2+\tilde Q_2^{\natural}\tilde Q_1)=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$ |
| $\circ$ | the generic operation of another structure of the catalogue, in §*The Isolation among the Twelve* |
| scalar law | commutative with central values: $\tilde Q_1\circ\tilde Q_2=\beta(\tilde Q_1,\tilde Q_2)e_t$, $\beta$ symmetric |
| $X_t$, $\vec X$ | the scalar coordinate and the vector part of $\tilde Q_1=X_t+\vec X$ |
| $\mathrm{Sc}(\tilde Q_1)=X_t$ | the scalar coordinate, read as a functional |
| $\langle\cdot,\cdot\rangle_{\natural}$ | the quaternion form $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=X_tY_t+(\vec X,\vec Y)$, symmetric, non-degenerate, of Gram matrix the identity |
| $L_{\tilde Q_1}$ | the left multiplication $\tilde Q_2\mapsto\tilde Q_1\bullet\tilde Q_2=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$, rank one for $\tilde Q_1\neq0$ |
| $E$ | the projection $E:\tilde Q_2\mapsto Y_te_t$ onto the central line, the operator of $e_t$ |
| $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$ | the central line and the vector subspace, the eigenspaces of the scalar coordinate |
| idempotent, projector | an element, and an operator, equal to its own square |
| $\mathbb{B}$ | the complex space $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |

## Further Reading

- [The Biquaternion Algebra and Its Vector Spaces](the-biquaternion-algebra-and-its-vector-spaces.html), for the criterion of the plain product, the model of the family.
- [The Specificities of the General Quaternionic Algebra](the-specificities-of-the-general-quaternionic-algebra.html), for the companion family of projectors in the general quaternionic product.
- [Introduction to the Symmetric Quaternionic Algebra](introduction-to-the-symmetric-quaternionic-algebra.html), for the governing formula $\tilde Q_1\bullet\tilde Q_2=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$ and for the absence of a unit.
- [The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra](the-radical-and-the-isotropic-elements-of-the-symmetric-quaternionic-algebra.html), for the trivial radical, the idempotents $0$ and $e_t$, and the isotropic cone of the square-zero elements.
- [The Multiplication Operators of the Symmetric Quaternionic Algebra](the-multiplication-operators-of-the-symmetric-quaternionic-algebra.html), for the composition law and the rank, trace and adjoint of the operators.
