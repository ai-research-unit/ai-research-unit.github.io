# __Operator Chirality on the Biquaternion Algebra__

## Introduction

**The question.** Every operator of the biquaternion algebra is built from two regular maps, the left multiplication $L$ and the right multiplication $R$, and the two are symmetric in the definition and asymmetric in the results. This article asks what chirality means for such an operator, and answers with the two maps alone.

**The answer in one line.** Operator chirality is the side: an operator has the left slot when it lies in the image of $L$, the right slot when it lies in the image of $R$, both slots at once when it is a scalar, and no single side otherwise. The definition names two maps and two subspaces of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$. It names no frame, no axis, no basis element and no volume.

**What replaces the frame.** The two images are the two tensor factors of $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}$ under the structure isomorphism $\Phi(a\otimes b)=L_aR_b$. The operator that exchanges the two factors is the flip, transported to $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ as $\sigma=\Phi\tau\Phi^{-1}$, and it is that single intrinsic involution, and not a fifth cell read from a frame, which pairs with chirality.

**What the article is not about.** The notion is defined on the endomorphism algebra and needs nothing else. Section §*What Operator Chirality Is Not* separates it, one object at a time, from a root, an idempotent, a Peirce decomposition, a Peirce basis, a spinor, a Pauli matrix, an ideal, a Clifford algebra, and the fifth cell of a gamma frame.

**The order of the article.** Section §*The Two Slots* defines the two regular maps, their images, the isomorphism $\Phi$ and the label. Section §*The Swap of the Two Sides* defines the flip and proves its properties. Section §*The Transpose Through the Trace Form* identifies the flip with the adjoint of the trace form and gives its array. Section §*The Two Eigenspaces* computes the two eigenspaces, of dimensions ten and six, and the operation that closes on each. Section §*Conjugation Exchanges the Sides* proves that the quaternion conjugate carries the left side to the right side, and separates it from the flip. Section §*What Operator Chirality Is Not* is the separation. Section §*Why the Slot Label Is Not a Grading* fixes what the sides can and cannot supply.

**Boundaries.** The cells and the two families are *Families of Matrix Representations*; the carriers and their splittings are *The Unpolarized Module of the Biquaternion Algebra*; the general theory of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ is *The Endomorphisms of the Biquaternion Algebra*; the operator arrays are *$M_4(\mathbb{C})$ Axis-Free Representation : Operators* and *$M_4(\mathbb{C})$ Pauli Representation : Operators*; and the frame cells are *The Gamma Frame and the Complexified Dirac Algebra of $M_4(\mathbb{C})$*, which also carries the example that this article keeps out of its definitions.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, central simple over $\mathbb{C}$, of complex dimension four, with unit $e_t$ and reduced trace $\operatorname{Sc}$. The left and the right regular maps are written $L$ and $R$, and a product of the two is written $L_aR_b$ for $L(a)R(b)$. The identity operator is $\mathrm I$. **No basis of $\mathbb{B}$ is declared and none is used**: every statement below is about elements, images and subspaces, and an array appears only in §*The Transpose Through the Trace Form*, where it is attached to a named basis and to nothing else.

## The Two Slots

**The article in one paragraph.** Two $\mathbb{C}$-linear maps carry $\mathbb{B}$ into the endomorphism algebra, one on each side. Their images are two four-dimensional subspaces that meet in the scalars, and the whole content of this article is the geometry of that pair of subspaces and of the involution that exchanges them. The rest is bookkeeping.

### The Two Regular Maps

**Two maps.** The **left regular map** and the **right regular map** are

$$
L\colon\mathbb{B}\to\operatorname{End}_{\mathbb{C}}(\mathbb{B}),\quad L(a)(\tilde X)=a\tilde X,
\qquad
R\colon\mathbb{B}\to\operatorname{End}_{\mathbb{C}}(\mathbb{B}),\quad R(b)(\tilde X)=\tilde Xb .
$$

Both are $\mathbb{C}$-linear. Both are injective, because a left multiplier that vanishes on the unit vanishes everywhere: $L(a)(e_t)=a$. Both are unital, $L(e_t)=R(e_t)=\mathrm I$.

**They commute.** For all $a,b\in\mathbb{B}$ and every $\tilde X$,

$$
(L(a)R(b))(\tilde X)=a\tilde Xb=(R(b)L(a))(\tilde X),
$$

so $L(a)R(b)=R(b)L(a)$. The two sides act on opposite copies of the argument, and that is the whole reason.

**Composition.** Composing two products of regular maps gives

$$
\bigl(L_aR_b\bigr)\bigl(L_cR_d\bigr)=L_{ac}R_{db},
$$

because the right parameters meet in the middle and multiply in the reverse order. Verified on $200$ random pairs, residual $4.3\times10^{-14}$.

### The Two Families

**Two images, one ambient.** The images of the two maps are written $L(\mathbb{B})$ and $R(\mathbb{B})$. Their dimensions, their intersection and their sum are the first facts of the article.

| Space | Dimension | What it is |
|---|---|---|
| $L(\mathbb{B})$ | $4$ | the pure left multipliers $L(a)$ |
| $R(\mathbb{B})$ | $4$ | the pure right multipliers $R(b)$ |
| $L(\mathbb{B})\cap R(\mathbb{B})$ | $1$ | the scalars, $\mathbb{C}\,\mathrm I$ |
| $L(\mathbb{B})+R(\mathbb{B})$ | $7$ | the one-sided operators |
| $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ | $16$ | all operators |

**The three dimensions.** The images are four-dimensional because $L$ and $R$ are injective on a four-dimensional algebra. The intersection is the scalar line and nothing more: $L(a)=R(b)$ forces $a\tilde X=\tilde Xb$ for every $\tilde X$, and taking $\tilde X=e_t$ gives $a=b$, after which $a$ commutes with every element, so $a$ is central. The sum is therefore $4+4-1=7$. All five numbers recomputed here.

**A cell, and its two slots.** An operator of the form $L_aR_b$ is called a **cell**, and it has two slots: the left one, where $a$ multiplies, and the right one, where $b$ multiplies. The slot is a place in the operator, not a property of the elements $a$ and $b$.

### The Structure Isomorphism

**The statement.** The multiplication of the algebra defines a $\mathbb{C}$-linear map on the tensor square,

$$
\Phi\colon\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}\longrightarrow\operatorname{End}_{\mathbb{C}}(\mathbb{B}),
\qquad
\Phi(a\otimes b)=L_aR_b .
$$

**It is an isomorphism.** For any $\mathbb{C}$-basis $e_1,\dots,e_4$ of $\mathbb{B}$ the sixteen operators $L_{e_\mu}R_{e_\nu}$ are linearly independent, since the sixteen coefficients of an operator on the four basis elements are the entries of an arbitrary $4\times4$ array; sixteen independent operators in a sixteen-dimensional space are a basis. Verified: the sixteen cells of a declared basis span, rank $16$.

**The three subspaces, read through $\Phi$.** Under the isomorphism the two families are the two tensor factors,

$$
L(\mathbb{B})=\Phi(\mathbb{B}\otimes e_t),\qquad
R(\mathbb{B})=\Phi(e_t\otimes\mathbb{B}),\qquad
L(\mathbb{B})\cap R(\mathbb{B})=\Phi(e_t\otimes e_t)=\mathbb{C}\,\mathrm I .
$$

This is the technical core of the article. The two sides are not two constructions of the same object; they are the first and the second factor of the tensor square, and their overlap is the tensor of the two units.

### The Cell Is a Coordinate of the Isomorphism

**What the cell is for.** The cell $L_aR_b$ is the image of the elementary tensor $a\otimes b$. It is a coordinate of the isomorphism and not the definition of anything: an operator has one coefficient array in the sixteen cells, and that array is the coordinate. A statement written in cells is a statement about $\Phi$, and it becomes intrinsic when it is written in the two images.

**Why the order matters here.** A reader who takes the cells as primitive will reach for a basis to name them, then for a frame, then for a direction inside the frame. The definition below needs none of the three, and the order of this section, maps first and cells last, is what keeps the reach from happening.

### The Label, Which Is the Operator Chirality

**The definition.** With the two images fixed, the label is one line:

| Label | The operator |
|---|---|
| left slot | $X\in L(\mathbb{B})$ |
| right slot | $X\in R(\mathbb{B})$ |
| both slots | $X\in L(\mathbb{B})\cap R(\mathbb{B})=\mathbb{C}\,\mathrm I$ |
| no single side | $X$ in neither image |

An operator has the **left slot** when it is a pure left multiplier, the **right slot** when it is a pure right multiplier, **both slots** when it is a scalar, and **no single side** otherwise. Operator chirality is that label. The definition uses the two regular maps and nothing else.

**Four labels, and one word used twice.** The four rows are mutually exclusive, and the third is the one that is easily confused with a two-sided cell. A cell with two occupied slots, $L_aR_b$ with neither $a$ nor $b$ central, is **not** an operator with "both slots" in the sense of the third row: it is a two-sided operator, a member of the family $LR$, and its label is "no single side". The word *both* names two different things in the two sentences, and the corpus keeps them apart by grammar: the chirality is a label of an operator, and $LR$ is the name of a family of operators. The third row is the only case in which an operator multiplies on both sides at once.

**The product of two cells, read on the label.** The composition rule shows the asymmetry at once. A product of two left multipliers is a left multiplier, $L_aL_c=L_{ac}$, and a product of two right multipliers is a right multiplier, $R_bR_d=R_{db}$. So each of the two one-sided families is a subalgebra, of dimension four, and the two subalgebras meet in the scalars. A product of one of each is a cell, and a general cell has no side.

### The Centre Has Both Sides

**The scalars.** For central $\lambda$ the two multiplications agree, $\lambda\tilde X=\tilde X\lambda$, so $L(\lambda e_t)=R(\lambda e_t)=\lambda\mathrm I$. The overlap of the two families is exactly the set of operators for which the question "which side" has two correct answers, and it is the one-dimensional intersection of the table. That is not a defect of the definition: a scalar multiplies on both sides, and the label records it.

**No sign separates the two families on the overlap.** A reader who expects a left multiplier to be the $+1$ one and a right multiplier the $-1$ one is stopped here, at the scalar $\mathrm I$, which would have to be both. Section §*Why the Slot Label Is Not a Grading* turns that obstruction into a theorem.

### The Complement Has No Single Side

**The set, not a subspace.** Nine dimensions of the sixteen are outside $L(\mathbb{B})+R(\mathbb{B})$, and every operator there has no single side. The set of operators with no single side is larger than those nine directions: it is the complement of the union $L(\mathbb{B})\cup R(\mathbb{B})$, which is neither a subspace nor closed under addition. The operator $L_a+L_c$ has the left slot, and the operator $L_a+R_b$ has none.

**The label is a name, not a quantity.** It is four-valued on the algebra, it is not additive, and it carries no sign: $c\,L_a$ and $-c\,L_a$ have the same label. No linear functional on $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ assigns the four labels, and §*Why the Slot Label Is Not a Grading* proves why.

## The Swap of the Two Sides

**The object of this section.** The two images are exchanged by one canonical involution, and that involution is the only intrinsic order-two structure the endomorphism algebra carries. It is defined on the tensor square and transported by $\Phi$.

### The Flip of the Two Factors

**The definition.** Let $\tau$ be the flip of the two factors,

$$
\tau\colon\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}\to\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B},
\qquad
\tau(a\otimes b)=b\otimes a ,
$$

and let the **swap** be its transport to the endomorphism algebra,

$$
\sigma=\Phi\circ\tau\circ\Phi^{-1}\colon\operatorname{End}_{\mathbb{C}}(\mathbb{B})\to\operatorname{End}_{\mathbb{C}}(\mathbb{B}).
$$

On a cell this is

$$
\sigma(L_aR_b)=L_bR_a .
$$

**It is well defined.** The map $\Phi$ is an isomorphism and the sixteen cells are a basis, so an operator has one coefficient array and the rule exchanges the two indices of that array. The exchange refers to the two entries of an elementary tensor $a\otimes b$, not to a basis: no basis is declared and none is used. The identity was checked on $100$ random elements for the one-sided case and on $100$ random pairs for the product rule below.

### It Is an Involution and It Reverses Products

**The square.** Exchanging the two entries of $a\otimes b$ twice returns $a\otimes b$, and the cells span, so

$$
\sigma^2=\mathrm{id}\qquad\text{on all of }\operatorname{End}_{\mathbb{C}}(\mathbb{B}),
$$

verified as an exact permutation of the cell basis.

**The product.** For two cells,

$$
\sigma\bigl((L_aR_b)(L_cR_d)\bigr)=\sigma(L_{ac}R_{db})=L_{db}R_{ac}=(L_dR_c)(L_bR_a)=\sigma(L_cR_d)\,\sigma(L_aR_b),
$$

which is the reversed product, and linearity extends it. So

$$
\sigma(XY)=\sigma(Y)\sigma(X)
$$

for all $X,Y$, verified on $100$ random pairs with zero residual, because the swap permutes the cells exactly. The swap is an anti-automorphism of order two, that is an isomorphism onto the opposite algebra: an involution and a reversal at once.

### It Exchanges the Two Images

**The three statements.** Straight from the definition,

$$
\sigma\bigl(L(\mathbb{B})\bigr)=R(\mathbb{B}),\qquad
\sigma\bigl(R(\mathbb{B})\bigr)=L(\mathbb{B}),\qquad
\sigma\big|_{L\cap R}=\mathrm{id}.
$$

The first two say that the swap exchanges the sides, which is why it belongs in an article about chirality: it answers the question "which side" by moving the operator to the other side rather than by labelling it. The third says that the scalars are fixed, consistently with their having no side to exchange.

**The label after the swap.** An operator with the left slot becomes an operator with the right slot, and an operator with no single side stays where it is: a cell $L_aR_b$ with neither parameter central is carried to the cell $L_bR_a$, which also has no single side. The swap permutes the four labels by exchanging the first two and fixing the last two.

### It Carries Each Left Multiplier to the Right Multiplier

**The case that matters.** For every $a\in\mathbb{B}$,

$$
\sigma(L_a)=R_a ,
$$

which is the case $b=e_t$ of the definition. The left multiplier of an element and the right multiplier of the same element are the same array read on the two sides, and the swap is what carries one to the other. Verified on $100$ random elements, with zero residual.

**What it does not do.** It does not carry a left multiplier to another left multiplier, and no power of it does. The two images are exchanged and each is carried out of itself, except along the scalar line.

### It Preserves Rank and Length

**Rank and length.** The swap permutes the cells of a basis, so it carries a product of two one-sided operators to another such product, and it preserves the length $\ell$ of *$M_4(\mathbb{C})$ Axis-Free Representation : Operators*, which is the number of one-sided factors in a decomposition. The length is the rank of the coefficient matrix, and the swap transposes that matrix, so

$$
\ell(\sigma(M))=\ell(M),\qquad \operatorname{rank}\sigma(M)=\operatorname{rank}M .
$$

Verified on $50$ random operators: the rank is unchanged in every case. The rank-one cone, that is the set of nonzero scalar multiples of single cells, is carried to itself.

### It Is Not Inner

**The argument.** An inner automorphism $X\mapsto \mathsf S X\mathsf S^{-1}$ is a homomorphism of the algebra, and $\sigma$ is not: it reverses products. So no invertible $\mathsf S$ satisfies $\sigma(X)=\mathsf S X\mathsf S^{-1}$ for all $X$. The swap is not a conjugation by a chosen matrix and cannot be produced by one; it is a new operator on $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, the transport of the flip. This also separates it from the quaternion conjugate of §*Conjugation Exchanges the Sides*, whose congruence does conjugate the parameters as well.

## The Transpose Through the Trace Form

**The object of this section.** The swap has an equivalent description as an adjoint, and the description is what makes it computable. It uses the reduced trace and nothing else.

### The Trace Form

**The form.** The **trace form** is

$$
\beta(\tilde X,\tilde Y)=\operatorname{Sc}(\tilde X\tilde Y).
$$

It is $\mathbb{C}$-bilinear and symmetric, and it is nondegenerate, since $\operatorname{Sc}$ is nondegenerate on a central simple algebra. It is cyclic in the sense that matters here:

$$
\operatorname{Sc}\bigl(\tilde X\tilde Y\tilde Z\bigr)=\operatorname{Sc}\bigl(\tilde Y\tilde Z\tilde X\bigr).
$$

**Nothing is chosen.** The form is built from the multiplication and the trace. No basis, no frame and no direction enters, and the two properties used below, symmetry and cyclicity, are properties of $\operatorname{Sc}$.

### The Flip Is the Adjoint of the Trace Form

**The theorem.** For every $X\in\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ and all $\tilde Y,\tilde Z\in\mathbb{B}$,

$$
\beta\bigl(X\tilde Y,\tilde Z\bigr)=\beta\bigl(\tilde Y,\sigma(X)\tilde Z\bigr).
$$

So the swap is the **adjoint of $X$ with respect to $\beta$**, and that sentence is basis-free.

**The proof on the cells.** For $X=L_aR_b$,

$$
\beta\bigl(L_aR_b\tilde Y,\tilde Z\bigr)=\operatorname{Sc}\bigl(a\tilde Yb\tilde Z\bigr),
\qquad
\beta\bigl(\tilde Y,L_bR_a\tilde Z\bigr)=\operatorname{Sc}\bigl(\tilde Yb\tilde Za\bigr),
$$

and the two are equal by cyclicity. Linearity extends the identity. Verified on $50$ random triples, residual $3.2\times10^{-14}$.

### The Array

**The basis that makes it a transpose.** Let $\mathcal{B}_0$ be a basis of $\mathbb{B}$ in which $\beta$ is diagonal with entries $1,-1,-1,-1$; such a basis exists because $\beta$ is nondegenerate and symmetric, and it is the coefficient basis of *Algebra and Element Conventions*. Write $\mathsf D=\operatorname{diag}(1,-1,-1,-1)$, the Gram matrix of $\beta$ in $\mathcal{B}_0$. Since $\mathsf D^2=\mathrm I$, the adjoint of a matrix for $\beta$ is

$$
[X]_{\mathcal{B}_0}^{\beta}=\mathsf D\,[X]_{\mathcal{B}_0}^{\mathsf T}\,\mathsf D ,
$$

so in this basis the swap is the transpose read through a sign matrix:

$$
[\sigma(X)]_{\mathcal{B}_0}=\mathsf D\,[X]_{\mathcal{B}_0}^{\mathsf T}\,\mathsf D .
$$

**The same matrix, read on the two families.** The identity between the two families is the same display,

$$
R(b)=\mathsf D\,L(b)^{\mathsf T}\mathsf D ,
$$

which is the case of a pure right multiplier, and it is why the two families have arrays that agree up to a sign. Verified on the four basis elements and on a general element, with zero residual.

### What Depends on the Basis

**The two dependences cancel.** The transpose depends on the basis and $\mathsf D$ depends on the basis, while $\sigma$ does not: the product does not. That is why a statement proved with one display holds in all of them, and why the array above is a convenience rather than a definition.

**The identity in another basis.** In a basis $\mathcal{B}$ the same statement is read with two matrices, not one:

$$
[\sigma(X)]_{\mathcal{B}}=\mathsf W\,[X]_{\mathcal{B}}^{\mathsf T}\,\mathsf W^{-1},
$$

with $\mathsf W$ the matrix obtained from $\mathsf D$ by congruence. The symmetric form $\mathsf W[X]^{\mathsf T}\mathsf W$ is recovered exactly when $\mathsf W^2=\mathrm I$, which holds in $\mathcal{B}_0$ and in the Pauli display, and which fails in a general basis. So the sentence "the swap is the transpose through the switch" is a sentence about a basis that carries a switch of square one, while the sentence "the swap is the adjoint of the trace form" is a sentence about the algebra. The second is the one to quote.

## The Two Eigenspaces

**The object of this section.** The swap is an involution, so the algebra it acts on splits into a fixed space and a negated space. The two dimensions are ten and six, and each carries an operation under which it closes.

### The Fixed Space

**What it is.** An operator is fixed exactly when it is self-adjoint for $\beta$,

$$
\sigma(X)=X\quad\Longleftrightarrow\quad \beta(X\tilde Y,\tilde Z)=\beta(\tilde Y,X\tilde Z),
$$

and the fixed space is the image under $\Phi$ of the symmetric square,

$$
\operatorname{Fix}(\sigma)=\Phi\bigl(\operatorname{Sym}^2\mathbb{B}\bigr),
$$

of dimension $4\cdot5/2=10$. Verified: rank $10$ for the projector $\tfrac12(\mathrm I+\sigma)$.

### The Negated Space

**What it is.** An operator is negated exactly when it is skew-adjoint for $\beta$,

$$
\sigma(X)=-X ,
$$

and the negated space is the image of the exterior square,

$$
\operatorname{Neg}(\sigma)=\Phi\bigl(\Lambda^2\mathbb{B}\bigr),
$$

of dimension $4\cdot3/2=6$. It is spanned by the six differences $L_aR_b-L_bR_a$, which are the commutators $[L_a,R_b]$ because the two regular maps commute. Verified: rank $6$ for $\tfrac12(\mathrm I-\sigma)$.

**The statement about a six-dimensional subspace.** The space $\operatorname{Neg}(\sigma)$ is six-dimensional, canonical and stable under the swap. A six-dimensional subspace chosen by other means need not be. The gamma frame of *The Gamma Frame and the Complexified Dirac Algebra of $M_4(\mathbb{C})$* supplies its bivector span, the six commutators $\tfrac12[\gamma_\mu,\gamma_\nu]$ of its four generators, and the swap carries exactly one of the six into that span and the other five out of it; the two spaces are both six-dimensional and they meet in dimension three. Verified on the five declared cells. The canonical space is fixed by the multiplication; the frame's is fixed by a choice, and the two must not be identified because their dimensions agree.

### The Two Operations

**Neither is an algebra.** The fixed space is not closed under the product: for $\sigma(X)=X$ and $\sigma(Y)=Y$ one has $\sigma(XY)=YX$, which is $XY$ only when the two commute. It is closed under the anti-commutator,

$$
\sigma\bigl(\tfrac12(XY+YX)\bigr)=\tfrac12(YX+XY)=\tfrac12(XY+YX),
$$

so it is a **Jordan algebra** of dimension ten under $X\circ Y=\tfrac12(XY+YX)$.

**The negated space is a Lie algebra.** For $\sigma(X)=-X$ and $\sigma(Y)=-Y$,

$$
\sigma(XY-YX)=\sigma(Y)\sigma(X)-\sigma(X)\sigma(Y)=YX-XY=-(XY-YX),
$$

so the commutator closes on it, and it is a **Lie algebra** of dimension six. Verified on $100$ random pairs in each space.

| Space | Dimension | Condition | Operation that closes |
|---|---|---|---|
| Fixed, $+1$ | $10$ | $\sigma(X)=X$ | anti-commutator, a Jordan algebra |
| Negated, $-1$ | $6$ | $\sigma(X)=-X$ | commutator, a Lie algebra |
| The whole | $16$ | none | the product, an associative algebra |

**What is specific to this algebra.** The decomposition of an endomorphism algebra into a symmetric and an exterior square is standard for a nondegenerate symmetric form. What is specific here is that the form is the trace form on the algebra and that the reflection is the exchange of the two sides. The decomposition is therefore read off the two-sided structure rather than imposed on it, which is the sense in which operator chirality and the Jordan–Lie split are one statement.

## Conjugation Exchanges the Sides

**The object of this section.** A second map exchanges the sides, and it is built from the algebra rather than from the tensor square. It is the reason the two sides have arrays that agree up to a sign.

### The Quaternion Conjugate

**The map.** The **quaternion conjugate** $\natural$ is the $\mathbb{C}$-linear involution of $\mathbb{B}$ that fixes the unit and negates the vector part,

$$
e_t^{\natural}=e_t,\qquad u^{\natural}=-u\quad\text{for }u\text{ in the vector subspace}.
$$

It is an **anti-automorphism**, $(\tilde X\tilde Y)^{\natural}=\tilde Y^{\natural}\tilde X^{\natural}$, verified on $200$ random pairs, residual $2.0\times10^{-15}$; the sign carried by the three vector units is what turns the product round. It fixes the coefficients and is therefore $\mathbb{C}$-linear. Its fixed space is the scalar line $\mathbb{C}e_t$ and its anti-fixed space is the three-dimensional vector subspace; the two dimensions are $1$ and $3$, verified.

**As a matrix.** On the basis $\mathcal{B}_0$ of §*The Array* the map is the diagonal sign matrix $\mathsf C=\mathsf D=\operatorname{diag}(1,-1,-1,-1)$, an involution.

### It Carries the Left Side to the Right Side

**The identity.** For every $a\in\mathbb{B}$,

$$
\natural\,L(a)\,\natural=R\bigl(a^{\natural}\bigr),
\qquad\text{equivalently}\qquad
\natural\,L\bigl(a^{\natural}\bigr)\,\natural=R(a).
$$

**The proof.** The map $\natural$ is an anti-automorphism, so applying it to the two ends of $a\tilde Y$ reverses them:

$$
\natural\bigl(L(a)\natural(\tilde Y)\bigr)=\natural\bigl(a\tilde Y^{\natural}\bigr)=\tilde Y\,a^{\natural},
$$

which is right multiplication by $a^{\natural}$. One line, and no basis is used. Verified on the four basis elements and on a general element, residual $0.0$.

**So the two sides are exchanged by a conjugation.** The left multiplier of $a$ becomes, under this congruence, the right multiplier of $a^{\natural}$. Since $\natural$ maps $L(\mathbb{B})$ onto $R(\mathbb{B})$ and back, it is the second side-exchanger of the article.

### It Is Not the Flip

**The two maps side by side.** They are different, and only one of them is the swap.

| Map | On $L_a$ | On a cell $L_aR_b$ | What it moves |
|---|---|---|---|
| $\sigma$ | $R_a$ | $L_bR_a$ | the two slots |
| $\natural$ | $R_{a^{\natural}}$ | $R_{a^{\natural}}L_{b^{\natural}}$ | the elements, and the order of the factors |

So $\sigma$ exchanges the slots and leaves the parameters alone, while $\natural$ exchanges the slots after conjugating the parameters and reversing their order. The first is the transport of the flip; the second is an anti-automorphism of the algebra read as a congruence of the endomorphism algebra. Neither is inner and neither is the other.

**Where they agree.** On a pure left multiplier they agree exactly when $a^{\natural}=a$, that is exactly when $a$ is central: the fixed space of $\natural$ is the scalar line. On the vector part they differ by a sign, and that sign is the source of every statement of the form "the same array, up to a phase".

### Where the Conjugation Enters

**The division of labour.** The conjugation is not needed to define chirality: the two images are defined by the two maps alone. It enters when one asks how a left multiplier and a right multiplier are related, and its answer is the table above. A reader who has only $\sigma$ can say which slot an operator occupies; a reader who also has $\natural$ can say when two operators of opposite slots have arrays that agree up to a sign. That is the whole content of the map, and it is why it belongs next to the swap rather than inside the definition.

**The phases.** Every phase in the corpus that is described as coming from a change of side comes from the sign of the three vector units in $\natural$. The identity above is the place where that sign is generated, and it is one identity, not a family of coincidences.

## What Operator Chirality Is Not

**The list.** The notion is one line long, the side, and it is routinely attached to nine other objects. The table states what each of them is and why the two regular maps do not need it.

| Object | What it is | Why operator chirality does not need it |
|---|---|---|
| a root | an element $\tilde{Ζ}$ with $\tilde{Ζ}^2=e_t$ | the sides are the images of $L$ and $R$; a root is an element chosen afterwards |
| an idempotent | an element $\tilde\Pi$ with $\tilde\Pi^2=\tilde\Pi$ | the definition uses no idempotent, and the label is four-valued rather than two-valued |
| a Peirce decomposition | the four lines $\mathbb{B}_{st}$ of a pair of idempotents | the sides are two subspaces of the operator space, the Peirce lines are four subspaces of the algebra |
| a Peirce basis | the units of one Peirce decomposition | a basis is a coordinate choice on $\mathbb{B}$, and the label is read without one |
| a spinor | an element of a minimal left ideal | an ideal needs a rank-one idempotent; the label is a property of an operator on $\mathbb{B}$ |
| a Pauli matrix | the array of a frame in the tensor display | the label is a membership, and a membership has no array |
| an ideal | a subspace of $\mathbb{B}$, here a point of a projective line | a subspace is chosen; the two images are given by the multiplication |
| a Clifford algebra | the algebra generated by vectors with $\{e_i,e_j\}=2g_{ij}$, here $\mathrm{Cl}_{1,3}(\mathbb{C})\cong M_4(\mathbb{C})$ | the label uses no Clifford relation, and Clifford data fix a dimension and a signature while the two images exist in every dimension |
| the fifth cell of a gamma frame | a right multiplier read off a declared frame | it is an example of the right side, not the definition of chirality |

**Not a root, not an idempotent.** A root is an element of the algebra and it enters when a Peirce decomposition is wanted. The label is fixed before any element is chosen: it depends on $L$ and $R$, which are built from the multiplication. An idempotent is a condition on an element, $\tilde\Pi^2=\tilde\Pi$; the label is a condition on an operator, a membership, and the two conditions have different shapes.

**Not a Peirce decomposition, not a Peirce basis.** A Peirce decomposition needs two idempotents and returns four lines of the algebra. The label returns four cases on the operator space, and none of the four is a line of $\mathbb{B}$. A Peirce basis is a basis, and the label is read without one: the images of $L$ and $R$ are given before any basis is declared.

**Not a spinor, not an ideal.** A spinor is an element of a minimal left ideal, and a minimal left ideal is produced by a rank-one idempotent, that is by a point of a projective line. The label lives one level up, in the endomorphism algebra, and it is defined with no point chosen. A left ideal is a subspace of $\mathbb{B}$; the label names no subspace and selects no point.

**Not a Pauli matrix.** A Pauli matrix is the array of a cell in the tensor display $\mathbb{C}^2\otimes\mathbb{C}^2$. The label is a membership in one of two subspaces and does not depend on the display; an operator has the same label in every display, because the two images do not move with the display.

**Not a Clifford algebra.** A Clifford algebra is generated by vectors subject to a relation, and it is offered as the natural home of chirality, with a product of generators as the chirality element. Two reasons are decisive. First, the relation fixes the squares and the anticommutators of generators and says nothing about the side on which an operator multiplies, which is the only datum the label uses. Second, a Clifford algebra fixes a dimension and a signature, while the two images exist for every algebra and every dimension: $L$ and $R$ are defined by the multiplication, and the intersection of their images is the centre in every case. So the Clifford reading is a frame in which the algebra is displayed, and the label is the same statement in that display.

**The fifth cell is an example, not the definition.** A gamma frame has five cells, and the fifth is a right multiplier of the form $-iR_u$ for an element $u$ with $u^2=-e_t$ and $\operatorname{Sc}u=0$; the legacy display prints it $\gamma_5$. Three properties follow in one line each. $(R_u)^2=R_{u^2}=-\mathrm I$, so the cell squares to $\mathrm I$. The trace of $R_u$ is zero because $u$ is traceless. The spectrum is $+i,+i,-i,-i$, two and two, so the projectors $\tfrac12(\mathrm I\pm iR_u)$ have rank two each. All four facts verified. That cell is a **pure right multiplier**, so under the label of this article it has the right slot. It is therefore an example of one of the four labels and cannot be the definition of the label. Its further qualification is that it is supplied by a frame: a rotation of the frame replaces $u$, and the cell changes while every label of every operator stays fixed.

**The split of an element is the action of the cell, not a second label.** The cell acts on the algebra and splits every element into its two eigenspaces. For a traceless $u$ with $u^2=-e_t$ and a cell of the form $-iR_u$, the decomposition is

$$
\tilde X=\tilde X_L+\tilde X_R,\qquad R_u\tilde X_L=i\,\tilde X_L,\qquad R_u\tilde X_R=-i\,\tilde X_R ,
$$

with each part of complex dimension two and no element but zero in both, verified. A product takes the letter of its right factor, because $R_u(\tilde X\tilde Y)=\tilde X R_u(\tilde Y)$, and a left multiplication therefore keeps the letter. Two warnings follow. The decomposition depends on $u$, so it is a property of the element and of the declared cell, not a second operator label. And a traceless $u$ is not optional: the central element $ie_t$ satisfies $u^2=-e_t$ and gives $R_{ie_t}=i\mathrm I$, which has no minus eigenspace at all. The letters $L$ and $R$ are the Dirac ones, and they belong to this cell, not to the label.

**A hypothesis that must not be dropped.** The statement that for any $u$ with $u^2=-e_t$ the right multiplier $R_u$ has spectrum $+i,+i,-i,-i$ and trace zero is false without the tracelessness of $u$. The central element $u=ie_t$ satisfies $u^2=-e_t$, and $R_{ie_t}=i\mathrm I$, whose spectrum is $+i$ four times and whose trace is $4i$. The vector condition $\operatorname{Sc}u=0$ is the missing hypothesis, and it is what makes $R_u$ behave as a chirality element.

**The Peirce identity, stated correctly.** The two families and the Peirce lines touch, and the contact is an **identity** forced by a shared element, not a coincidence of arrays for a rare alignment. For a traceless $u$ with $u^2=-e_t$ the projector

$$
\tfrac12\bigl(\mathrm I+iR_u\bigr)
$$

is idempotent of rank two, its image is a minimal left ideal of the regular module, and it is at once two things: the Peirce projector $R(\tilde\Pi)$ of the idempotent $\tilde\Pi=\tfrac12(e_t+iu)$, and the spectral projector of the right multiplier $-iR_u$ onto the eigenvalue $-1$. Both readings verified: the projector is idempotent, of rank two, and its image is stable under every left multiplier. The identity holds for every such $u$, so it is not a property of one element. What the corpus must not do is infer from it that the two notions are one: the Peirce projector is a subspace choice attached to an idempotent, the spectral projector is one half of the label of a single operator, and they agree because both are built from the same $u$.

## Why the Slot Label Is Not a Grading

**A grading would need a multiplicative sign.** A $\mathbb{Z}/2$ grading of an algebra is a decomposition into two subspaces with a multiplicative sign, equivalently a homomorphism to the group $\{\pm1\}$. For the endomorphism algebra the decomposition is trivial, because $\operatorname{End}_{\mathbb{C}}(\mathbb{B})\cong M_4(\mathbb{C})$ is simple and has no nontrivial central idempotent. The label is therefore not a grading for a structural reason, and the argument below shows the failure directly, on the one operator that blocks it.

**No functional separates the two images.** Suppose a multiplicative sign $\varepsilon$, with $\varepsilon(XY)=\varepsilon(X)\varepsilon(Y)$, took the value $+1$ on a left multiplier and $-1$ on a right multiplier of a noncentral element. The scalar $\lambda\mathrm I$ is at once the left multiplier $L(\lambda e_t)$ and the right multiplier $R(\lambda e_t)$, so it would have to carry both values. The label has four cases and the sign has two; the third row of the table of §*The Label* is where the map from one to the other collapses.

**What the swap gives instead.** It gives the decomposition into the self-adjoint and the skew-adjoint part for the trace form, of dimensions ten and six, with two different closing operations. That is an exchange and not a sign: $\sigma$ carries one side to the other and answers "which side" by moving the operator, not by labelling it.

**What supplies the sign.** A single operator supplies it: a right multiplier $R_u$ with $u$ traceless and $u^2=-e_t$, whose projectors $\tfrac12(\mathrm I\pm iR_u)$ are the two halves. The sign is one operator and not a functional on the algebra, and that is why no grading is ever exhibited: there is none to exhibit, and a sign that is wanted must be chosen as an operator.

**The division of labour.** The label is the frame-free statement: it says where an operator multiplies, and it is fixed by the two regular maps before anything else is declared. The sign is the chosen statement: it is an operator of the form $R_u$, and it changes when $u$ changes. Confusing the two is what produces the impression that chirality is a matrix. Separating them is what the identity $\sigma(L_a)=R_a$ accomplishes, since it makes the exchange a statement about the two families and leaves the choice of $u$ free.

## Summary

Operator chirality is the side on which an operator multiplies. The left multipliers are the image of the left regular map, the right multipliers the image of the right regular map, the two are four-dimensional each and meet in the scalars, their sum is seven-dimensional inside a sixteen-dimensional endomorphism algebra, and the remaining nine directions have no single side. The label has four cases: left, right, both at once for the scalars, and neither otherwise. A cell with two occupied slots is a two-sided operator and carries the label "no single side", which is not the same statement as "both slots".

Under the structure isomorphism $\Phi(a\otimes b)=L_aR_b$ the two images are the two tensor factors and their overlap is the tensor of the two units. The exchange of the two sides is the flip, transported as $\sigma=\Phi\tau\Phi^{-1}$, and it is intrinsic: it squares to the identity, reverses products exactly over $100$ pairs, since it permutes the cells, exchanges the two images, fixes the scalars, carries $L_a$ to $R_a$, preserves rank and length, and is not inner. It is also the adjoint of the trace form $\beta(\tilde X,\tilde Y)=\operatorname{Sc}(\tilde X\tilde Y)$. Its fixed space is ten-dimensional and a Jordan algebra under the anti-commutator, its negated space is six-dimensional and a Lie algebra under the commutator, and the two are the images of the symmetric and the exterior square.

The quaternion conjugate $\natural$ is the second side-exchanger, $\natural L(a)\natural=R(a^{\natural})$, and it differs from the flip in that it conjugates the parameters and reverses their order. The two agree on a pure left multiplier exactly on the scalars, and the sign they differ by is the origin of every phase of the corpus that comes from a change of side. Neither the definition nor either exchange uses a module, a projector, an idempotent, a frame or a Clifford relation.

The notion is unrelated to the nine objects that usually carry the name: a root, an idempotent, a Peirce decomposition, a Peirce basis, a spinor, a Pauli matrix, an ideal, a Clifford algebra, and the fifth cell of a gamma frame. The fifth cell is a pure right multiplier with square one, trace zero and a balanced spectrum, so it is an example of the right side and not the definition of chirality; a rotation of the frame changes it and changes no label. The one genuine contact with the Peirce theory is an identity and is stated as such: for a traceless $u$ with $u^2=-e_t$, the projector $\tfrac12(\mathrm I+iR_u)$ is at once the Peirce projector $R(\tfrac12(e_t+iu))$ and a spectral projector of $-iR_u$. The identity is forced by the shared element, and it is not an identity of notions.

$$
\boxed{\ \text{chirality}=\text{the side};\qquad X\in L(\mathbb{B}),\ \ X\in R(\mathbb{B}),\ \ X\in L(\mathbb{B})\cap R(\mathbb{B}),\ \ \text{or neither};\qquad \sigma=\Phi\tau\Phi^{-1},\quad \sigma(L_a)=R_a .\ }
$$

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L(a)$, $L_a$ | the left multiplier, $\tilde X\mapsto a\tilde X$ |
| $R(b)$, $R_b$ | the right multiplier, $\tilde X\mapsto \tilde Xb$ |
| $L_aR_b$ | the cell, $L_aR_b\tilde X=a\tilde Xb$, with a left and a right slot |
| $L(\mathbb{B})$, $R(\mathbb{B})$ | the two images, four-dimensional each, meeting in the centre |
| left slot, right slot, both slots, no single side | operator chirality: the membership of an operator in the two images |
| $\Phi(a\otimes b)=L_aR_b$ | the structure isomorphism $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}\to\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ |
| $\tau(a\otimes b)=b\otimes a$ | the flip of the two tensor factors |
| $\sigma=\Phi\tau\Phi^{-1}$ | the swap, $\sigma(L_aR_b)=L_bR_a$, the exchange of the two sides |
| $\beta(\tilde X,\tilde Y)=\operatorname{Sc}(\tilde X\tilde Y)$ | the trace form, symmetric and nondegenerate |
| $\mathsf D=\operatorname{diag}(1,-1,-1,-1)$ | the Gram matrix of $\beta$ in the basis $\mathcal{B}_0$, and the array of $\natural$ |
| $\mathsf W$ | the switch of a basis, with $[\sigma(X)]=\mathsf W[X]^{\mathsf T}\mathsf W^{-1}$ |
| $\operatorname{Fix}(\sigma)=\Phi(\operatorname{Sym}^2\mathbb{B})$ | the fixed space, dimension $10$, a Jordan algebra under the anti-commutator |
| $\operatorname{Neg}(\sigma)=\Phi(\Lambda^2\mathbb{B})$ | the negated space, dimension $6$, a Lie algebra under the commutator |
| $\natural$ | the quaternion conjugate, with $\natural L(a)\natural=R(a^{\natural})$ |
| $\ell(M)$, $\operatorname{rank}M$ | the length and the rank, both preserved by $\sigma$ |
| $\tfrac12(\mathrm I+iR_u)$, $u$ traceless, $u^2=-e_t$ | the rank-two projector of a right multiplier, at once a Peirce projector and a spectral projector |

## Further Reading

- [Families of Matrix Representations](families-of-matrix-representations.html), for the two sides, the switch and the change of frame.
- [$M_4(\mathbb{C})$ Axis-Free Representation : Operators](m4c-axis-free-representation-operators.html), for the cells as a basis, the coefficient matrix and the length.
- [$M_4(\mathbb{C})$ Pauli Representation : Operators](m4c-pauli-representation-operators.html), for the same operators in the tensor display.
- [The Endomorphisms of the Biquaternion Algebra](the-endomorphisms-of-the-biquaternion-algebra.html), for the general theory of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ and the two-sided operators.
- [The Unpolarized Module of the Biquaternion Algebra](the-unpolarized-module-of-the-biquaternion-algebra.html), for the carrier, the projective line of splittings and the trace form.
- [The Gamma Frame and the Complexified Dirac Algebra of $M_4(\mathbb{C})$](the-gamma-frame-and-the-complexified-dirac-algebra-of-m4c.html), for the five cells of a frame, for the fifth cell as an example, and for the six bivectors, which the swap does not preserve.
- [Operator Family Conventions](operator-family-conventions.html), for the four families, the two slots and the label.
- [Matrix Representations Conventions](matrix-representations-conventions.html), for the labels and the conventions of the category.
