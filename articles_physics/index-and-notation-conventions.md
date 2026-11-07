# __Index and Notation Conventions__

## Introduction

These are the conventions of the marks and of the labels. They assume the base of *Algebra and Element Conventions* and the operators of *Operator and Calculus Conventions*.

The order is from the mark to the label. The marks come first, which say what a caret carries and what a subscript carries. Then the labels, every one of them low, and the few of this corpus among them. Then the subscript itself, which counts or names and is never a derivative.

## The Upper and Low Marks

**These rules are real, and partial.** They fix the marks of the common uses and they bind wherever they apply. They do not cover every use: a mark that falls outside them is governed by the section that fixes it, and a stricter rule stated in the corpus overrides them — the derivation convention of *Operator and Calculus Conventions*, §*Conventions for Derivation*, the Fock and opposite tokens of §*The Labels*, and the forms of §*The Subscripts*.

**A caret carries four things and no label:**

- a power, $2^k$, $e^\lambda$, $(-1)^j$, $\alpha^k$, $2^{k/2-1}$;
- a conjugation, $a^{*}$, $a^{\dagger}$, $a^{\natural}$;
- a transposition, $L^T$, $\tilde{Ξ}_{\mathrm{sp}}^T$;
- a construction, $\mathbb{B}^\times$, $S^{\otimes n}$, $\mathrm{sym}^l$, $\Lambda^kTM$ (degree).

**A subscript carries one of two things: an index or a label.**

- an index — a numeric count, $Q_1$, $M_2$; the slot of a coordinate, $q_i$, $x_i$, $p_i$, $Q_i$, $\theta_i$, $\zeta_k$, $v_i$; the slot of a basis vector or a gamma, $\vec e_i$, $\gamma_i$; the slots of an invariant symbol, $\delta_{ij}$, $\varepsilon_{ijk}$, $\eta_{ij}$; the generator of a gauge, colour, isospin or spin family, $T_a$, $G_a$, $\sigma_z$; the slot of a connection or curvature component, $\Gamma_k$, $\mathrm{Ric}_{ij}$, $\omega_i$, $g_{ij}$; the slot of a differential, $dx_i$.
- a label naming the object, a part of it or a role of it, $E_{\mathrm{wkb}}$, $s_{\mathrm{tot}}$, $S_{\mathrm{int}}$, with every label of §*The Labels*; the label comes first in the subscript and an index already there follows it after a comma, $T_{\mathrm{em},\mu\nu}$; the family letters of a regular matrix are of this kind, $L$ and $R$ naming the left and the right part, $\mathsf M_{4L}$ and $\mathsf M_{4R}$.

**The word *metric* has one meaning in the series. There is one metric, the unit metric $\delta_{\mu\nu}=(1,1,1,1)$: diagonal, all four coefficients $+1$, the matrix of the interval $\sum_\mu Q_\mu^2$. A frame carries a coordinate, not a metric. The minus of the material sector is not a metric: it is $i^2=-1$ in $Q_t=i c r'_t$, made once on the time.**

**No index is raised, because the one metric is the identity.** The series has one metric, the unit metric $\delta_{\mu\nu}=(1,1,1,1)$, and raising with it changes nothing: a raised index would be the same index. A gamma is written low, $\gamma_\mu$, and the weight does the only work a raising could do, $\gamma^\mu=-\varepsilon_\mu\gamma_\mu$. A text that needs a raised index on a coefficient is writing a metric the series does not have.

**The object is not the role.** A coordinate, a basis vector, a gamma, an invariant symbol, a gauge generator, a component of a connection and a differential are seven kinds of object, and the low mark does one thing on all seven: it gives the index that names the slot of the family the glyph belongs to. The index says **which** member, never **what kind**, and the kind is carried by the glyph itself, $x_i$ against $\gamma_i$ against $\delta_{ij}$. A differential carries the same mark as the coordinate it differentiates, $x_i$ and $dx_i$, because the slot is the same in both. Nor does the alphabet divide the work: a letter is an index in $q_i$ and a number is an index in $Q_1$, and the two are of different kinds only where a coefficient and an element meet (§*The Subscripts*).

**The lists rule on these uses, not on the names.** A raised grade, parameter, sector or order is a name, not a power, a conjugation, a transposition or a construction, and the article that uses it says which name it is. A label is a name of that kind, and it names the object the glyph denotes, $E_{\mathrm{wkb}}$, a part of that object, $S_{\mathrm{int}}$, or a role of it, $s_{\mathrm{tot}}$; the word separates the three, since the series has one slot for all of them.

## The Caret

**The caret carries a power, a conjugation, a transposition and a construction.** Those four are the whole of its list, and they are read at a glance because each is italic or a symbol: $2^k$, $e^\lambda$, $(-1)^j$, $\alpha^k$ are powers; $a^{*}$, $a^{\dagger}$, $a^{\natural}$ conjugations; $L^T$, $\tilde{Ξ}_{\mathrm{sp}}^T$ transpositions; $\mathbb{B}^\times$, $S^{\otimes n}$, $\mathrm{sym}^l$, $\Lambda^kTM$ constructions.

**An operator name written with its argument is the one word that stands there.** $\operatorname{sym}(V)$ names the symmetric algebra of a space, $\operatorname{sym}^2(E)$ the symmetric square of a bundle. The word names a structure of the glyph rather than a variant of it, it carries its argument with it and never stands bare, and it is therefore not a label: it takes no entry in §*The Labels*. It is written lowercase, as a label is, and a capital in that position is a defect.

**No label stands in the caret.** A variant of an object is a name, and every name stands in the subscript (§*The Labels*). Italic is a power and upright is a name, and the slot agrees with the face: $E_{\mathrm{wkb}}$ is the labelled energy and not the WKB power of $E$, $T_{\mathrm{em},\mu\nu}$ the electromagnetic part of the tensor and not its $\mu\nu$ power, and $a_{\mathrm{fop}}$ the Fock ladder and not a power of $a$. A display that raises a label is a defect.

**No index is raised, and the caret never carries one.** Every coordinate, component, basis vector and sign symbol is written low (§*The Upper and Low Marks*), and a contraction is written as a form: $\langle\tilde\nabla,\tilde Q_{\mathrm f}\rangle_{\natural}$ for a derivative with a field, $\langle\tilde\nabla\rangle_{\natural}=\Box$ for two derivatives (*Operator and Calculus Conventions*, §*The Krein Product, Its Form and Its Norm*). Where a contraction is written with indices, the sum names the summed index — $\sum_\mu e_\mu\partial/\partial Q_\mu$ — and is never a repeated index left to the summation convention.

## The Labels

**Every label stands in the subscript.** A label is the upright roman name of a variant of an object: a construction, a frame, a sector, a reading, a part of the object or a role it plays. It is written low, at the length the article that introduces it fixes; that article also fixes what the word abbreviates, and the label enters the index with the article.

**The label comes first, and an index already in the field follows it after a comma.** $T_{\mathrm{em},\mu\nu}$ and not $T_{\mu\nu,\mathrm{em}}$, $L_{\mathrm{axf},e_\mu}$ and not $L_{e_\mu,\mathrm{axf}}$, $\tilde S_{\mathrm{tot},k}$ and not $\tilde S_{k,\mathrm{tot}}$, $\mathsf M_{4L,\mathrm{pau}}$ with the frame closing the field the size opened. A field that already carried the index is reordered and never duplicated. One field is written without the comma, the label carried into a coefficient beside its direction, $Q_{\mathrm{f}t}$ and $Q_{\mathrm{f}\mu}$, where the two letters are read as one weight. The rule, its reasons and its four contrasts are stated in the mathematical *Index and Notation Conventions*, §*The Labels*.

**The label names the object, a part of it or a role of it, and the word and its article decide which.** $\mathrm{axf}$ names the display a regular matrix is read in, $\mathbb{B}_{\mathrm{spl}}$ a variant of an algebra, $S_{\mathrm{int}}$ a part of a total, $s_{\mathrm{tot}}$ a role in a coupling. There is one slot, so the height decides nothing; the word decides, and the article that introduces it says so.

**The label is two or three letters, and it keeps the capital of a name.** A common word is abbreviated to its letters, $\mathrm{wkb}$, $\mathrm{axf}$, $\mathrm{orb}$, $\mathrm{ret}$, $\mathrm{inc}$; a proper name or an initialism keeps its capital, $\mathrm{Had}$ the Hadamard gate, $\mathrm{CS}$ the Chern–Simons term, $\mathrm{LT}$ the Lorentz transformation, $\mathrm{FS}$ the Fubini–Study form, $\mathrm{YM}$ and $\mathrm{SM}$ the two gauge programmes, $\mathrm{HS}$ the Hilbert–Schmidt norm. The index of the labels, mathematical and physical together, is the mathematical *Index and Notation Conventions*, §*The Three-Letter Labels*; a label of this corpus enters it with the article that spends it.

**$\mathrm{fop}$ marks the Fock layer.** The marks of the elements say what a glyph **is**, not that it is an **operator** (*Operator and Calculus Conventions*, §*The Operators*). The single exception is the **Fock layer**, whose operators act on a Fock space and are **not** elements of the algebra. Only these carry the label $\mathrm{fop}$:

$$
a_{\mathrm{fop}},\quad b_{\mathrm{fop}},\quad a_{\mathrm{fop}}^{\dagger},\quad b_{\mathrm{fop}}^{\dagger},\quad \tilde{Ξ}_{\mathrm{fop}},\quad N_{\mathrm{fop}},\quad H_{\mathrm{fop}},\quad F_{\mathrm{fop}},\quad Ϙ_{\mathrm{fop}},\quad U_{\mathrm{fop}} .
$$

The label says exactly one thing — the glyph is not an element, it is an operator on the Fock space — and it is written on nothing else. It is not a general mark of operators: the momentum $\vec p=-\frac{m\,c\,i}{k_m}\nabla$ keeps its element glyph and never takes the label, the quadratures $x$ and $p$ of the oscillator are written $x$ and $p$, the spin $S_k=\frac{m\,c}{2\,k_m}\sigma_k$ is written $S_k$, and the parity, charge-conjugation and time-reversal maps $P$, $C$ and $T$ carry no label. Where a ladder is meant as an element of the algebra it is written with the element's glyph, the truncated pair $\vec\Upsilon_1,\vec\Upsilon_2$, and the abstract ladder operator keeps the label, $a_{\mathrm{fop}}$.

**The dagger is the general adjoint, and it stands in the caret.** The dagger is the general adjoint (*Operator and Calculus Conventions*, §*The Operators*) and the label marks the Fock operator, so the two occupy two slots and never compete for one: $(a_{\mathrm{fop}})^{\dagger}$, contracted to $a_{\mathrm{fop}}^{\dagger}$. The dagger alone never says that its glyph is an operator, and the label alone never says that the Fock operator is self-adjoint; the two are read together, so that $a_{\mathrm{fop}}^{\dagger}$ is the adjoint of the ladder and $N_{\mathrm{fop}}$ is written without an adjoint because it is self-adjoint.

**The bar is the coefficient conjugation, and it is never the Dirac adjoint.** It is the involution of *Algebra and Element Conventions*, $\bar{\tilde Q}=\bar Q_te_t+\bar Q_x\vec e_x+\bar Q_y\vec e_y+\bar Q_z\vec e_z$, and it conjugates the coefficients of an element. The Dirac adjoint is not an involution of the algebra and takes no mark of its own: it is the adjoint of the column followed by the timelike frame cell, written as the two multipliers of that cell,
$$
\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\,iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x} \;=\; \tilde{Ξ}_{\mathrm{sp}}^{\dagger}\,iR_{\mathrm{axf},\vec e_x} .
$$
In a bilinear the cell multiplies the one that follows, $\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\bigl(iR_{\mathrm{axf},\vec e_x}\Gamma\bigr)\tilde{Ξ}_{\mathrm{sp}}$. No letter stands for the cell (*Matrix Representations Conventions*, §*The Clifford Structure*), and the bar is not reused for the composite: a display that writes $\tilde{Ξ}_{\mathrm{sp}}^{\dagger}iR_{\mathrm{axf},\vec e_x}$ and reads it as the adjoint puts a conjugation and a frame cell under one mark. A display already written that way is read as the expression above, and the bar itself stays the conjugation, as in $\bar{\tilde Q}$.

**$\mathrm{opp}$ marks the opposite algebra.** The reversed-product algebra, $a\cdot b=ba$, takes the label $\mathrm{opp}$ — $\mathbb{B}_{\mathrm{opp}}$, $A_{\mathrm{opp}}$, $M_n(D)_{\mathrm{opp}}$ — and it is the **algebra name** that takes it, where $\mathrm{fop}$ marks a **Fock-operator glyph**. The two labels are distinct and neither is read for the other: $a_{\mathrm{fop}}$ is never an opposite algebra, and $\mathbb{B}_{\mathrm{opp}}$ is never an operator.

**On an element the label names a tensor factor.** Written on an element it means the same element read in the opposite algebra, $e_{\mathrm{opp},\nu}$, and it is written there for that one purpose: to name the second factor of the tensor product $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}_{\mathrm{opp}}$, whose elementary tensors $e_\mu\otimes e_{\mathrm{opp},\nu}$ are the cells $L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}$ of the two-sided operators. The element is not thereby an operator, the label says nothing about a side, and on an operator glyph it is a defect. It marks an algebra, a module of one, and an element read in that algebra; it never marks a set or a bare vector space.

**Three qualifiers name a variant of an algebra.** They stand low, three lowercase letters each: $\mathrm{spl}$ on a split variant, $\mathbb{C}_{\mathrm{spl}}$ the split-complex numbers, $\mathbb{H}_{\mathrm{spl}}$ the split-quaternions and $\mathbb{B}_{\mathrm{spl}}$ the split-biquaternions; $\mathrm{red}$ on the reduced biquaternions, $\mathbb{B}_{\mathrm{red}}$; $\mathrm{dln}$ on the dual numbers, $\mathbb{C}_{\mathrm{dln}}=\mathbb{R}[\varepsilon]/(\varepsilon^{2})$. The label is the first thing in the field, so $\mathbb{C}_{\mathrm{spl}}$ is never a power of $\mathbb{C}$. **$\mathrm{dln}$ is not $\mathrm{dual}$**: $\mathrm{dual}$ marks the Hodge dual of a field, $F_{\mathrm{dual}}$, and the two labels are never exchanged. **$\mathbb{B}_{\mathrm{red}}$ is not a part of $\mathbb{B}$.** The reduced biquaternions are $\mathbb{C}\oplus\mathbb{C}$, of real dimension four, and the biquaternions are of real dimension eight; the qualifier names a different algebra and not a subalgebra of $\mathbb{B}$.

**The physical corpus writes labels of its own.** $\mathrm{orb}$ on the orbital part, $\mathrm{inc}$ on the incident field, $\mathrm{out}$ on the outgoing solution, $\mathrm{ret}$ on the retarded field, $\mathrm{reg}$ on the regular representation, $\mathrm{can}$ on the canonical tensor, $\mathrm{pol}$ on the polarisation vector, $\mathrm{lor}$ on the Lorentz object, $\mathrm{wkb}$ on the approximation, $\mathrm{mhv}$ on the amplitude, $\mathrm{epr}$ on the steering value, $\mathrm{sp}$ on the spinor, $\mathrm{em}$ on the electromagnetic part, and $\mathrm{axf}$ and $\mathrm{pau}$ on the two displays of the regular matrices, axis-free and Pauli, which the gamma sections keep. Each stands low on the glyph it qualifies, and the word names the part or the role it marks.

**Six codes separate two spellings.** $\mathrm{rgs}$, $\mathrm{tpl}$, $\mathrm{prm}$, $\mathrm{dfc}$, $\mathrm{obf}$, $\mathrm{adg}$, each separating the rarer of two words that share three letters — regularised from regular, topological from top, perimeter from periodic, defective from defining, orbifold from orbital, adjugate from adjoint. A code is a label and stands low with the rest, on the object it qualifies: $h_{\mathrm{tpl}}$ the topological entropy.

**The twelve algebraic structures carry no code at all.** A product is written by its two slots and the conjugation each one carries, $\tilde Q_1\tilde Q_2$, $\tilde Q_1\tilde Q_2^{*}$, $\tilde Q_1^{\natural}\tilde Q_2$, $\tilde Q_1^{\natural}\tilde Q_2^{*}$, $\tilde Q_1\bullet\tilde Q_2$, $\tilde Q_1\bullet_{*}\tilde Q_2$, $\tilde Q_1\bullet_{\natural}\tilde Q_2$, $\tilde Q_1\bullet_{\natural*}\tilde Q_2$, $\tilde Q_1\wedge\tilde Q_2$, $\tilde Q_1\wedge_{*}\tilde Q_2$, $\tilde Q_1\wedge_{\natural}\tilde Q_2$, $\tilde Q_1\wedge_{\natural*}\tilde Q_2$, and the operator names the structure on its own.

## The Subscripts

A subscript is written with the underscore, `_`, inside the math delimiters, and the underscore takes a single token: one character is written bare, $Q_t$ and $Q_k$, and two characters or more are wrapped in braces, $Q_{n+1}$ and $\tilde Q_{\mathrm{f}t}$, because a bare underscore would take the first character alone.

**The label is written first in the field, and an index already there follows it after a comma.** $L_{\mathrm{axf},e_\mu}$ is the matrix of $\vec e_\mu$ in the axis-free frame, $s_{\mathrm{tot},z}$ the projection of the total, $\tilde S_{\mathrm{tot},k}$ the generator; the rule, its reasons and its four contrasts are stated in the mathematical *Index and Notation Conventions*, §*The Labels*.

**A subscript is never a partial derivative.** The subscript is an index or a label, a partial derivative is written with $\partial$, and the rule is fixed in *Operator and Calculus Conventions*, §*Conventions for Derivation*.

**A coefficient carries a letter index and an element a number.** In the quaternionic layers a coefficient is indexed by the direction it multiplies, $Q_x$ and $q_x$, and an element that is counted carries a number on its tilde, $\tilde Q_1, \tilde Q_2$. In the commutative layers, which have no direction, both the element and its coefficients carry the number of the element, $Q_1 = q_1 + iq'_1$. The two indices are of different kinds, a letter against a number, so a coefficient index is never read as the number of an element, nor the reverse.

**It is allowed to add subscripts when several elements of the same kind are used.** The permission covers the general elements, the units, the roots, the idempotents and the nilpotents alike: wherever a statement carries more than one element of one kind, the occurrences are told apart by a subscript.

**A subscript counts, or it names.** A subscript that only tells one occurrence from another is numeric, so that a family is $\tilde Q_1, \tilde Q_2, \dots$ and a second numbered family of the same statement takes the next numbers. A subscript that names the object or the role it qualifies is a **role label**, and a role label is written in upright roman, as in $\tilde Q_{\mathrm{f}t}$ and $\tilde U_{\mathrm r}$.

**A role-labelled element carries its label in its coefficients.** The generic element-valued field is $\tilde Q_{\mathrm f}=Q_{\mathrm{f}r_t}e_t+\vec Q_{\mathrm f}$, and its components are $Q_{\mathrm{f}t}$ and $Q_{\mathrm{f}\mu}$: the label $\mathrm f$ belongs to the element and is carried once into the component subscript, beside the direction, so that the components are $Q_{\mathrm{f}t}$ and $Q_{\mathrm{f}\mu}$; it does not count a family. A numbered family is unaffected, $\tilde Q_1=Q_{1t}e_t+\vec Q_1$.

**The two parts are named by their star.** The Hermitian part is $\tilde R_\Psi$, the fixed element of the star, and the anti-Hermitian part is $\tilde R_\Phi$, its anti-fixed element: $\tilde Q=\tilde R_\Psi+\tilde R_\Phi$ is the split read on the coefficients, defined in *Algebra and Element Conventions*, §*The Hermitian and Anti-Hermitian Subspaces*. The words **informational** and **material** name $\tilde R_\Psi$ and $\tilde R_\Phi$ in the physical articles. The two letters label the parts of one element and not two fields, so no label passes into the coefficients: $\tilde R_\Psi$ and $\tilde R_\Phi$ keep the names $Q_t,Q_x,Q_y,Q_z$ and select the slots.

**An angular-momentum total takes the role subscript, and its projection the axis.** A spin label is $s$ with projection $s_z$; the total of an orbital and a spin part, or of several spins, is $s_{\mathrm{tot}}$ with projection $s_{\mathrm{tot},z}$, and the operator is $\tilde S_{\mathrm{tot},k}=\tilde L_k+\tilde S_k$. The subscript $k$ is the vector index of the operator, and the three components close on $[\tilde S_{\mathrm{tot},i},\tilde S_{\mathrm{tot},j}]=\frac{m\,c\,i\,\epsilon_{ijk}\,\tilde{S}_{\mathrm{tot},k}}{k_m}$. The projection is not a component of the operator: it is the scalar weight, the eigenvalue of $\tilde S_{\mathrm{tot},3}$ on $|s_{\mathrm{tot}},s_{\mathrm{tot},z}\rangle$, and it names the axis $z$ on which the measurement is made. The role is repeated in the projection so that $s_{1z}$, $s_{2z}$ and $s_{\mathrm{tot},z}$ are told apart without the context; the operator keeps the vector index $k$, and the weight never takes it. The role and the axis share one pair of braces, $s_{\mathrm{tot},z}$, with a comma between them.

**A sign is a subscript where the statement needs one**, the member attached to $+1$ taking the subscript $+$ and the member attached to $-1$ the subscript $-$, as in $\tilde\Pi_+$ and $\tilde\Pi_-$. In the reduced biquaternion layer the sign belongs to the idempotent pair and to its coordinates, $\Pi_\pm$, $Q_{+}$ and $Q_{-}$, the two basis coordinates carrying the triangles, $Q_{\blacktriangle}$ and $Q_{\blacktriangledown}$, and a numbered element putting its number first in either case, $Q_{1+}$ and $Q_{1\blacktriangle}$; the element they build is $\breve Q$. The sign is read with the glyph: $\tilde Q_\pm$ names an element of the sector $\mathbb{B}_{\Psi}$ or $\mathbb{B}_{\Phi}$, while $Q_\pm$ names the idempotent coordinates of $\breve Q$.

The forms a subscript takes are these.

| The subscript is | Example |
|---|---|
| a digit | $\tilde Q_1$, $\tilde Q_2$ |
| a letter | $Q_k$, $Q_\mu$ |
| two indices | $Q_{ab}$ |
| a sign | $\tilde\Pi_\pm$ |
| an upright word | $\tilde Q_{\mathrm{f}t}$, $\tilde U_{\mathrm r}$ |
| a grouped expression | $Q_{n+1}$ |

**The letter $\iota$ is not used.** No physics article uses $\iota$, in any spelling. The comparison of the biquaternion algebra with the even Clifford algebra is written by its values, $e_t\mapsto I_4$ and $\vec e_x\mapsto\gamma_2\gamma_3$, or by the words "the Clifford image", and never by a symbol. An interior product is written as the pairing it is, $\omega(X_f,\,\cdot\,)=df$, and an inner automorphism in words. The letter is not reserved for a third object: it carries no meaning in the series, and a display that introduces it is a defect.

## Summary

Every **label** stands in the subscript, the label first in the field and an index already there after a comma, $T_{\mathrm{em},\mu\nu}$. Two of them mark the layer of a glyph: $\mathrm{fop}$ marks the Fock operator, the one glyph that is not an element, and $\mathrm{opp}$ marks the opposite algebra, written on an algebra name or on an element that names a tensor factor. Three qualifiers name a variant of an algebra, $\mathrm{spl}$, $\mathrm{red}$, $\mathrm{dln}$, and the corpus writes labels of its own, $\mathrm{orb}$, $\mathrm{inc}$, $\mathrm{out}$, $\mathrm{ret}$, $\mathrm{reg}$, $\mathrm{lor}$, $\mathrm{wkb}$, $\mathrm{epr}$ among them. A label of a common word is lowercase, a label of a name keeps its capital, $\mathrm{Had}$, $\mathrm{CS}$, $\mathrm{LT}$. The index is the mathematical *Index and Notation Conventions*, §*The Three-Letter Labels*.

A subscript is written with the underscore and one token. It is a component or a label, never a derivative. A coefficient carries a letter index and a counted element a number; a subscript either counts or names, and a role label is carried once into the coefficients. A sign is a subscript where the statement needs one. The allowed forms are the digit, the letter, two indices, a sign, an upright word and a grouped expression. The family letters $L$ and $R$ of a regular matrix are labels of that kind, and they are written italic as the letters of the operators rather than upright as a word; they follow the size in the same subscript, $\mathsf M_{4L}$ and $\mathsf M_{4R}$. A label is written first in the subscript and an index already there follows it after a comma, $L_{\mathrm{axf},e_\mu}$ and $T_{\mathrm{em},\mu\nu}$; the frame closes the same field, $\mathsf M_{4L,\mathrm{pau}}$. The caret carries a power, a conjugation, a transposition and a construction, and no label; $\operatorname{sym}(V)$ is the one word that stands there. The letter $\iota$ is not used at all. An **angular-momentum total** takes the role subscript, $s_{\mathrm{tot}}$, and its projection the axis, $s_{\mathrm{tot},z}$; the operator carries the vector index, $\tilde S_{\mathrm{tot},k}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{fop}$ | The Fock-operator mark, the one glyph that is not an element |
| $\mathrm{opp}$ | The opposite algebra, written on an algebra name or on an element that names a tensor factor |
| $\mathrm{orb}$, $\mathrm{inc}$, $\mathrm{out}$, $\mathrm{lor}$, $\mathrm{rgs}$, $\mathrm{tpl}$, $\mathrm{prm}$, $\mathrm{dfc}$, $\mathrm{obf}$, $\mathrm{adg}$ | The three-letter labels of a construction or a variant, the last six separating two spellings; the index is the mathematical *Index and Notation Conventions*, §*The Three-Letter Labels* |
| $\tilde Q_1\tilde Q_2$, $\tilde Q_1^{\natural}\tilde Q_2$, $\tilde Q_1\tilde Q_2^{*}$, $\tilde Q_1^{\natural}\tilde Q_2^{*}$ | The four general products, written by their two slots and their conjugations, never by a code; with $\bullet$ their symmetric parts and with $\wedge$ their antisymmetric parts, the class carried by the subscript |
| $Q_{\mathrm{f}t}$, $Q_{n+1}$, $\tilde\Pi_\pm$, $L_{\mathrm{axf},e_\mu}$ | The subscript forms: a label carried with its direction in one field, a grouped expression, a sign, a label first and an index after a comma |
| $s_{\mathrm{tot}}$, $s_{\mathrm{tot},z}$, $\tilde S_{\mathrm{tot},k}$ | Total angular-momentum label, its projection, and the operator, which carries the vector index $k$ |

## Further Reading

- [Algebra and Element Conventions](algebra-and-element-conventions.html), for the base these conventions qualify.
- [Physics Units and Common Elements Conventions](physics-units-and-common-elements-conventions.html), for the physical units and the glyphs these marks qualify.
- [Operator and Calculus Conventions](operator-and-calculus-conventions.html), for the operators that take the Fock mark and the derivative that is never a subscript.
- [Conventions in Mathematics](../articles_maths/index-and-notation-conventions.html), for the same subscript rules on the mathematical corpus.
