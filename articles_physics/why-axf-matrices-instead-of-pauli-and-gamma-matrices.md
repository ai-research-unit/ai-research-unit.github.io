# __Why AXF Matrices instead of Pauli and Gamma Matrices__

## Introduction

This article defends one claim: writing a fundamental equation of physics with the Pauli or gamma matrices is a formal defect, and the axis-free matrices are the display that does not have it. The defect is that both the Pauli and gamma matrices single out one spatial direction, and physical space has no preferred spatial direction. The laws are isotropic and the arrays are not, so every formula written in them carries a datum the physics does not contain, and the notation gives no place to mark that datum and no way to subtract it.

The damage is worse than a decoration, and this is the part usually missed. A display that fixes a direction silently absorbs whatever depends on that direction, so the page stops showing it. It can hide a physical structure, by writing an object that is one orbit under rotation as several unrelated entries. It can hide a property of an equation, by making an invariance look like an accident of the entries. It can hide a correspondence, by presenting as two different equations what is one operator in two frames. No result changes and no computation is wrong. What is lost is the ability to see, on the page, which statements belong to the physics and which belong to the notation, and a structure that cannot be seen cannot be used.

The axis-free display writes no direction, and that is why it is the display of the physics articles of this corpus.

One piece of precision is needed before either claim can be checked. A display is an array read in a basis, and the basis is the choice. An operator here is an element of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})\cong M_4(\mathbb{C})$, of complex dimension sixteen, and its display is a $4\times4$ array in a basis of the carrier $\mathbb{B}$, of complex dimension four. The $\mathrm{axf}$ display and the $\mathrm{pau}$ display are two bases of that one carrier: two arrays of one operator, related by a conjugation. The gamma form is not a third basis but a list of five fixed cells of the operator algebra, and a gamma formula writes an operator as a sum of those five and their products. A change from one display to another preserves every product, every trace, every determinant and every spectrum, so the choice is never a question of correctness.

The article has four parts.

The first part takes the Pauli matrices as they are printed, finds the direction in $\sigma_3$, proves in one line why the third matrix is the diagonal one, and follows the direction into the four-dimensional array, into the root of the Peirce frame, into the idempotents, into the ideal, into the column and into the gamma set. Section *The Direction Inside the Gamma Matrices* does the same for the five gammas, where the direction sits in the frame instead of in a diagonal entry, and shows that no choice of gamma basis can remove it.

The second part states the defect in physical terms, and the section *Why a Direction in the Notation Is a Defect* is the core of the article: an equation of general physics must not be written under a display that singles out a direction the physical reality does not contain.

The third part gives the alternative. Section *The Axis-Free Matrices* prints the $\mathrm{axf}$ arrays, proves that no direction can enter them, and lists what they buy and what they cost. Section *The Intrinsic Form* states the preferred form of a physical equation, which is not a matrix at all: a pair of multipliers acting on an element, with no basis.

The fourth part is practical. Section *Migrating from the Pauli Framework* gives the three passes that carry a section of physics into the $\mathrm{axf}$ and intrinsic forms, the dictionary, the four statements that turn out false in the move, and the checks that catch them.

## The Direction Inside the Pauli Matrices

### The Three Matrices

The Pauli matrices are

$$
\sigma_1=\begin{pmatrix}0&1\\ 1&0\end{pmatrix},\qquad
\sigma_2=\begin{pmatrix}0&-i\\ i&0\end{pmatrix},\qquad
\sigma_3=\begin{pmatrix}1&0\\ 0&-1\end{pmatrix}.
$$

Two of them carry $i$ or carry zeros on the diagonal. The third is real and diagonal. That difference is the subject of this section, and it is not a difference between three operators. It is a difference between three positions in a list, produced by the order in which the list was built.

The same asymmetry appears in the two-dimensional image of a general element. The image of $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ is

$$
\mathsf M_2(\tilde Q)=Q_t\,\mathrm I_2-i\bigl(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3\bigr)
=\begin{pmatrix}Q_t-iQ_z&-iQ_x-Q_y\\ -iQ_x+Q_y&Q_t+iQ_z\end{pmatrix}.
$$

The diagonal of this matrix carries $Q_t$ and $Q_z$. The off-diagonal carries $Q_x$ and $Q_y$. The trace and the determinant are unaffected — the trace is $2Q_t$ and the determinant is $Q_t^2+Q_x^2+Q_y^2+Q_z^2$ in every display — but the shape of the array is not neutral. It puts one spatial coefficient in the diagonal slots and the other two in the off-diagonal slots, and a reader has no way to learn from the array that this was a decision.

### Why the Third Matrix Is the Diagonal One

The reason is the construction, not the algebra. The two-dimensional image is left multiplication read on a minimal left ideal, and the ideal is built from an idempotent. The idempotents used are the Peirce idempotents of the root $\vec{Ζ}=i\vec e_z$,

$$
\tilde\Pi_\pm=\tfrac12\bigl(e_t\pm i\vec e_z\bigr),
$$

with $\tilde\Pi_+\tilde\Pi_-=0$ and $\tilde\Pi_++\tilde\Pi_-=e_t$. The carrier of the image is $\mathbb{B}\tilde\Pi_+$, of complex dimension two, and the matrix of $\vec e_z$ on that carrier is diagonal because $\vec e_z$ built the carrier.

The computation is one line. Multiply the idempotent by the unit:

$$
\tilde\Pi_+\vec e_z=\tfrac12\bigl(\vec e_z+i\vec e_z^2\bigr)=\tfrac12\bigl(\vec e_z-i e_t\bigr)=-i\,\tfrac12\bigl(e_t+i\vec e_z\bigr)=-i\tilde\Pi_+.
$$

So $\vec e_z$ acts on the ideal as the scalar $-i$, and its array is $-i\sigma_3$: diagonal, with the two eigenvalues $-i$ and $+i$ in the two slots. The other two units permute the two slots, so their arrays are off-diagonal. The root $i\vec e_z$ is the datum the display consumes, and the diagonal of $\sigma_3$ is its footprint.

Nothing forced $\vec e_z$. The same construction runs on $\vec e_x$ or on $\vec e_y$, with the idempotents $\tfrac12(e_t\pm i\vec e_x)$ and $\tfrac12(e_t\pm i\vec e_y)$, and produces a triplet whose diagonal member is the unit used. The algebra has three interchangeable spatial units, and the display needs exactly one of them.

### The Direction in the Four-Dimensional Array

The four-dimensional Pauli array of the same element is the two-dimensional image in both slots, because left multiplication does not mix the two Peirce components:

$$
L_{\mathrm{pau}}(\tilde Q)=\mathrm I_2\otimes\mathsf M_2(\tilde Q).
$$

The arrays of the four units show the direction twice. The time unit is the identity, the $\vec e_z$ array is diagonal, and the other two are off-diagonal inside each of the two identical blocks:

$$
L_{\mathrm{pau},e_t}=\mathrm I_4,\qquad
L_{\mathrm{pau},\vec e_z}=\begin{pmatrix}-i&0&0&0\\ 0&i&0&0\\ 0&0&-i&0\\ 0&0&0&i\end{pmatrix},
$$

$$
L_{\mathrm{pau},\vec e_x}=\begin{pmatrix}0&-i&0&0\\ -i&0&0&0\\ 0&0&0&-i\\ 0&0&-i&0\end{pmatrix},\qquad
L_{\mathrm{pau},\vec e_y}=\begin{pmatrix}0&-1&0&0\\ 1&0&0&0\\ 0&0&0&-1\\ 0&0&1&0\end{pmatrix}.
$$

Three statements follow, and each is a statement about the page and not about the algebra.

Exactly one of the three spatial units is diagonal. A triplet with this shape cannot be written without deciding which unit it is, because the shape of the list — one diagonal member, two off-diagonal members — is what a triplet of this kind is. The decision is made at the moment the arrays are written, and it is made silently.

The diagonal unit appears twice, once in each block. The repetition is not an accident of the layout; it is $\mathrm I_2\otimes\cdot$, the statement that the frame was built from a root and that the root appears in both slots.

The two remaining spatial units carry the same weight. No entry distinguishes $\vec e_x$ from $\vec e_y$, which is correct, because no entry should. The asymmetry is therefore exactly one-against-two, and it sits in the diagonal.

### The Diagonal Cells Tell the Same Story

The same fact can be stated without writing a single array, and the statement is the one used later.

A cell is diagonal in a basis when it sends each basis vector to a multiple of itself. In the coefficient basis the diagonal cells are the four squares, $e_te_t$, $\vec e_x\vec e_x$, $\vec e_y\vec e_y$ and $\vec e_z\vec e_z$: the square of a unit is a scalar, so it multiplies every basis vector by that scalar. No other cell is diagonal, because a cell with two different slots multiplies a unit by a different unit.

In the Pauli display the diagonal cells are four others. They are $e_te_t$, $e_t\vec e_z$, $\vec e_ze_t$ and $\vec e_z\vec e_z$: both slots take their value from the pair $\{e_t,\vec e_z\}$. The declared unit appears twice, and the two other spatial units appear in no diagonal cell at all.

| basis | cells that are diagonal |
|---|---|
| the four units, in any order of the three spatial units | $e_te_t$, $\vec e_x\vec e_x$, $\vec e_y\vec e_y$, $\vec e_z\vec e_z$ |
| a frame built on the unit $u$ | $e_te_t$, $e_tu$, $ue_t$, $uu$ |

The second row was verified for $u=\vec e_x$, $u=\vec e_y$ and $u=\vec e_z$: in each case the diagonal set is the four cells named, and no other. The pattern is therefore not a property of $\vec e_z$. It is the mark of a frame built on any declared unit, and it moves when the declared unit moves.

A reader who can see which cells are diagonal can read the hidden unit off the page. That is the compensation the Pauli display offers, and it is a real one. The information is present; it is simply never stated, and it is carried by a list of four products rather than by a sentence.

### What the Direction Carries

The direction does not stay in the triplet. It is inherited by every construction built from the root, and the inheritance is mechanical: whatever is built from $\vec e_z$ carries $\vec e_z$. Each item below is a place where a reader meets the choice without being told.

The root. The Peirce frame is the frame of the root $\vec{Ζ}=i\vec e_z$, of square $e_t$. The root is the choice, named or not.

The idempotents. $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$. The unit appears inside both, with opposite signs.

The mixed units. $\vec\Upsilon_\pm=\tfrac12(i\vec e_x\pm\vec e_y)$. The two remaining spatial units are consumed here, and consumed in an order: $\vec e_x$ multiplied by $i$ comes first, $\vec e_y$ second. The pair $(\vec e_x,\vec e_y)$ is no longer a set; it is an ordered pair, and its orientation is part of the frame.

The Peirce decomposition. The four components are read in the order $(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$, which is a second choice, independent of the first: the two middle slots can be exchanged.

The adapted basis and its scale. The mixed units are defined only up to $\vec\Upsilon_+\mapsto\lambda\vec\Upsilon_+$ and $\vec\Upsilon_-\mapsto\lambda^{-1}\vec\Upsilon_-$, so the frame carries a free nonzero scalar as well. The scale is harmless for the algebra and fatal for a display that pretends to be unique.

The minimal left ideal. $\mathbb{B}\tilde\Pi_+$ is the two-dimensional carrier of the older literature. It is built from the unit, and it is the idempotent of the unit that selects it.

The projector and the block split. The projector $\tfrac12(\mathrm I-\gamma_5[\mathbb{B}_{\Phi}])$ has rank two and its range is the ideal $\mathbb{B}\tilde\Pi_+$. The four-dimensional array is $\mathrm I_2\otimes\mathsf M_2(\tilde Q)$: two identical blocks, and the split of the array is the split of the ideal, written twice.

The two-component column, and the spinor. A column of two components is an element of the ideal written in the basis $(\tilde\Pi_+,i\tilde\Pi_+)$, and the spinor of the older literature is that column. This is a consequence of the frame and not of the algebra: a state is an element of $\mathbb{B}$, which needs no ideal, no column and no frame, and it becomes a column only after the ideal has been chosen. The column is the most consequential item of the list, because a whole literature is written in it.

The gamma frame. In the five gammas the unit $\vec e_y$ is the common right multiplier of the spatial three, and $\vec e_z$ is the axis of the fifth cell. Neither fact is stated anywhere on a page that prints the five matrices.

The Dirac adjoint. The adjoint $\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\gamma_0[\mathbb{B}_{\Phi}]$ needs a chosen time generator. It is a statement about a pairing, and the pairing imports the frame.

The charge conjugation. The cell $C=L_{e_t}R_{\vec e_x}$ serves as the charge conjugation of the reference frame, with $C^2=-1$. That this one cell serves is a fact of the frame; which cell it is, is a choice.

The third component of spin. A triplet whose third member is diagonal makes $\sigma_3$ the distinguished one, and every later sentence that measures "the third component" inherits the distinction.

The sentences. "The third member is the diagonal one." "The upper half of the column is the left part." "The diagonal member is the energy." Each is true in the frame that produced it, false in a rotated one, and printed in the same font as the identities that hold everywhere.

| object | the direction it carries | what happens on a relabelling of the spatial units |
|---|---|---|
| the root $i\vec e_z$ | the unit $\vec e_z$ | the root becomes another root |
| the idempotents $\tilde\Pi_\pm$ | the unit $\vec e_z$, twice, with opposite signs | the idempotents change |
| the mixed units $\vec\Upsilon_\pm$ | the ordered pair $(\vec e_x,\vec e_y)$ | the pair changes, and the orientation with it |
| the Peirce decomposition | the order of the four components | the two middle slots exchange |
| the minimal left ideal | the idempotent of the unit | a different ideal |
| the two-component column, and the spinor | the basis of that ideal | a different column |
| the block split | the split of the ideal, twice | a different block split |
| the gamma set | $\vec e_y$ as the common right multiplier, $\vec e_z$ as the axis of the fifth cell | a different five-element set |
| the Dirac adjoint | the chosen time generator $\gamma_0[\mathbb{B}_{\Phi}]$ | a different $\gamma_0[\mathbb{B}_{\Phi}]$ |
| the charge conjugation | the cell $L_{e_t}R_{\vec e_x}$ | a different cell |
| the third component of spin | the diagonal member of the triplet | the diagonal moves |

## The Direction Inside the Gamma Matrices

### The Five Cells

The gamma set is five cells of the operator algebra:

$$
\gamma_0[\mathbb{B}_{\Phi}]=iR_{\vec e_x},\qquad
\gamma_1[\mathbb{B}_{\Phi}]=iL_{\vec e_x}R_{\vec e_y},\qquad
\gamma_2[\mathbb{B}_{\Phi}]=iL_{\vec e_y}R_{\vec e_y},\qquad
\gamma_3[\mathbb{B}_{\Phi}]=iL_{\vec e_z}R_{\vec e_y},\qquad
\gamma_5[\mathbb{B}_{\Phi}]=-iR_{\vec e_z}.
$$

The frame is named in brackets and it is $\mathbb{B}_{\Phi}$ throughout this article; below the label is dropped, and every $\gamma_\mu[\mathbb{B}_{\Phi}]$ is $\gamma_\mu[\mathbb{B}_{\Phi}]$. Two of the five are single multipliers, because $L_{e_t}$ is the identity of the operator algebra: $e_t$ is the unit of $\mathbb{B}$. The five satisfy the cell relation of that frame, with $\delta_{\mu\nu}=(1,1,1,1)$ the unit metric,

$$
\{\gamma_\mu[\mathbb{B}_{\Phi}],\gamma_\nu[\mathbb{B}_{\Phi}]\}=2\varepsilon_\mu\delta_{\mu\nu}\,\mathrm I_4,\qquad
\varepsilon=(1,-1,-1,-1),$$

so that $\gamma_0[\mathbb{B}_{\Phi}]^2=+\mathrm I_4$ and $\gamma_k[\mathbb{B}_{\Phi}]^2=-\mathrm I_4$; their product is the fifth, $\gamma_5[\mathbb{B}_{\Phi}]=i\gamma_0[\mathbb{B}_{\Phi}]\gamma_1[\mathbb{B}_{\Phi}]\gamma_2[\mathbb{B}_{\Phi}]\gamma_3[\mathbb{B}_{\Phi}]$, with $\gamma_5[\mathbb{B}_{\Phi}]^2=\mathrm I_4$. All of this was verified on the arrays.

In the Pauli display of the previous section the five become

$$
\gamma_0[\mathbb{B}_{\Phi}]=\begin{pmatrix}0&\mathrm I_2\\ \mathrm I_2&0\end{pmatrix},\qquad
\gamma_k[\mathbb{B}_{\Phi}]=\begin{pmatrix}0&\sigma_k\\ -\sigma_k&0\end{pmatrix},\qquad
\gamma_5[\mathbb{B}_{\Phi}]=\begin{pmatrix}-\mathrm I_2&0\\ 0&\mathrm I_2\end{pmatrix}.
$$

This is the block form that the Peirce frame produces. It is not a form chosen afterwards, and that is the point of the section.

### The Three Spatial Units Have Three Different Jobs

In the five cells the three spatial units are not interchangeable, and the asymmetry is visible in the definitions.

The unit $\vec e_x$ is the right multiplier of the time gamma, and it is also the left multiplier of the first spatial gamma.

The unit $\vec e_y$ is the common right multiplier of all three spatial gammas. That is what makes the three spatial terms of the Dirac operator combine into one term, as shown below.

The unit $\vec e_z$ is never the right multiplier of a spatial gamma. It appears once, as the axis of the fifth cell, and it is the only unit that does.

### The Relabelling Test

The test is a relabelling. Take the five definitions and permute the names $x,y,z$ among the units. For the permutation that sends $\vec e_x\to\vec e_y$, $\vec e_y\to\vec e_z$ and $\vec e_z\to\vec e_x$, the five cells become

$$
iR_{\vec e_y},\qquad iL_{\vec e_y}R_{\vec e_z},\qquad iL_{\vec e_z}R_{\vec e_z},\qquad iL_{\vec e_x}R_{\vec e_z},\qquad -iR_{\vec e_x},
$$

which is not the original set. The same failure occurs for all five non-trivial permutations, as checked on the cells. So the gamma set is tied to a labelling of the spatial units, and a relabelling produces a different frame, related to the first by a conjugation.

The distinction is worth stating exactly, because it is easy to overstate. The Clifford relations are invariant: the relabelled cells satisfy the same relations with the same metric, because a permutation of the three spatial units is an automorphism of the algebra and leaves the metric alone. What is not invariant is the set of five. The metric cannot tell the three units apart, and the five-cell list can.

### Every Gamma Display Writes One Direction

The choice cannot be removed by choosing a better gamma basis, and the reason is a one-line argument.

Suppose a display made both $\gamma_0[\mathbb{B}_{\Phi}]$ and $\gamma_5[\mathbb{B}_{\Phi}]$ diagonal. Both are invertible, so their diagonal entries are nonzero. They anticommute, and two diagonal matrices anticommute only if the entrywise product of their diagonals vanishes in every slot. That product vanishes, so $\gamma_0[\mathbb{B}_{\Phi}]\gamma_5[\mathbb{B}_{\Phi}]=0$, which contradicts invertibility. Hence at most one of the two is diagonal.

The two standard displays are the two ways of spending that one allowance. The Dirac display makes $\gamma_0[\mathbb{B}_{\Phi}]$ diagonal and $\gamma_5[\mathbb{B}_{\Phi}]$ off-diagonal: it writes the time direction, which the plain weight does distinguish, into the array. The block display, and the Pauli display of this corpus, makes $\gamma_5[\mathbb{B}_{\Phi}]$ diagonal and $\gamma_0[\mathbb{B}_{\Phi}]$ off-diagonal: it writes a spatial direction, which the plain weight does not distinguish, into the array. A page that prints gammas has made the choice before it prints anything, and the notation gives the reader no way to tell which choice was made.

### The Split the Pauli Display Shows

The fifth cell is $i$ times a real signed permutation with zeros on the whole diagonal in $\mathrm{axf}$, and it is $\operatorname{diag}(-1,-1,1,1)$ in the Pauli display. Its eigenvalues are $\pm1$ in both, its square is the identity in both, and its trace is zero in both. What changes is whether the array splits into two blocks, and the split is the Peirce split of the same unit.

The projector $\tfrac12(\mathrm I-\gamma_5[\mathbb{B}_{\Phi}])$ is $\operatorname{diag}(1,1,0,0)$ and the projector $\tfrac12(\mathrm I+\gamma_5[\mathbb{B}_{\Phi}])$ is $\operatorname{diag}(0,0,1,1)$, both of rank two. Their ranges are the two left ideals of the frame: the eigenvalue $-1$ holds on $\mathbb{B}\tilde\Pi_+$ and the eigenvalue $+1$ on $\mathbb{B}\tilde\Pi_-$, as verified on both ideals. So the block, the left ideal, the two-component column and the projector are one object seen four times, and one choice of unit produces all four.

The three cells $-iR_{\vec e_x}$, $-iR_{\vec e_y}$ and $-iR_{\vec e_z}$ are conjugate to one another, and the conjugation is implemented by an operator of the algebra. For $s$ the quarter-turn versor about $\vec e_y$, the conjugation $L_sR_{s^{-1}}$ carries $\vec e_z$ to $\vec e_x$ and carries $-iR_{\vec e_z}$ to $-iR_{\vec e_x}$ exactly. So the choice of which spatial unit carries the fifth cell is a labelling, and every labelling gives a split of the same kind. Only one of the three is diagonal in the display, and it is the one the frame was built on.

## Why a Direction in the Notation Is a Defect

### Physical Space Has No Preferred Spatial Direction

Take any two spatial directions. A rotation of the algebra carries one to the other, and the rotation is an automorphism: it preserves the product, the metric, the trace and the determinant. For $s$ a nonzero versor, the operator $L_sR_{s^{-1}}$ is such an automorphism, and it acts on the units by $u\mapsto sus^{-1}$. The three spatial units are one orbit.

No experiment distinguishes them. A laboratory that is turned by ninety degrees measures the same physics, and the transformation that relates the two descriptions is a symmetry of the theory and not a relabelling of a measurement error. Isotropy is not a convenience of notation; it is a property of space, and it is the reason angular momentum is conserved.

An equation of general physics therefore does not contain a spatial direction. If it did, the direction would have to be supplied by something outside the equation, and the equation would be about a situation rather than about a law. The Dirac operator of a free field, the wave equation, the Maxwell equations and the Klein–Gordon equation all have this property: each is form-invariant under the rotation, and none of them names a direction.

### The Display Adds a Direction the Equation Does Not Have

A display is a function of a basis. Written in a basis, an operator becomes numbers, and a rotation of the basis becomes a conjugation of the array. The pair (operator, array) is therefore covariant: the operator is fixed and the array moves.

The standard Pauli display breaks the covariance of the page. The array $L_{\mathrm{pau}}(\tilde Q)$ is written in a basis fixed by a root, and the rotation that exchanges $\vec e_z$ with $\vec e_x$ does not produce another array of the same shape: it produces an array in another frame. So the sentence "$\sigma_3$ is diagonal" is not a statement that survives the symmetry. It is a statement about the frame, printed in the grammar of a statement about the algebra.

The defect is not that the display has a direction. The defect is that the direction is unmarked. A sentence $\sigma_3[u]$, with $u$ the axis, would be complete and could be rotated. The sentence $\sigma_3$, with no axis, is incomplete and cannot be rotated, and the notation supplies no place to put the missing name. A formula of general physics is then printed with a datum it does not contain, and the reader has no way to subtract the datum.

### The Defect Hides Structures, Properties and Correspondences

An unmarked direction does not only add a datum. It also removes one, because whatever depends on the direction is absorbed into the frame and stops being visible. Three examples from the material of this article show the damage.

A physical structure disappears. The three spatial cells of the gamma set are one orbit: a conjugation of the algebra carries any one of them to any other, so the statement "these three are one object" is a statement of physics. In the Pauli display the third of them is $\operatorname{diag}(1,-1)$ inside its block and the other two are off-diagonal, so the page shows one member and two others, and the orbit is not on the page. A reader who wants to use the symmetry must first discover that it exists, and the display is what conceals it.

A property of an equation disappears. The axis-free array satisfies $L(\tilde Q)^{\mathsf T}=L(\tilde Q^{\natural})$, so the transpose of the array is again the array of an element, and the adjoint operation is basis-free. In the Pauli display no such rule holds: the transpose of the array is not the array of any conjugation of the element, and the property is not available to a reader who works in that display. It is not that the property is false. It is that the display cannot state it.

A correspondence disappears. The Dirac operator written in the block form and the same operator written in the Dirac form are one operator in two frames, and the matrix that carries one to the other is $C_{\Pi}$. On a page that prints both, the correspondence has to be supplied by a sentence. On a page that prints only one, the other is not visible at all, and two articles that use different conventions look like two different theories.

The pattern is general. A frame that is declared nowhere is a frame nobody can undo, and an object written in it carries the frame in place of the information it displaced.

### Not Every Frame Is a Defect

The argument would be worthless if it condemned every frame, and it does not. A frame is legitimate whenever the physics supplies one.

A measurement supplies one. A Stern–Gerlach apparatus has an axis, and the axis is in the laboratory, not in the notation. An experiment on a beam has a beam axis. A scattering process has a plane, and the plane has a normal. A background field breaks isotropy, and its direction is part of the solution. In each of these cases a frame is a physical datum, and the correct practice is to name it, use it, and say that the result is about that frame.

The squares of the units supply one, and it is a different kind of direction. Time is distinguished from space by the sign, $e_t^2=e_t$ and $\vec e_k^2=-e_t$, and that asymmetry is carried by the units themselves. Every formula inherits it automatically and correctly, with no sentence and no declaration, because it lives in an object and not in a layout. That is the model: an asymmetry that the physics has should be carried by an object of the algebra, where a reader can see it and where it cannot be lost.

The defect is the third case, which is neither of these: a direction that the problem does not supply, that the notation supplies anyway, that is used in every formula of the article, and that is never named.

### The Test Is Covariance

The test of a displayed statement is mechanical. Apply the automorphism, re-read the statement, and compare.

The statement
$$
\vec e_k^2=-e_t
$$
returns itself, with $k$ renamed. It is a fact about $\mathbb{B}$.

The statement
$$
\sigma_3=\operatorname{diag}(1,-1)
$$
does not return itself. Under the exchange of $\vec e_z$ with $\vec e_x$ the diagonal member becomes the first one, and the array is not the array that was printed. It is a fact about the page.

Both are printed as equalities, in the same font, with no marker. The first is true of every direction. The second is true of one direction and false of the other two. A reader who wants to know which kind of statement is in front of him has nothing to consult, and a writer who copies the second into a rotated context produces a formula that is wrong without being detectable as wrong.

### The Four Things the Reader Loses

The loss is practical, and it can be listed.

He cannot sort. Two statements with the same grammar and different status stand side by side, and nothing in the notation separates the invariant from the frame-dependent one.

He cannot check. Verifying that an equation is rotation-invariant requires seeing how it transforms. In the standard display the transformation is invisible, so the check cannot be done on the page and must be redone from the algebra every time.

He cannot copy. A declaration is local. It is dropped when the formula moves into the next article, into a program as a literal array, or into a comparison with a paper that uses another convention. What travels is the array, and the array carries the direction while the sentence that named it stays behind.

He cannot reuse a proof. A theorem proved for one split of the three units must be reproved for the other two, or shown to be covariant, and the second task is the harder one precisely because the statement was written in a form that hides the transformation.

### What Is Not Claimed

No computation done in the Pauli or gamma display is wrong. The Clifford relations hold in every display, every trace and every determinant is invariant, and an amplitude computed with gammas is correct. The Dirac equation written with the five gammas is a correct equation, and it is the equation of the literature.

The claim is narrower and it is about the page. A fundamental equation should not be written in a form that privileges a direction the physical reality does not contain, because the privilege then travels with the formula and cannot be distinguished from the physics. The remedy is not a correction of any result. It is a rule of writing: the direction is an object of the sentence, with a name, and it appears only where the construction is the subject.

## The Axis-Free Matrices

### The Definition

The coefficient basis is $(e_t,\vec e_x,\vec e_y,\vec e_z)$, and it is the basis the multiplication table already provides. The $\nu$-th column of the left array is the coordinate column of the product $\tilde Qe_\nu$:

$$
L_{\mathrm{axf}}(\tilde Q)_{\mu\nu}=\bigl[\tilde Qe_\nu\bigr]_\mu,\qquad
L_{\mathrm{axf}}(\tilde Q)=
\begin{pmatrix}
Q_t&-Q_x&-Q_y&-Q_z\\
Q_x&Q_t&-Q_z&Q_y\\
Q_y&Q_z&Q_t&-Q_x\\
Q_z&-Q_y&Q_x&Q_t
\end{pmatrix}.
$$

Every entry is a structure constant of the algebra or a coefficient of the element. The array is the multiplication table read as a matrix, and nothing else enters it: no idempotent, no root, no direction.

The four unit arrays show why no direction can enter.

$$
L_{\mathrm{axf},e_t}=\mathrm I_4,\qquad
L_{\mathrm{axf},\vec e_x}=\begin{pmatrix}0&-1&0&0\\ 1&0&0&0\\ 0&0&0&-1\\ 0&0&1&0\end{pmatrix},
$$

$$
L_{\mathrm{axf},\vec e_y}=\begin{pmatrix}0&0&-1&0\\ 0&0&0&1\\ 1&0&0&0\\ 0&-1&0&0\end{pmatrix},\qquad
L_{\mathrm{axf},\vec e_z}=\begin{pmatrix}0&0&0&-1\\ 0&0&-1&0\\ 0&1&0&0\\ 1&0&0&0\end{pmatrix}.
$$

All three spatial arrays have zero diagonal. Not one of them is preferred, and none of them can be read as "the diagonal one".

### Why No Direction Is Chosen

The diagonal cells of this display are the four squares, and the set is

$$
\{e_te_t,\ \vec e_x\vec e_x,\ \vec e_y\vec e_y,\ \vec e_z\vec e_z\}.
$$

Each spatial unit is diagonal in exactly one cell, its own square, and in no other. The three are on the same footing: a permutation of the spatial units permutes the last three members of the set and leaves the set unchanged. The set therefore carries no information about which unit was used in any construction, because no construction was used.

Compare the second row of the table of §*The Diagonal Cells Tell the Same Story*. There the declared unit appears twice in the diagonal set and the other two appear never. Here every unit appears once and none appears twice. The difference between "once each" and "twice for one, never for the others" is the difference between a display that has made a choice and a display that has not.

### The Good Properties

The axis-free display is not merely neutral. It has properties that the Pauli display lacks, and they follow from the same fact: the basis is the one the algebra carries.

Every one of the sixteen cells is a real signed permutation matrix: one nonzero entry in each row and in each column, of modulus one, of determinant one, of Hilbert–Schmidt norm two. The sixteen were checked one by one. In the Pauli display eight are real and eight carry $i$.

The four unit arrays and their negatives form a group of order eight isomorphic to the quaternion group. The array of a product is the product of the arrays, and the array of a unit is a column of the multiplication table. The display is the algebra's own multiplication table, so nothing is added by the act of writing it.

The invariants are read directly, from the array's own entries:

$$
\operatorname{Tr}L_{\mathrm{axf}}(\tilde Q)=4Q_t,\qquad
\det L_{\mathrm{axf}}(\tilde Q)=\bigl\langle\tilde Q\bigr\rangle_{\natural}^{2},
$$

where $\langle\tilde Q\rangle_\natural=Q_t^2+Q_x^2+Q_y^2+Q_z^2$. Both were verified on random elements. The trace is four times the scalar coefficient and the determinant is the square of the natural norm, so the two invariants a physicist needs come out of the display's own structure.

The transpose is the natural conjugation:

$$
L_{\mathrm{axf}}(\tilde Q)^{\mathsf T}=L_{\mathrm{axf}}(\tilde Q^{\natural}),\qquad
\tilde Q^{\natural}=Q_te_t-Q_x\vec e_x-Q_y\vec e_y-Q_z\vec e_z.
$$

The Pauli display has no such rule: the transpose of its array is not the array of any conjugation of the element. This is the property that makes the adjoint operation basis-free, and it is lost in the display that has a direction.

The right family is the transpose of the left one between a fixed diagonal sign matrix:

$$
R_{\mathrm{axf}}(\tilde Q)=\mathsf D\,L_{\mathrm{axf}}(\tilde Q)^{\mathsf T}\mathsf D,\qquad
\mathsf D=\operatorname{diag}(1,-1,-1,-1).
$$

The five gammas are not marked out. In this display they are $i$ times five of the sixteen cells, of the same kind as the other eleven, and nothing in the array distinguishes them. Which five cells form the frame is a statement of the physics, made in words, where a reader can check it.

| property | $\mathrm{axf}$ | $\mathrm{pau}$ |
|---|---|---|
| the diagonal cells | the four squares, one per unit | $e_te_t$, $e_t\vec e_z$, $\vec e_ze_t$, $\vec e_z\vec e_z$ |
| the diagonal set under a permutation of the spatial units | unchanged | changed |
| the sixteen cells | all real signed permutations, determinant one | eight real, eight carrying $i$ |
| the transpose rule | $L(\tilde Q)^{\mathsf T}=L(\tilde Q^{\natural})$ | absent |
| the trace | $4Q_t$ | $4Q_t$ |
| the determinant | $\langle\tilde Q\rangle_\natural^2$ | $\langle\tilde Q\rangle_\natural^2$ |
| the block structure | none | two identical blocks |
| the five gammas | five of the sixteen cells, not distinguished | three Pauli matrices, one of them diagonal |
| the direction written into the page | none | one spatial unit |

### What the Display Gives Up

The neutrality has a price, and the price should be stated in the same breath.

The Pauli display shows the block, the ideal and the column as diagonal entries. The axis-free display shows none of them. A reader of an $\mathrm{axf}$ page who wants the Peirce split must be told which cell produces it, and must apply the projector $\tfrac12(\mathrm I-\gamma_5[\mathbb{B}_{\Phi}])$ explicitly. The information is not absent, but it is not free either: it costs one sentence.

That trade is the whole content of the choice between the two displays. The Pauli display gives the block for free and charges a silent direction. The axis-free display charges a sentence and gives no direction. For a formula of general physics the second price is the lower one, because general physics has no direction to give.

## The Intrinsic Form

### The Operator Is a Pair

A matrix display is already a compromise. The object an equation of the corpus names is not an array but an action on an element:

$$
\tilde{Ξ}_{\mathrm{sp}}\longmapsto a\,\tilde{Ξ}_{\mathrm{sp}}\,b.
$$

The pair $(a,b)$ is the operator, written $L_aR_b$ when a name is needed. It carries seven effective parameters rather than eight, because $(a,b)$ and $(\lambda a,\lambda^{-1}b)$ give the same action for any nonzero scalar $\lambda$. No basis appears in the definition, and none appears in the result.

This is the form the physics equations of the corpus take when the equation is the subject and no array is required. Each factor is named, so a reader sees which factor carries the mass, which the momentum and which the grading, and no factor is an entry of a display.

### Composition and Invariants

Composition is one line, with the second slot reversed because right multiplications compose in the opposite order:

$$
\bigl(L_aR_b\bigr)\bigl(L_cR_d\bigr)=L_{ac}R_{db}.
$$

Powers, inverses and the adjoint follow without a display:

$$
\bigl(L_aR_b\bigr)^n=L_{a^n}R_{b^n},\qquad
\bigl(L_aR_b\bigr)^{-1}=L_{a^{-1}}R_{b^{-1}},\qquad
\bigl(L_aR_b\bigr)^{\approx}=L_bR_a.
$$

The trace and the determinant are read from the multipliers:

$$
\operatorname{Tr}L_aR_b=4\,a_tb_t,\qquad
\det L_aR_b=\bigl\langle a\bigr\rangle_\natural^{2}\bigl\langle b\bigr\rangle_\natural^{2}.
$$

The signs are the squares of the units, and no separate metric is needed:

$$
e_t^2=e_t,\qquad \vec e_k^2=-e_t,\qquad
\mathrm{Sc}\bigl(\tilde Q^2\bigr)=Q_t^2-Q_x^2-Q_y^2-Q_z^2.
$$

### The Carrier Is the Algebra

The intrinsic form takes the carrier to be $\mathbb{B}$ itself, with its own multiplication, so the objects of an equation are elements and their products. Nothing else is introduced: no ideal, no column, no projector, no frame.

Two consequences follow, and both are properties of the algebra rather than of a display.

The split of the algebra into its two sectors is the conjugation $\natural$, and it is carried by the algebra. A column of $\mathbb{C}^4$ carries no conjugation of its own, and a display in columns must import the split as extra structure.

The five gammas belong to a frame and not to the algebra. In the intrinsic form they are written out as the cells they are, $iR_{\vec e_x}$, $iL_{\vec e_k}R_{\vec e_y}$ and $-iR_{\vec e_z}$, and a reader sees the three spatial units in three different jobs on the same line. That is the defect of §*The Three Spatial Units Have Three Different Jobs* made visible at the place where it enters, which is the most a notation can do about it.

### When a Matrix Is Still Needed

Some statements are about an array: a comparison of two displays, the census of the sixteen cells, a sentence that makes the direction visible, a program that multiplies numbers. For those, the array is the object of the sentence and must be written.

The natural array is the $\mathrm{axf}$ one, because it is the only one that adds nothing. A reader who sees an $\mathrm{axf}$ array can be sure that any direction in the surrounding paragraph came from the physics and not from the layout.

The order of preference is therefore four-level: the action first, a cell when the operator must be one symbol, an $\mathrm{axf}$ array when an array is unavoidable, and a Pauli or gamma array only where the array itself is the subject, as in a comparison or a dictionary.

| level | object | needs a basis | used when |
|---|---|---|---|
| the action | the pair $(a,b)$ | no | the operator is the subject |
| the cell | $L_aR_b$ as one element of a basis of operators | no | the operator must be one symbol |
| the array | $L_{\mathrm{axf}}(\tilde Q)$ | yes, the coefficient basis | an array is the object of the sentence |
| the Pauli array | $L_{\mathrm{pau}}(\tilde Q)$ | yes, the Peirce frame | a block, an ideal or a gamma is the subject |

## Migrating from the Pauli Framework

An article written in the Pauli framework does not have to be rewritten at once. The move has three passes, and each pass is mechanical enough to be checked.

### The First Pass: From Arrays to Cells

Replace every array by the cell it displays. A cell is written $L_{e_\mu}R_{e_\nu}$, and its array is read in whichever frame the sentence needs. The pass removes the frame from the algebra and leaves it in the notation, where it can be seen.

A cell with a time slot collapses, because $e_t$ is the unit of the algebra: $L_{e_t}$ and $R_{e_t}$ are the identity operator, and a cell with two time slots is the identity. Two of the five gammas are single multipliers for exactly this reason.

During this pass an array may stay only where the array is the object: a comparison of two displays, the table of the sixteen cells, a sentence whose content is which entry is nonzero. Everything else becomes a cell.

### The Second Pass: From Cells to Actions

Replace every cell by what it does. The rule is one line, and it is the whole pass:

$$
\tilde{Ξ}_{\mathrm{sp}}\longmapsto a\,\tilde{Ξ}_{\mathrm{sp}}\,b.
$$

The pass removes the operator symbol as well. A mass term is $\lambda_m^{-1}\tilde{Ξ}_{\mathrm{sp}}$; a derivative term is a term of the Dirac operator written out; a product is a product of elements. The composition law of §*Composition and Invariants* replaces every matrix multiplication. Here $\lambda_m=\hbar/(mc)$ is the mass length.

An article that reaches this pass has no arrays and no ideals in its body, and reads its operators off the formula itself.

### The Third Pass: Keep the Axis-Free Array Where an Array Is Required

The remaining arrays are the ones the sentence is about. Write them in $\mathrm{axf}$, and put the frame label low: $L_{\mathrm{axf}}(\tilde Q)$ and $L_{\mathrm{pau}}(\tilde Q)$. The label is a name and not an exponent, and no label stands in the caret.

A section that survives all three passes has no Pauli object in its body, and any Pauli object it keeps is inside a closing block whose subject is the dictionary.

### The Dictionary

The three passes need a table, and one table serves all three. Each row gives the name in the old notation, the object behind it, and the action.

| Pauli or gamma name | object | $\mathrm{axf}$ array | action |
|---|---|---|---|
| the identity $\mathrm I_4$ | $L_{e_t}R_{e_t}$ | $\mathrm I_4$ | $\tilde{Ξ}_{\mathrm{sp}}\mapsto\tilde{Ξ}_{\mathrm{sp}}$ |
| the image $\mathsf M_2(\tilde Q)$ | the left action on $\mathbb{B}\tilde\Pi_+$ | $\mathrm I_2\otimes\mathsf M_2(\tilde Q)$ | the action read on one ideal |
| $\gamma_0[\mathbb{B}_{\Phi}]$ | $iR_{\vec e_x}$ | $iR_{\mathrm{axf},\vec e_x}$ | $\tilde{Ξ}_{\mathrm{sp}}\mapsto i\tilde{Ξ}_{\mathrm{sp}}\vec e_x$ |
| $\gamma_k[\mathbb{B}_{\Phi}]$ | $iL_{\vec e_k}R_{\vec e_y}$ | $iL_{\mathrm{axf},\vec e_k}R_{\mathrm{axf},\vec e_y}$ | $\tilde{Ξ}_{\mathrm{sp}}\mapsto i\vec e_k\tilde{Ξ}_{\mathrm{sp}}\vec e_y$ |
| $\gamma_5[\mathbb{B}_{\Phi}]$ | $-iR_{\vec e_z}$ | $-iR_{\mathrm{axf},\vec e_z}$ | $\tilde{Ξ}_{\mathrm{sp}}\mapsto-i\tilde{Ξ}_{\mathrm{sp}}\vec e_z$ |
| the mass term | $\lambda_m^{-1}L_{e_t}R_{e_t}$ | $\lambda_m^{-1}\mathrm I_4$ | $\tilde{Ξ}_{\mathrm{sp}}\mapsto \lambda_m^{-1}\tilde{Ξ}_{\mathrm{sp}}$ |
| the Peirce projector $\tfrac12(\mathrm I-\gamma_5[\mathbb{B}_{\Phi}])$ | $\tfrac12\bigl(L_{e_t}R_{e_t}+iR_{\vec e_z}\bigr)$ | $\tfrac12\bigl(\mathrm I_4-iR_{\mathrm{axf},\vec e_z}\bigr)$ | $\tilde{Ξ}_{\mathrm{sp}}\mapsto\tfrac12\bigl(\tilde{Ξ}_{\mathrm{sp}}-i\tilde{Ξ}_{\mathrm{sp}}\vec e_z\bigr)$ |
| the Dirac adjoint | a pairing, not an action | — | needs the frame that declares the pairing |

The last row is the one that has no action, and that is the honest answer: the adjoint is not an operator on the element but a pairing of two elements.

### The Conjugation and What It Preserves

The two displays are related by one matrix. With the Peirce vectors as columns,

$$
C_{\Pi}=\bigl(\tilde\Pi_+\ \ \vec\Upsilon_+\ \ \vec\Upsilon_-\ \ \tilde\Pi_-\bigr),\qquad
L_{\mathrm{pau}}(\tilde Q)=C_{\Pi}^{-1}L_{\mathrm{axf}}(\tilde Q)\,C_{\Pi},
$$

and $\det C_{\Pi}=-\tfrac14$. Every invariant survives the change: products, anticommutators, traces, determinants, spectra, ranks and the eigenvalue count. This is why the migration cannot change a result, and why it must be checked on invariants rather than on entries.

The conjugation is the check. Take an identity, conjugate both sides, and verify that the two sides remain equal. If a statement survives the conjugation, it was a statement about the operator. If it does not, it was a statement about the display.

### The Four Traps

A migration that has been done once already leaves a record of what went wrong, and the record is four statements that looked like algebra and were notation.

The transpose rule. It holds in $\mathrm{axf}$, $L(\tilde Q)^{\mathsf T}=L(\tilde Q^{\natural})$, and it does not hold in the Pauli display. A proof that uses it is a proof about the axis-free frame, and it must be stated as such or re-proved.

The blocks. The two identical blocks of the Pauli array are the statement that left multiplication preserves the two Peirce components. In $\mathrm{axf}$ there are no blocks, and the same content is the statement that the right slot of the cell $L_{\vec e_k}R_{\vec e_y}$ does not move. A sentence about "the blocks" has to be rewritten as a sentence about the ideal.

The diagonal member. In the Pauli display one spatial unit sits on the diagonal, and a sentence about "the diagonal entry" is a sentence about that unit. In $\mathrm{axf}$ every diagonal cell is a square, and the entry says nothing about any unit. A sentence of that kind must be rewritten with the unit named.

The swap. The right family is the transpose of the left one between $\mathsf D$ and its own inverse in $\mathrm{axf}$, and the Pauli display has no such rule. A symmetry argument that uses the swap is a symmetry of the coefficient basis.

### The Checklist

Five checks catch a migration that has gone wrong, and all five are mechanical.

The glyph census. Count the occurrences of the array delimiters and of the symbols $\sigma$, $\gamma$, $\Pi$ and $\Upsilon$ in the body, everything before the closing block. A body with no array, no $\sigma$ and no $\gamma$ has passed the first two passes.

The operator census. Count the occurrences of the letters $L$ and $R$ carrying a subscript, section by section. A section that has reached the third pass has none, except a cell the section is about.

The invariant test. Evaluate both sides of every identity on a hundred random elements and compare. A mismatch is a conjugation error, not a typo.

The permutation test. Rename the three spatial units by a cycle and re-read the section. Every sentence that becomes false was a sentence about the display. This test is the reason the article exists, and it is the one a migration usually skips.

The link test. Every cited title must resolve, and a rewritten section must not cite a section that no longer exists.

### The Rules of Use

Write the action first, $\tilde{Ξ}_{\mathrm{sp}}\mapsto a\tilde{Ξ}_{\mathrm{sp}} b$, and name the operator only when the operator is the subject.

Write one term per line. A sum is a sum of terms, and each term is a pair.

Never compress a sum into one symbol unless its coefficient matrix has rank one.

Keep the coefficient matrix out of the page. It is a diagnostic of the dictionary, not a datum of the physics.

Use no arrays, columns or Kronecker products in a physical formula.

Name the basis once, where it is used, and state a change of pair of spatial units where it occurs.

Enter the Pauli chain only where it is the subject: a Pauli array, a root, an idempotent, a Peirce basis, an ideal or a block.

Put the gamma form in one closing section, with the dictionary and no derivation, except in an article whose subject is the comparison, as in this one.

## Summary

The Pauli matrices carry a direction and do not say so. The asymmetry is one-against-two: exactly one of the three spatial units is diagonal, and it is the unit that built the idempotents of the display. The direction then propagates to the root, the idempotents, the ordered mixed pair, the Peirce decomposition, the adapted basis, the minimal left ideal, the two-component column, the spinor, the block split, the gamma frame, the adjoint, the charge conjugation and every sentence that speaks of "the third member" or "the upper block".

The gamma matrices carry the same direction in the frame. The five cells use the three spatial units in three different jobs, and a relabelling of the units produces a different five-element set. The Clifford relations do not notice the change, because a permutation of the units is an automorphism; the list of five does notice it.

No gamma display can avoid the choice. The two gammas $\gamma_0[\mathbb{B}_{\Phi}]$ and $\gamma_5[\mathbb{B}_{\Phi}]$ anticommute, so at most one of them is diagonal, and the display spends that allowance on the time direction or on a spatial one. The Pauli display of this corpus spends it on the spatial one.

The defect is a formal defect, and its source is physical. Physical space has no preferred spatial direction, and a fundamental equation therefore contains none. A display that singles one out adds a datum the equation does not have, and the addition is unmarked, so the reader cannot subtract it. It also hides what depends on that direction: the orbit of the three spatial cells, the basis-free form of the adjoint, and the correspondence between two frames become invisible on the page, which is worse than a stray datum. A frame is legitimate when a measurement, an apparatus or a background supplies the direction, and then it is named; the defect is the default frame no problem asked for.

The $\mathrm{axf}$ display writes no direction. Its diagonal cells are the four squares, one per unit, and the set is unchanged by any permutation of the three spatial units. Every cell is a real signed permutation of determinant one, the trace is $4Q_t$, the determinant is the square of the natural norm, and the transpose is the natural conjugation.

The preferred form of a physical equation is not a matrix at all. The operator is a pair of multipliers acting on an element, $\tilde{Ξ}_{\mathrm{sp}}\mapsto a\tilde{Ξ}_{\mathrm{sp}} b$, with no basis in the definition.

The migration has three passes — arrays to cells, cells to actions, keep the axis-free array where an array is required — a dictionary, four traps and five checks.

| question | the Pauli and gamma displays | the $\mathrm{axf}$ display |
|---|---|---|
| what fixes the display? | a declared unit, unmarked | the multiplication table, and nothing else |
| what does the array write into the page? | one spatial direction | no direction |
| which cells are diagonal? | $e_te_t$, $e_tu$, $ue_t$, $uu$ | the four squares, one per unit |
| what is the block? | the split of the array into two halves | a named projector, with no diagonal |
| where does a state come from? | a column in a chosen ideal | an element of $\mathbb{B}$ |
| what is the cost? | the direction travels with the formula | the block must be named |

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, $\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, complex dimension four |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the units, $e_t^2=e_t$ and $\vec e_k^2=-e_t$ |
| the four squares | $e_te_t$, $\vec e_x\vec e_x$, $\vec e_y\vec e_y$, $\vec e_z\vec e_z$; the diagonal cells of the coefficient basis, a set unchanged by a permutation of the three spatial units |
| $L_a$, $R_b$ | left and right multiplication, $L_a\tilde{Ξ}_{\mathrm{sp}}=a\tilde{Ξ}_{\mathrm{sp}}$ and $R_b\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp}} b$ |
| $L_aR_b$ | the two-sided operator, $L_aR_b\tilde{Ξ}_{\mathrm{sp}}=a\tilde{Ξ}_{\mathrm{sp}} b$ |
| $L_{\mathrm{axf}}(\tilde Q)$, $L_{\mathrm{pau}}(\tilde Q)$ | the left array of $\tilde Q$ in the axis-free and in the Pauli display; the label is a name, not an exponent |
| $L_{\mathrm{axf},e_\mu}$, $R_{\mathrm{axf},e_\mu}$ | the arrays of the units in the axis-free display |
| $C_{\Pi}$ | the change of basis from the coefficient basis to the Peirce frame, $\det C_{\Pi}=-\tfrac14$ |
| $\sigma_1,\sigma_2,\sigma_3$ | the Pauli matrices; the diagonal one is the mark of the declared unit |
| $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$ | the idempotents of the root, $\tilde\Pi_+\tilde\Pi_-=0$ and $\tilde\Pi_++\tilde\Pi_-=e_t$ |
| $\vec\Upsilon_\pm=\tfrac12(i\vec e_x\pm\vec e_y)$ | the mixed Peirce units, defined up to $\vec\Upsilon_+\mapsto\lambda\vec\Upsilon_+$, $\vec\Upsilon_-\mapsto\lambda^{-1}\vec\Upsilon_-$ |
| $\vec{Ζ}=i\vec e_z$ | the root, of square $e_t$; the direction the Peirce frame fixes |
| $\gamma_\mu[\mathbb{B}_{\Phi}]$ | the five frame cells, $iR_{\vec e_x}$, $iL_{\vec e_k}R_{\vec e_y}$ and $-iR_{\vec e_z}$; the frame is $\mathbb{B}_{\Phi}$ and the index is low |
| $\mathrm{axf}$ | the label of the coefficient basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ |
| $\mathrm{pau}$ | the label of the Pauli display, the Peirce frame of the root $i\vec e_z$ |
| $\langle\tilde Q\rangle_\natural$ | the natural norm, $Q_t^2+Q_x^2+Q_y^2+Q_z^2$; its square is the determinant of the left array |
| the chain | the constructions from the Pauli triplet to the two blocks, each used only where it is the subject |

## Further Reading

- [Conventions of the Matrix Models](matrix-representations-conventions.html), for the axis-free and Pauli arrays, the sixteen cells and the switch between them.
- [Conventions of the Frames](frame-and-metric-conventions.html), for the two frames, their coordinates and the gamma cells.
- [The Gamma Frame and the Complexified Dirac Algebra of $M_4(\mathbb{C})$](../articles_maths/the-gamma-frame-and-the-complexified-dirac-algebra-of-m4c.html), for the five cells as a generating set, the graded basis and the non-canonicity of the frame.
- [Element and Operator Representations: The Three Actions](element-and-operator-representations-the-three-actions.html), for the left and right actions, the sandwich and the vocabulary of the representations.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the Clifford algebra, its even part and the degree grading.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the Clifford algebra, the minimal left ideals and the representation of the gammas.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the geometric reading of the Dirac operator and the even subalgebra as the algebra of spacetime.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions," *Proceedings of the London Mathematical Society* **4** (1873) 381–395, for the biquaternion algebra and the word "rotor".
- Joe Harris, *Algebraic Geometry: A First Course*, Graduate Texts in Mathematics 133 (Springer, 1992), for the Segre variety, the Segre embedding and the rank-one determinantal variety.
