# __The Multi-Qubit Split, II: The Sign Condition, the Concurrence Form and the Central Bit__

## Introduction

Three objects are computed here, and they are one object seen three times. The pair of systems has a positivity condition that the single system cannot express, an entanglement measure that the single system cannot write, and a central bit that the single system does not possess. Each is a positive residue of the failure proved in [The Multi-Qubit Split, I](the-multi-qubit-split-i-the-antilinear-obstruction-and-the-corner-collapse.html): the label is gone, and what the label would have organised reappears as a constraint, a form, and a charge.

The positivity condition. Of the eight diagonal Hermitian candidates for a two-qubit state, exactly four are states. The four are selected by the sign condition $\epsilon_1\epsilon_2\epsilon_3=+1$, and the reason is group-theoretic: those four sign patterns are the four characters of the Klein four-group, and the other four are not.

The measure. The concurrence amplitude is the determinant of the coefficient array, and it is a quadratic form of split signature. It cannot be written as the expectation of an algebra element, and the proof is one line: a determinant scales by $e^{2i\theta}$ under a global phase, and an expectation does not.

The charge. Over $\mathbb{R}$ the tensor product doubles, and the doubling is split by a central involution. In the complex quotient that involution is the number $-1$. So the bit is not hidden; it is frozen, which is a different thing and a weaker one.

The order. *The eight diagonal candidates* sets up the computation. *The sign condition* proves it, with the group of order four as the reason. *The reduction is blind* shows that no partial trace sees the sign. *The second quadratic form* computes the concurrence and proves it is not an expectation. *The real tensor product* and *the physical summand* construct the central bit. *The count for $n$ factors* generalises. *Three residues of one failure* puts the three together.

The article uses [The Material-Informational Split as a Superselection Structure in Biquaternionic Form](the-material-informational-split-as-a-superselection-structure-in-biquaternionic-form.html) for the sectors, [The Multi-Qubit Split, I](the-multi-qubit-split-i-the-antilinear-obstruction-and-the-corner-collapse.html) for the obstruction and the corner collapse, [The Bell Basis as the Idempotent Basis of $\mathbb{B}\otimes\mathbb{B}$](the-bell-basis-as-the-idempotent-basis-of-b-tensor-b.html) for the four idempotents and the state vector, and [The Duo-Complex Bridge](the-duo-complex-bridge-the-three-canonical-forms-and-their-tensor-powers.html) for the identification of the concurrence with a canonical form of the duo-complex space. The two-summand structure over $\mathbb{R}$ is proved in the mathematics corpus under [The Tensor Product of Two Biquaternion Algebras](../articles_maths/the-tensor-product-of-two-biquaternion-algebras.html).

## The Eight Diagonal Candidates

**Why the diagonal ansatz is the natural one.** The two-qubit state must be a Hermitian element of $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}$ of trace one. The most economical candidates are the elements built from matched tensor products of the four units, because those are the elements that a product of two sector pictures would produce: informational times informational for the first pair of slots, material times material for the second. With the identity $e_t\otimes e_t=\mathrm I_4$ and the four material tensors $\vec e_{\imath}\otimes\vec e_{\imath}$ there are exactly eight such elements of trace one — the eight candidates of [The Bell Basis as the Idempotent Basis of $\mathbb{B}\otimes\mathbb{B}$](the-bell-basis-as-the-idempotent-basis-of-b-tensor-b.html), written there with the same letter $\tilde\Pi_{\mathrm{id}}$,

$$
\tilde\Pi_{\mathrm{id},\epsilon}=\tfrac14\Bigl(e_t\otimes e_t+\sum_{\imath\in\{x,y,z\}}\epsilon_{\imath}\,\vec e_{\imath}\otimes\vec e_{\imath}\Bigr),\qquad \epsilon_{\imath}=\pm1 ,
$$

each Hermitian, since $e_t\otimes e_t$ and each $\vec e_{\imath}\otimes\vec e_{\imath}$ are Hermitian, and each of trace one, since $\operatorname{tr}(e_t\otimes e_t)=4$ and $\operatorname{tr}(\vec e_{\imath}\otimes\vec e_{\imath})=\operatorname{tr}(\vec e_{\imath})^{2}=0$ because the quaternion units have vanishing scalar part.

What the eight are, in the Pauli model. With $e_t=\mathrm I_2$ and $\vec e_{\imath}=i\sigma_{\imath}$,

$$
\vec e_{\imath}\otimes\vec e_{\imath}=(i\sigma_{\imath})\otimes(i\sigma_{\imath})=-\sigma_{\imath}\otimes\sigma_{\imath},
$$

so

$$
\tilde\Pi_{\mathrm{id},\epsilon}=\tfrac14\Bigl(\mathrm I_4-\sum_{\imath\in\{x,y,z\}}\epsilon_{\imath}\,\sigma_{\imath}\otimes\sigma_{\imath}\Bigr).
$$

In this display the eight candidates are the eight ways of signing the three spin-spin correlation terms, which is what a reader expects: the diagonal candidates are the states whose correlations are extremal in all three directions.

Two of them are familiar. $\tilde\Pi_{\mathrm{id},(+,+,+)}$ is $\tfrac14(\mathrm I-\sigma_x\otimes\sigma_x-\sigma_y\otimes\sigma_y-\sigma_z\otimes\sigma_z)$, the projector onto the singlet, and $\tilde\Pi_{\mathrm{id},(-,-,-)}$ is the projector onto the triplet $|00\rangle$. Both have spectrum $(0,0,0,1)$ and both are pure. The other six are the subject of the next section.

## The Sign Condition

**The theorem.** $\tilde\Pi_{\mathrm{id},\epsilon}$ is a state, that is positive semidefinite, exactly when $\epsilon_1\epsilon_2\epsilon_3=+1$. In that case it is a rank-one projector and a Bell state. When $\epsilon_1\epsilon_2\epsilon_3=-1$ it has spectrum $(-\tfrac12,\tfrac12,\tfrac12,\tfrac12)$ and is not a state.

The four tensors form a group of order four. Put $B_{\imath}=\vec e_{\imath}\otimes\vec e_{\imath}$ and $A=e_t\otimes e_t=\mathrm I_4$. Then

$$
A^{2}=A,\qquad AB_{\imath}=B_{\imath} A=B_{\imath},\qquad B_{\imath}^{2}=A,
$$

and, for distinct $k,l$ with $m$ the third index,

$$
B_{\imath} B_l=B_lB_{\imath}=B_m .
$$

The first two lines are immediate. The third is the one that matters and it has a one-line reason: $B_{\imath} B_l=(\vec e_{\imath}\vec e_l)\otimes(\vec e_{\imath}\vec e_l)$, and the sign produced by $\vec e_{\imath}\vec e_l=\pm\vec e_m$ appears twice, once in each slot, so it squares to $+1$. Hence $B_{\imath} B_l=+\vec e_m\otimes\vec e_m=B_m$, and the same computation in the reverse order gives the same result because the two sign changes cancel together.

So $\{A,B_x,B_y,B_z\}$ is a group isomorphic to $\mathbb{Z}_2\times\mathbb{Z}_2$. The four elements are pairwise commuting involutions with $B_xB_y=B_z$ and cyclic. That is the Klein four-group, and the eight candidates are its four group elements with the four sign choices, that is the eight elements $\tfrac14(A+\sum_{\imath\in\{x,y,z\}}\epsilon_{\imath} B_{\imath})$ of the four-dimensional commutative algebra $\mathbb{R}[\mathbb{Z}_2\times\mathbb{Z}_2]$.

A character is exactly a sign pattern with product $+1$. A complex character of $\mathbb{Z}_2\times\mathbb{Z}_2$ assigns $\pm1$ to each of the three involutions consistently: $\chi(B_x)\chi(B_y)=\chi(B_z)$, which is $\epsilon_1\epsilon_2=\epsilon_3$, equivalently $\epsilon_1\epsilon_2\epsilon_3=+1$ because each sign is its own inverse. There are exactly four such patterns, namely $(+,+,+)$, $(+,-,-)$, $(-,+,-)$ and $(-,-,+)$, and they are the four characters of the group.

The projectors are the characters. For a character $\chi$ the element

$$
p_\chi=\tfrac14\sum_{g}\chi(g)\,g=\tfrac14\bigl(A+\chi(B_x)B_x+\chi(B_y)B_y+\chi(B_z)B_z\bigr)
$$

is idempotent, because the orthogonality of characters makes $p_\chi^{2}=p_\chi$, and it is Hermitian because every $g$ and every $\chi(g)$ is. Its trace is $\tfrac14\operatorname{tr}A=1$. So it is a rank-one projector, and the four of them are orthogonal and sum to $A$.

The other four are the complements. If $\epsilon_1\epsilon_2\epsilon_3=-1$ then $\epsilon'=-\epsilon$ satisfies $\epsilon'_1\epsilon'_2\epsilon'_3=+1$, and

$$
\tilde\Pi_{\mathrm{id},\epsilon}=\tfrac14\bigl(A-\textstyle\sum_{\imath\in\{x,y,z\}}\epsilon'_{\imath} B_{\imath}\bigr)=\tfrac12 A-p_{\epsilon'} ,
$$

since $\tfrac12A-p_{\epsilon'}=\tfrac12A-\tfrac14(A+\sum\epsilon'B)=\tfrac14(A-\sum\epsilon'B)$. A rank-one projector subtracted from $\tfrac12$ of the identity has spectrum $(-\tfrac12,\tfrac12,\tfrac12,\tfrac12)$. So the four remaining candidates are not states, and each is exactly one half of the identity minus one of the four states.

Everything is checked numerically. The eight spectra were computed: the four with product $+1$ gave $(0,0,0,1)$ and the four with product $-1$ gave $(-\tfrac12,\tfrac12,\tfrac12,\tfrac12)$, in exact agreement, with traces equal to one in all eight cases and Hermiticity to $10^{-16}$.

What the sign condition is and is not. It is not a superselection rule and not a constraint imposed from outside. It is the statement that the diagonal candidates split into the projectors of a four-group algebra and their complements, and that only the projectors are positive. The pair of systems offers four diagonal states where the single system offers two pure states on an axis, and the four are the four characters.

## The Reduction Is Blind

The partial trace kills every correlation term. For a two-qubit element $X$ the reduction to the first factor is the partial trace over the second. Every $B_{\imath}=\vec e_{\imath}\otimes\vec e_{\imath}$ has vanishing partial trace, because $\operatorname{tr}\vec e_{\imath}=0$, and $A$ has partial trace $\operatorname{tr}_{\!2}(e_t\otimes e_t)=2e_t$. Hence for every $\epsilon$,

$$
\operatorname{tr}_{\!2}\tilde\Pi_{\mathrm{id},\epsilon}=\tfrac14\cdot 2e_t=\tfrac12 e_t ,
$$

which is the maximally mixed one-qubit state.

**So all eight reduce to the same qubit.** Four of them are pure two-qubit states, four are not states at all, and the reduction cannot tell them apart. The sign lives entirely in the correlated terms, and the correlated terms are exactly the ones a partial trace discards.

The statement in the corpus's language. A reduction is a partial scalar part, and a partial scalar part of a tensor of two material factors vanishes. So the operation that recovers a subsystem from a joint element is, at this level, insensitive to the sector structure. This is the same blindness that [Spin Entropy and the Lorentz Group in Biquaternionic Form](spin-entropy-and-the-lorentz-group-in-biquaternionic-form.html) records from the other side: there the maximally mixed state is a fixed point of the unital channel, so the reduction carries no record of what the congruence did, and here the reduction carries no record of the sign.

Why this is a positive result and not a complaint. The blindness localises the sign. It says that the information distinguishing the four states from their four complements is not in either subsystem but in the correlation, and that a quantity which is a function of one subsystem cannot be the one that measures it. That is a statement about where to look, and the next section looks there.

## The Second Quadratic Form

The amplitude. Write a two-qubit state in the product basis as

$$
\lvert\tilde\Xi\rangle=c_{00}\lvert00\rangle+c_{01}\lvert01\rangle+c_{10}\lvert10\rangle+c_{11}\lvert11\rangle ,
$$

and put

$$
D(\psi)=c_{00}c_{11}-c_{01}c_{10}=\det\begin{pmatrix}c_{00}&c_{01}\\ c_{10}&c_{11}\end{pmatrix}.
$$

The concurrence is $C=2\lvert D\rvert$. The vanishing of $D$ is the rank-one condition on the coefficient array, hence the product-state condition; the normalised modulus is the entanglement measure.

The Bell-basis diagonalisation. With $\lvert b_{\imath}\rangle$ the four Bell states and $\psi=\sum_{\imath} b_{\imath}\lvert b_{\imath}\rangle$,

$$
2D(\psi)=b_1^{2}-b_2^{2}-b_3^{2}+b_4^{2},
$$

so the concurrence is the modulus of a quadratic form of inertia $(2,2)$ on the Bell-basis amplitudes. The biquaternion norm, by contrast, is $\sum_{\imath} c_{\imath}^{2}$ in the quaternion basis and $\sum_{\imath} b_{\imath}^{2}$ in the Bell basis, because the Bell transform is orthogonal; the two forms are different and the change of basis separates them.

The two forms are independent. They are not proportional: the norm has inertia $(4,0)$ on real amplitudes in its diagonal basis and the concurrence form has $(2,2)$, and inertia is a congruence invariant. So the two-qubit module carries two independent quadratic forms where the one-qubit module carries one, and the corpus's interval form is the one that does not measure entanglement.

**The concurrence amplitude is not an expectation.** Suppose that for some element $\tilde A$ of the algebra, acting on the module $\mathbb{C}^4$, one had $D(\psi)=\langle\psi\rvert\tilde A\lvert\psi\rangle$ for all $\psi$. Under a global phase $\psi\mapsto e^{i\theta}\psi$ the right side is unchanged, since $\langle e^{i\theta}\psi\rvert\tilde A\lvert e^{i\theta}\psi\rangle=\langle\psi\rvert\tilde A\lvert\psi\rangle$, while the left side becomes $e^{2i\theta}D(\psi)$. For $\theta=\pi/4$ the two differ unless $D(\psi)=0$. So no such element exists.

The same conclusion by the corpus's own route. On the module $\mathbb{C}^4\cong\mathbb{B}$ the concurrence amplitude requires the exchange of the two factors. The permutation that exchanges $\vec e_x$ and $\vec e_y$ and fixes $e_t$ and $\vec e_z$ is not a left multiplication: if it were, its value on $e_t$ would be the multiplier, hence the identity, and the identity fixes everything. So the measure needs the tensor structure and not the algebra. The two arguments agree, and the phase argument is the shorter one.

What survives of the algebra's role. The *modulus* $\lvert D\rvert$ is phase-invariant, and $C=2\lvert D\rvert$ is therefore not excluded by the argument above. What is excluded is that the amplitude itself be an expectation; the measure is a modulus of a bilinear pairing, and the pairing is the subject of [The Duo-Complex Bridge](the-duo-complex-bridge-the-three-canonical-forms-and-their-tensor-powers.html), where it is identified with the tensor square of the alternating form of the duo-complex space.

## The Real Tensor Product

Drop the identification. In $\mathbb{B}\otimes_{\mathbb{R}}\mathbb{B}$ the two central scalars are independent. Put

$$
\mathsf J=i\otimes i .
$$

Then $\mathsf J^{2}=i^{2}\otimes i^{2}=e_t\otimes e_t$, so $\mathsf J$ is an involution, and it is central because $i$ is central in each factor.

**Written $\mathsf J$ and not $J$, deliberately.** The element article uses $J$ for the complex structure $\tilde Q\mapsto i\tilde Q$ of one algebra. The two objects are different: $J$ is a real-linear map of $\mathbb{B}$, and $\mathsf J$ is an element of the tensor square. The sans-serif letter keeps them apart.

The two idempotents. Since $\mathsf J$ is a central involution,

$$
u=\tfrac12\bigl(e_t\otimes e_t+\mathsf J\bigr),\qquad v=\tfrac12\bigl(e_t\otimes e_t-\mathsf J\bigr),
$$

are central idempotents, orthogonal and summing to the identity. They are the two idempotents of the scalar extension $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$, tensored with the rest of the algebra.

The decomposition.

$$
\mathbb{B}\otimes_{\mathbb{R}}\mathbb{B}\;\cong\;(\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C})\otimes_{\mathbb{R}}(\mathbb{H}\otimes_{\mathbb{R}}\mathbb{H})\;\cong\;(\mathbb{C}\oplus\mathbb{C})\otimes_{\mathbb{R}}M_4(\mathbb{R})\;\cong\;M_4(\mathbb{C})\oplus M_4(\mathbb{C}).
$$

The real dimension is sixty-four, that is thirty-two over $\mathbb{C}$, two copies of sixteen. The centre is four-real-dimensional, spanned by $e_t\otimes e_t$, $i\otimes e_t$, $e_t\otimes i$ and $\mathsf J$; the two ideals $u(\mathbb{B}\otimes_{\mathbb{R}}\mathbb{B})$ and $v(\mathbb{B}\otimes_{\mathbb{R}}\mathbb{B})$ are each of real dimension thirty-two.

The check. Under $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\to\mathbb{C}\oplus\mathbb{C}$, $a\otimes b\mapsto(ab,\bar a b)$, the element $i\otimes i$ maps to $(-1,+1)$. So $\mathsf J$ has eigenvalue $-1$ on one summand and $+1$ on the other, and the idempotents $u,v$ project onto the two.

## The Physical Summand

The complex tensor product is one of the two. The quotient that defines $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}$ imposes $i\otimes e_t=e_t\otimes i$. On a summand where $\mathsf J=-1$ that relation holds: there the central elements $i\otimes e_t$ and $e_t\otimes i$ act as scalars $\alpha,\beta$ with $\alpha^{2}=\beta^{2}=-1$, and $\mathsf J=i\otimes i=(i\otimes e_t)(e_t\otimes i)$ acts as $\alpha\beta$, which is $-1$ exactly when $\beta=\alpha$. On the other summand $\mathsf J=+1$ and the relation fails, holding instead with the opposite sign, which is the tensor product with the conjugate algebra.

So the physical summand is the one where $v$ is the identity, that is $v=1$, $\mathsf J=-1$, $i\otimes e_t=e_t\otimes i$. The notation is easy to invert, so it is worth stating twice: $v=\tfrac12(e_t\otimes e_t-\mathsf J)$ selects the summand on which $\mathsf J=-1$, and that summand is the complex tensor product.

What the other summand is. It is the tensor square against the conjugate algebra: the algebra of pairs in which the second factor's scalar is conjugated. Its elements are the two-qubit operators built with the opposite convention for the second subsystem's imaginary unit — a legitimate algebra, not the one the corpus uses, and the one that composition would supply if the two subsystems were given independent scalars.

The frozen charge. Over $\mathbb{C}$ the involution $\mathsf J$ is the number $-1$, since $i\otimes i=i^{2}=-1$ in the quotient. So the choice of summand is not a choice: the quotient makes it once and for all, and no element of the complex algebra can detect it. The bit is not hidden by a superselection rule, since nothing commutes with everything and takes two values; it is frozen, because the algebra in which it would be a variable has been quotiented away.

**The distinction matters for what can be claimed.** A frozen quantity is a parameter of the description and not an observable. So the central bit is not a new degree of freedom of two qubits; it is the record of a choice that the complex description has already made. The next section states how many such choices there are for $n$ factors.

## The Count for $n$ Factors

The general decomposition. For $n$ factors, $\mathbb{C}^{\otimes_{\mathbb{R}}n}\cong\mathbb{C}^{2^{n-1}}$, and $\mathbb{H}^{\otimes n}\otimes_{\mathbb{R}}\mathbb{C}\cong M_{2^{n}}(\mathbb{C})$, because $\mathbb{H}^{\otimes n}$ is central simple of degree $2^{n}$ over $\mathbb{R}$ and complexification gives a full matrix algebra. Hence

$$
\mathbb{B}^{\otimes_{\mathbb{R}}n}\;\cong\;\bigoplus_{k=1}^{2^{n-1}}M_{2^{n}}(\mathbb{C}),
$$

of real dimension $2^{3n}$: sixty-four at $n=2$, five hundred and twelve at $n=3$.

The alignment reading. The $2^{n-1}$ summands are the $2^{n-1}$ ways of aligning the $n$ central scalars up to a global sign. The complex tensor product is the summand in which all $n$ agree, and exactly one summand has that property. So the freedom is $n-1$ bits, and the physical description uses one value of them.

Two counts, and they must not be confused. The sector grading of [The Multi-Qubit Split, I](the-multi-qubit-split-i-the-antilinear-obstruction-and-the-corner-collapse.html) keeps one bit out of $2^{n}$ patterns: the parity of the number of material factors. The summand count keeps $n-1$ bits out of the alignment. The first is a statement about the star, the second about the central scalars, and they are different invariants of the same algebra. Both are exact.

**Why the count is not physics.** No experiment can read $n-1$ bits of alignment, because the complex description has already fixed them. What the count says is how much structure the real algebra has that the complex one discards, and it is the honest measure of what refusing the quotient would buy.

## Three Residues of One Failure

**The failure.** One sentence: the partial star does not descend, so the pair has no per-subsystem label.

The first residue is a constraint. Because the corners collapse, the diagonal candidates are the elements of a four-group algebra, and positivity selects the four characters. A label would have said *this term is informational and that one material*; the constraint says *these four sign patterns are states and those four are not*. The information is not lost; it is converted from a name into an inequality.

The second residue is a form. Because the corners collapse onto the Hermitian part, the second quadratic form lives in the same space as the first, and the two are independent. A label would have separated them by sector; the collapse makes them two forms on one space, of inertia $(4,0)$ and $(2,2)$, and the second measures entanglement.

The third residue is a charge. Because the collapse is a consequence of $i\otimes i=-1$, the element $i\otimes i$ is a central involution of the real algebra and the number $-1$ in the complex one. A label would have given $2^{n}$ sectors; the collapse gives two, and the doubling over $\mathbb{R}$ gives the alignment of scalars as the object that produced the collapse in the first place.

The pattern. Each residue is a place where a name became a number: state or not a state, positive or indefinite, aligned or anti-aligned. That is what happens when a structure is quotiented: the distinctions that survive appear as values of invariants rather than as members of a list.

## Summary

The eight diagonal Hermitian candidates $\tilde\Pi_{\mathrm{id},\epsilon}=\tfrac14(e_t\otimes e_t+\sum_{\imath\in\{x,y,z\}}\epsilon_{\imath}\vec e_{\imath}\otimes\vec e_{\imath})$ are the elements of the Klein four-group algebra spanned by $e_t\otimes e_t$ and the three $\vec e_{\imath}\otimes\vec e_{\imath}$, because the sign twist of the quaternion product squares away in a tensor square. Positivity selects exactly the four sign patterns that are characters, $\epsilon_1\epsilon_2\epsilon_3=+1$, which are the four Bell projectors; the other four are $\tfrac12-p$ and have spectrum $(-\tfrac12,\tfrac12,\tfrac12,\tfrac12)$. All eight reduce to $\tfrac12e_t$, so no partial trace sees the sign. The concurrence amplitude $D=c_{00}c_{11}-c_{01}c_{10}$ is a quadratic form of inertia $(2,2)$, independent of the biquaternion norm, and it is not the expectation of any algebra element, because it scales by $e^{2i\theta}$ under a global phase while an expectation does not. Over $\mathbb{R}$ the tensor product is $M_4(\mathbb{C})\oplus M_4(\mathbb{C})$, split by the central involution $\mathsf J=i\otimes i$ into the summands of $u=\tfrac12(1+\mathsf J)$ and $v=\tfrac12(1-\mathsf J)$; the complex tensor product is the summand where $\mathsf J=-1$, selected by $v$, and there the bit is frozen rather than hidden. For $n$ factors there are $2^{n-1}$ summands, and the physical description fixes one.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\tilde\Pi_{\mathrm{id},\epsilon}$ | the eight diagonal Hermitian candidates, of trace one |
| $B_{\imath}=\vec e_{\imath}\otimes\vec e_{\imath}$ | the three material tensors; $B_{\imath}^{2}=e_t\otimes e_t$ and $B_{\imath} B_l=B_m$ |
| $\epsilon_1\epsilon_2\epsilon_3=+1$ | the sign condition; the four characters of $\mathbb{Z}_2\times\mathbb{Z}_2$ |
| $\tfrac12 e_t-p$ | the form of the four non-positive candidates |
| $\operatorname{tr}_{\!2}\tilde\Pi_{\mathrm{id},\epsilon}$ | the reduction, equal to $\tfrac12e_t$ in all eight cases |
| $D=c_{00}c_{11}-c_{01}c_{10}$ | the concurrence amplitude; $C=2\lvert D\rvert$ |
| $b_1^{2}-b_2^{2}-b_3^{2}+b_4^{2}$ | $2D$ in the Bell basis, inertia $(2,2)$ |
| $\mathsf J=i\otimes i$ | the central involution of the real tensor product |
| $u=\tfrac12(1+\mathsf J)$, $v=\tfrac12(1-\mathsf J)$ | the two central idempotents; $v$ selects the physical summand |
| $2^{n-1}$ | the number of summands of $\mathbb{B}^{\otimes_{\mathbb{R}}n}$ |

## Further Reading

In this category. [The Multi-Qubit Split, I](the-multi-qubit-split-i-the-antilinear-obstruction-and-the-corner-collapse.html) proves the obstruction and the collapse used here. [Composite Systems and the Multi-Qubit Extension](composite-systems-and-the-multi-qubit-extension.html) places the central bit among the things only the algebra route would supply. [The Duo-Complex Bridge](the-duo-complex-bridge-the-three-canonical-forms-and-their-tensor-powers.html) identifies $2D$ with the tensor square of the alternating form of the duo-complex space, which is the reason the concurrence exists at all. [The Bell Basis as the Idempotent Basis of $\mathbb{B}\otimes\mathbb{B}$](the-bell-basis-as-the-idempotent-basis-of-b-tensor-b.html) gives the four idempotents that the sign condition reproduces and the state-vector identification used for the coefficient array. [Spin Entropy and the Lorentz Group in Biquaternionic Form](spin-entropy-and-the-lorentz-group-in-biquaternionic-form.html) is the entropy as a function of the reduction, hence the example of what the blindness excludes.

In the mathematics corpus. [The Tensor Product of Two Biquaternion Algebras](../articles_maths/the-tensor-product-of-two-biquaternion-algebras.html) proves the two-summand decomposition, the central involution and the alignment count. [The Three Canonical Forms on $\mathbb{C}^2$](../articles_maths/the-three-canonical-forms-on-c2.html) supplies the alternating form whose tensor square is the concurrence.
