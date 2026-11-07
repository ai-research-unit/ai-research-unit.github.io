# __Operator Chirality on the Biquaternion Algebra__

## Introduction

Every operator on the biquaternion algebra multiplies on a side, and the side is given by the multiplication itself: $L(a)$ multiplies an element on the left, $R(b)$ multiplies it on the right. Operator chirality is the name of that side. The definition is one line long, it names no frame, and everything else in this article follows from it.

The obvious route to the notion goes through a frame, and it is worth saying why that route misleads. Choose a direction, take the four frame cells that point along it, multiply them, and a cell comes out whose eigenspaces are two halves of the algebra. The construction is correct, and the physics uses it. But its order is wrong: it produces an operator and then reads a chirality off it. The error shows in the product. The cell so obtained is a pure right multiplier, so by any definition of chirality worth the name it has a chirality of its own; and an object that has a chirality cannot be what chirality means. Here the sides come first, and the frame cell becomes one example of one of them.

The article is purely algebraic. The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, central simple over $\mathbb{C}$, of complex dimension four, with unit $e_t$ and reduced trace $\operatorname{Sc}$; the identity operator is $\mathrm I$. No basis of $\mathbb{B}$ is declared anywhere except in one place, where an array is the convenience being discussed, and that place says so. The cells and the two families belong to *Families of Matrix Representations*. The carriers and their splittings belong to *The Unpolarized Module of the Biquaternion Algebra*. The ambient operator space belongs to *The Endomorphisms of the Biquaternion Algebra*, and the arrays to the two operator articles of the $M_4(\mathbb{C})$ representation. The frame, with the cell this article no longer defines itself by, belongs to *The Gamma Frame and the Complexified Dirac Algebra of $M_4(\mathbb{C})$*.

## The Two Sides

The multiplication gives two maps into the endomorphism algebra, one for each end of a product,

$$
L\colon\mathbb{B}\to\operatorname{End}_{\mathbb{C}}(\mathbb{B}),\quad L(a)(\tilde X)=a\tilde X,
\qquad
R\colon\mathbb{B}\to\operatorname{End}_{\mathbb{C}}(\mathbb{B}),\quad R(b)(\tilde X)=\tilde Xb .
$$

Both are complex-linear, both are unital, and both are injective, because a multiplier that vanishes on the unit vanishes everywhere: $L(a)(e_t)=a$. The two families are written $L(\mathbb{B})$ and $R(\mathbb{B})$.

They commute. That is the first structural fact and the reason the whole subject exists:

$$
L(a)R(b)(\tilde X)=a\tilde Xb=R(b)L(a)(\tilde X).
$$

The left factor and the right factor act on the two ends of the argument, so they cannot meet. Products of cells multiply accordingly,

$$
\bigl(L_aR_b\bigr)\bigl(L_cR_d\bigr)=L_{ac}R_{db},
$$

with the reversal on the right, because the two right parameters meet in the middle and the one that was farther from the argument is now applied first.

The two images are four-dimensional, since $L$ and $R$ are injective on a four-dimensional algebra. Their intersection is the line of scalars and nothing else. If $L(a)=R(b)$ then $a\tilde X=\tilde Xb$ for every $\tilde X$; at $\tilde X=e_t$ this gives $a=b$, and then $a$ commutes with everything, so $a$ is central. A central element gives the equality back, so the intersection is exactly $\mathbb{C}\,\mathrm I$. Their sum is therefore seven-dimensional, inside the sixteen-dimensional endomorphism algebra:

$$
\dim L(\mathbb{B})=\dim R(\mathbb{B})=4,\qquad \dim\bigl(L(\mathbb{B})\cap R(\mathbb{B})\bigr)=1,\qquad \dim\bigl(L(\mathbb{B})+R(\mathbb{B})\bigr)=7 .
$$

These numbers are worth reading twice. The second says that the two sides overlap in a line, and the fourth says that nine of the sixteen dimensions lie outside the sum: those are the operators that multiply on neither side alone.

The two families are not two constructions of one object. They are the two factors of a tensor square. The multiplication defines

$$
\Phi\colon\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}\to\operatorname{End}_{\mathbb{C}}(\mathbb{B}),\qquad \Phi(a\otimes b)=L_aR_b ,
$$

and $\Phi$ is an isomorphism, because for any basis $e_1,\dots,e_4$ the sixteen cells $L_{e_\mu}R_{e_\nu}$ are independent: an operator on a four-dimensional space is an arbitrary array of sixteen numbers, and the cells supply the sixteen coordinate directions. Under $\Phi$ the two sides become the two factors, and their overlap becomes the tensor of the two units:

$$
L(\mathbb{B})=\Phi(\mathbb{B}\otimes e_t),\qquad
R(\mathbb{B})=\Phi(e_t\otimes\mathbb{B}),\qquad
L(\mathbb{B})\cap R(\mathbb{B})=\Phi(e_t\otimes e_t).
$$

This is the technical core of the article. A cell $L_aR_b$ is a coordinate of $\Phi$ and not a primitive object, and a statement written in cells is a statement about $\Phi$ which becomes intrinsic once it is written in the two images.

**Definition.** An operator has the **left slot** when it lies in $L(\mathbb{B})$, the **right slot** when it lies in $R(\mathbb{B})$, **both slots** when it lies in the intersection, and **no single side** otherwise:

$$
X\in L(\mathbb{B}),\qquad X\in R(\mathbb{B}),\qquad X\in L(\mathbb{B})\cap R(\mathbb{B})=\mathbb{C}\,\mathrm I,\qquad X\notin L(\mathbb{B})\cup R(\mathbb{B}).
$$

Operator chirality is that label. It is a property of an operator, it takes four values, and it is fixed by the multiplication before anything else is chosen.

The third case is the one that needs care. A cell such as $L_aR_b$ with neither parameter central occupies both slots in the plain sense of the words, and it has not both slots in the sense of the definition: it has no single side. The word *both* names two different things in the two sentences, a label and a family, and the corpus keeps them apart by grammar. The cell $L_aR_b$ is a member of the family $LR$; its label is *no single side*. The third case is reserved for the operators that genuinely multiply on both ends at once, and those are the scalars.

The asymmetry appears the moment one multiplies. The product of two left multipliers is a left multiplier, and the product of two right multipliers is a right multiplier, so each side is a four-dimensional subalgebra and the two subalgebras meet in the scalars. A product of one of each is a cell, and a general cell is on neither side. The label is therefore not respected by the product, except on the scalars, and this is the first hint that it is not a grading; the last section makes that a theorem.

The label is also a name and not a quantity. It is not additive: $L_a+L_c$ has the left slot while $L_a+R_b$ has none, so the set of operators with no single side is the complement of a union and not a subspace. It carries no sign: $cL_a$ and $-cL_a$ are labelled alike. No linear functional on the endomorphism algebra assigns the four labels, for the reason given at the end.

## The Swap

The two sides are exchanged by one canonical involution, and that involution is what does the work the frame's volume cell was once asked to do. It is defined on the tensor square and transported by $\Phi$. Let $\tau$ be the flip of the two factors, $\tau(a\otimes b)=b\otimes a$, and put

$$
\sigma=\Phi\circ\tau\circ\Phi^{-1},\qquad\text{so that}\qquad \sigma(L_aR_b)=L_bR_a .
$$

The rule exchanges the two entries of an elementary tensor; it refers to no basis. It is well defined because the cells are a basis of the endomorphism algebra, so every operator has one coefficient array and the rule permutes its two indices.

**Theorem.** The map $\sigma$ is an involution and an anti-automorphism, and it exchanges the two images:

$$
\sigma^2=\mathrm{id},\qquad \sigma(XY)=\sigma(Y)\sigma(X),\qquad \sigma\bigl(L(\mathbb{B})\bigr)=R(\mathbb{B}),\qquad \sigma\bigl(R(\mathbb{B})\bigr)=L(\mathbb{B}).
$$

*Proof.* The flip is its own inverse, so $\sigma$ is. For the reversal, take two cells:

$$
\sigma\bigl((L_aR_b)(L_cR_d)\bigr)=\sigma(L_{ac}R_{db})=L_{db}R_{ac}=(L_dR_c)(L_bR_a)=\sigma(L_cR_d)\,\sigma(L_aR_b),
$$

and linearity extends it. The exchange of the images is the case of one factor, $\sigma(L_a)=R_a$ and $\sigma(R_b)=L_b$, and linearity extends that too. On the intersection the two statements agree, so the scalars are fixed.

The one case to remember is the case of a single factor:

$$
\sigma(L_a)=R_a\qquad\text{for every }a\in\mathbb{B}.
$$

The left multiplier of an element and the right multiplier of the same element are the same operator written on the two ends, and the swap is what changes the writing. This is why the two families have arrays that agree up to a sign, and it is why every statement about a left multiplier has a twin statement about a right one.

Two further properties are used later. The swap permutes the cells of any basis, so it preserves the number of one-sided factors in a decomposition, which is the length $\ell$ of the operator articles. It also preserves the rank, since it transposes the coefficient matrix:

$$
\ell\bigl(\sigma(M)\bigr)=\ell(M),\qquad \operatorname{rank}\sigma(M)=\operatorname{rank}M .
$$

And it is not inner. An inner automorphism $X\mapsto \mathsf SX\mathsf S^{-1}$ preserves products, while $\sigma$ reverses them, so no matrix conjugates the swap. The exchange of the sides cannot be produced by choosing a frame, changing a display or picking a basis. It is an operation on operators.

## The Trace Form

An exchange is easy to define and hard to compute. The trace form supplies both a computation and a second description of $\sigma$ that is manifestly independent of every choice:

$$
\beta(\tilde X,\tilde Y)=\operatorname{Sc}(\tilde X\tilde Y).
$$

The form is complex-bilinear, symmetric and nondegenerate, since the reduced trace is nondegenerate on a central simple algebra, and it is cyclic in the sense that $\operatorname{Sc}(\tilde X\tilde Y\tilde Z)=\operatorname{Sc}(\tilde Y\tilde Z\tilde X)$. Nothing is chosen here: the form is built from the multiplication and the trace.

**Theorem.** For every operator $X$ and all elements $\tilde Y,\tilde Z$,

$$
\beta\bigl(X\tilde Y,\tilde Z\bigr)=\beta\bigl(\tilde Y,\sigma(X)\tilde Z\bigr).
$$

The swap is the adjoint of $X$ with respect to $\beta$.

*Proof.* For a cell, the left side is $\operatorname{Sc}(a\tilde Yb\tilde Z)$ and the right side is $\operatorname{Sc}(\tilde Yb\tilde Za)$, and cyclicity makes them equal. Linearity extends the identity to all operators.

The identity is worth pausing on. Adjointness is a basis-free notion, so the theorem describes $\sigma$ using the multiplication and the trace and nothing else, and it says what the exchange of sides is in the language a bilinear form provides. The frame-based reading of the same fact is an array, and an array has to be written in a basis. Here it is. In a basis $\mathcal{B}_0$ where $\beta$ has Gram matrix $\mathsf D=\operatorname{diag}(1,-1,-1,-1)$, the adjoint of a matrix is $\mathsf D[X]^{\mathsf T}\mathsf D$. So

$$
[\sigma(X)]_{\mathcal{B}_0}=\mathsf D\,[X]_{\mathcal{B}_0}^{\mathsf T}\,\mathsf D,
\qquad
R(b)=\mathsf D\,L(b)^{\mathsf T}\mathsf D .
$$

The second display is the one-factor case, and it is the reason the two families print as transposes of one another.

The array, however, is a statement about $\mathcal{B}_0$ and not about the algebra. In a general basis the same identity reads

$$
[\sigma(X)]_{\mathcal{B}}=\mathsf W\,[X]_{\mathcal{B}}^{\mathsf T}\,\mathsf W^{-1},
$$

with $\mathsf W$ the switch of that basis, and the symmetric form $\mathsf W[X]^{\mathsf T}\mathsf W$ is recovered only when $\mathsf W^2=\mathrm I$. So the sentence "the swap is the transpose through the switch" holds only in the bases that carry a switch of square one. It is a coincidence of a good choice. The sentence "the swap is the adjoint of the trace form" holds everywhere, and it is the one to quote. The two dependences cancel, and that cancellation is the whole reason a computation may be done in a convenient display.

## The Two Eigenspaces

An involution splits the algebra it acts on, and this one splits it into a fixed part and a negated part. The two parts have dimensions ten and six, and each is closed under an operation of its own.

The fixed operators are the self-adjoint ones, $\sigma(X)=X$, and they are the image under $\Phi$ of the symmetric square:

$$
\operatorname{Fix}(\sigma)=\Phi\bigl(\operatorname{Sym}^2\mathbb{B}\bigr),\qquad \dim=10 .
$$

The negated operators are the skew-adjoint ones, $\sigma(X)=-X$, and they are the image of the exterior square:

$$
\operatorname{Neg}(\sigma)=\Phi\bigl(\Lambda^2\mathbb{B}\bigr),\qquad \dim=6 .
$$

The second space is spanned by the six differences $L_aR_b-L_bR_a$, which are the commutators $[L_a,R_b]$ because the two regular maps commute. With $10+6=16$ the two spaces account for the algebra.

Neither is closed under composition. For two fixed operators, $\sigma(XY)=YX$, which equals $XY$ only when the two commute. The fixed space closes under the anti-commutator instead, since

$$
\sigma\bigl(\tfrac12(XY+YX)\bigr)=\tfrac12(YX+XY)=\tfrac12(XY+YX),
$$

so it is a Jordan algebra of dimension ten. The negated space closes under the commutator, since

$$
\sigma(XY-YX)=\sigma(Y)\sigma(X)-\sigma(X)\sigma(Y)=YX-XY=-(XY-YX),
$$

so it is a Lie algebra of dimension six. Both computations are one line and both use only the anti-automorphism property; the involution decides which operation survives, and that is the sense in which the exchange of sides and the Jordan–Lie split are one statement. The decomposition of an endomorphism algebra into a symmetric and an exterior square is standard for a nondegenerate symmetric form. What is specific here is that the form is the trace form of the algebra and the reflection is the exchange of the two sides, so the split is read off the two-sided structure rather than imposed on it.

A caution belongs here, because the two six-dimensional spaces are easy to confuse. $\operatorname{Neg}(\sigma)$ is canonical. A frame supplies another six-dimensional space, the span of the six bivectors $\tfrac12[\gamma_\mu,\gamma_\nu]$ of its four generators. The swap does not preserve it. One bivector is carried into the span and the other five out of it, and the two spaces meet in dimension three. Equal dimensions, different objects, and only the first is fixed by the multiplication.

## Conjugation Exchanges the Sides

The swap exchanges the sides and leaves the elements alone. A second map exchanges the sides and moves the elements, and it is the one the physics reaches for.

The **quaternion conjugate** $\natural$ fixes the unit and negates the vector part, $e_t^{\natural}=e_t$ and $u^{\natural}=-u$ for $u$ in the three-dimensional vector subspace. It fixes the coefficients, so it is complex-linear, and the sign on the three vectors makes it an anti-automorphism:

$$
(\tilde X\tilde Y)^{\natural}=\tilde Y^{\natural}\tilde X^{\natural}.
$$

Its fixed space is the line of scalars and its anti-fixed space is the vector subspace; the dimensions $1$ and $3$ add to four.

**Theorem.** For every $a\in\mathbb{B}$,

$$
\natural\,L(a)\,\natural=R\bigl(a^{\natural}\bigr).
$$

*Proof.* Apply $\natural$ to the two ends of $a\natural(\tilde Y)$ and use that it reverses products:

$$
\natural\bigl(L(a)\natural(\tilde Y)\bigr)=\natural\bigl(a\tilde Y^{\natural}\bigr)=\tilde Y a^{\natural},
$$

which is right multiplication by $a^{\natural}$. No basis is used.

The two side-exchangers are therefore different maps, and the difference is the interesting part. The swap exchanges the slots and keeps the parameters: $\sigma(L_aR_b)=L_bR_a$. The conjugation exchanges the slots after conjugating the parameters and reversing their order: $L_aR_b\mapsto R_{a^{\natural}}L_{b^{\natural}}$. On a pure left multiplier the two agree only when $a^{\natural}=a$, that is only on the scalars. The agreement is as small as it can be. Away from the scalars they differ by the sign of the three vector units, and that sign is where every phase in the corpus that comes from a change of side is generated. It is one identity, not a family of coincidences.

The division of labour is then clear. The swap tells you which slot an operator occupies, and it is the map that belongs to the definition. The conjugation tells you when two operators of opposite slots have arrays that agree up to a sign, and it is the map that belongs to the display. Neither is inner, and neither replaces the other.

## What Operator Chirality Is Not

Nine objects are routinely offered as the home of chirality. Each is a genuine object with a genuine use, and none is needed here. The reason repeats: the label is a membership in one of two subspaces of the endomorphism algebra, and a membership requires the two subspaces and nothing else.

A **root** is an element $\tilde Z$ with $\tilde Z^2=e_t$, and it is what a Peirce decomposition is built from. It enters after the label, not before: the label depends on $L$ and $R$, which the multiplication supplies, while a root is a further choice made when a splitting of the algebra is wanted. An **idempotent** is a condition on an element, $\tilde\Pi^2=\tilde\Pi$; the label is a condition on an operator, a membership, and the two conditions have different shapes and different carriers.

A **Peirce decomposition** takes two idempotents and returns four lines of $\mathbb{B}$. The label returns four cases on the operator space, and not one of those cases is a line of the algebra. A **Peirce basis** is a basis, and the label is read without one: the images of $L$ and $R$ exist before any basis is declared, and they do not move when a basis changes.

A **spinor** is an element of a minimal left ideal, and a minimal left ideal is produced by a rank-one idempotent, which is a point of a projective line. The label lives one level up, in the endomorphism algebra, and it selects no point. An **ideal** is a subspace of the algebra; the label names no subspace and chooses no point. These two are the same objection twice, and it is the objection that matters most, because the temptation to turn chirality into a state space is strong and it is a category error.

A **Pauli matrix** is the array of a cell in the tensor display $\mathbb{C}^2\otimes\mathbb{C}^2$. The label is a membership, and a membership has no array; the display is a convenience for printing, and printing changes nothing.

A **Clifford algebra** is the algebra generated by vectors with $\{e_i,e_j\}=2g_{ij}$, and it is offered as the natural home of chirality with a product of generators as the chirality element. Two reasons settle it. The relation fixes squares and anticommutators and says nothing about the side on which an operator multiplies, which is the only datum the label uses. And a Clifford algebra fixes a dimension and a signature, while the two images exist for every algebra in every dimension: $L$ and $R$ are defined by the multiplication, and their intersection is the centre, always. The Clifford reading is a display of the algebra, and it is a correct display; it is not a foundation.

The **fifth cell of a gamma frame** is the case that matters, because it is the object the older reading took for the definition, and it repays a careful look. A frame has five cells, and the fifth is a right multiplier $-iR_u$ for an element $u$ with $u^2=-e_t$ and $\operatorname{Sc}u=0$. Three properties follow in a line each. Since $R_u^2=R_{u^2}=-\mathrm I$, the cell squares to $\mathrm I$. Its trace is zero, because $u$ is traceless. Its spectrum is $+i,+i,-i,-i$, so the projectors $\tfrac12(\mathrm I\pm iR_u)$ have rank two apiece and the split is balanced. A cell with square one, trace zero and a balanced spectrum is exactly what a chirality element should be, and it is a pure right multiplier. That is the whole point. Under the definition of this article the cell has the right slot; it is an example of one of the four labels, and an example cannot be the definition of the label. What it also is, and this is its limitation rather than its virtue, is a cell of a chosen frame: rotate the frame and $u$ changes, the cell changes, and every label of every operator stays where it was.

One hypothesis must not be dropped in that computation, because it is false without it. The statement that $R_u$ has spectrum $+i,+i,-i,-i$ and trace zero for **any** $u$ with $u^2=-e_t$ fails at the central element $ie_t$, which satisfies the square condition and gives $R_{ie_t}=i\mathrm I$, a spectrum of $+i$ four times and a trace of $4i$. Tracelessness is the missing hypothesis, and it is what makes $R_u$ behave as a chirality element rather than as a scalar in disguise.

The cell acts on the algebra as well as on the operator space, and that action is where the Dirac letters come from. For a traceless $u$ with $u^2=-e_t$ every element splits,

$$
\tilde X=\tilde X_L+\tilde X_R,\qquad R_u\tilde X_L=i\tilde X_L,\qquad R_u\tilde X_R=-i\tilde X_R,
$$

with each part of complex dimension two and no element but zero in both. A product takes the letter of its right factor, since $R_u(\tilde X\tilde Y)=\tilde X R_u(\tilde Y)$, and a left multiplication therefore keeps the letter. The letters are the Dirac ones, they belong to this cell, and they belong to the element rather than to the operator: a different $u$ gives a different pair of halves. That is why the split is a property of the element and of the declared frame, and why the operator label, which needs neither, is the more primitive notion.

The one genuine contact between the two theories is an identity, and it should be stated as an identity rather than as a coincidence of arrays. For a traceless $u$ with $u^2=-e_t$ the projector $\tfrac12(\mathrm I+iR_u)$ is idempotent of rank two, and its image is a minimal left ideal. It is at once the Peirce projector $R(\tilde\Pi)$ of the idempotent $\tilde\Pi=\tfrac12(e_t+iu)$ and the spectral projector of $-iR_u$ onto its eigenvalue $-1$. It holds for every such $u$, because both readings are built from the same element, and that is the reason it holds. What must not be inferred from it is that the two notions are one. The Peirce projector is a subspace chosen by an idempotent. The spectral projector is one half of the sign of a single operator. They agree here because $u$ was chosen to make them agree.

## Why the Slot Label Is Not a Grading

A $\mathbb{Z}/2$ grading is a decomposition into two subspaces with a multiplicative sign, equivalently a homomorphism to $\{\pm1\}$. The label is not one, and the obstruction is a single operator.

Suppose such a sign existed, taking $+1$ on a left multiplier and $-1$ on a right multiplier of a noncentral element. The scalar $\lambda\mathrm I$ is the left multiplier of $\lambda e_t$ and the right multiplier of $\lambda e_t$ at the same time, so it would have to carry both values. The label has four cases and a sign has two, and it is the third case that collapses the map from one to the other. There is nothing to repair: the endomorphism algebra is simple and has no nontrivial central idempotent, so no nontrivial grading exists in the first place.

What the swap gives instead is an exchange, and an exchange is not a sign. It carries one side to the other, answers the question "which side" by moving the operator rather than by labelling it, and splits the algebra into a self-adjoint and a skew-adjoint part of dimensions ten and six, with two different closing operations.

A sign, when the physics wants one, has to be chosen as an operator. Any $R_u$ with $u$ traceless and $u^2=-e_t$ supplies it, and its two projectors are the two halves. The sign is therefore an object of the algebra and not a functional on it, which is why no grading is ever exhibited: there is none, and the sign is a choice of $u$. The contrast is the moral of the article. The label is fixed before anything is chosen, and the sign moves when $u$ moves; confusing the two is what produces the impression that chirality is a matrix.

## Summary

Operator chirality is the side on which an operator multiplies. The left multipliers form a four-dimensional image, the right multipliers another, the two meet in the scalars and span seven of the sixteen dimensions, and the remaining nine directions multiply on neither side alone. An operator is labelled left, right, both, or neither; the scalar line is the third case, and a two-sided cell is the fourth.

Under the structure isomorphism $\Phi(a\otimes b)=L_aR_b$ the two sides are the two tensor factors and their overlap is the tensor of the two units. The exchange of the sides is the flip transported to the endomorphism algebra, $\sigma=\Phi\tau\Phi^{-1}$. It is intrinsic. It squares to the identity, reverses products, exchanges the two images and fixes the scalars. It carries every $L_a$ to $R_a$, preserves rank and length, and is not inner. It is the adjoint of the trace form, and in a basis where that form is diagonal it is the transpose through a sign matrix. Its fixed part is a ten-dimensional Jordan algebra and its negated part a six-dimensional Lie algebra, and the two are the symmetric and the exterior square.

The quaternion conjugate is the second side-exchanger, $\natural L(a)\natural=R(a^{\natural})$. It differs from the swap in that it conjugates the parameters and reverses their order, and the sign in which the two differ is the origin of every phase the corpus obtains from a change of side.

None of this needs a root, an idempotent, a Peirce decomposition, a Peirce basis, a spinor, a Pauli matrix, an ideal, a Clifford algebra or the fifth cell of a frame. The fifth cell is the instructive case: a pure right multiplier with square one, trace zero and a balanced spectrum, hence an example of the right side and not the definition of chirality, and a cell of a chosen frame besides. The one contact with the Peirce theory is an identity forced by a shared element, and it is an identity of two constructions and not of two notions.

$$
\boxed{\ \text{chirality}=\text{the side};\qquad X\in L(\mathbb{B}),\ \ X\in R(\mathbb{B}),\ \ X\in L(\mathbb{B})\cap R(\mathbb{B}),\ \ \text{or neither};\qquad \sigma=\Phi\tau\Phi^{-1},\quad \sigma(L_a)=R_a .\ }
$$

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L(a)$, $L_a$ | the left multiplier, $\tilde X\mapsto a\tilde X$ |
| $R(b)$, $R_b$ | the right multiplier, $\tilde X\mapsto\tilde Xb$ |
| $L_aR_b$ | the cell, with a left and a right slot |
| $L(\mathbb{B})$, $R(\mathbb{B})$ | the two images, four-dimensional, meeting in the centre |
| left slot, right slot, both slots, no single side | operator chirality, a membership in the two images |
| $\Phi(a\otimes b)=L_aR_b$ | the structure isomorphism $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}\to\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ |
| $\tau(a\otimes b)=b\otimes a$ | the flip of the two tensor factors |
| $\sigma=\Phi\tau\Phi^{-1}$ | the swap, $\sigma(L_aR_b)=L_bR_a$ |
| $\beta(\tilde X,\tilde Y)=\operatorname{Sc}(\tilde X\tilde Y)$ | the trace form, symmetric and nondegenerate |
| $\mathsf D$, $\mathsf W$ | the Gram matrix $\operatorname{diag}(1,-1,-1,-1)$ and the switch of a general basis |
| $\operatorname{Fix}(\sigma)=\Phi(\operatorname{Sym}^2\mathbb{B})$ | dimension $10$, a Jordan algebra under the anti-commutator |
| $\operatorname{Neg}(\sigma)=\Phi(\Lambda^2\mathbb{B})$ | dimension $6$, a Lie algebra under the commutator |
| $\natural$ | the quaternion conjugate, $\natural L(a)\natural=R(a^{\natural})$ |
| $\ell(M)$, $\operatorname{rank}M$ | the length and the rank, preserved by $\sigma$ |
| $\tfrac12(\mathrm I+iR_u)$, with $u$ traceless and $u^2=-e_t$ | the rank-two projector of a right multiplier, Peirce and spectral at once |

## Further Reading

- [Families of Matrix Representations](families-of-matrix-representations.html), for the two sides, the switch and the change of frame.
- [$M_4(\mathbb{C})$ Axis-Free Representation : Operators](m4c-axis-free-representation-operators.html), for the cells as a basis, the coefficient matrix and the length.
- [$M_4(\mathbb{C})$ Pauli Representation : Operators](m4c-pauli-representation-operators.html), for the same operators in the tensor display.
- [The Endomorphisms of the Biquaternion Algebra](the-endomorphisms-of-the-biquaternion-algebra.html), for the ambient operator space and the two-sided operators.
- [The Unpolarized Module of the Biquaternion Algebra](the-unpolarized-module-of-the-biquaternion-algebra.html), for the carrier, the projective line of splittings and the trace form.
- [The Gamma Frame and the Complexified Dirac Algebra of $M_4(\mathbb{C})$](the-gamma-frame-and-the-complexified-dirac-algebra-of-m4c.html), for the five cells of a frame, the fifth cell as an example, and the six bivectors.
- [Operator Family Conventions](operator-family-conventions.html), for the four families and the slot label.
- [Matrix Representations Conventions](matrix-representations-conventions.html), for the labels and the conventions of the category.
