# __Operator Chirality on the Biquaternion Algebra__

## Introduction

**The question.** Every operator of the biquaternion algebra is built from left and right multiplications, $L_aR_b$, and the two sides are symmetric in the definition and asymmetric in the results. This article asks what chirality means for such an operator, and answers with the operator alone.

**The answer in one line.** Operator chirality is the side on which an operator multiplies: the left slot, the right slot, or both. The chirality operator of a frame is its volume cell, $\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3=-iL_{e_t}R_{\vec e_z}$ in the axis-free frame, and it is a pure right multiplier. The swap $\sigma$ is the operator that exchanges the two sides, and the natural conjugation is the operator that exchanges them while reversing the units.

**What the article is not about.** The notion is defined on the endomorphism algebra of $\mathbb{B}$ and needs nothing else. Section §*What Operator Chirality Is Not* separates it, one object at a time, from a root, an idempotent, a Peirce decomposition, a Peirce basis, a spinor, a Pauli matrix, an ideal and a Clifford algebra, and records the single coincidence of arrays that makes the confusion possible.

**The order of the article.** Section §*The Two Slots* defines the sides, their dimensions and their overlap. Section §*The Chirality Operator of the Frame* reads the volume cell as a pure right multiplier and lists what it satisfies. Section §*The Subscript on an Element* gives the two values of that cell on the elements, $L$ and $R$. Section §*Conjugation Exchanges the Sides* proves that the natural conjugate of a left multiplier is a right multiplier, which is the second side-exchanging map and the origin of the phases. Sections §*The Swap of the Two Sides* to §*The Swap on the Frame* prove the exchange operator, its matrix, its two eigenspaces and its action on the frame. Section §*The Bivectors Are Not Stable* records what the swap moves. Section §*What Operator Chirality Is Not* is the separation. Section §*Why the Slot Label Is Not a Grading* fixes what the sides can and cannot supply.

**Boundaries.** The cells, the two families and the switch are *Families of Matrix Representations*; the frames are *$M_4(\mathbb{C})$ Axis-Free Representation* and *$M_4(\mathbb{C})$ Pauli Representation*, with their operator articles *$M_4(\mathbb{C})$ Axis-Free Representation : Operators* and *$M_4(\mathbb{C})$ Pauli Representation : Operators*; the carrier and its splittings are *The Unpolarized Module of the Biquaternion Algebra*; the general theory of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ is *The Endomorphisms of the Biquaternion Algebra*.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on $\mathcal{E}=(e_t,\vec e_x,\vec e_y,\vec e_z)$, with $\vec e_k^2=-e_t$, $\vec e_x\vec e_y=\vec e_z$ and cyclic, and $i$ central. The cells are $L_aR_b$ with $L_aR_b\tilde X=a\tilde Xb$, and the sixteen of them are a basis of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$. In the axis-free frame the gamma frame is
$$
\gamma_0=iL_{e_t}R_{\vec e_x},\qquad \gamma_1=iL_{\vec e_x}R_{\vec e_y},\qquad \gamma_2=iL_{\vec e_y}R_{\vec e_y},\qquad \gamma_3=iL_{\vec e_z}R_{\vec e_y},\qquad \gamma_5=-iL_{e_t}R_{\vec e_z},
$$
with $\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}$ and $g=\operatorname{diag}(-1,+1,+1,+1)$, so that $\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3$. The anticommutation is a computed property of these five cells, not an axiom: no Clifford algebra enters the definitions of this article. The Peirce sign of the third axis is $P=R_{i\vec e_z}=iR_{\vec e_z}$, and it is used only where it is named.

## The Two Slots

**The cell and its two slots.** A cell is $L_aR_b$, that is $\tilde X\mapsto a\tilde Xb$, and it has two slots: the left one, where $a$ multiplies, and the right one, where $b$ multiplies. The sixteen cells are linearly independent, so every operator has one coefficient array and the two slots are the two indices of that array.

**The two one-sided families.** An operator is a pure left multiplier when only the left slot is occupied, $c\,L_a$, and a pure right multiplier when only the right slot is occupied, $c\,R_b$. The two families are four-dimensional each and they overlap in one dimension, the centre:

| Space | Dimension | What it is |
|---|---|---|
| $L(\mathbb{B})$ | $4$ | the pure left multipliers $L_a$ |
| $R(\mathbb{B})$ | $4$ | the pure right multipliers $R_b$ |
| $L\cap R$ | $1$ | the scalars, $\mathbb{C}\,\mathrm I$, the centre |
| $L+R$ | $7$ | the one-sided operators, left, right and central |
| $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ | $16$ | all operators |

**Nine directions use both slots.** Since $L+R$ has dimension seven, an arbitrary operator of the sixteen-dimensional endomorphism algebra is a pure one-sided operator only inside that seven-dimensional subspace; the other nine directions carry both slots at once. Most operators have no single side, and the side is a property of the pure part.

**Chirality is the slot.** With the two families fixed, the definition is one line: an operator has the **left slot** when it is a pure left multiplier, the **right slot** when it is a pure right multiplier, and **both slots** otherwise. Operator chirality is that label. The definition uses the algebra and nothing else: no root, no idempotent, no subspace, no carrier.

**What the label is not.** The slot is a name, not a quantity. It is two-valued on the one-sided part and undefined outside it, it is not additive, and it carries no sign: $L_a+L_b$ and $L_a-L_b$ both have the left slot, and no linear functional separates a left multiplier from a right one by a sign. Section §*Why the Slot Label Is Not a Grading* proves the algebraic reason.

**The centre is both sides.** The scalars are simultaneously pure left and pure right multipliers, since $\lambda\tilde X=\lambda\tilde X=\tilde X\lambda$ for central $\lambda$. The overlap is not a defect of the definition: a scalar has no side, and the one-dimensional intersection is exactly the set of operators for which the question has no answer.

## The Chirality Operator of the Frame

**The volume cell.** The product of the four generators of the frame is a cell, because a product of left multipliers is a left multiplier and a product of right multipliers is a right multiplier:
$$
\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3=-iL_{e_t}R_{\vec e_z}.
$$
In the axis-free frame $L_{e_t}=\mathrm I$, so
$$
\gamma_5=-iR_{\vec e_z},
$$
a **pure right multiplier**. That is the whole content of the operator: the chirality operator of the frame multiplies on the right by the third direction, with the phase $-i$.

**What it satisfies.** Four properties, each read off the display:

| Property | Value |
|---|---|
| square | $\gamma_5^2=\mathrm I$ |
| trace | $\operatorname{tr}\gamma_5=0$ |
| spectrum | $+1$ and $-1$, two dimensions each |
| with the frame | $\{\gamma_\mu,\gamma_5\}=0$ for $\mu=0,1,2,3$ |

The anticommutation says that the four generators of the frame are odd under the right multiplication by $\vec e_z$. It is a consequence, computed on five cells, and it is not a definition: nothing in this article is built by asking which operators anticommute with what.

**Only the frame is used.** The four generators and their product. No root, no idempotent, no subspace of $\mathbb{B}$, no decomposition of anything, no carrier, and no Clifford algebra: the relation $\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}$ holds for these five cells as an identity of matrices, and the chirality operator is the fifth of them. The operator is available as soon as the frame is declared, and a frame is a basis: the weakest of the choices the algebra offers.

**The side is the point.** A reader who writes $\gamma_5$ as a diagonal matrix with two $+1$'s and two $-1$'s is reading the array of the operator in a basis where it is diagonal. The operator itself is $R_{\vec e_z}$ up to a phase, and its content is the side: it multiplies on the right. The gradient of the frame, $L(\tilde\nabla)$, multiplies on the left. That difference of sides is operator chirality, and it survives every change of basis.

## The Subscript on an Element

**Chirality is the subscript.** The volume cell acts on an element by
$$
\gamma_5\tilde X=-i\,\tilde X\vec e_z ,
$$
and an element is $L$ or $R$, which are the two values of the subscript. The letters are the Dirac ones: in the display where $\gamma_5=\operatorname{diag}(-I_2,I_2)$ the $L$ part is the upper block, as $\psi_L$ is in *The Dirac Equation in Biquaternionic Form*. Every element is a sum of one of each, and only the zero element is both.

**The rules.** A product takes the letter of its right factor, $(\tilde X\tilde Y)\vec e_z=\tilde X(\tilde Y\vec e_z)$, and left multiplication keeps the letter. A unit, a product and a general element therefore carry the subscript as well as a state does, because the subscript is a function of the element and of the declared frame and of nothing else.

**Three uses of the two letters.** The corpus writes $L$ and $R$ in three ways, told apart by position.

| Glyph | What it labels |
|---|---|
| $L_a$, $R_b$ | the left and the right multiplier, an operator |
| $M_4^{L}$, $M_4^{R}$ | the left and the right regular matrix, an array |
| $\tilde X_L$, $\tilde X_R$, $\psi_L$, $\psi_R$ | the chirality of an element |

Only the third applies to every element of the algebra, and it is the only one that is a subscript which is a word of one letter.

## Conjugation Exchanges the Sides

**The natural conjugate.** The map $\natural$ reverses the three vector units and fixes the scalar unit,
$$
e_t^{\natural}=e_t,\qquad \vec e_x^{\natural}=-\vec e_x,\qquad \vec e_y^{\natural}=-\vec e_y,\qquad \vec e_z^{\natural}=-\vec e_z,
$$
and is extended to $\mathbb{B}$ so that it fixes the coefficients. It is complex-linear, it is an involution, and it is an automorphism: the reversed units multiply among themselves with the same structure constants, $(-\vec e_x)(-\vec e_y)=\vec e_z=\vec e_x\vec e_y$. It is the involution used throughout the corpus under the name quaternion conjugate.

**The same reversal as a matrix.** On the coefficient space $\mathbb{C}^4$ the map is the diagonal matrix
$$
\mathsf C=\operatorname{diag}(1,-1,-1,-1),
$$
complex-linear, with $\mathsf C^2=\mathrm I$. In the axis-free frame $\mathsf C=D$, the switch of the frame.

**It carries the left side to the right side.** For every element $a\in\mathbb{B}$,
$$
\mathsf C\,L(a^{\natural})\,\mathsf C=R(a),
$$
and equivalently $\mathsf C\,L(a)\,\mathsf C=R(a^{\natural})$. On a unit this is $\mathsf C L(\vec e_k)\mathsf C=R(-\vec e_k)$, one sign for each of the three vector units; on a general element it follows by linearity. So the left multiplier of the conjugate is the right multiplier read through the switch, and the two sides are exchanged by a conjugation.

**The sign is the phase.** The identity carries no phase of its own, and the sign of the three vector units is where every phase in the corpus comes from. A left multiplier of the frame and a right multiplier of the frame have arrays that agree up to that sign, which is the origin of every statement of the form "the same array, up to a phase".

**It is not the swap.** The two maps are different and only one of them is the swap of this article:

| Map | On $L_a$ | On a cell $L_aR_b$ | What it moves |
|---|---|---|---|
| $\sigma$ | $R_a$ | $L_bR_a$ | the two indices |
| $\mathsf C$ | $R_{a^{\natural}}$ | $R_{a^{\natural}}L_{b^{\natural}}$ | the units, and the order |

So $\sigma$ exchanges the slots and leaves the units alone, while $\mathsf C$ exchanges the slots after conjugating the units and reversing their order. On a pure left multiplier the two agree exactly when $a=a^{\natural}$, that is when $a$ lies in the even part, the span of the scalar unit and the three bivectors; on the odd part, the span of the three vector units and the trivector, they differ by a sign.

**Where the conjugation enters, and where it does not.** The conjugation is not needed to define chirality: the slots are defined by the cells alone. It enters when one asks how a left multiplier and a right multiplier are related, and its answer is the table above. A reader who has only $\sigma$ can say which slot an operator occupies; a reader who also has $\mathsf C$ can say when two operators of opposite slots have the same array. That is the whole content of the map, and it is why it belongs in this article next to the swap rather than in the definition.

## The Swap of the Two Sides

**The definition.** The **swap** is the map
$$
\sigma\colon\operatorname{End}_{\mathbb{C}}(\mathbb{B})\longrightarrow\operatorname{End}_{\mathbb{C}}(\mathbb{B}),\qquad
\sigma(L_aR_b)=L_bR_a .
$$

**It is well defined.** The sixteen cells $L_{e_\mu}R_{e_\nu}$ are linearly independent, since they are the basis of *$M_4(\mathbb{C})$ Axis-Free Representation : Operators*, so an operator has one coefficient array in the cell basis, and the rule acts on the array by exchanging its two indices. There is no ambiguity and no dependence on the frame: the cell $L_aR_b$ is a coordinate-free operator, and exchanging $a$ and $b$ refers to no basis.

**It is an involution.** Exchanging the indices twice returns the cell, and the cells span the algebra, so $\sigma^2=\mathrm{id}$ on the whole of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$.

**It is an anti-automorphism.** For cells,
$$
\sigma\bigl((L_aR_b)(L_cR_d)\bigr)=\sigma(L_{ac}R_{db})=L_{db}R_{ac}=(L_dR_c)(L_bR_a)=\sigma(L_cR_d)\,\sigma(L_aR_b),
$$
which is the reversed product, and the identity extends by linearity. So $\sigma(XY)=\sigma(Y)\sigma(X)$ and $\sigma$ is not a homomorphism of the algebra: it is an isomorphism onto the opposite algebra, of order two.

**It preserves the cone.** The swap permutes the cells, so it carries a product of two one-sided operators to another product, and it preserves the length: $\ell(\sigma(M))=\ell(M)$. The rank-one cone of the products is mapped to itself, and the Segre variety of the coefficient matrices is mapped to itself with its two factors exchanged.

**What it is not.** The swap is not inner. No invertible $\mathsf S$ satisfies $\sigma(X)=\mathsf S X\mathsf S^{-1}$ for all $X$, because an inner map is a homomorphism and $\sigma$ reverses products. It is therefore a genuinely new operator, not a conjugation of the frame.


## The Matrix of the Swap

**The array.** In the cell basis, ordered lexicographically, $\sigma$ is a permutation matrix of size sixteen. Each cell $L_aR_b$ with $a\neq b$ is exchanged with $L_bR_a$, which gives six transpositions, and the four cells $L_aR_a$ are fixed. The diagonal cells are exactly the four products of a unit with itself,
$$
L_{e_t}R_{e_t}=\mathrm I,\qquad L_{\vec e_x}R_{\vec e_x},\qquad L_{\vec e_y}R_{\vec e_y},\qquad L_{\vec e_z}R_{\vec e_z},
$$
and each is fixed because exchanging the two copies of the same unit changes nothing.

**The invariants of the permutation.** With four fixed points and six transpositions, the trace is $4$ and the determinant is $(-1)^6=+1$. The swap is a symmetry of the cell basis of order two and determinant one: an even permutation of the sixteen cells.

**The orbits.** The permutation has one orbit of size one on each diagonal cell and one orbit of size two on each off-diagonal pair, so the array is the direct sum of four one-dimensional blocks $[1]$ and six blocks $\begin{pmatrix}0&1\\1&0\end{pmatrix}$. In the eigenbasis this is ten $+1$'s and six $-1$'s, which is the decomposition computed in §*The Two Eigenspaces*.

**Reading the array on the algebra.** The fixed cells and the symmetric sums $L_aR_b+L_bR_a$ span the fixed space, of dimension $4+6=10$; the antisymmetric differences $L_aR_b-L_bR_a$ span the negated space, of dimension six. The two dimensions are the dimensions of $\operatorname{Sym}^2V$ and $\Lambda^2V$ for $V$ of dimension four, and the identification is made in §*The Two Eigenspaces*.


## The Transpose Through the Switch

**The statement.** Let $\mathsf W$ be the switch of the frame, the matrix with $R(\tilde Q)=\mathsf W\,L(\tilde Q)^{\mathsf T}\mathsf W$, normalized so that $\mathsf W^2=\mathrm I$. Then for every $X\in\operatorname{End}_{\mathbb{C}}(\mathbb{B})$,
$$
\sigma(X)=\mathsf W\,X^{\mathsf T}\,\mathsf W .
$$
So the swap is the transpose read through the switch: **transpose, then conjugate by $\mathsf W$.**

**The proof on the cells.** The switch identity applied to the two units gives $R_b=\mathsf W L_b^{\mathsf T}\mathsf W$, hence $R_b^{\mathsf T}=\mathsf W L_b\mathsf W$ because $\mathsf W^2=\mathrm I$. Then
$$
\mathsf W(L_aR_b)^{\mathsf T}\mathsf W=\mathsf W R_b^{\mathsf T}L_a^{\mathsf T}\mathsf W=(\mathsf W R_b^{\mathsf T}\mathsf W)(\mathsf W L_a^{\mathsf T}\mathsf W)=L_bR_a=\sigma(L_aR_b),
$$
and linearity extends the identity to the algebra.

**Why the square is the identity.** Composing the transpose with the conjugation gives $\sigma^2(X)=\mathsf W\mathsf W^{\mathsf T}X\mathsf W^{\mathsf T}\mathsf W$, which is $X$ whenever $\mathsf W$ is symmetric with $\mathsf W^2=\mathrm I$. The switch has both properties in each frame — $D$ is a diagonal sign matrix and $\mathsf P$ is a pure swap — and its symmetry is forced rather than chosen: the switches differ from the Gram matrix of $\beta(\tilde X,\tilde Y)=\operatorname{Sc}(\tilde X\tilde Y)$ by a left multiplication, and $D\,L(\tilde P)$ is symmetric exactly when $\tilde P$ is central, so the symmetric switch is unique up to a scale, which $W^2=\mathrm I$ fixes.

**The dependence on the frame.** The transpose depends on the frame and so does $\mathsf W$, while $\sigma$ does not: the two dependences cancel. This is the reason the swap can be defined by the cells and computed by a transpose, and the reason a statement proved with one display holds in all of them.

**The two frames.** In the axis-free frame $\mathsf W=D$, the diagonal sign matrix, and the transpose identity is the one of the axis-free article. In the Pauli frame $\mathsf W=\mathsf P$, the pure swap of the two tensor factors, and the same identity holds with $\mathsf P$ in place of $D$. The transpose through a sign matrix says something different from the transpose through a swap of factors, and the fact that both express the same $\sigma$ is the clearest sign that the swap is the frame-independent object.


## The Two Eigenspaces

**The fixed space.** An operator is fixed by the swap exactly when $\mathsf W X=X^{\mathsf T}\mathsf W$, that is exactly when $X$ is self-adjoint for the symmetric form with matrix $\mathsf W$. The fixed space has dimension ten, is spanned by the four diagonal cells and the six symmetric sums, and is $\operatorname{Sym}^2V$ once $V$ is identified with its dual through the form whose matrix is the switch; in the axis-free frame that form is the trace form $\beta$.

**It is a Jordan algebra, not an algebra.** On the fixed space the product of two elements is not fixed: for $\sigma(X)=X$ and $\sigma(Y)=Y$ one has $\sigma(XY)=YX$, which equals $XY$ only when the two commute. The fixed space is closed instead under the anti-commutator,
$$
\sigma\bigl(\tfrac12(XY+YX)\bigr)=\tfrac12\bigl(YX+XY\bigr)=\tfrac12(XY+YX),
$$
so it is a Jordan algebra of dimension ten under $X\circ Y=\tfrac12(XY+YX)$. It is not a subalgebra of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ under the ordinary product.

**The negated space.** An operator is negated by the swap exactly when $\mathsf W X=-X^{\mathsf T}\mathsf W$, that is exactly when $X$ is skew-adjoint for the same form. The space has dimension six, is spanned by the six differences $L_aR_b-L_bR_a$, and those differences are the commutators $[L_a,R_b]$, since left and right multiplications commute.

**It is a Lie algebra.** For $\sigma(X)=-X$ and $\sigma(Y)=-Y$,
$$
\sigma(XY-YX)=\sigma(Y)\sigma(X)-\sigma(X)\sigma(Y)=YX-XY=-(XY-YX),
$$
so the negated space is closed under the commutator. It is a Lie algebra of dimension six, and over $\mathbb{C}$ it is $\mathfrak{so}(4,\mathbb{C})$ for the switch form. The anti-commutator of two skew elements is fixed, by the same computation, so the two spaces interact in the way a symmetric form prescribes.

| Space | Dimension | Condition | Operation that closes |
|---|---|---|---|
| Fixed, $+1$ | $10$ | $\mathsf W X=X^{\mathsf T}\mathsf W$ | anti-commutator, a Jordan algebra |
| Negated, $-1$ | $6$ | $\mathsf W X=-X^{\mathsf T}\mathsf W$ | commutator, a Lie algebra |
| The whole | $16$ | none | the product, an associative algebra |

**What the pair is.** The decomposition $\operatorname{End}_{\mathbb{C}}V=\operatorname{Sym}^2V\oplus\Lambda^2V$ is the standard one for a nondegenerate symmetric form, and the swap is its reflection. The content specific to this algebra is that in the axis-free frame the form is the trace form on the cells and that the reflection is the exchange of the two sides, so the decomposition of the endomorphism algebra is read off the two-sided structure rather than imposed.


## The Swap on the Frame

**The three multipliers.** The left multipliers of the frame are the three cells $L_{\vec e_k}$. The swap carries each to the right multiplier of the same unit, and the right multipliers are identified with the gamma frame by the dictionary of the frame articles:

| Cell | Swap | In the gamma frame |
|---|---|---|
| $L_{\vec e_x}$ | $R_{\vec e_x}$ | $-i\gamma_0$ |
| $L_{\vec e_y}$ | $R_{\vec e_y}$ | $i\gamma_1\gamma_2\gamma_3$ |
| $L_{\vec e_z}$ | $R_{\vec e_z}$ | $i\gamma_5$ |

**The reading.** The three left multipliers are the spacelike bivectors themselves, $L_{\vec e_x}=\gamma_2\gamma_3$, $L_{\vec e_y}=\gamma_3\gamma_1$, $L_{\vec e_z}=\gamma_1\gamma_2$, so the rotation generators $\vec e_k/2$ are half of them. The swap sends them to a vector, a trivector and the chirality operator. So the exchange of the two sides does not preserve the kind of object: it permutes the degrees of a Clifford algebra, taking a bivector to a vector, to a trivector and to a four-form.

**The inverse direction.** Applying the table backwards, $\gamma_0\mapsto iL_{\vec e_x}$, and $i\gamma_5\mapsto L_{\vec e_z}$. The four-form and the chirality operator are the same cell, since $\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3=-iL_{e_t}R_{\vec e_z}$ and $L_{e_t}=\mathrm I$.

**The single identity that matters.** Combining the last row with the definitions,
$$
\sigma(L_{\vec e_z})=R_{\vec e_z}=i\gamma_5=-iP .
$$
The swap of the rotation generator about the third axis is $i$ times the chirality operator, and $-i$ times the Peirce sign. Both signs are correct, and their coincidence is examined in §*What Operator Chirality Is Not*.


## The Bivectors Are Not Stable

**The six bivectors are cells.** Each $\gamma_\mu\gamma_\nu$ is a product of two cells, hence a cell with coefficient $\pm1$, and the six of them are

| Bivector | As a cell | Its swap |
|---|---|---|
| $\gamma_0\gamma_1$ | $L_{\vec e_x}R_{\vec e_z}$ | $L_{\vec e_z}R_{\vec e_x}$ |
| $\gamma_0\gamma_2$ | $L_{\vec e_y}R_{\vec e_z}$ | $L_{\vec e_z}R_{\vec e_y}$ |
| $\gamma_0\gamma_3$ | $L_{\vec e_z}R_{\vec e_z}$ | $L_{\vec e_z}R_{\vec e_z}$ |
| $\gamma_1\gamma_2$ | $L_{\vec e_z}R_{e_t}$ | $L_{e_t}R_{\vec e_z}$ |
| $\gamma_1\gamma_3$ | $-L_{\vec e_y}R_{e_t}$ | $-L_{e_t}R_{\vec e_y}$ |
| $\gamma_2\gamma_3$ | $L_{\vec e_x}R_{e_t}$ | $L_{e_t}R_{\vec e_x}$ |

**Exactly one is fixed.** Of the six, only $\gamma_0\gamma_3=L_{\vec e_z}R_{\vec e_z}$ is carried to itself, because it is the one whose two units agree. The other five are moved, each to a cell that is not in the bivector span.

**The two six-dimensional spaces.** Let $\mathcal{B}$ be the span of the six bivectors, and $\sigma\mathcal{B}$ its image. Both have dimension six, their intersection has dimension one — the line of $\gamma_0\gamma_3$ — and their sum has dimension eleven:
$$
\dim\mathcal{B}=6,\qquad \dim\sigma\mathcal{B}=6,\qquad \dim(\mathcal{B}\cap\sigma\mathcal{B})=1,\qquad \dim(\mathcal{B}+\sigma\mathcal{B})=11 .
$$
So $\mathcal{B}$ is not stable under the swap, and the Lorentz Lie algebra of the frame is not an invariant of the unpolarized algebra: it is a choice, and the swap moves it to a different six-dimensional space.

**The consequence for the symmetry articles.** This is the algebraic statement behind the observation of the symmetry articles that the left multipliers are bivectors and the right ones are a vector, a trivector and a four-form. The pair of multipliers is not a pair of bivectors, and no reading of the two $\mathrm{SU}(2)$'s as the self-dual and anti-self-dual halves can repair it: the swap sends a rotation generator to the chirality operator, and the self-dual split would require it to stay inside the bivectors.

**Why this is the sharpest test.** The natural guess is that the exchange of the two sides preserves the kind of object, since the two sides are constructed by the same rule. It does not, and the failure is measured: five of six. A reader who assumes the symmetry of the construction implies a symmetry of the objects will compute the wrong algebra, and the table above is the correction.


## What Operator Chirality Is Not

**The list.** The notion is one line long — the side — and it is routinely attached to eight other objects. The table states what each of them is and why it is not needed.

| Object | What it is | Why operator chirality does not need it |
|---|---|---|
| a root | an element $\tilde\Xi$ with $\tilde\Xi^2=e_t$ | $\gamma_5$ is a cell of the frame, and a root is an element chosen later |
| an idempotent | an element $\tilde\Pi$ with $\tilde\Pi^2=\tilde\Pi$ | the operator satisfies $\gamma_5^2=\mathrm I$, which is not $\gamma_5^2=\gamma_5$ |
| a Peirce decomposition | the four lines $\mathbb{B}_{st}$ of a pair of idempotents | the sides are two, the Peirce lines are four, and none of the four is a side |
| a Peirce basis | the units of one Peirce decomposition | a basis is a coordinate choice on $\mathbb{B}$, and the side is read without one |
| a spinor | an element of a minimal left ideal | an ideal needs a rank-one idempotent; the side is a property of an operator on $\mathbb{B}$ |
| a Pauli matrix | the array of a frame in the tensor display | the same operator is $-iR_{\vec e_z}$ in the axis-free frame |
| an ideal | a subspace of $\mathbb{B}$, here a point of a projective line | a subspace is chosen; $\gamma_5$ chooses no point |
| a Clifford algebra | the algebra generated by vectors with $\{e_i,e_j\}=2g_{ij}$, here $\mathrm{Cl}_{1,3}(\mathbb{C})\cong M_4(\mathbb{C})$ | the anticommutation of the frame is a property of five cells, and no Clifford relation is used to define the side |

**Not a root.** A root is an element of the algebra and it enters when a Peirce decomposition is wanted. The chirality operator is a cell of the frame and the frame is declared before any root is mentioned. Changing the root changes nothing in $\gamma_5$; there is no root in its definition to change.

**Not an idempotent.** The operator satisfies $\gamma_5^2=\mathrm I$ and an idempotent satisfies $\tilde\Pi^2=\tilde\Pi$. The two conditions are different, and the difference is not cosmetic: from $\gamma_5$ one can build the projectors $\tfrac12(\mathrm I\pm\gamma_5)$, which are idempotents, but they are derived objects. The pair of the previous section is written without them.

**Not a Peirce decomposition, not a Peirce basis.** A Peirce decomposition needs two idempotents and returns four lines, of dimensions one, one, one and one. The two sides are two, they are not subspaces of $\mathbb{B}$ but parts of an operator, and no Peirce line is a side: the Peirce lines are corners $\mathbb{B}_{st}$, and the sides are the slots of a multiplication.

**Not a spinor.** A spinor is an element of a minimal left ideal, and a minimal left ideal is produced by a rank-one idempotent, that is by a point of a projective line. The side lives one level up, in the endomorphism algebra, and it is defined without any point being chosen.

**Not a Pauli matrix.** The Pauli display is a frame, the tensor factorisation $\mathbb{C}^2\otimes\mathbb{C}^2$, and a Pauli matrix is the array of a cell in that display. The chirality operator exists in the axis-free frame, where it is the single cell $-iR_{\vec e_z}$, and in the Pauli frame where it is the same array written with two factors. The display changes; the side does not.

**Not an ideal.** A left ideal of $\mathbb{B}$ is a subspace, and the minimal ones are indexed by the points of a projective line, with no point distinguished. An operator that multiplied on one side and selected a point would be an ideal in disguise. The chirality operator selects nothing: it multiplies, and its two eigenspaces are two-dimensional subspaces of the coefficient space $\mathbb{C}^4$, present in every frame.

**Not a Clifford algebra.** A Clifford algebra is generated by vectors subject to $\{e_i,e_j\}=2g_{ij}$, and it is offered as the natural home of chirality, with $\gamma_5$ as the product of the generators. In this algebra the relation is a theorem about five cells of the frame, verified by multiplying them, and it is not used in any definition. The reason is structural: the relation fixes the squares and the anticommutators of four cells and says nothing about the side on which an operator multiplies, which is the only datum operator chirality needs. A Clifford algebra also fixes a dimension and a signature; the sides exist in every dimension and are read from the cells alone. So the Clifford reading is a frame in which the algebra is displayed, and the chirality of a frame is the same statement in that display.

**Why no anticommutation gives it.** A reader might expect the chirality operator to be characterised by anticommuting with the frame. It cannot be, and the reason is one line: $L(e_t)=\mathrm I$ is one of the operators that a candidate would have to anticommute with, and an operator that anticommutes with the identity is zero. So the sign in this algebra is never produced by an anticommutator; it is produced by the side, which is what the slots supply and what no Clifford relation can supply.

**The one coincidence, and why it matters.** There is a single place where the two families of notions touch, and it must be stated or the whole section is misleading. For the root aligned with the volume direction, $\tilde\Xi=i\vec e_z$, the Peirce sign is
$$
P=R_{i\vec e_z}=iR_{\vec e_z}=-\gamma_5,
$$
and the projector on the ideal of $\tilde\Pi_+=\tfrac12(e_t+i\vec e_z)$ is
$$
R(\tilde\Pi_+)=\tfrac12(\mathrm I+P)=\tfrac12(\mathrm I-\gamma_5).
$$
So for that one root the Peirce projector and the chiral projector are the same operator. For any other root they are not: with $\tilde\Xi=i\vec e_x$ the Peirce projector is $\tfrac12(\mathrm I+iR_{\vec e_x})$, which is neither $\tfrac12(\mathrm I-\gamma_5)$ nor $\tfrac12(\mathrm I+\gamma_5)$.

**The moral.** The coincidence is a coincidence of arrays for one root out of the projective line, and it is the origin of every statement in the corpus that the Peirce sign and the chirality operator agree up to a phase. The two notions share a value there and share no definition: one is a subspace choice, the other is a side. Writing the side first, as this article does, keeps the shared value visible as a coincidence instead of letting it stand as an identity.

## Why the Slot Label Is Not a Grading

**A grading would need a multiplicative sign.** A $\mathbb{Z}/2$ grading of an algebra is a homomorphism to $\{\pm1\}$, that is a linear functional with $\varepsilon(XY)=\varepsilon(X)\varepsilon(Y)$. No such functional separates the left multipliers from the right ones: the two families overlap in the scalars, and a scalar is neither $+1$ nor $-1$ by virtue of its side.

**What the swap gives instead.** It gives the decomposition into the self-adjoint and the skew-adjoint part for the switch form, of dimensions ten and six, and that is a decomposition of the underlying space with two different closing operations. It is an exchange, not a sign: $\sigma(L_a)=R_a$, so the swap carries one side to the other and answers the question "which side" by moving it, not by labelling it.

**What supplies the sign.** An operator with $\gamma_5^2=\mathrm I$ and $\{\gamma_\mu,\gamma_5\}=0$, which is the volume cell. It is a single operator of the algebra, its two eigenspaces have equal dimension, and its array is diagonal in a basis that diagonalises it. So the sign is one operator, not a functional on the algebra, and that is why no grading is ever exhibited: there is none to exhibit.

**The division of labour.** The slot is the frame-independent statement: it says where an operator multiplies, and every cell has its two slots before a frame is declared. The sign is the frame-dependent statement: it is the volume cell of the frame, $\gamma_5=-iR_{\vec e_z}$, and its array depends on the frame. Confusing the two is what produces the impression that chirality is a diagonal matrix. Separating them is what the identity $\gamma_5=-i\sigma(L_{\vec e_z})$ accomplishes, and it is the reason the swap belongs in an article about chirality.

## Summary

Operator chirality is the side on which an operator multiplies: the left slot, the right slot, or both. The pure left multipliers form a four-dimensional family, the pure right multipliers another, the two overlap in the scalars, and their sum is seven-dimensional inside a sixteen-dimensional endomorphism algebra; the remaining nine directions carry both slots and have no side.

The chirality operator of a frame is its volume cell, $\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3=-iL_{e_t}R_{\vec e_z}$, which in the axis-free frame is the pure right multiplier $-iR_{\vec e_z}$. It squares to the identity, has trace zero, splits the coefficient space two and two, and anticommutes with the four generators. On the elements it is the subscript: $\tilde X$ is $L$ or $R$, two values and no more, and a product takes the letter of its right factor. A pure left multiplier is the operator $L(a)$ for an element $a$; its natural conjugate is the right multiplier $\mathsf C\,L(a^{\natural})\,\mathsf C=R(a)$, so the conjugation is the second map that exchanges the sides, and the two maps differ by the sign of the three vector units. Neither the definition nor either exchange uses a module, a projector, an idempotent or a Clifford relation.

The swap $\sigma(L_aR_b)=L_bR_a$ is well defined on the cells, involutive, anti-multiplicative and independent of the frame; it is the transpose read through the switch, it has four fixed cells, trace four and determinant one, and its eigenspaces are the self-adjoint and skew-adjoint operators of dimensions ten and six. It carries the rotation generator $L_{\vec e_z}$ to $i\gamma_5$, which is the identity that ties the swap to chirality.

The notion is unrelated to the eight objects that usually carry the name: a root, an idempotent, a Peirce decomposition, a Peirce basis, a spinor, a Pauli matrix, an ideal and a Clifford algebra. It touches them once, at the root aligned with the volume direction, where $P=-\gamma_5$ and the Peirce projector equals $\tfrac12(\mathrm I-\gamma_5)$; that single coincidence of arrays is the source of the confusion, and it is not an identity of notions.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_aR_b$ | the cell, $L_aR_b\tilde X=a\tilde Xb$, with a left and a right slot |
| $L(\mathbb{B})$, $R(\mathbb{B})$ | the pure left and pure right multipliers, four-dimensional each, overlapping in the centre |
| left slot, right slot, both slots | operator chirality: on which side an operator multiplies |
| $\gamma_5$ | the volume cell of the frame, $-iL_{e_t}R_{\vec e_z}=-iR_{\vec e_z}$ in the axis-free frame, a pure right multiplier |
| $\gamma_5\tilde X=-i\tilde X\vec e_z$ | the action of the volume cell on an element, of spectrum $+1,+1,-1,-1$ |
| $\tilde X_L$, $\tilde X_R$ | the parts of an element, $\gamma_5\tilde X_L=-\tilde X_L$ and $\gamma_5\tilde X_R=+\tilde X_R$, of dimension two each; the same subscript as $\psi_L$, $\psi_R$ in the Dirac literature, and available on every element of $\mathbb B$ |
| $\mathsf C$ | the natural conjugation as a matrix, $\operatorname{diag}(1,-1,-1,-1)$, with $\mathsf C L(a^{\natural})\mathsf C=R(a)$ |
| $\sigma$ | the swap, $\sigma(L_aR_b)=L_bR_a$, the exchange of the two sides |
| $\mathsf W$ | the switch of a frame, $R(\tilde Q)=\mathsf W L(\tilde Q)^{\mathsf T}\mathsf W$ |
| $D=\operatorname{diag}(1,-1,-1,-1)$ | the switch of the axis-free frame, and the matrix of $\mathsf C$ |
| $\mathsf P$ | the switch of the Pauli frame, the pure swap of the two factors |
| $\beta(\tilde X,\tilde Y)$ | the trace form $\operatorname{Sc}(\tilde X\tilde Y)$, with Gram matrix $D$ in the axis-free frame |
| $\operatorname{Sym}^2V$ | the fixed space of $\sigma$, dimension $10$, a Jordan algebra under $X\circ Y$ |
| $\Lambda^2V$ | the negated space of $\sigma$, dimension $6$, a Lie algebra under $[X,Y]$ |
| $\ell(M)$ | the length $\operatorname{rank}c(M)$, preserved by $\sigma$ |
| $\mathcal{B}$ | the span of the six Lorentz bivectors, dimension $6$, not $\sigma$-stable |
| $P=R_{i\vec e_z}=iR_{\vec e_z}$ | the Peirce sign of the third axis; $P=-\gamma_5$, and it is not used in the definition of chirality |

## Further Reading

- [The Unpolarized Module of the Biquaternion Algebra](the-unpolarized-module-of-the-biquaternion-algebra.html), for the carrier, the projective line of splittings and the trace form.
- [$M_4(\mathbb{C})$ Axis-Free Representation : Operators](m4c-axis-free-representation-operators.html), for the cells as an orthogonal basis and the coefficient matrix.
- [$M_4(\mathbb{C})$ Pauli Representation : Operators](m4c-pauli-representation-operators.html), for the same operators in the tensor display.
- [Families of Matrix Representations](families-of-matrix-representations.html), for the two sides, the switch and the change of frame.
- [The Endomorphisms of the Biquaternion Algebra](the-endomorphisms-of-the-biquaternion-algebra.html), for the general theory of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ and the two-sided operators.
- [Matrix Representations Conventions](matrix-representations-conventions.html), for the labels and the conventions of the category.

