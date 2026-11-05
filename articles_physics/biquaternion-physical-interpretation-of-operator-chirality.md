# __Biquaternion Physical Interpretation of Operator Chirality__

## Introduction

**The question.** What does the operator chirality of the biquaternion algebra predict, and what does it leave to physics?

**The answer in one line.** The chirality operator of a frame is a pure right multiplier, $\mathsf{V}^{\mathrm{vol}}=-iR_{\vec e_z}$ in the axis-free frame; the Dirac operator is a pure left multiplier; the two commute because they sit on opposite sides; and the mass is the one term of the equation that has no side at all.

**What this article does.** It restates the mathematics in the form a physicist reads, identifies the operator with the $\gamma_5$ of the Dirac equation, and states what the algebra does not supply. The proofs are in *Operator Chirality on the Biquaternion Algebra*, one click away, and nothing here is proved twice.

**What it does not do.** It does not derive a gauge group, a matter content or a mass value. It does not claim that the sides are two inequivalent representations of the Lorentz group: they are not, and §*What the Algebra Does Not Supply* states that limit in full.

**The order of the article.** Section §*Operator Chirality in One Page* gives the definition and the dimensions. Section §*The Chirality Operator Is Gamma Five* identifies the operator and its four properties. Section §*The Dirac Equation Reads the Sides* shows what the sides do to the equation and where the mass sits. Section §*The Eight Objects the Physics Does Not Need* takes the list of unrelated mathematical objects and states, for each, the physical reason it is not needed. Section §*What the Earlier Reading Adjoined* records the route this article replaces, and §*What the Algebra Does Not Supply* records the one thing the replacement does not buy.

**Conventions.** The algebra, the cells and the two slots are those of *Algebra and Element Conventions* and *Operator Family Conventions*; the frame cells $\gamma_0,\dots,\gamma_3$, the gradient and the array rule are those of *Matrix Representations Conventions* and *Operator and Calculus Conventions*, and none is redefined here. This article's own glyph is the chirality cell of the axis-free frame, $\mathsf{V}^{\mathrm{vol}}=-iR_{\vec e_z}$, printed as $\mathsf{V}^{\mathrm{vol}}$ throughout.

## The Results It Uses

| Mathematical Content | Source |
| --- | --- |
| The two slots, the two one-sided families and their dimensions | [Operator Chirality on the Biquaternion Algebra](../articles_maths/operator-chirality-on-the-biquaternion-algebra.html) |
| The chirality operator as the volume cell, a pure right multiplier | same |
| The list of eight objects the notion does not need | same |
| The swap $\sigma(L_aR_b)=L_bR_a$ and the conjugation $\mathsf C\,L(a^{\natural})\,\mathsf C=R(a)$ | same |
| The cells as a basis, the coefficient matrix and the length | [$M_4(\mathbb{C})$ Axis-Free Representation : Operators](../articles_maths/m4c-axis-free-representation-operators.html) |
| The regular module, its two minimal left ideals and the carrier | [The Unpolarized Module of the Biquaternion Algebra](../articles_maths/the-unpolarized-module-of-the-biquaternion-algebra.html) |
| The conjugate module and its inequivalence to $S$ | [The Unpolarized Module of the Biquaternion Algebra](../articles_maths/the-unpolarized-module-of-the-biquaternion-algebra.html) |
| The chiral pair of the Dirac equation and its two-sided variant | [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html) |
| The two forms of the equation on the algebra, and the statement that the pair needs no carrier beyond the algebra | [The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism](the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html) |

## Operator Chirality in One Page

**The definition.** An operator of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ is a sum of cells, and a cell has two slots: the left one, where $a$ multiplies, and the right one, where $b$ multiplies. Operator chirality is the slot: the left slot for a pure left multiplier, the right slot for a pure right multiplier, both slots otherwise.

**The dimensions.** The two families are four-dimensional each, they overlap in the scalars, and their sum is seven-dimensional inside the sixteen-dimensional endomorphism algebra:

| Space | Dimension | Physical reading |
| --- | --- | --- |
| $L(\mathbb{B})$ | $4$ | the operators that multiply on the left |
| $R(\mathbb{B})$ | $4$ | the operators that multiply on the right |
| $L\cap R$ | $1$ | the scalars, which multiply on both sides and have no side |
| $L+R$ | $7$ | the one-sided operators |
| $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ | $16$ | all operators; the other nine directions have both slots |

**What this buys physically.** Two facts that the older routes obtained after adjoining a root and complexifying the algebra are here obtained from the frame alone. The chirality operator exists, and its side is forced rather than chosen: among the one-sided operators of the frame, only the right multipliers square to the identity and anticommute with the four generators, while the left candidates $\pm iL_{\vec e_z}$ fail the anticommutation. Nothing is adjoined, no root is chosen, no module is declared.

**What it costs.** Nothing is said about states. The slot is a property of an operator, and §*The Dirac Equation Reads the Sides* shows how that property reaches the equation.

## The Chirality Operator Is Gamma Five

**The identification.** The product of the four generators is a cell, and it is the chirality operator:
$$
\mathsf{V}^{\mathrm{vol}}=i\gamma_0\gamma_1\gamma_2\gamma_3=-iL_{e_t}R_{\vec e_z}=-iR_{\vec e_z},
$$
the last equality because $L_{e_t}=\mathrm I$. It is the cell that the Dirac literature calls $\gamma_5$, written with no matrix.

**Its properties.** Four, each verified by multiplying cells:

| Property | Value | Physical reading |
| --- | --- | --- |
| square | $(\mathsf{V}^{\mathrm{vol}})^2=\mathrm I$ | an involution, so a chirality |
| trace | $\operatorname{tr}\mathsf{V}^{\mathrm{vol}}=0$ | the two chiral halves are of equal size |
| spectrum | $+1$ and $-1$, two dimensions each | two chiral components, two states each |
| with the frame | $\{\gamma_\mu,\mathsf{V}^{\mathrm{vol}}\}=0$ | the frame is odd under the right multiplication by $\vec e_z$ |

**The side, which is the point of the article.** $\mathsf{V}^{\mathrm{vol}}$ multiplies on the **right**. The gradient multiplies on the **left**. This is not a detail of notation: it is the reason the two operators commute,
$$
L(a)\,R(b)=R(b)\,L(a)\quad\text{for all }a,b,
$$
so that
$$
[\,L(\tilde\nabla),\mathsf{V}^{\mathrm{vol}}\,]=0 .
$$
A left multiplier and a right multiplier never fail to commute. The chirality operator and the Dirac operator are the two sides of the same algebra, and their commutation is a consequence of the sides, not a computation about gammas.

**The chirality of a field.** Since $\mathsf{V}^{\mathrm{vol}}$ is an operator on $\mathbb{B}$, every biquaternion splits into two chiral halves,
$$
\tilde{Ξ}^{\mathrm{spn}}=\tilde{Ξ}^{\mathrm{spn}}_++\tilde{Ξ}^{\mathrm{spn}}_-,\qquad \mathsf{V}^{\mathrm{vol}}\tilde{Ξ}^{\mathrm{spn}}_\pm=\pm\tilde{Ξ}^{\mathrm{spn}}_\pm,
$$
with $\tilde{Ξ}^{\mathrm{spn}}_\pm=\tfrac12(\mathrm I\pm\mathsf{V}^{\mathrm{vol}})\tilde{Ξ}^{\mathrm{spn}}$. The two halves are two-dimensional over $\mathbb{C}$ and each is closed under left multiplication, so each is a copy of the simple left module $S$. That sentence is the whole physical content and the whole physical limit of the construction: the halves exist, and they are copies. §*What the Algebra Does Not Supply* takes it up.

## The Dirac Equation Reads the Sides

**The equation.** The biquaternion Dirac equation is the chiral pair
$$
\tilde\nabla\tilde{Ξ}^{\mathrm{spn}}_R=m\tilde{Ξ}^{\mathrm{spn}}_L,\qquad \tilde\nabla^{\natural}\tilde{Ξ}^{\mathrm{spn}}_L=m\tilde{Ξ}^{\mathrm{spn}}_R,
$$
in which both operators act by left multiplication: the first by $\tilde\nabla$, the second by its natural conjugate $\tilde\nabla^{\natural}$. The conjugation is what relates the two, and its identity is the one of the mathematics article,
$$
\mathsf C\,L(a^{\natural})\,\mathsf C=R(a),
$$
so the conjugate member of the pair is the same operator read on the other side. Nothing else is used: no carrier, no splitting of a carrier, no projector, no idempotent, no ideal. This is the point recorded where the corpus separates its three forms of the equation — the pair written on the algebra holds without any choice of module.

**The massless case, and the chirality split.** At $m=0$ the pair decouples into $\tilde\nabla\tilde{Ξ}^{\mathrm{spn}}_R=0$ and $\tilde\nabla^{\natural}\tilde{Ξ}^{\mathrm{spn}}_L=0$. For a null gradient the solution space of either member is two-dimensional over $\mathbb{C}$, and $\mathsf{V}^{\mathrm{vol}}$ acts on it with the two eigenvalues $+1$ and $-1$, one state each. So a massless biquaternion Dirac field carries **one state of each chirality**, which is the standard statement that a massless Dirac fermion has both helicities. The mechanism is the commutation above: the solution space is stable under $\mathsf{V}^{\mathrm{vol}}$, so a solution of definite chirality can be chosen.

**Why the two displays do not conflict.** In the Clifford display the Dirac operator anticommutes with $\mathsf{V}^{\mathrm{vol}}$; in the cell display it commutes, because a left multiplier commutes with a right one. The two are consistent and they say the same physical thing from opposite sides. Anticommutation means the operator exchanges the two halves of the space it acts on; commutation means it preserves the two halves of $\mathbb{B}$. In both displays the conclusion for a solution is identical: if $\tilde{Ξ}^{\mathrm{spn}}$ is a massless solution then $\mathsf{V}^{\mathrm{vol}}\tilde{Ξ}^{\mathrm{spn}}$ is one too, so the solution space is stable under the chirality operator and the two signs are available on it. The physical statement is therefore independent of the display, which is what the operator reading is for.

**The mass is the term with no side.** The mass term multiplies the field by the scalar $m$, and a central scalar is the one operator that is simultaneously a left multiplier and a right multiplier. It is therefore the only term of the equation that has no side, and it is exactly the term that couples the two sides. The algebra says this without any computation: a term that couples the sides cannot itself belong to one of them.

| Term | Multiplier | Slot |
| --- | --- | --- |
| $\tilde\nabla\tilde{Ξ}^{\mathrm{spn}}_R$ | left by $\tilde\nabla$ | left |
| $\tilde\nabla^{\natural}\tilde{Ξ}^{\mathrm{spn}}_L$ | left by the conjugate | left |
| $m\tilde{Ξ}^{\mathrm{spn}}$ | central scalar | both, hence no side |

## The Eight Objects the Physics Does Not Need

**The list.** The mathematics article separates operator chirality from eight objects. The table repeats the separation and states, for each object, what a physicist would otherwise think it is doing.

| Object | What a physicist might expect it to do | Why the physics does not need it |
| --- | --- | --- |
| a root | supply the axis along which chirality is defined | the axis is the frame's third direction, declared with the frame |
| an idempotent | supply a state or a superselection sector | the chirality operator is an involution, $(\mathsf{V}^{\mathrm{vol}})^2=\mathrm I$, not a projector |
| a Peirce decomposition | supply the two chiral halves | the halves are the eigenspaces of one operator, not four corners of two idempotents |
| a Peirce basis | supply the working basis | a basis is a display; the side is read without one |
| a spinor | supply the object that carries chirality | the operator is defined before any ideal is chosen |
| a Pauli matrix | supply $\mathsf{V}^{\mathrm{vol}}$ | the same operator is the single cell $-iR_{\vec e_z}$ |
| an ideal | supply the state space | the state space is $\mathbb{B}$ itself, and no point of a projective line is chosen |
| a Clifford algebra | supply the anticommutation $\{\gamma_\mu,\mathsf{V}^{\mathrm{vol}}\}=0$ | the anticommutation holds for five cells; it is computed, not postulated |

**No root.** A root $\tilde{Ζ}$ with $\tilde{Ζ}^2=e_t$ is a direction chosen in the algebra, and it is needed when a Peirce decomposition is wanted. The frame's third direction already fixes the operator, so nothing further is chosen. A change of root changes the Peirce data and leaves $\mathsf{V}^{\mathrm{vol}}$ untouched.

**No idempotent.** An idempotent satisfies $\tilde\Pi^2=\tilde\Pi$, and it is the algebraic form of a projection, hence of a state-preparation. $\mathsf{V}^{\mathrm{vol}}$ satisfies $(\mathsf{V}^{\mathrm{vol}})^2=\mathrm I$ and is not a projection: it is a sign, and a sign is not a state. The projectors $\tfrac12(\mathrm I\pm\mathsf{V}^{\mathrm{vol}})$ are built from it when a projection is wanted, and they are derived objects.

**No Peirce decomposition and no Peirce basis.** A Peirce decomposition needs two idempotents and returns four lines. The chiral splitting is one operator and returns two halves. Four lines and two halves are not the same partition, and the difference is measurable: the Peirce lines are one-dimensional corners of $\mathbb{B}$, and the chiral halves are two-dimensional left modules.

**No spinor.** A spinor is an element of a minimal left ideal, which is produced by a rank-one idempotent, which is a point of a projective line. The chirality operator is defined before any point is chosen, and it is defined on the whole algebra.

**No Pauli matrix.** The Pauli display is the tensor factorisation $\mathbb{C}^2\otimes\mathbb{C}^2$, and the Pauli matrices are the arrays of the cells in that display. The operator exists in the axis-free frame as the single cell $-iR_{\vec e_z}$ and looks the same in the Pauli frame. The display is a convenience for printing; the side is not.

**No ideal.** The minimal left ideals of $\mathbb{B}$ are indexed by the points of a projective line, and no point is distinguished. An operator that multiplied on one side and selected a point would be an ideal in disguise. $\mathsf{V}^{\mathrm{vol}}$ selects nothing: it multiplies, and its eigenspaces exist in every frame.

**No Clifford algebra.** This deserves a paragraph of its own, because the Clifford reading is the one a physicist is most likely to reach for. A Clifford algebra is generated by vectors with $\{e_i,e_j\}=2g_{ij}$, and in it $\mathsf{V}^{\mathrm{vol}}$ is the product of the generators by construction. In the biquaternion algebra the relation holds as an identity of five cells, verified by multiplying them, and it is not an axiom. What it fixes is squares and anticommutators; what operator chirality needs is the side, and the relation says nothing about sides. A Clifford algebra also fixes a dimension and a signature, while the sides exist in every dimension. So the Clifford reading is a display of the same algebra, and it is a correct display; it is not a foundation, and nothing in the physics is derived from it that the cells do not already give.

**Why no anticommutation can give the sign.** It is worth stating the reason, because it explains why the side is the right notion and not merely an available one. If the chirality operator were characterised by anticommuting with the frame, it would have to anticommute with $L(e_t)$, which is the identity, and an operator anticommuting with the identity is zero. There is no such operator. The sign in this algebra is not produced by an anticommutator; it is produced by the side.

## What the Earlier Reading Adjoined

**The earlier route.** An earlier reading of this article took the chirality to be the central sign of the conjugate pair. That route adjoins a root of $-1$ to $\mathbb{B}_{\mathbb{R}}$, complexifies to $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B}_{\mathbb{R}}\cong\mathbb{B}\oplus\mathbb{B}$, takes the central idempotents
$$
e_\pm=\tfrac12(1\pm i\tilde{Ζ}_{\mathrm{ad}}),\qquad \chi=i\tilde{Ζ}_{\mathrm{ad}}=e_+-e_-,
$$
and reads $\xi$ on the Dirac module $\Delta=S\oplus S^{\mathrm{c}}$ as $\operatorname{diag}(-I_2,I_2)$.

**What it got right.** The array. The operator chirality is the same cell,
$$
\mathsf{V}^{\mathrm{vol}}=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=-iR_{\vec e_z}^{\mathrm{axf}}=\rho(\xi),
$$
whose Peirce array is $\operatorname{diag}(-I_2,I_2)$ — the section that reads it in that display is §*The Legacy Pauli Gamma Formulation* — and whose axis-free array is a signed permutation. The two readings agree on every number they print.

**What it cost.** Three structures that the physics does not need: an adjoined root, a complexification of the real algebra, and a declaration of a module. Each of them is a choice, and each of them is invisible in the array, which is why the two readings were taken for one another for as long as they were.

**The relation between them.** The Peirce sign of the root aligned with the third axis is $P=R_{i\vec e_z}=-\mathsf{V}^{\mathrm{vol}}$, and the projector of the aligned Peirce idempotent is
$$
R(\tilde\Pi_+)=\tfrac12(\mathrm I+P)=\tfrac12(\mathrm I-\mathsf{V}^{\mathrm{vol}}),
$$
so for that one root the Peirce projector and the chiral projector are the same operator. For any other root they are not. The coincidence is a coincidence of arrays for one root out of a projective line, and stating it as a coincidence rather than as an identity is what removes the need for the root.

## What the Algebra Does Not Supply

**The halves are copies.** This is the limit that no amount of operator bookkeeping removes, and it must be stated plainly. The two chiral halves of $\mathbb{B}$ are two-dimensional and each is stable under left multiplication, so each is isomorphic to the simple left module $S$. The grading is therefore a grading between **two copies** of one Lorentz module, and a gauge action by left multiplication acts identically on the two. In the language of the Standard Model it is vector-like.

**What the physics needs instead.** The Standard Model chirality distinguishes two **inequivalent** Lorentz modules: the left-handed Weyl spinor $S$ and its conjugate $S^{\mathrm{c}}$. Those two are not two copies of one module, and the biquaternion algebra contains only the first. The distinction is a property of the pair $S\oplus S^{\mathrm{c}}$, and it is the content of *The Unpolarized Module of the Biquaternion Algebra*.

**So what has been gained.** The operator chirality supplies, without adjoining anything, the object that the physics calls $\mathsf{V}^{\mathrm{vol}}$: an involution of the algebra, of trace zero, with two equal halves, commuting with the Dirac operator and anticommuting with the frame. That is what a Lagrangian needs in order to write a chiral projector, a chiral current or an axial anomaly coefficient. What it does not supply is the inequivalence of the two halves, and no operator of $\mathbb{B}$ can supply it, because every operator of $\mathbb{B}$ grades copies.

**A biquaternion field.** A field $\tilde{Ξ}^{\mathrm{spn}}\in\mathbb{B}$ therefore does carry a chirality, in the precise sense that $\mathsf{V}^{\mathrm{vol}}\tilde{Ξ}^{\mathrm{spn}}_\pm=\pm\tilde{Ξ}^{\mathrm{spn}}_\pm$; and both halves are left-handed in the Lorentz sense, since both are copies of $S$. A reader who wants the Standard Model pair must pass to $\Delta=S\oplus S^{\mathrm{c}}$, where the same array grades two inequivalent modules and the same operator does the physical work.

## Limits

- **No derivation of the gauge group.** The algebra supplies the chirality operator; it does not supply the Standard Model gauge group, its representations or its breaking pattern.
- **No inequivalent chiral pair.** Both halves of $\mathbb{B}$ are copies of $S$; the inequivalence of $S$ and $S^{\mathrm{c}}$ is a statement about the conjugate module, not about the algebra.
- **No matter content and no generations.** The number of copies is an input.
- **No mass value and no spectrum.** The algebra fixes the slot of the mass term, which is the centre, and the number $m$ is dynamical.
- **No dynamics.** Nothing here says how a field moves between the sides.
- **The left/right naming is a convention.** Which half is called left is fixed by the sign in $\mathsf{V}^{\mathrm{vol}}=-iR_{\vec e_z}$; exchanging the name changes nothing.
- **The frame is still a choice.** $\mathsf{V}^{\mathrm{vol}}$ is the volume cell of a declared frame; a different frame gives a different fifth cell and the same algebra.
- **No claim that the Clifford reading is wrong.** It is a correct display of the same operators, and the article says where it stops being a foundation.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, and the frame is named on the coordinate.

**What the frame is.** The gammas are a frame of the algebra, five cells of the sixteen, and not a different algebra. In that frame the chirality operator, the side and the split read as follows.

| Statement | In cells | In the gamma frame |
| --- | --- | --- |
| the chirality operator | $-iR_{\vec e_z}$ | $\mathsf{V}^{\mathrm{vol}}=i\gamma_0\gamma_1\gamma_2\gamma_3$ |
| its side | right | the fifth generator of the frame |
| the Dirac operator | $L(\tilde\nabla)$ | $i\gamma^\mu\,\partial/\partial x_\mu$ in the Clifford display |
| their relation | commutation, because the sides differ | anticommutation in the Clifford display |
| the mass | a central scalar, no side | the term that couples the halves |

**The display.** Where this article prints an array it prints both displays: the Peirce one, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and the axis-free one after it, labelled $\mathrm{axf}$, which is the display of the body. The body of the article writes the same operators in the axis-free display, and the change of display is a conjugation, $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, which preserves every product, every trace and every determinant. A statement about the side is therefore a statement about both displays at once, and an array is a statement about one.

## Summary

Operator chirality is the side on which an operator multiplies. The chirality operator of a frame is its volume cell, $\mathsf{V}^{\mathrm{vol}}=i\gamma_0\gamma_1\gamma_2\gamma_3=-iR_{\vec e_z}$, a pure right multiplier, while the Dirac operator is the pure left multiplier $L(\tilde\nabla)$; the two commute, because a left multiplier never fails to commute with a right one, and that commutation is why a massless field carries states of both chiralities. The mass is the central scalar, the one term of the equation with no side, and therefore the term that couples the two.

The construction needs none of the eight objects that usually carry the name: no root, no idempotent, no Peirce decomposition, no Peirce basis, no spinor, no Pauli matrix, no ideal and no Clifford algebra. Each of them enters the older route as a choice, and each of them is invisible in the array, which is why the arrays were mistaken for the notion. The array of $\mathsf{V}^{\mathrm{vol}}$ is the same in every reading; the structures that were adjoined to obtain it are not needed to obtain it.

The limit is stated once and it is not small: the two chiral halves of $\mathbb{B}$ are copies of one Lorentz module, so the grading of the algebra is vector-like, and the inequivalence of $S$ and $S^{\mathrm{c}}$ that the Standard Model uses is a property of the conjugate module rather than of $\mathbb{B}$.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $L_aR_b$ | the cell, $L_aR_b\tilde X=a\tilde Xb$, with a left and a right slot |
| left slot, right slot, both slots | operator chirality |
| $\tilde\nabla$ | the biquaternion gradient, acting by left multiplication |
| $\tilde\nabla^{\natural}$ | its natural conjugate, related to the other side by $\mathsf C L(a^{\natural})\mathsf C=R(a)$ |
| $\mathsf{V}^{\mathrm{vol}}=-iL_{e_t}R_{\vec e_z}=-iR_{\vec e_z}$ | the chirality operator of the frame, a pure right multiplier |
| $\tfrac12(\mathrm I\pm\mathsf{V}^{\mathrm{vol}})$ | the chiral projectors, derived from the sign |
| $\tilde{Ξ}^{\mathrm{spn}}_\pm$ | the two chiral halves of a biquaternion field |
| $S$ | the simple left module; both halves of $\mathbb{B}$ are copies of it |
| $S^{\mathrm{c}}$ | the conjugate module, inequivalent to $S$ over $\mathbb{C}$ |
| $\Delta=S\oplus S^{\mathrm{c}}$ | the Dirac module, where the same array grades two inequivalent modules |
| $P=R_{i\vec e_z}=-\mathsf{V}^{\mathrm{vol}}$ | the Peirce sign of the aligned root, a coincidence of arrays |
| $m$ | the mass, the central scalar of the equation |
| $\mathrm{pau}$, $\mathrm{axf}$ | the Peirce and axis-free displays of the same operators |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- [Operator Chirality on the Biquaternion Algebra](../articles_maths/operator-chirality-on-the-biquaternion-algebra.html), for the definition, the dimensions, the swap, the conjugation and the list of unrelated objects.
- [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html), for the chiral pair, the one-sided and the two-sided equation, and the plane-wave solutions.
- [The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism](the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html), for the two forms of the equation and the gauge covariance of the pair on the algebra.
- [The Unpolarized Module of the Biquaternion Algebra](../articles_maths/the-unpolarized-module-of-the-biquaternion-algebra.html), for the inequivalence of $S$ and $S^{\mathrm{c}}$, the pairing and the mass operator on $\Delta$; the regular module, its minimal left ideals and the carrier.
- [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html), for the chiral projectors and the mass selection rule in the physics corpus.
- [The Two Chiralities of $M_4(\mathbb{C})$](../articles_maths/the-two-chiralities-of-m4c.html), for the comparison with the matrix case.
