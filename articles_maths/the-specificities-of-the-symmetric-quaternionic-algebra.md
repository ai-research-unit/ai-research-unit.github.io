# __The Specificities of the Symmetric Quaternionic Algebra__

## Introduction

The symmetric quaternionic bilinear product $\tilde P\bullet\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)$ is governed by one formula, proved in *Introduction to the Symmetric Quaternionic Algebra of Biquaternions* and read throughout the block,

$$
\tilde P\bullet\tilde Q=N(\tilde P,\tilde Q)\,e_0,\qquad
N(\tilde P,\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q),
$$

in which $N$ is the quaternion form, symmetric, non-degenerate, of Gram matrix the identity on the basis. The formula makes the algebra element-theoretically the poorest of the twelve: it is commutative with vanishing commutator, its image is the central line $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$, it has no unit, its radical is $\{0\}$ because the form is non-degenerate, and its idempotents are $0$ and $e_0$ alone (*The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*).

Its **operator** theory is nevertheless exactly computable, and again in one line, because the value of the product reads its two arguments only through the form: the left multiplication is the rank-one operator $L_{\tilde X}:\tilde Y\mapsto N(\tilde X,\tilde Y)e_0$, and its square is

$$
L_{\tilde X}^{2}=X_0\,L_{\tilde X},
$$

with $X_0$ the scalar coordinate of $\tilde X$. This article reads the two consequences. The elements whose left multiplication is a **projector** are those of the affine hyperplane $X_0=1$, together with the origin: the first are pairwise distinct rank-one projections onto the central line, the second is the zero operator. The elements whose left multiplication is **square-zero** are those of the hyperplane $X_0=0$, which is the vector subspace $\mathrm{Vect}(\mathbb{B})$, the orthogonal complement of the central line; the nonzero ones have rank one, and the zero elements of this family are distinct from the square-zero elements of the algebra, which are the isotropic cone.

The point of the article is the proof behind the row of the symmetric quaternionic product in the comparison table of *The Specificities of the General Plain Algebra*, which states that the projectors come from the elements of scalar coordinate $1$ and from the origin. The article states and proves the exclusive law of the block on the same model as the two articles that began the family: the **scalar law**, which demands that the product be commutative and that its values be central, is satisfied by the block and by no other operation of the twelve, and §*The Eleven Failures* runs the eleven comparisons with a witness for each. The projectors do not come from isolated elements and not from the unit: they come from a hyperplane, they are indexed by that hyperplane and not by the idempotents of the algebra, and even the element $e_0$ gives the projection onto the central line and not the identity, because the algebra has no unit. The algebra therefore produces a full family of projectors and disowns all but one of their indices, exactly as the general quaternionic product does; the difference is the size and the shape of the family.

**Placement.** The article is the second and closing entry of the *Specific Theory* section of the symmetric quaternionic algebra, after *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*, and it is the third of the family that *The Specificities of the General Plain Algebra* began and *The Specificities of the General Quaternionic Algebra* continued. It uses the governing formula of *Introduction to the Symmetric Quaternionic Algebra of Biquaternions*, the non-degeneracy and the trivial radical of the radical article, the composition law of the multiplication operators in *The Multiplication Operators of the Symmetric Quaternionic Algebra*, the element idempotents of *Idempotents of the General Plain Algebra*, and the criterion of the article that began the family.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with $e_1e_2=e_3$ and central scalar imaginary $i$. The product is written $\bullet$, as in the *Specific Theory* entries of the block, and coincides with the $\star$ of *Introduction to the Symmetric Quaternionic Algebra of Biquaternions* and of *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra*; juxtaposition is the plain product and $\natural$ the natural conjugation. An element is $\tilde X=X_0+\mathbf X$ with $X_0$ its scalar coordinate and $\mathbf X=(X_1,X_2,X_3)$ its vector part, and $N(\tilde X,\tilde Y)=X_0Y_0+(\mathbf X,\mathbf Y)$ is the quaternion form, non-degenerate and of Gram matrix the identity. The **left multiplication** is $L_{\tilde X}(\tilde Y)=\tilde X\bullet\tilde Y$, and the subscript is the element. An **idempotent** of the algebra is an element equal to its own square, and a **projector** is an idempotent operator, that is an idempotent of the morphism space; the zero operator is one, and the two levels are never interchanged. An idempotent element corresponds to a projector when its multiplication operator is idempotent, and the content of §*The Projectors* is exactly the scalar equation $X_0=1$, together with the origin.

## The Exclusive Law of the Block

The family of specificities articles states, for each block, one law that the block has and the other eleven do not, proves it, and runs the eleven comparisons (*The Specificities of the General Plain Algebra*, *The Specificities of the General Quaternionic Algebra*). The law of the symmetric quaternionic block is the following.

**Definition (the scalar law).** Let $\circ$ be a product on $\mathbb{B}$. The product satisfies the **scalar law** when

1. it is **commutative**, $\tilde X\circ\tilde Y=\tilde Y\circ\tilde X$ for all $\tilde X,\tilde Y$; and
2. its **values are central**, $\tilde X\circ\tilde Y\in\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ for all $\tilde X,\tilde Y$.

**Theorem (the equivalent form).** A product $\circ$ satisfies the scalar law if and only if there is a symmetric $\mathbb{C}$-bilinear form $\beta$ on $\mathbb{B}$ with

$$
\tilde X\circ\tilde Y=\beta(\tilde X,\tilde Y)\,e_0\qquad\text{for all }\tilde X,\tilde Y .
$$

**Proof.** If $\circ$ satisfies the scalar law, its value is central, so it reads $\beta(\tilde X,\tilde Y)e_0$ with $\beta$ the scalar coefficient; the bilinearity of the product gives the bilinearity of $\beta$, and its commutativity gives the symmetry. Conversely a product of the displayed shape has central values by construction and is commutative because $\beta$ is symmetric.

**Theorem (the block is the only structure with the scalar law).** The symmetric quaternionic product satisfies the scalar law, with $\beta=N$; and among the twelve operations of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* it is the only one that does.

**Proof.** The product is $\tilde P\star\tilde Q=N(\tilde P,\tilde Q)e_0$ with $N$ symmetric, bilinear and central-valued by *Introduction to the Symmetric Quaternionic Algebra of Biquaternions*, so the law holds; the uniqueness is §*The Eleven Failures*, where every other operation is exhibited with a witness of the failure of clause 1 or of clause 2.

**Theorem (the operator reading).** The left multiplications of the block obey the composition law

$$
L_{\tilde X}L_{\tilde Z}=\mathrm{Sc}(\tilde X)\,L_{\tilde Z}\qquad\text{for all }\tilde X,\tilde Z,
$$

where $\mathrm{Sc}(\tilde X)=X_0$ is the scalar coordinate; and no other one of the twelve operations admits a law of the form $L^{\circ}_{\tilde X}L^{\circ}_{\tilde Z}=\ell(\tilde X)L^{\circ}_{\tilde Z}$ with $\ell$ depending on the first factor alone.

**Proof.** The law of the block is the composition law of *The Multiplication Operators of the Symmetric Quaternionic Algebra*, $L_{\tilde A}L_{\tilde B}=N(\tilde A,e_0)L_{\tilde B}$, with $N(\tilde A,e_0)=\mathrm{Sc}(\tilde A)$; its specialisation $\tilde A=\tilde B=\tilde X$ is $L_{\tilde X}^2=X_0L_{\tilde X}$ of §*The Operator Identity*. The failures of the other eleven are in §*The Eleven Failures*.

**Remark (why the two forms of the law are kept).** The element form and the operator form are not the same statement in general, and the article keeps both. The operator form is the one the block's whole operator theory reads, and it is the form in which the four columns of the projectors and the square-zero operators are computed; the element form is the one the eleven comparisons settle, because its two clauses are decided on pairs of basis elements. The block is the unique structure that passes both.

## The Left Multiplication Is Rank One

**Theorem (the shape of the operator).** For all $\tilde X,\tilde Y$,

$$
L_{\tilde X}(\tilde Y)=N(\tilde X,\tilde Y)\,e_0 .
$$

For $\tilde X\neq0$ the operator has image the central line $\mathbb{C}e_0$, kernel the hyperplane $N(\tilde X,\cdot)=0$, and rank one; it is the zero operator exactly at $\tilde X=0$.

**Proof.** The display is the governing formula read as an operator identity. The form $N$ is non-degenerate, so for $\tilde X\neq0$ the functional $N(\tilde X,\cdot)$ is nonzero and its kernel is a hyperplane; the image is the span of $e_0$, of complex dimension one. For $\tilde X=0$ the functional vanishes and the operator is $0$; conversely $L_{\tilde X}=0$ gives $N(\tilde X,\tilde Y)=0$ for every $\tilde Y$ and hence $\tilde X=0$ by non-degeneracy.

**Corollary (the map of elements is faithful).** $L_{\tilde X}=L_{\tilde Z}$ if and only if $\tilde X=\tilde Z$.

**Proof.** The operators agree exactly when the functionals $N(\tilde X,\cdot)$ and $N(\tilde Z,\cdot)$ agree, that is when $N(\tilde X-\tilde Z,\cdot)=0$, that is when $\tilde X-\tilde Z=0$ by non-degeneracy.

The corollary is what makes the operator theory exact: an operator identity of $\bullet$ is an element identity of the space, and no information is lost. It is the analogue of the faithfulness of the plain left multiplications, and it is the property the two sesquilinear members of the symmetric family do not have.

**Remark (the operator is one for the whole hyperplane, not for the line).** The image of $L_{\tilde X}$ is the central line and never a proper subspace of it, so the operators are as small as a nonzero operator can be: rank one, by the smallest possible argument. The algebra is a rank-one pairing, and its whole operator theory is the theory of the nonzero linear functionals on the space, read with a fixed value $e_0$.

## The Operator Identity

**Theorem (the square of the left multiplication).** For every $\tilde X$,

$$
L_{\tilde X}^{2}=X_0\,L_{\tilde X}.
$$

**Proof.** $L_{\tilde X}^{2}(\tilde Y)=L_{\tilde X}\bigl(N(\tilde X,\tilde Y)e_0\bigr)=N(\tilde X,\tilde Y)L_{\tilde X}(e_0)=N(\tilde X,\tilde Y)N(\tilde X,e_0)e_0$, and $N(\tilde X,e_0)=X_0$; so the composite is $X_0N(\tilde X,\tilde Y)e_0=X_0L_{\tilde X}(\tilde Y)$.

The theorem is the specialisation of the composition law $L^{\bullet}_{\tilde A}L^{\bullet}_{\tilde B}=N(\tilde A,e_0)L^{\bullet}_{\tilde B}$ of *The Multiplication Operators of the Symmetric Quaternionic Algebra* to the single element $\tilde A=\tilde B=\tilde X$, and it is stated here as the identity the whole article reads. It is the exact replacement of the criterion of *The Specificities of the General Plain Algebra*, which in this algebra would read $L_{\tilde X}^{2}=L_{\tilde X\bullet\tilde X}$; the two are not the same, and the comparison is made at §*The Criterion Fails Here*.

**Corollary (the monoid law).** $L_{\tilde X}L_{\tilde Z}=X_0\,L_{\tilde Z}$ for all $\tilde X,\tilde Z$, so the family of left multiplications is stable under composition, it is a monoid with the reversed convention of composition, and every element of scalar coordinate $1$ is a left identity of the monoid.

**Proof.** The composite of the identity of the theorem with an arbitrary $L_{\tilde Z}$ gives the display, and at $X_0=1$ it reads $L_{\tilde X}L_{\tilde Z}=L_{\tilde Z}$: such an $L_{\tilde X}$ is a left identity.

**Remark (the monoid is not the algebra).** The multiplication of the algebra is commutative and has no unit, and the monoid of its left multiplications is non-commutative as soon as both factors have nonzero scalar coordinate ($L_{\tilde X}L_{\tilde Z}=X_0L_{\tilde Z}$ against $L_{\tilde Z}L_{\tilde X}=Z_0L_{\tilde X}$) and has left identities only. The passage from the algebra to its operators therefore changes both the commutativity and the unit, which is the sharpest illustration of the theme of the family: the element structure and the operator structure of these products are different objects.

## The Eleven Failures

Every operation of the catalogue other than the block is exhibited here with a witness: first a pair of elements witnessing the failure of the scalar law, then, for the operator reading, a witness of the failure of the composition law. The three groups are the three mechanisms — reading a general product whole, symmetrising, antisymmetrising.

### The Four General Products Read Whole

None of the four is commutative, and none has central values.

| the operation | the failure of commutativity | the value that is not central |
|---|---|---|
| $\tilde X\tilde Y$ | $e_1e_2=e_3$, $e_2e_1=-e_3$ | $e_0e_1=e_1$ |
| $\tilde X^{\natural}\tilde Y$ | $e_0^{\natural}e_1=e_1$, $e_1^{\natural}e_0=-e_1$ | $e_0^{\natural}e_1=e_1$ |
| $\tilde X\tilde Y^{*}$ | $e_0e_1^{*}=-e_1$, $e_1e_0^{*}=e_1$ | $e_0e_1^{*}=-e_1$ |
| $\tilde X^{\natural}\tilde Y^{*}$ | $e_1^{\natural}e_2^{*}=e_3$, $e_2^{\natural}e_1^{*}=-e_3$ | $e_0^{\natural}e_1^{*}=-e_1$ |

The first row is the reason the asymmetric siblings of the block exist at all: the plain product carries the off-diagonal signs of the quaternion table, and the block is what remains of those signs when the two slots are symmetrised.

### The Other Three Symmetrisations

The three symmetrisations other than the block split into three uniques, and the split is the exact statement of what the scalar law adds to the symmetrisation. In the table $\circ$ is the operation of the row.

| the operation | commutative? | central values? | the witness |
|---|---|---|---|
| $\tfrac12(\tilde X\tilde Y+\tilde Y\tilde X)$ | yes | no | $e_0\circ e_1=e_1\notin\mathbb{C}e_0$ |
| $\tfrac12(\tilde X\tilde Y^{*}+\overline{\tilde Y}\tilde X^{\natural})$ | no | yes | $e_0\circ ie_0=-ie_0$, $ie_0\circ e_0=ie_0$ |
| $\tfrac12(\tilde X^{\natural}\tilde Y^{*}+\tilde Y^{*}\tilde X^{\natural})$ | no | no | $e_0\circ ie_0=-ie_0$; $e_0\circ e_1=-e_1$ |

The first row is the Jordan product of the plain algebra: it is commutative like the block, and it fails only the centrality, because the plain product's vector part survives the symmetrisation. The second row is the Hermitian reading: it has central values like the block, and it fails only the commutativity, because its conjugation is written in the second slot and conjugates a scalar. The third row fails both. The block is thus the intersection of the two rows that survive one clause each, and no other operation of the twelve lies in that intersection.

### The Four Antisymmetrisations

The two bilinear antisymmetrisations are alternating, $\tilde X\circ\tilde X=0$, and none of the four is commutative or central-valued; the two sesquilinear ones are **not** alternating, the plain one taking $\tilde X=e_0+ie_1$ to $2ie_1$ and the quaternionic one taking $\tilde X=e_2+ie_3$ to $-2ie_1$. In the table $\circ$ is the operation of the row.

| the operation | the witness of non-commutativity | the non-central value |
|---|---|---|
| $\tfrac12(\tilde X\tilde Y-\tilde Y\tilde X)=\mathbf X\times\mathbf Y$ | $e_1\circ e_2=e_3$, $e_2\circ e_1=-e_3$ | $e_1\circ e_2=e_3$ |
| $\tfrac12(\tilde X^{\natural}\tilde Y-\tilde Y^{\natural}\tilde X)=X_0\mathbf Y-Y_0\mathbf X-\mathbf X\times\mathbf Y$ | $e_0\circ e_1=e_1$, $e_1\circ e_0=-e_1$ | $e_0\circ e_1=e_1$ |
| $\tfrac12(\tilde X\tilde Y^{*}-\overline{\tilde Y}\tilde X^{\natural})$ | $e_0\circ e_1=-e_1$, $e_1\circ e_0=e_1$ | $e_0\circ e_1=-e_1$ |
| $\tfrac12(\tilde X^{\natural}\tilde Y^{*}-\tilde Y^{*}\tilde X^{\natural})=\mathbf X\times\overline{\mathbf Y}$ | $e_1\circ e_2=e_3$, $e_2\circ e_1=-e_3$ | $e_1\circ e_2=e_3$ |

### The Verdicts

| the structure | commutative? | central values? | the scalar law | the mechanism |
|---|---|---|---|---|
| the plain product | no | no | no | read whole |
| the quaternionic product | no | no | no | read whole |
| the plain sesquilinear product | no | no | no | read whole |
| the quaternionic sesquilinear product | no | no | no | read whole |
| the symmetric plain product | **yes** | no | no | symmetrised, the vector part survives |
| **the symmetric quaternionic product** | **yes** | **yes** | **yes** | symmetrised, and central |
| the symmetric plain sesquilinear product | no | **yes** | no | symmetrised, the conjugation conjugates a scalar |
| the symmetric quaternionic sesquilinear product | no | no | no | symmetrised |
| the antisymmetric plain product | no | no | no | antisymmetrised |
| the antisymmetric quaternionic product | no | no | no | antisymmetrised |
| the antisymmetric plain sesquilinear product | no | no | no | antisymmetrised |
| the antisymmetric quaternionic sesquilinear product | no | no | no | antisymmetrised |

### The Operator Reading Fails for the Eleven as Well

**Proposition (the five bilinear failures away from the block).** For the plain product and the symmetric plain product the element $e_0$ is a two-sided unit, and for the quaternionic product it is a left unit, so in the three cases $L_{e_0}$ is the identity; a law $L_{\tilde X}L_{\tilde Z}=\ell(\tilde X)L_{\tilde Z}$ taken at $\tilde Z=e_0$ would make $L_{\tilde X}$ a scalar multiple of the identity, and it is not: for the plain product $L_{e_1}(e_0)=e_1$ while $L_{e_1}(e_2)=e_3$; for the quaternionic product $L_{e_1}(e_0)=-e_1$ while $L_{e_1}(e_2)=-e_3$; for the symmetric plain product $L_{e_1}(e_0)=e_1$ while $L_{e_1}(e_1)=-e_0$. For the antisymmetric plain product the witness is $\tilde X=\tilde Z=e_1$, where $L_{e_1}(e_2)=e_3$ while $L_{e_1}^2(e_2)=-e_2$; for the antisymmetric quaternionic product the same pair, where $L_{e_1}(e_2)=-e_3$ while $L_{e_1}^2(e_2)=-e_2$.

**Proposition (the six sesquilinear failures, by parity).** In the six sesquilinear operations — the plain and the quaternionic, the symmetric and the antisymmetric ones — the left multiplication is conjugate-linear in its argument, while a composite $L_{\tilde X}L_{\tilde Z}$ is $\mathbb{C}$-linear. A linear operator equal to a conjugate-linear one vanishes, so a law $L_{\tilde X}L_{\tilde Z}=\ell(\tilde X)L_{\tilde Z}$ would force $L_{\tilde X}L_{\tilde Z}=0$ for all $\tilde X,\tilde Z$, and the composite is not always zero: for the plain and the quaternionic sesquilinear products $L_{e_0}^2$ is the identity, since ${}^{*}$ is an involution; for the symmetric plain sesquilinear product $L_{e_0}^2(\tilde W)=W_0e_0$, nonzero at $\tilde W=e_0$; for the symmetric quaternionic sesquilinear product $L_{e_0}$ is the star involution, so $L_{e_0}^2$ is the identity; for the antisymmetric plain sesquilinear product $L_{e_0}^2$ is the projection $\tilde W\mapsto\mathbf W$ onto the vector subspace, nonzero at a generic argument; and for the antisymmetric quaternionic sesquilinear product $L_{e_1}^2(e_2)=-e_2\neq0$. The parity obstruction is the same one that the article of the plain algebra records for its sesquilinear neighbours, and it is why the two sesquilinear members of the symmetric family carry no projector but the zero operator (§*The Symmetric Family, in Detail*).

## The Projectors

**Theorem (the classification).** The operator $L_{\tilde X}$ is a projector if and only if $\tilde X=0$ or $X_0=1$.

**Proof.** By §*The Operator Identity* the condition is $(X_0-1)L_{\tilde X}=0$. If $X_0=1$ it holds. If $X_0\neq1$ then $L_{\tilde X}=0$, and by the faithfulness of §*The Left Multiplication Is Rank One* this is $\tilde X=0$, whose scalar coordinate is $0\neq1$; so the two cases are disjoint and cover the condition.

**Corollary (the family and its shape).** The projectors are the operators $L_{\tilde X}$ with $X_0=1$, one for each point of the affine hyperplane $\{X_0=1\}$, together with the zero operator at $\tilde X=0$. Each is the projection onto the central line $\mathbb{C}e_0$ along the hyperplane $\ker N(\tilde X,\cdot)$, it fixes $e_0$ and kills that kernel, the family is of complex dimension three, and its members are pairwise distinct.

**Proof.** At $X_0=1$ the operator is idempotent by the theorem, its image is $\mathbb{C}e_0$ and its kernel is a hyperplane by §*The Left Multiplication Is Rank One*, and the two are complementary because $N(\tilde X,e_0)=X_0=1$ does not vanish on the image: the operator is the projection onto $\mathbb{C}e_0$ along the kernel, and it fixes $e_0$. The distinctness is the faithfulness of §*The Left Multiplication Is Rank One*, and the hyperplane has complex dimension three.

**Remark (the projection is onto the line, not onto the element's own span).** Every member of the family is a projection of rank one onto the **same** line $\mathbb{C}e_0$, and the members differ only in the direction along which they project, which is the kernel of $L_{\tilde X}$. The family is therefore a projective space of directions rather than a family of subspaces: the kernels $N(\tilde X,\cdot)=0$, that is the points of the dual projective space $\mathrm{PG}(3,\mathbb{C})^{*}$ whose hyperplane does not contain the central line, the index $\tilde X$ ranging over the affine chart $X_0=1$. The hyperplanes that do contain the central line form the projective plane $X_0=0$ inside that dual space, and they are exactly the kernels excluded here.

**Remark (the algebra disowns its projectors).** The idempotents of the algebra are $0$ and $e_0$ alone, and the projectors are indexed by the hyperplane $X_0=1$ and by the origin. The overlap of the two descriptions is one element, besides the origin: $e_0$. Even there the coincidence is misleading, because $L_{e_0}$ is not the identity: it is the projection $E:\tilde Y\mapsto Y_0e_0$ onto the central line, the identity being unavailable since the algebra has no unit. The family is thus indexed by elements that are not idempotents of the algebra, and it is a full three-parameter family all the same.

**Remark (the parallel with the general quaternionic product).** In the general quaternionic algebra the projectors are the plain left multiplications indexed by the plain idempotents, a family of complex dimension two (*The Specificities of the General Quaternionic Algebra*). Here the family is indexed by the hyperplane $X_0=1$, of complex dimension three, and by itself: the index set and the family have the same dimension. In both cases the algebra disowns its projectors, the element idempotents being far fewer than the operator ones, and in both cases the disjunction has one source, that the operator reads the element only through a pairing and so cannot see the idempotent equation.

## The Square-Zero Operators

**Theorem (the classification).** The operator $L_{\tilde X}$ is square-zero if and only if $X_0=0$.

**Proof.** By §*The Operator Identity* $L_{\tilde X}^{2}=X_0L_{\tilde X}$, which vanishes when $X_0=0$. Conversely if $L_{\tilde X}^{2}=0$ and $X_0\neq0$ then $L_{\tilde X}=0$, hence $\tilde X=0$ by faithfulness, and $0$ has scalar coordinate $0$, a contradiction.

**Corollary (the set and its shape).** The square-zero operators are the operators $L_{\tilde X}$ with $X_0=0$, that is with $\tilde X$ in the vector subspace $\mathrm{Vect}(\mathbb{B})=\mathbb{C}e_1+\mathbb{C}e_2+\mathbb{C}e_3$, which is the orthogonal complement of the central line and is of complex dimension three; the operator is zero at $\tilde X=0$ and of rank one elsewhere, and it is a two-step flag $\{0\}\subseteq\mathbb{C}e_0\subseteq\ker N(\tilde X,\cdot)$.

**Proof.** The vanishing of $X_0$ is the vanishing of the scalar coordinate, that is membership in the vector subspace; the rank statement is §*The Left Multiplication Is Rank One*, and the flag is the image inside the kernel, which is the shape of a square-zero operator.

**Remark (the two meanings of square-zero).** The square-zero **elements** of the algebra are the isotropic ones, the cone $N(\tilde X,\tilde X)=0$ of complex dimension three (*The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*), and the square-zero **operators** are the elements of the vector subspace, also of complex dimension three. The two sets are different: the isotropic cone contains $e_1+ie_2$, whose scalar coordinate is $0$ and which therefore does belong to both, and it contains $e_0+e_1$, whose scalar coordinate is $1$ and whose operator is a projector rather than a square-zero one. The coincidence of the dimensions is arithmetic and the two sets are not equal.

**Remark (the sharp asymmetry between the two halves).** The theorem and the classification before it split the space by the scalar coordinate alone, and the split is the whole operator theory: $X_0=1$ gives the projectors, $X_0=0$ the square-zero ones, and every other element gives an operator that is neither. The property of being a projector is therefore not an algebraic property of the element in this algebra but the single scalar equation $X_0=1$, which is why the family is a hyperplane and why the algebra's own idempotent equation meets it in one element.

## The Criterion Fails Here

The criterion of *The Specificities of the General Plain Algebra* reads $L_{\tilde X}^{2}=L_{\tilde X\bullet\tilde X}$ and characterises the left-alternative products. In this algebra the two sides are $X_0L_{\tilde X}$ and, by §*The Operator Identity* read at the element $\tilde X\bullet\tilde X=N(\tilde X,\tilde X)e_0$,

$$
L_{\tilde X\bullet\tilde X}=N(\tilde X,\tilde X)\,L_{e_0}=N(\tilde X,\tilde X)\,E,\qquad E:\tilde Y\mapsto Y_0e_0 ,
$$

so the criterion would demand $X_0N(\tilde X,\tilde Y)=N(\tilde X,\tilde X)Y_0$ for every $\tilde Y$, that is the pair of conditions $X_0^{2}=N(\tilde X,\tilde X)$ and $X_0X_k=0$ for $k=1,2,3$. The conditions fail at the first vector, where the two sides of the alternativity law are

$$
e_1\bullet(e_1\bullet e_0)=0,\qquad (e_1\bullet e_1)\bullet e_0=e_0 ,
$$

since $e_1\bullet e_0=N(e_1,e_0)e_0=0$ while $e_1\bullet e_1=N(e_1,e_1)e_0=e_0$. The algebra is not left-alternative, the criterion is not available, and the classification above is not an instance of it: it is read from the identity of §*The Operator Identity*, which holds for the algebra's own reason, the rank-one shape of the product.

## The Symmetric Family, in Detail

The four symmetric products of the complex space behave alike at the element level and differently at the operator level. The table below collects the projectors of the left multiplication, the quantity whose row of *The Specificities of the General Plain Algebra* this article corrects.

| structure | product | elements with an idempotent left multiplication | the operator |
|---|---|---|---|
| SPA | $\tfrac12(\tilde X\tilde Y+\tilde Y\tilde X)$ | $0$ and $e_0$ alone | $0$ and the identity |
| SQA | $\tfrac12(\tilde X^{\natural}\tilde Y+\tilde Y^{\natural}\tilde X)$ | the origin, and the hyperplane $X_0=1$ | $0$, and rank-one projections onto $\mathbb{C}e_0$ |
| SPS | $\tfrac12(\tilde X\tilde Y^{*}+\overline{\tilde Y}\tilde X^{\natural})$ | $0$ alone | $0$ |
| SQS | $\tfrac12(\tilde X^{\natural}\tilde Y^{*}+\tilde Y^{*}\tilde X^{\natural})$ | $0$ alone | $0$ |

The pattern is the failure of left alternativity in all four and the collapse of the element idempotents, and the operator answers separate them: the symmetric plain product recovers the identity and nothing else, the symmetric quaternionic product a hyperplane of rank-one projections, and the two symmetric sesquilinear products only the zero operator, because their left multiplications are conjugate-linear and a conjugate-linear operator that is idempotent is zero (§*The Twisted Second Slot* of the article that began the family). The symmetric quaternionic product is the one member whose operator family is a hyperplane, and it is the reason its row in the comparison table is the only one of the symmetric family that needed a correction.

## Summary

The symmetric quaternionic product satisfies the **scalar law** — it is commutative and its values lie in the centre, equivalently $\tilde P\bullet\tilde Q=N(\tilde P,\tilde Q)e_0$ for a symmetric bilinear form — and it is the only one of the twelve operations that does: the two other symmetrisations that survive one clause each fail the other (the symmetric plain product is commutative and not central, the symmetric plain sesquilinear product central and not commutative), and the four general products and the four antisymmetrisations fail both. Its left multiplication is the rank-one operator $L_{\tilde X}\tilde Y=N(\tilde X,\tilde Y)e_0$, faithful in $\tilde X$ because the form is non-degenerate, and the single identity $L_{\tilde X}^{2}=X_0L_{\tilde X}$ classifies everything: the operator is a projector exactly when $\tilde X=0$ or $X_0=1$, and square-zero exactly when $X_0=0$; the operator reading $L_{\tilde X}L_{\tilde Z}=X_0L_{\tilde Z}$ likewise fails for the other eleven, for the six sesquilinear ones by the parity obstruction and for the rest on explicit witnesses. The projectors are the affine hyperplane $X_0=1$ together with the zero operator, a family of complex dimension three of pairwise distinct rank-one projections onto the central line, indexed by the hyperplane and not by the idempotents of the algebra, which are $0$ and $e_0$ alone; even the element $e_0$ gives the projection onto the central line and not the identity, since the algebra has no unit. The square-zero operators are the vector subspace $X_0=0$, which is not the isotropic cone of the square-zero elements, the two coinciding only on the intersection. Among the four symmetric products the block is the only one with a hyperplane of projectors, and that is the row it proves in the comparison table of *The Specificities of the General Plain Algebra*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\bullet$, $\star$ | the symmetric quaternionic product $\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)=N(\tilde P,\tilde Q)e_0$ |
| $\circ$ | the generic operation of another structure of the catalogue, in the comparison tables |
| scalar law | commutative with central values: $\tilde X\circ\tilde Y=\beta(\tilde X,\tilde Y)e_0$, $\beta$ symmetric |
| $X_0$, $\mathbf X$ | the scalar coordinate and the vector part of $\tilde X=X_0+\mathbf X$ |
| $\mathrm{Sc}(\tilde X)=X_0$ | the scalar coordinate, read as a functional |
| $N$ | the quaternion form $N(\tilde X,\tilde Y)=X_0Y_0+(\mathbf X,\mathbf Y)$, symmetric, non-degenerate, of Gram matrix the identity |
| $L_{\tilde X}$ | the left multiplication $\tilde Y\mapsto\tilde X\bullet\tilde Y=N(\tilde X,\tilde Y)e_0$, rank one for $\tilde X\neq0$ |
| $E$ | the projection $E:\tilde Y\mapsto Y_0e_0$ onto the central line, the operator of $e_0$ |
| $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$ | the central line and the vector subspace, the eigenspaces of the scalar coordinate |
| idempotent, projector | an element, and an operator, equal to its own square |
| $\mathbb{B}$ | the complex space $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |

## Further Reading

- *The Specificities of the General Plain Algebra* (`articles_maths/the-specificities-of-the-general-plain-algebra.md`), for the criterion that classifies the twelve structures and for the row this article proves.
- *The Specificities of the General Quaternionic Algebra* (`articles_maths/the-specificities-of-the-general-quaternionic-algebra.md`), for the companion family of projectors in the general quaternionic product.
- *Introduction to the Symmetric Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-algebra-of-biquaternions.md`), for the governing formula $\tilde P\bullet\tilde Q=N(\tilde P,\tilde Q)e_0$ and for the absence of a unit.
- *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra* (`articles_maths/the-radical-and-the-isotropic-elements-of-the-symmetric-quaternionic-algebra.md`), for the trivial radical, the idempotents $0$ and $e_0$, and the isotropic cone of the square-zero elements.
- *The Multiplication Operators of the Symmetric Quaternionic Algebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-quaternionic-algebra.md`), for the composition law and the rank, trace and adjoint of the operators.
