# __Index and Notation Conventions__

## Introduction

This article states the marks that are read on a glyph rather than on the object: what the caret carries, the labels that stand in the subscript, the subscript rules and their admitted forms, the working conventions of the corpus and the typography of the source. It assumes the eight companions, whose glyphs it indexes, and it is followed by *Reserved Letters Conventions*, which gathers the five letters that are spent once.

The caret comes first, because it carries four things and nothing else; the labels follow, because every one of them stands in one slot and the order and the separators of that slot are fixed there; the subscripts come next, because their rule depends on the derivation convention fixed in *Operator and Calculus Conventions*. The working conventions of the corpus follow — the menus, the groups inside a category, the article files, the skeleton and the boundaries — and the typography closes the article.

The article is the ninth of the ten and the index of the notation: the table below collects the tokens and the working marks that belong to the corpus rather than to the algebra, while the table of *Algebra and Element Conventions* collects the glyphs of the algebra.

## The Upper and Low Marks

**These rules are real, and partial.** They fix the marks of the common uses and they bind wherever they apply. They do not cover every use: a mark that falls outside them is governed by the section that fixes it, and a stricter rule stated in the corpus overrides them — the derivation convention of *Operator and Calculus Conventions*, §*Conventions for Derivation*, the caret of §*The Caret*, and the forms of §*The Subscripts*.

**A caret carries four things and no label:**

- a power, $2^k$, $e^\lambda$, $(-1)^j$, $\alpha^k$, $2^{k/2-1}$;
- a conjugation, $a^{*}$, $a^{\dagger}$, $a^{\natural}$;
- a transposition, $L^T$, $\psi^T$;
- a construction, $\mathbb{B}^\times$, $S^{\otimes n}$, $\mathrm{sym}^l$, $\Lambda^kTM$ (degree).

**A low mark is the exclusive carrier of two things: an index and a label.**

- an index — a numeric count, $Q_1$, $M_2$; the slot of a coordinate, $q_i$, $x_i$, $p_i$, $Q_i$, $\theta_i$, $\zeta_k$, $v_i$; the slot of a basis vector or a gamma, $\vec e_i$, $\gamma_i$; the slots of an invariant symbol, $\delta_{ij}$, $\varepsilon_{ijk}$, $\eta_{ij}$; the generator of a frame group, colour, isospin or spin family, $T_a$, $G_a$, $\sigma_z$; the slot of a connection or curvature component, $\Gamma_k$, $R_{ij}$, $\omega_i$, $g_{ij}$; the slot of a differential, $dx_i$.
- a label naming the object, a part of it or a role of it, $L_{\mathrm{axf}}$, $\mathbb{B}_{\mathrm{opp}}$, $a_{\mathrm{fop}}$, $S_{\mathrm{int}}$, $s_{\mathrm{tot}}$, with every label of §*The Two-Letter Labels* and §*The Three-Letter Labels*; the label comes first in the subscript and an index already there follows it after a comma, $L_{\mathrm{axf},e_\mu}$; the family letters of a regular matrix are of this kind, $L$ and $R$ naming the left and the right part, $\mathsf M_{4L}$ and $\mathsf M_{4R}$.

**The word *metric* has one meaning in the corpus. There is one metric, the unit metric $\delta_{\mu\nu}=(1,1,1,1)$: diagonal, all four coefficients $+1$, the matrix of the interval $\sum_\mu Q_\mu^2$. A frame carries a coordinate, not a metric. The minus of the material sector is not a metric: it is $i^2=-1$ in $Q_t=iq'_t$, made once on the time.**

**Contravariant notation is not allowed.** The series has one metric, the unit metric $\delta_{\mu\nu}=(1,1,1,1)$, and a metric that is the identity raises nothing: a raised index would name the same index. The raised form is therefore not a shorthand, not a convenience and not a concession to another text's habit; it is a defect wherever it stands, and the series prints none. Raising is replaced by the weight, and the weight is always written out.

**The ban is stated in words and not by example, and it is stated in every convention article.** A rule that printed the defect it forbids would print the defect, so this article names no contravariant glyph, here or anywhere: no letter of the series carries a raised spacetime index, in a display, in a table, in a caption, in a definition or in a quotation. The ban is repeated in *Frame and Metric Conventions*, in *Matrix Representations Conventions*, in *Product and Form Conventions*, in *Operator and Calculus Conventions* and in every other convention article of the two corpora, so that no reader meets the raised form without meeting the rule against it in the same article.

**Every index is low, and the weight replaces the raising.**

- A coefficient is low: $A_\mu$, $x_\mu$, $p_\mu$, $k_\mu$, $j_\mu$, $F_{\mu\nu}$, $T_{\mu\nu}$, $\epsilon_{L,\mu}$, $\partial_\mu$. The raised spelling of a coefficient is a defect, and the series prints none of them.
- A gamma is low, $\gamma_\mu$. A basis operator is low, $\mathsf C_\mu$, $\vec e_i$. The raised spelling of either is a defect, and the series prints none of them.
- A trace is a sum, $\sum_\mu\varepsilon_\mu T_{\mu\mu}$. A trace that would carry one index up and one down is a defect, and the series prints none.
- A contraction names its summed index and carries the weight, $\sum_\mu\varepsilon_\mu A_\mu B_\mu$. A repeated index left to the summation convention is a defect, and so is a contraction that would carry one index up and one down.
- The weight does what a raising would have done: $\gamma_\mu\gamma_\mu=\varepsilon_\mu I_4$ with no sum, so a Dirac sum is $\sum_\mu\varepsilon_\mu\gamma_\mu\gamma_\mu=4I_4$ and a Dirac operator is $-i\sum_\mu\varepsilon_\mu\gamma_\mu\partial_\mu$.

**A quoted display is the one exception, and it is named.** A display quoted from another text keeps that text's spelling, and the sentence that introduces it says so; the article's own displays, including the one that reads the quotation, carry the low form. Where an article must speak of a raised index of another text, it names it in words and does not print the symbol.

**The object is not the role.** A coordinate, a basis vector, a gamma, an invariant symbol, a symmetry generator, a component of a connection and a differential are seven kinds of object, and the low mark does one thing on all seven: it gives the index that names the slot of the family the glyph belongs to. The index says **which** member, never **what kind**, and the kind is carried by the glyph itself, $x_i$ against $\gamma_i$ against $\delta_{ij}$. A differential carries the same mark as the coordinate it differentiates, $x_i$ and $dx_i$, because the slot is the same in both. Nor does the alphabet divide the work: a letter is an index in $q_i$ and a number is an index in $Q_1$, and the two are of different kinds only where a coefficient and an element meet (§*The Subscripts*).

**The lists rule on these uses, not on the names.** A raised grade, parameter, sector or order is a name, not a power, a conjugation, a transposition or a construction, and the article that uses it says which name it is. A label is a name of that kind, and it names the object the glyph denotes, $\mathbb{B}_{\mathrm{opp}}$, $a_{\mathrm{fop}}$, $L_{\mathrm{axf}}$, a part of that object, $S_{\mathrm{int}}$, or a role of it, $s_{\mathrm{tot}}$; the word separates the three, since the corpus has one slot for all of them.

### Marks That Are Not Indices

**The prime marks the imaginary coordinate.** A prime marks the second, imaginary coefficient of a complex, split-complex or dual element, $R=r+ir'$, and of a biquaternion coefficient, $R_\mu=r_\mu+ir'_\mu$; a primed glyph takes the primed parameters throughout. It never marks a derivative, and no further use of it is admitted.

**The bar marks a conjugate.** A bar marks the conjugate of a glyph, $\bar Q$ and $\bar\Pi$, and on an index the conjugate spinor, $\bar l$ and $\bar\alpha$.

**The underline marks a scope.** In geometric calculus the differentiated factor is underlined, $\underline{\partial}(AB)=\underline{\partial}A\,B+\underline{A}\,\underline{\partial}B$.

A prime may follow a subscript as well as precede it, `q'_t` and `q_t'`, and an article keeps one order throughout.

## The Caret

**The caret carries a power, a conjugation, a transposition and a construction.** Those four are the whole of its list, and they are read at a glance because each is italic or a symbol: $e^\lambda$, $2^k$, $(-1)^k$ are powers; $a^{*}$, $a^{\dagger}$, $a^{\natural}$ conjugations; $L^T$, $\psi^T$ transpositions; $\mathbb{B}^\times$, $S^{\otimes n}$, $\mathrm{sym}^l$, $\Lambda^kTM$ constructions. $M_4^\sigma$ and $B^\sigma$ carry a Greek letter that names an automorphism of the glyph and not a variant of it.

**An operator name written with its argument is the one word that stands there.** $\gamma_n^{\operatorname{sym}}$ on a divided-power structure, $K^{\operatorname{gal}(K/F)}$, $\kappa_{\mathrm{cf}}^{(\kappa)}$, $M_{\mathrm{co}}^{H}$. The word names a structure of the glyph rather than a variant of it, it carries its argument with it and never stands bare, and it is therefore not a label: it is not indexed in §*The Labels* and it takes no entry in either table. It is written lowercase, as a label is, and a capital in that position is a defect.

**No label stands in the caret.** A variant of an object is a name, and every name stands in the subscript (§*The Labels*). Italic is a power and upright is a name, and the slot agrees with the face: $L_{\mathrm{axf},\vec e_x}$ is the matrix of $\vec e_x$ in the axis-free frame, and it is not the $x$-th power of an operator.

**The caret never carries an index.** A contravariant index is not allowed anywhere in the corpus (§*The Upper and Low Marks*), so the caret cannot carry one either: every coordinate, component, basis vector, frame operator and sign symbol is written low — $x_\mu$, $A_\mu$, $\vec e_i$, $\gamma_i$, $\varepsilon_{ijk}$ (§*The Upper and Low Marks*). A contraction is written as an explicit sum with the sign vector or as the quaternionic product that carries it: the form $\langle\tilde\nabla_\Phi,\tilde Q_{\mathrm f}\rangle_{\natural}$ for a derivative with a field, and $\langle\tilde\nabla_\Phi\rangle_{\natural}=\Box_\Phi$ for two derivatives (*Operator and Calculus Conventions*, §*The Krein Product, Its Form and Its Norm*). Where a contraction is written with indices, the sum names the summed index — $\sum_\mu e_\mu\partial/\partial Q_\mu$, $\sum_k\vec e_kA_k$ — and is never a repeated index left to the summation convention. The rule is the one of *Operator and Calculus Conventions*, §*Conventions for Derivation*.

## The Labels

**Every label stands in the subscript.** A label is the upright roman name of a variant of an object: a construction, a frame, a sector, a reading, a part of the object or a role it plays. It is written low, in lowercase, at the length the article that introduces it fixes; that article also fixes what the word abbreviates, and the label enters the index with the article.

**The label comes first, and an index already in the field follows it after a comma.** The subscript is read from the label outward: $L_{\mathrm{axf},e_\mu}$ and not $L_{e_\mu,\mathrm{axf}}$, $\tilde S_{\mathrm{tot},k}$ and not $\tilde S_{k,\mathrm{tot}}$, $\mathbb{C}_{\mathrm{spl},2}$ and not $\mathbb{C}_{2,\mathrm{spl}}$, $T_{\mathrm{em},\mu\nu}$ and not $T_{\mu\nu,\mathrm{em}}$. A field that already carried the index is reordered and never duplicated, $V_K^{\mathrm{fin}}$ becoming $V_{\mathrm{fin},K}$. One field is written without the comma, the label carried into a coefficient beside its direction, $Q_{\mathrm{f}t}$ and $Q_{\mathrm{f}\mu}$, where the two letters are read as one weight.

**The label names the object, a part of it or a role of it, and the word and its article decide which.** $L_{\mathrm{axf}}$ names the frame a regular matrix is read in, $\mathbb{B}_{\mathrm{opp}}$ a variant of an algebra, $S_{\mathrm{int}}$ a part of a total, $s_{\mathrm{tot}}$ a role in a coupling. There is one slot, so the height decides nothing; the word decides, and the article that introduces it says so.

**Most labels are two or three letters, and a longer word is kept whole where the short form would be ambiguous.** The two families are indexed below. A fourth letter is admitted where three do not carry the word, $\mathrm{lift}$, $\mathrm{dual}$, $\mathrm{deph}$, $\mathrm{refl}$, and a compound whose abbreviation would collide with a neighbour is written out, $\mathrm{singlet}$, $\mathrm{coroot}$, $\mathrm{grevlex}$, $\mathrm{boost}$. One letter's difference at subscript size does not separate two meanings, so a pair that would differ by one letter is not written; that is why $\mathrm{op}$ is not a label beside $\mathrm{opp}$.

**$\mathrm{fop}$ marks the Fock layer.** The marks of the elements say what a glyph **is**, not that it is an **operator** (*Operator and Calculus Conventions*, §*The Operators*). The single exception is the **Fock layer** of the physical corpus, whose operators act on a Fock space and are **not** elements of the algebra. Only these carry the label $\mathrm{fop}$:

$$
a_{\mathrm{fop}},\quad b_{\mathrm{fop}},\quad a_{\mathrm{fop}}^{\dagger},\quad \psi_{\mathrm{fop}},\quad N_{\mathrm{fop}},\quad H_{\mathrm{fop}},\quad F_{\mathrm{fop}},\quad Q_{\mathrm{fop}},\quad U_{\mathrm{fop}} .
$$

The label says exactly one thing — the glyph is not an element, it is an operator on the Fock space — and it is written on nothing else. It is not a general mark of operators: the momentum $\vec p$, the position $x$, the spin $S$ and the parity, charge-conjugation and reversal maps $P$, $C$ and $T$ carry no label, because each keeps the glyph of its element or is a map with a glyph of its own. The dagger is the general adjoint, and it stands in the caret, so the two marks occupy two slots and never compete for one: $a_{\mathrm{fop}}^{\dagger}$ is the raised dagger on a labelled glyph. The dagger alone never marks a glyph as an operator, and the label alone never asserts self-adjointness.

**$\mathrm{opp}$ marks the opposite algebra.** The **opposite algebra**, whose multiplication is reversed, $a\cdot b=ba$, takes the label $\mathrm{opp}$ — $A_{\mathrm{opp}}$, $\mathbb{B}_{\mathrm{opp}}$, $M_n(D)_{\mathrm{opp}}$ — and it is the **algebra name** that takes it, where $\mathrm{fop}$ marks a Fock-operator glyph. The two meanings are separated by the word itself and not by context.

**On an element the label names a tensor factor.** Written on an element it means the same element read in the opposite algebra, $e_{\mathrm{opp},\nu}$, and it is written there for that one purpose: to name the second factor of the tensor product $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}_{\mathrm{opp}}$, whose elementary tensors $e_\mu\otimes e_{\mathrm{opp},\nu}$ are the basis operators $L_{e_\mu}R_{e_\nu}$ of the two-sided operators. The element is not thereby an operator, the label says nothing about a side, and on an operator glyph it is a defect. It marks an algebra, a module of one, and an element read in that algebra; it never marks a set or a bare vector space.

**The two-letter form $\mathrm{op}$ is not a label.** It differs from $\mathrm{opp}$ by one letter, at the size a label is set, and a page carrying both would be undecidable at reading speed. It is therefore not a token of the corpus in any sense, and the one place where it survives, the bar $\lVert A\rVert_{\mathrm{op}}$ of §*The Two-Letter Labels*, is a defect. In particular it does not mark the operator norm: the norm is written $\lVert A\rVert$ bare, and the norms it is compared with carry their own labels, $\langle A\rangle_*^{1/2}$, $\lVert A\rVert_{\mathrm{nuc}}$, $\langle A\rangle_*^{1/2}$, $\lVert A\rVert_*$, so that the unmarked bar is the operator norm by default and never by elimination. It does not mark an operator either: an operator glyph is the element's glyph, and the explicit form is written where the letter is taken, as in the gradient $\tilde\nabla_\Phi$ and the momentum $\vec p$.

### The Two-Letter Labels

The table is an index of labels and not a list of tokens: a label names an object, a construction, a frame or a variant of one, the article that introduces it fixes what it abbreviates, and a label enters the table with that article.

**The section holds two tables.** The first indexes the two-letter labels that name an object, a construction, a frame or a variant, and it carries thirty rows. The second table carries the four labels of the norm bar.

**Two letters are the shorter length of the label, and they are made as the three are.** Either the initials of a two-word term — $\mathrm{sa}$ the self-adjoint part, $\mathrm{rs}$ the regular semisimple locus, $\mathrm{df}$ the discrete and faithful representations, $\mathrm{em}$ the electromagnetic part — or the consonants of a single word — $\mathrm{fn}$ a function, $\mathrm{sh}$ the sheafification, $\mathrm{bl}$ the blow-up, $\mathrm{cl}$ the classical value, $\mathrm{tr}$ the transpose, $\mathrm{gr}$ the gradient, $\mathrm{pf}$ the profinite completion, $\mathrm{sw}$ the swap. The three letters of the other family are what a word that does not shorten gives, $\mathrm{opp}$, $\mathrm{fop}$, $\mathrm{axf}$, $\mathrm{nil}$, and neither length is a shortening of the other: the index of the longer family is §*The Three-Letter Labels*.

**A pair that would be read for the other is refused.** $\mathrm{op}$ differs from $\mathrm{opp}$ by one letter and would name a variant of the same algebra on the same glyph, so it is not a label. The prefix relation alone is no defect: twenty-four two-letter labels begin a three-letter one — $\mathrm{sc}$ beside $\mathrm{scl}$, $\mathrm{st}$ beside $\mathrm{str}$, $\mathrm{sp}$ beside $\mathrm{spl}$, $\mathrm{ad}$ beside $\mathrm{adj}$ — and each pair is admitted because the two members never stand on one glyph in one role. What the rule refuses is a pair that names the same kind of object on the same glyph.

**$\mathrm{sp}$ is the one label of the spinor, and $\mathrm{pau}$ its Pauli counterpart.** $\mathrm{sp}$ marks the Dirac field, $\tilde\Xi_{\mathrm{sp}}=\tilde\Xi_{\mathrm{sp},L}+\tilde\Xi_{\mathrm{sp},R}$, the spinor role written on its own density, $\rho_{\mathrm{sp}}=\lvert\tilde\Xi_{\mathrm{sp}}\rangle\langle\tilde\Xi_{\mathrm{sp}}\rvert$, and the spinor reading of a glyph whose Pauli reading is $\mathrm{pau}$, $\sigma_{\mathrm{sp},k}$ beside $\sigma_{\mathrm{pau},k}$. The two labels name a relation and not an object, so each is written on the glyph whose reading it fixes, and the article that writes it says what the reading carries. The label is two letters: the field is `\tilde\Xi_{\mathrm{sp}}` everywhere in the corpus, and no three-letter variant of it is written.

**A two-letter label is read as a three-letter one is.** It names the object the glyph denotes, $G_{\mathrm{ab}}$, $X_{\mathrm{an}}$, $\hat G_{\mathrm{pf}}$, or a part or a role of that object, $G_{\mathrm{ad}}$, $G_{\mathrm{sc}}$, $\lVert f\rVert_{\mathrm{sp}}$, and §*The Subscripts* rules on the slot. One token is carried by two readings: $\mathrm{sp}$ on a spinor density, or on the Dirac field itself, is the spinor; $\mathrm{sp}$ on the bar, $\lVert f\rVert_{\mathrm{sp}}$, is the spectral norm. The bar is the discriminator, and no glyph carries the two readings at once.

| Label | Names |
|---|---|
| $\mathrm{ab}$ | the abelianisation of a group, $G_{\mathrm{ab}}=G/[G,G]$ |
| $\mathrm{ad}$ | the adjoint of a prespectrum; the adic space |
| $\mathrm{an}$ | the Berkovich analytification, $X_{\mathrm{an}}$ |
| $\mathrm{av}$ | the averaged map, $\sigma_{\mathrm{av}}$ |
| $\mathrm{ax}$ | the axial extension of a holomorphic function, $f_{\mathrm{ax},0}$ |
| $\mathrm{bl}$ | the blow-up, $X_{\mathrm{bl}}$ |
| $\mathrm{cl}$ | the classical value, $\mathcal A_{\mathrm{cl}}$ |
| $\mathrm{df}$ | the discrete and faithful representations, $\mathrm{Hom}_{\mathrm{df}}(\pi_1(S),PSL_2(\mathbb{R}))$ |
| $\mathrm{em}$ | the electromagnetic part, $F_{\mathrm{em},\mu\nu}$ |
| $\mathrm{eq}$ | the equivalence relation generated by a relation, $R_{\mathrm{eq}}$ |
| $\mathrm{ev}$ | the even part, $H_{\mathrm{ev}}$ |
| $\mathrm{ex}$ | the exchange kernel, $K_{\mathrm{ex}}$ |
| $\mathrm{fn}$ | a function from a domain into the algebra, $F_{\mathrm{fn}}:\Omega\to\mathbb{B}$ |
| $\mathrm{gr}$ | the gradient index of a slowly changing medium, $\epsilon_{\mathrm{gr}}=\mathrm{grad}\sqrt{\epsilon}/\sqrt{\epsilon}$ |
| $\mathrm{id}$ | the identity reading, the ordinary one: the left multiplication $\Lambda_{\mathrm{id},a}=L_a$ |
| $\mathrm{im}$ | the image of a domain under a diffeomorphism, $\Omega_{\mathrm{im}}$ |
| $\mathrm{in}$ | the incoming field, $u_{\mathrm{in}}$ |
| $\mathrm{io}$ | the monoid generated by the involution and the complement, $M_{\mathrm{io}}$ |
| $\mathrm{pf}$ | the profinite completion, $\hat G_{\mathrm{pf}}$ |
| $\mathrm{rs}$ | the regular semisimple locus, $M_{\mathrm{rs},5}$ |
| $\mathrm{sa}$ | the self-adjoint part, $B(H)_{\mathrm{sa}}$ |
| $\mathrm{sc}$ | the scattered field, $u_{\mathrm{sc}}$ |
| $\mathrm{sh}$ | the sheafification, $(M\otimes_A B)_{\mathrm{sh}}$ |
| $\mathrm{si}$ | the signed inner conjugation, $\operatorname{Ad}_{\mathrm{si},v}$ |
| $\mathrm{sp}$ | the spinor: the Dirac field $\tilde\Xi_{\mathrm{sp}}$, its density $\rho_{\mathrm{sp}}$, and the spinor reading that pairs with $\mathrm{pau}$ for the Pauli matrices |
| $\mathrm{st}$ | the supertranspose |
| $\mathrm{sw}$ | the swap of the regular bimodule, ${}_{\mathrm{sw}}{}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}$ |
| $\mathrm{tr}$ | the transpose, $T_{\mathrm{tr}}$ |
| $\mathrm{tw}$ | the twisted local system, $\mathbb{Z}_{\mathrm{tw}}$ |
| $\mathrm{un}$ | the unital one, $\operatorname{Aut}_{\mathrm{un},R}$ |

**The second table is the norm bar, and its base reading is the square root of the Hermitian norm.** On an element of an algebra the bar is that root,

$$
\lVert X\rVert=\bigl(\langle X\rangle_{*}\bigr)^{1/2},
$$

which for a matrix is $\bigl(\operatorname{tr}(X^{*}X)\bigr)^{1/2}$, the norm the earlier notation called the Frobenius or the Hilbert–Schmidt norm. That norm is written with the bracket, $\langle X\rangle_{*}^{1/2}$, and no longer as a bar; the two names survive as names of the same object and never as symbols. On an **operator** the bare bar is the operator norm, $\lVert T\rVert=\sup\{\lVert Tx\rVert:\lVert x\rVert\leq1\}$, which is not the root of a Hermitian form; the object tells the two readings apart, an element of the algebra or an operator on a Hilbert space.

**A label stands on the bar for a norm that is neither.** The nuclear norm, the spectral norm, the sup norm and the operator norm keep a label, and the operator norm keeps one wherever the object could be read as an element: the form $\lVert A\rVert_{\mathrm{op}}$ says which norm is meant and is not a defect, since the bare bar on the same $A$ is the Hermitian root.

| Label | Names |
|---|---|
| $\lVert A\rVert_{\mathrm{nuc}}$ | the nuclear norm |
| $\lVert f\rVert_{\mathrm{sp}}$ | the spectral norm, $\lim_m\lVert f^m\rVert^{1/m}$ |
| $\lVert f\rVert_{\mathrm{sup}}$ | the sup norm |
| $\lVert A\rVert_{\mathrm{op}}$ | the operator norm, written where $A$ could be read as an element |

**The angle labels are outside this section.** All thirty name an angle of $\theta$ and stand in its subscript, all are three letters, and they are indexed in §*The Three-Letter Labels*; a two-letter label never stands on $\theta$.

**The table is closed at thirty.** A two-letter token that the corpus spends and this table does not carry is admitted with the article that spends it, or it is a defect, as a three-letter one is.

### The Three-Letter Labels

**The section holds two tables.** The first indexes the labels that name an object, a construction, a frame or a variant, and it carries seventy-eight rows. The second table carries the thirty angle labels.

**The split is the rule of the angle.** Where one formula holds two angles the first keeps the bare $\theta$ and the second takes a label, so an angle label names a role and not an object, and the two tables never share a row: a label of an object never stands on $\theta$, and an angle label never stands elsewhere. A label that neither table carries enters with the article that spends it.

**Every label is written in lowercase.** The label is set at subscript size, where the case of a two- or a three-letter word is not read reliably, so the corpus writes every one of them in lowercase; the rule is the one that refuses $\mathrm{op}$ beside $\mathrm{opp}$, applied to case instead of to spelling. The bar is the one place where a capital survives, and only there: $\langle A\rangle_*^{1/2}$.

**No label carries a capital.** A capital in that position is a defect, and the corpus writes every label lowercase.

**Six codes separate two spellings.** Where one three-letter word carries two English words, the rarer reading takes a code of its own, made the same way and written in the same place: $\mathrm{rgs}$ beside $\mathrm{reg}$, $\mathrm{tpl}$ beside $\mathrm{top}$, $\mathrm{prm}$ beside $\mathrm{per}$, $\mathrm{dfc}$ beside $\mathrm{def}$, $\mathrm{obf}$ beside $\mathrm{orb}$, $\mathrm{adg}$ beside $\mathrm{adj}$. Each of the six names one word only, and a glyph may carry either member of a pair. A code is a label and stands low with the others, on the object it qualifies: $h_{\mathrm{tpl}}$ the topological entropy, $\Lambda_{\mathrm{top}}$ the top exterior power. The twelve algebraic structures carry no code at all: a product is written by its two slots and the conjugation each one carries, $\tilde Q_1\tilde Q_2$, $\tilde Q_1\tilde Q_2^{*}$, $\tilde Q_1^{\natural}\tilde Q_2$, $\tilde Q_1^{\natural}\tilde Q_2^{*}$, $\tilde Q_1\bullet\tilde Q_2$, $\tilde Q_1\bullet_{*}\tilde Q_2$, $\tilde Q_1\bullet_{\natural}\tilde Q_2$, $\tilde Q_1\bullet_{\natural*}\tilde Q_2$, $\tilde Q_1\wedge\tilde Q_2$, $\tilde Q_1\wedge_{*}\tilde Q_2$, $\tilde Q_1\wedge_{\natural}\tilde Q_2$, $\tilde Q_1\wedge_{\natural*}\tilde Q_2$, and the operator names the structure of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* on its own.

**The indexed label is one field.** Where a label and an index name the same object they share one subscript, the label first, $s_{\mathrm{tot},z}$, $\tilde K_{\mathrm{mod},W}$, $\tilde H_{\mathrm{pos},l}$. A part or a role is a label like the others, $\lVert A\rVert_{\mathrm{nuc}}$, $M_{\mathrm{tor}}$, $S_{\mathrm{int}}$, $E_{\mathrm{vac}}$, and so is an operator name written low, $\operatorname{col}A$, $\operatorname{row}A$, $\sum_{\mathrm{cyc}}$.

| Label | Names |
|---|---|
| $\mathrm{adg}$ | the adjugate matrix, $A_{\mathrm{adg}}$, the reading that shared $\mathrm{adj}$ before the code was made |
| $\mathrm{adj}$ | the adjoint spin of a representation |
| $\mathrm{aff}$ | the affine Weyl group of a root system |
| $\mathrm{alg}$ | the algebraic left multiplication |
| $\mathrm{arc}$ | the arc-length parametrisation of a curve |
| $\mathrm{aut}$ | the automorphism attached to a triple isomorphism |
| $\mathrm{avg}$ | the group average of a projection |
| $\mathrm{axf}$ | the axis-free frame |
| $\mathrm{cop}$ | the coproduct of a Hopf algebra |
| $\mathrm{cov}$ | the universal cover here, the covariant fundamental solution there |
| $\mathrm{cts}$ | the continuous dual |
| $\mathrm{def}$ | the defining spin; the deformation stratum |
| $\mathrm{dfc}$ | the defective part, $\Sigma_{\mathrm{dfc},10}$ |
| $\mathrm{dif}$ | the difference, or antisymmetrised, product |
| $\mathrm{est}$ | an unbiased estimator |
| $\mathrm{ext}$ | the extended affine Weyl group |
| $\mathrm{fat}$ | the fat Cantor set |
| $\mathrm{fin}$ | the non-Archimedean places |
| $\mathrm{fix}$ | the fixed points of the involution |
| $\mathrm{fop}$ | the Fock operator |
| $\mathrm{geo}$ | the geometric phase |
| $\mathrm{har}$ | the harmonic Fischer projection |
| $\mathrm{hom}$ | the homogeneous solution of a linear equation |
| $\mathrm{hyp}$ | the hyperbolic area of a rapidity triangle |
| $\mathrm{imp}$ | the improvement term of the tensor |
| $\mathrm{ind}$ | the induced character |
| $\mathrm{inv}$ | the invariant measure |
| $\mathrm{iso}$ | the maximal isotropic real plane |
| $\mathrm{lin}$ | the linearisation |
| $\mathrm{lor}$ | the Lorentz object, the group or the Green function |
| $\mathrm{mat}$ | the matrix imaginary, the image of the scalar imaginary |
| $\mathrm{mix}$ | the mixture of a pair of states |
| $\mathrm{mod}$ | the stable module category, $\underline{\mathrm{mod}}\,A$, and $\mathrm{mod}\,A$ |
| $\mathrm{mon}$ | the monogenic Fischer operator |
| $\mathrm{new}$ | the new subspace |
| $\mathrm{nil}$ | the nilpotent direction |
| $\mathrm{obf}$ | the orbifold Euler characteristic, $\chi_{\mathrm{obf}}$ |
| $\mathrm{odd}$ | the odd part of a graded algebra |
| $\mathrm{old}$ | the old subspace |
| $\mathrm{opp}$ | the opposite algebra |
| $\mathrm{out}$ | the outgoing solution |
| $\mathrm{pau}$ | related to the Pauli matrices |
| $\mathrm{per}$ | the periodic cyclic complex; the periodic integration domain |
| $\mathrm{pre}$ | the presheaf |
| $\mathrm{prm}$ | the perimeter coefficient, $\mu_{\mathrm{prm}}$ |
| $\mathrm{red}$ | the reduced object |
| $\mathrm{reg}$ | the regular representation, $\rho_{\mathrm{reg}}$, $\operatorname{Tr}_{\mathrm{reg}}$, $\chi_{\mathrm{reg}}$ |
| $\mathrm{rel}$ | the relative transfer |
| $\mathrm{rep}$ | the representing function |
| $\mathrm{res}$ | the residual part; the residue field |
| $\mathrm{ret}$ | the retarded field |
| $\mathrm{rev}$ | the reversed process |
| $\mathrm{rgs}$ | the regularised kernel, $G_{\mathrm{rgs},R}$ |
| $\mathrm{set}$ | the underlying set of a structure |
| $\mathrm{sgn}$ | the sign |
| $\mathrm{src}$ | the source point of a short-time kernel |
| $\mathrm{str}$ | the structure group |
| $\mathrm{sub}$ | the submultiplicative seminorm |
| $\mathrm{sym}$ | the symmetrised form; on a divided-power structure, the symmetric one |
| $\mathrm{top}$ | the top exterior power |
| $\mathrm{tot}$ | the total tensor |
| $\mathrm{tpl}$ | the topological entropy and susceptibility, $h_{\mathrm{tpl}}$ |
| $\mathrm{vol}$ | the fifth frame operator of a frame, $\mathsf{V}_{\mathrm{vol}}$, the chirality operator of the frame |
| $\mathrm{wkb}$ | the WKB approximation |

**The second table is the angle family.** Each row is a role that a second angle plays in one formula, and the glyph is the same in every row: the label is what tells one angle from another. The table reads alphabetically by the label, and no angle label names an object — the object is the element and the angle is one of its coordinates.

| Label | Names |
|---|---|
| $\theta_{\mathrm{axc}}$ | the axicon angle of a Bessel beam |
| $\theta_{\mathrm{axr}}$ | the rotation angle of a rotor about an arbitrary axis |
| $\theta_{\mathrm{axs}}$ | the rotation angle about $\vec u_y$ in the Majorana chart |
| $\theta_{\mathrm{azm}}$ | the azimuthal angle |
| $\theta_{\mathrm{blc}}$ | the angle the Bloch vector turns |
| $\theta_{\mathrm{btw}}$ | the angle between two directions |
| $\theta_{\mathrm{dfl}}$ | the small deflection angle |
| $\theta_{\mathrm{drb}}$ | the angle from the Darboux to the Frenet frame |
| $\theta_{\mathrm{drc}}$ | the direction angle of a unit vector |
| $\theta_{\mathrm{dua}}$ | the duality-rotation angle of an electromagnetic wave |
| $\theta_{\mathrm{eul}}$ | the spin angle of a symmetric top |
| $\theta_{\mathrm{foc}}$ | the colatitude of a point on the sphere |
| $\theta_{\mathrm{cph}}$ | the phase angle of a local central phase |
| $\theta_{\mathrm{hpa}}$ | the hyperbolic angle of a split-complex number |
| $\theta_{\mathrm{intr}}$ | the rotation angle of the internal clock |
| $\theta_{\mathrm{lna}}$ | the angle of the line $a$ |
| $\theta_{\mathrm{lnb}}$ | the angle of the line $b$ |
| $\theta_{\mathrm{mgn}}$ | the angle between a magnetic moment and the field |
| $\theta_{\mathrm{pha}}$ | the phase angle of a complex number or of a gate, $\theta_{\mathrm{pha}}=\arg\omega$ |
| $\theta_{\mathrm{phb}}$ | the second phase angle, the split-complex phase of a reduced biquaternion |
| $\theta_{\mathrm{phs}}$ | the phase of a scalar field, $\theta_{\mathrm{phs}}=2\pi S/h$, a full-turn angle |
| $\theta_{\mathrm{pla}}$ | the angle in the first invariant plane |
| $\theta_{\mathrm{plb}}$ | the angle in the second invariant plane |
| $\theta_{\mathrm{prc}}$ | the precession angle of a gyroscope |
| $\theta_{\mathrm{rat}}$ | the angle a rate forms with time, $\omega t'$ |
| $\theta_{\mathrm{rgp}}$ | the second rotation angle about one axis |
| $\theta_{\mathrm{sct}}$ | the scattering angle |
| $\theta_{\mathrm{sol}}$ | the solid angle |
| $\theta_{\mathrm{stk}}$ | the rotation angle in Stokes space |
| $\theta_{\mathrm{tnp}}$ | the rotation angle in the tangent plane |
| $\theta_{\mathrm{vac}}$ | the vacuum angle of a connection field |
| $\theta_{\mathrm{wav}}$ | the angle between a wave vector and a boost |
| $\theta_{\mathrm{wgn}}$ | the Wigner angle of a boost product |

**An angle label enters with the article that spends it, and it enters this table and not the other.** The thirty-three rows stand for thirty-three roles and 3,446 occurrences in the two corpora; the largest, $\theta_{\mathrm{pha}}$, names the phase angle, because every polar word and every gate spends it.

**A phase is written here and not in a letter of its own.** The 91 occurrences that $\phi$ carried as a phase are $\theta_{\mathrm{pha}}$, the row that already named the phase angle in the complete polar decomposition, so the phase cost no new label. The $\alpha$ that the polar-word articles carried for that angle is the same row, and the $\beta$ that paired with it is $\theta_{\mathrm{phb}}$: a reduced biquaternion spends two phases, one on the complex unit and one on the split unit, and they are $\theta_{\mathrm{pha}}$ and $\theta_{\mathrm{phb}}$. Where a phase is a geometric phase the row is the same one: a Berry or a Pancharatnam phase is an angle read modulo $2\pi$, and the article that spends it says so in its own words.

**A label is read with its article.** The word names the object the glyph denotes, a part of it or a role of it, and the word and the article separate the three, since one slot carries all of them: $L_{\mathrm{axf}}$ names a frame, $S_{\mathrm{int}}$ a part, $s_{\mathrm{tot}}$ a role, and §*The Subscripts* rules on the slot. One word is carried by four uses and is read with its argument: $\operatorname{sym}(P)$ the symmetric group, $\operatorname{sym}^2(E)$ the symmetric square, $\gamma_n^{\operatorname{sym}}$ the divided-power structure, $f^{\operatorname{sym}}$ the symmetrised part. The word is one and it is lowercase in all four; the argument says which. The vocabulary is not private to a slot, and it is not ambiguous either: $\mathrm{cov}$ names the universal cover in one article and the covariant fundamental solution in another, $\mathrm{res}$ names the residual part and the residue field, and the article that writes a label says which object it names. Where one spelling would name two objects that a reader must tell apart at a glance, the rarer reading takes a code of its own rather than a second height: $\mathrm{rgs}$, $\mathrm{tpl}$, $\mathrm{prm}$, $\mathrm{dfc}$, $\mathrm{obf}$, $\mathrm{adg}$ stand beside $\mathrm{reg}$, $\mathrm{top}$, $\mathrm{per}$, $\mathrm{def}$, $\mathrm{orb}$, $\mathrm{adj}$, and each of the twelve names one word only.

## The Subscripts

A subscript is written with the underscore, `_`, inside the math delimiters, and the underscore takes a single token: one character is written bare, $Q_t$ and $Q_k$, and two characters or more are wrapped in braces, $Q_{n+1}$ and $\mathbb{B}_{\mathrm{red}}$, because a bare underscore would take the first character alone. A subscript label is written in the upright roman of the labels, and the two lists are read together (§*The Three-Letter Labels*). The family letters $L$ and $R$ of a regular matrix are labels of that kind, and they are written italic as the letters of the operators rather than upright as a word; they follow the size in the same subscript, $\mathsf M_{4L}$ and $\mathsf M_{4R}$.

**The label is written first in the field.** $L_{\mathrm{axf},e_\mu}$ is the matrix of $\vec e_\mu$ in the axis-free frame, and the rule is stated in §*The Labels*; the rest of this section rules on the index, and on the label where it accompanies one.

**A subscript is never a partial derivative.** The subscript is an index or a label, a partial derivative is written with $\partial$, and the rule is fixed in *Operator and Calculus Conventions*, §*Conventions for Derivation*.

**A coefficient carries a letter index and an element a number.** In the quaternionic layers a coefficient is indexed by the direction it multiplies, $Q_x$ and $q_x$, and an element that is counted carries a number on its tilde, $\tilde Q_1, \tilde Q_2$. In the commutative layers, which have no direction, both the element and its coefficients carry the number of the element, $Q_1 = q_1 + iq'_1$. The two indices are of different kinds, a letter against a number, so a coefficient index is never read as the number of an element, nor the reverse.

**It is allowed to add subscripts when several elements of the same kind are used.** The permission covers the units, the roots, the idempotents and the nilpotents as well as the general elements: wherever a statement carries more than one element of one kind, the occurrences are told apart by a subscript.

**A subscript counts, or it names.** A subscript that only tells one occurrence from another is numeric, so that a family is $\tilde Q_1, \tilde Q_2, \dots$ and a second numbered family of the same statement takes the next numbers. A subscript that names the object or the role it qualifies is a **role label**, and a role label is written in upright roman, as in $\mathbb{B}_{\mathrm{red}}$ and $\tilde U_{\mathrm b}$.

**A role-labelled element carries its label in its coefficients.** The generic element-valued field is $\tilde Q_{\mathrm f}=Q_{\mathrm{f}t}e_t+\vec Q_{\mathrm f}$, and its components are $Q_{\mathrm{f}t}$ and $Q_{\mathrm{f}\mu}$: the label $\mathrm f$ belongs to the element and is carried once into the component subscript, beside the direction, so that the components are $Q_{\mathrm{f}t}$ and $Q_{\mathrm{f}\mu}$; it does not count a family. A numbered family is unaffected, $\tilde Q_1=Q_{1t}e_t+\vec Q_1$.

**An angular-momentum total takes the role subscript, and its projection the axis.** A spin label is $s$ with projection $s_z$; the total of an orbital and a spin part, or of several spins, is $s_{\mathrm{tot}}$ with projection $s_{\mathrm{tot},z}$. The generator is $\tilde S_k=\tfrac12i\vec e_k$; the tilde marks the operator and keeps it distinct from the simple module $S$ and its minimal left ideals $S_\pm(\vec u)$. The total generator carries the role subscript and the vector index: $\tilde S_{\mathrm{tot},k}=L_k\otimes1+1\otimes\tilde S_k$ on a coupled module, and the vector index $k$ follows the role. The subscript $k$ is the vector index; the projection is the scalar weight, the eigenvalue of the third component on $|s_{\mathrm{tot}},s_{\mathrm{tot},z}\rangle$, and it names the axis $z$ of the measurement and no vector index. The role is repeated in the projection so that $s_{1z}$, $s_{2z}$ and $s_{\mathrm{tot},z}$ are told apart without the context. The role and the axis share one pair of braces, $s_{\mathrm{tot},z}$, with a comma between them. The letter $j$ is the hyperbolic unit in the biquaternion corpus and does not label a spin there; the letter $m$ is an index.

**A sign is a subscript where the statement needs one**, the member attached to $+1$ taking the subscript $+$ and the member attached to $-1$ the subscript $-$, as in $\tilde\Pi_{\mathrm{id},+}$ and $\tilde\Pi_{\mathrm{id},-}$. In the reduced biquaternion layer the sign belongs to the idempotent pair and to its coordinates, $\Pi_{\mathrm{id},\pm}$, $Q_{+}$ and $Q_{-}$, the two basis coordinates carrying the triangles, $Q_{\blacktriangle}$ and $Q_{\blacktriangledown}$, and a numbered element putting its number first in either case, $Q_{1+}$ and $Q_{1\blacktriangle}$; the element they build is $\breve Q$. The sign is read with the glyph, and no identity is implied between the pairs: $\tilde Q_\pm$ names the two quaternionic components of a split-biquaternion, $\vec Q_\pm$ their vector parts, and $Q_\pm$ the idempotent coordinates of $\breve Q$.

The kind of a potent element is the first word of its subscript, after the sector label and before the sign: $\tilde\Pi_{\mathrm{id},\Phi,\mathrm{id}}$ and $\tilde\Pi_{\mathrm{id},+}$. The tag is part of the subscript and takes no separator, so $\tilde\Pi_{\mathrm{id},1,2}(\vec u)$ carries one subscript of four words; a site whose subscript does not begin with $\mathrm{id}$ or $\mathrm{nil}$ is either a missed site or a new one, and it is checked before it is added.

The forms a subscript takes are these.

| The subscript is | Example |
|---|---|
| a digit | $\tilde Q_1$, $\tilde Q_2$ |
| a letter | $Q_k$, $Q_\mu$ |
| two indices | $Q_{ab}$ |
| a sign | $\tilde\Pi_{\mathrm{id},\pm}$ |
| an upright word | $\mathbb{B}_{\mathrm{red}}$, $\tilde U_{\mathrm b}$ |
| a grouped expression | $Q_{n+1}$ |

**The size and the family share one subscript.** A regular matrix carries the size of its array and the letters of its family in the same subscript, the size first and the family after it with no separator: $\mathsf M_{4L}$ and $\mathsf M_{4R}$ for the one-sided families, $\mathsf M_{4LR}$ and $\mathsf M_{4LR\ast}$ for the two-sided one. The family letters keep the italic capitals of the operators $L$ and $R$, against the upright roman of a role label, and the frame closes the same subscript after a comma, $\mathsf M_{4L,\mathrm{pau}}$. A bare size, as in $M_4(\mathbb{C})$, names a matrix algebra and no family.

The decorations that may stand in the subscript slot are these: all 450 distinct glyphs of the KaTeX 0.16.9 symbol table, one entry per glyph, with a single command written where several commands draw the same glyph. An entry that takes an argument is shown on $n$, and an entry that is text is written inside \text. The upper-case upsilon is left out: the letter names no object of either corpus, so a subscript that would name one is written in words.

**Binary operators.** ${}_{\pm}$, ${}_{\times}$, ${}_{\div}$, ${}_{\dagger}$, ${}_{\ddagger}$, ${}_{\mp}$, ${}_{\dotplus}$, ${}_{\setminus}$, ${}_{\ast}$, ${}_{\circ}$,
${}_{\bullet}$, ${}_{\land}$, ${}_{\lor}$, ${}_{\cap}$, ${}_{\cup}$, ${}_{\wr}$, ${}_{\uplus}$, ${}_{\sqcap}$, ${}_{\sqcup}$, ${}_{\oplus}$,
${}_{\ominus}$, ${}_{\otimes}$, ${}_{\oslash}$, ${}_{\odot}$, ${}_{\circledcirc}$, ${}_{\circledast}$, ${}_{\circleddash}$, ${}_{\boxplus}$, ${}_{\boxminus}$, ${}_{\boxtimes}$,
${}_{\boxdot}$, ${}_{\intercal}$, ${}_{\veebar}$, ${}_{\barwedge}$, ${}_{\diamond}$, ${}_{\cdot}$, ${}_{\star}$, ${}_{\divideontimes}$, ${}_{\ltimes}$, ${}_{\rtimes}$,
${}_{\leftthreetimes}$, ${}_{\rightthreetimes}$, ${}_{\curlyvee}$, ${}_{\curlywedge}$, ${}_{\Cap}$, ${}_{\Cup}$, ${}_{\lessdot}$, ${}_{\gtrdot}$, ${}_{\triangleright}$, ${}_{\bigtriangledown}$,
${}_{\triangleleft}$, ${}_{\bigcirc}$, ${}_{\amalg}$, ${}_{\doublebarwedge}$

**Relations.** ${}_{\lt}$, ${}_{\gt}$, ${}_{\in}$, ${}_{\ni}$, ${}_{\backepsilon}$, ${}_{\propto}$, ${}_{\mid}$, ${}_{\nmid}$, ${}_{\parallel}$, ${}_{\nparallel}$,
${}_{\therefore}$, ${}_{\because}$, ${}_{\sim}$, ${}_{\backsim}$, ${}_{\nsim}$, ${}_{\eqsim}$, ${}_{\simeq}$, ${}_{\cong}$, ${}_{\ncong}$, ${}_{\approx}$,
${}_{\approxeq}$, ${}_{\asymp}$, ${}_{\Bumpeq}$, ${}_{\bumpeq}$, ${}_{\doteq}$, ${}_{\Doteq}$, ${}_{\fallingdotseq}$, ${}_{\risingdotseq}$, ${}_{\eqcirc}$, ${}_{\circeq}$,
${}_{\triangleq}$, ${}_{\equiv}$, ${}_{\le}$, ${}_{\ge}$, ${}_{\leqq}$, ${}_{\geqq}$, ${}_{\lneqq}$, ${}_{\gneqq}$, ${}_{\ll}$, ${}_{\gg}$,
${}_{\between}$, ${}_{\nless}$, ${}_{\ngtr}$, ${}_{\nleq}$, ${}_{\ngeq}$, ${}_{\lesssim}$, ${}_{\gtrsim}$, ${}_{\lessgtr}$, ${}_{\gtrless}$, ${}_{\prec}$,
${}_{\succ}$, ${}_{\preccurlyeq}$, ${}_{\succcurlyeq}$, ${}_{\precsim}$, ${}_{\succsim}$, ${}_{\nprec}$, ${}_{\nsucc}$, ${}_{\subset}$, ${}_{\supset}$, ${}_{\subseteq}$,
${}_{\supseteq}$, ${}_{\nsubseteq}$, ${}_{\nsupseteq}$, ${}_{\subsetneq}$, ${}_{\supsetneq}$, ${}_{\sqsubset}$, ${}_{\sqsupset}$, ${}_{\sqsubseteq}$, ${}_{\sqsupseteq}$, ${}_{\vdash}$,
${}_{\dashv}$, ${}_{\perp}$, ${}_{\vDash}$, ${}_{\Vdash}$, ${}_{\Vvdash}$, ${}_{\nvdash}$, ${}_{\nvDash}$, ${}_{\nVdash}$, ${}_{\nVDash}$, ${}_{\vartriangleleft}$,
${}_{\vartriangleright}$, ${}_{\trianglelefteq}$, ${}_{\trianglerighteq}$, ${}_{\origof}$, ${}_{\imageof}$, ${}_{\multimap}$, ${}_{\Join}$, ${}_{\backsimeq}$, ${}_{\Subset}$, ${}_{\Supset}$,
${}_{\pitchfork}$, ${}_{\lll}$, ${}_{\ggg}$, ${}_{\lesseqgtr}$, ${}_{\gtreqless}$, ${}_{\curlyeqprec}$, ${}_{\curlyeqsucc}$, ${}_{\npreceq}$, ${}_{\nsucceq}$, ${}_{\lnsim}$,
${}_{\gnsim}$, ${}_{\precnsim}$, ${}_{\succnsim}$, ${}_{\ntriangleleft}$, ${}_{\ntriangleright}$, ${}_{\ntrianglelefteq}$, ${}_{\ntrianglerighteq}$, ${}_{\frown}$, ${}_{\smile}$, ${}_{\vartriangle}$,
${}_{\blacktriangleright}$, ${}_{\blacktriangleleft}$, ${}_{\leqslant}$, ${}_{\geqslant}$, ${}_{\lessapprox}$, ${}_{\gtrapprox}$, ${}_{\lneq}$, ${}_{\gneq}$, ${}_{\lnapprox}$, ${}_{\gnapprox}$,
${}_{\lesseqqgtr}$, ${}_{\gtreqqless}$, ${}_{\eqslantless}$, ${}_{\eqslantgtr}$, ${}_{\preceq}$, ${}_{\succeq}$, ${}_{\precneqq}$, ${}_{\succneqq}$, ${}_{\precapprox}$, ${}_{\succapprox}$,
${}_{\precnapprox}$, ${}_{\succnapprox}$, ${}_{\subseteqq}$, ${}_{\supseteqq}$, ${}_{\subsetneqq}$, ${}_{\supsetneqq}$, ${}_{\nshortmid}$, ${}_{\nshortparallel}$, ${}_{\lvertneqq}$, ${}_{\gvertneqq}$,
${}_{\ngeqq}$, ${}_{\ngeqslant}$, ${}_{\nleqslant}$, ${}_{\nleqq}$, ${}_{\nsubseteqq}$, ${}_{\varsubsetneqq}$, ${}_{\nsupseteqq}$, ${}_{\varsupsetneqq}$, ${}_{\varsubsetneq}$, ${}_{\varsupsetneq}$,
${}_{\not}$

**Arrows.** ${}_{\gets}$, ${}_{\uparrow}$, ${}_{\to}$, ${}_{\downarrow}$, ${}_{\leftrightarrow}$, ${}_{\updownarrow}$, ${}_{\nwarrow}$, ${}_{\nearrow}$, ${}_{\searrow}$, ${}_{\swarrow}$,
${}_{\nleftarrow}$, ${}_{\nrightarrow}$, ${}_{\twoheadleftarrow}$, ${}_{\twoheadrightarrow}$, ${}_{\leftarrowtail}$, ${}_{\rightarrowtail}$, ${}_{\mapsto}$, ${}_{\hookleftarrow}$, ${}_{\hookrightarrow}$, ${}_{\looparrowleft}$,
${}_{\looparrowright}$, ${}_{\leftrightsquigarrow}$, ${}_{\nleftrightarrow}$, ${}_{\Lsh}$, ${}_{\Rsh}$, ${}_{\curvearrowleft}$, ${}_{\curvearrowright}$, ${}_{\circlearrowleft}$, ${}_{\circlearrowright}$, ${}_{\leftharpoonup}$,
${}_{\leftharpoondown}$, ${}_{\restriction}$, ${}_{\upharpoonleft}$, ${}_{\rightharpoonup}$, ${}_{\rightharpoondown}$, ${}_{\downharpoonright}$, ${}_{\downharpoonleft}$, ${}_{\rightleftarrows}$, ${}_{\leftrightarrows}$, ${}_{\leftleftarrows}$,
${}_{\upuparrows}$, ${}_{\rightrightarrows}$, ${}_{\downdownarrows}$, ${}_{\leftrightharpoons}$, ${}_{\rightleftharpoons}$, ${}_{\nLeftarrow}$, ${}_{\nLeftrightarrow}$, ${}_{\nRightarrow}$, ${}_{\Leftarrow}$, ${}_{\Uparrow}$,
${}_{\Rightarrow}$, ${}_{\Downarrow}$, ${}_{\Leftrightarrow}$, ${}_{\Updownarrow}$, ${}_{\Lleftarrow}$, ${}_{\Rrightarrow}$, ${}_{\leadsto}$, ${}_{\dashleftarrow}$, ${}_{\dashrightarrow}$, ${}_{\longleftarrow}$,
${}_{\longrightarrow}$, ${}_{\longleftrightarrow}$, ${}_{\Longleftarrow}$, ${}_{\Longrightarrow}$, ${}_{\Longleftrightarrow}$, ${}_{\longmapsto}$

**Large operators.** ${}_{\prod}$, ${}_{\coprod}$, ${}_{\sum}$, ${}_{\int}$, ${}_{\iint}$, ${}_{\iiint}$, ${}_{\oint}$, ${}_{\oiint}$, ${}_{\oiiint}$, ${}_{\bigwedge}$,
${}_{\bigvee}$, ${}_{\bigcap}$, ${}_{\bigcup}$, ${}_{\bigodot}$, ${}_{\bigoplus}$, ${}_{\bigotimes}$, ${}_{\biguplus}$, ${}_{\bigsqcup}$

**Symbols.** ${}_{\text{\textdollar}}$, ${}_{\text{\textasciicircum}}$, ${}_{\text{\textbar}}$, ${}_{\text{\textasciitilde}}$, ${}_{\pounds}$, ${}_{\yen}$, ${}_{\neg}$, ${}_{\circledR}$, ${}_{\degree}$, ${}_{\wp}$,
${}_{\mho}$, ${}_{\Game}$, ${}_{\forall}$, ${}_{\complement}$, ${}_{\partial}$, ${}_{\exists}$, ${}_{\nexists}$, ${}_{\emptyset}$, ${}_{\tilde\nabla_\Phi}$, ${}_{\surd}$,
${}_{\infty}$, ${}_{\angle}$, ${}_{\measuredangle}$, ${}_{\sphericalangle}$, ${}_{\top}$, ${}_{\varvdots}$, ${}_{\circledS}$, ${}_{\diagup}$, ${}_{\diagdown}$, ${}_{\blacksquare}$,
${}_{\Box_\Phi}$, ${}_{\blacktriangle}$, ${}_{\blacktriangledown}$, ${}_{\Diamond}$, ${}_{\bigstar}$, ${}_{\spadesuit}$, ${}_{\heartsuit}$, ${}_{\diamondsuit}$, ${}_{\clubsuit}$, ${}_{\flat}$,
${}_{\natural}$, ${}_{\sharp}$, ${}_{\checkmark}$, ${}_{\maltese}$, ${}_{\blacklozenge}$

**Letters.** ${}_{\text{\\AE}}$, ${}_{\text{\O}}$, ${}_{\text{\ss}}$, ${}_{\text{\ae}}$, ${}_{\eth}$, ${}_{\text{\o}}$, ${}_{\text{\i}}$, ${}_{\text{\OE}}$, ${}_{\text{\oe}}$, ${}_{\text{\j}}$,
${}_{\Gamma}$, ${}_{\Delta_\Phi}$, ${}_{\Theta}$, ${}_{\Lambda}$, ${}_{Ζ}$, ${}_{\Pi_{\mathrm{id}}}$, ${}_{\Sigma}$, ${}_{\Phi}$, ${}_{\Psi}$,
${}_{\Omega}$, ${}_{\alpha}$, ${}_{\beta}$, ${}_{\gamma}$, ${}_{\delta}$, ${}_{\varepsilon}$, ${}_{\omega}$, ${}_{\eta}$, ${}_{\theta}$, ${}_{\iota}$,
${}_{\kappa}$, ${}_{\lambda}$, ${}_{\mu}$, ${}_{\nu}$, ${}_{\zeta}$, ${}_{\omicron}$, ${}_{\pi}$, ${}_{\rho}$, ${}_{\varsigma}$, ${}_{\sigma}$,
${}_{\tau}$, ${}_{\upsilon}$, ${}_{\varphi}$, ${}_{\chi}$, ${}_{\psi}$, ${}_{\omega}$, ${}_{\vartheta}$, ${}_{\phi}$, ${}_{\varpi}$, ${}_{\digamma}$,
${}_{\varkappa}$, ${}_{\varrho}$, ${}_{\epsilon}$, ${}_{\Im}$, ${}_{\ell}$, ${}_{\Re}$, ${}_{\Finv}$, ${}_{\aleph}$, ${}_{\beth}$,
${}_{\gimel}$, ${}_{\daleth}$, ${}_{\imath}$, ${}_{\jmath}$

**Delimiters.** ${}_{\lparen}$, ${}_{\rparen}$, ${}_{\lceil}$, ${}_{\rceil}$, ${}_{\lfloor}$, ${}_{\rfloor}$, ${}_{\lmoustache}$, ${}_{\rmoustache}$, ${}_{\ulcorner}$, ${}_{\urcorner}$,
${}_{\llcorner}$, ${}_{\lrcorner}$, ${}_{\langle}$, ${}_{\rangle}$, ${}_{\lgroup}$, ${}_{\rgroup}$

**Ellipses.** ${}_{\ldots}$, ${}_{\cdots}$, ${}_{\ddots}$

**Punctuation.** ${}_{\#}$, ${}_{\%}$, ${}_{\&}$, ${}_{\ldotp}$, ${}_{\lbrack}$, ${}_{\backslash}$, ${}_{\rbrack}$, ${}_{\_}$, ${}_{\{}$, ${}_{\}}$,
${}_{\S}$, ${}_{\P}$, ${}_{\text{\textendash}}$, ${}_{\text{\textemdash}}$, ${}_{\text{\textquoteleft}}$, ${}_{\text{\textquoteright}}$, ${}_{\text{\textquotedblleft}}$, ${}_{\text{\textquotedblright}}$, ${}_{\prime}$, ${}_{\backprime}$

**Accents.** ${}_{\ddot{n}}$, ${}_{\c{n}}$, ${}_{\^{n}}$, ${}_{\v{n}}$, ${}_{\={n}}$, ${}_{\'{n}}$, ${}_{\`{n}}$, ${}_{\u{n}}$, ${}_{\.{n}}$, ${}_{\r{n}}$,
${}_{\~{n}}$, ${}_{\H{n}}$, ${}_{\vec{n}}$

**Spacing.** The command ${}_{\ }$ draws no mark; it sets a space.

Beyond the table the slot takes any expression: an upright word, ${}_{\mathrm{tor}}$; a text string, ${}_{\text{word}}$; a nested index, ${}_{i_1}$; and the compound ${}_{\natural*}$ that the biquaternion articles use.

## A Word and Two Letters

**The word "interval".** In the mathematical corpus an **interval** is an order-theoretic object: a convex subset of a linearly ordered set, the interval $[a,b]=\{x:a\le x\le b\}$ of a lattice or of a poset of effects, defined by the order and not by a form. The value of a quadratic form is never called an interval here; where a sign must be named, the corpus writes *the form value* or *the quadratic form*.

**The letter $\iota$ is not used in Part VI.** Every article registered under *Part VI : Synthetic Studies* of `maths.md` writes no $\iota$, in any spelling. The letter is not reserved there and names no object of those studies: a comparison with a Clifford algebra is written by its values or by the words "the Clifford image", an interior product as the pairing $\omega(X_f,\,\cdot\,)=df$, and an inner automorphism in words. A display in Part VI that introduces $\iota$ is defective.

**The deformation parameter is $h_{\mathrm{def}}$.** The formal parameter of a star product, of a Weyl quantisation $\mathrm{Op}^w$ and of the semiclassical calculus is dimensionless and is written $h_{\mathrm{def}}$; no other symbol carries it.

## LaTeX and Typesetting

Inline mathematics is written between single dollars and never across a line break; display mathematics between double dollars on lines of their own, indented four spaces inside a list; tables are Markdown tables and never a LaTeX array. A heading that introduces a comparison or a classification is a real `###` heading, and the objects are defined before they are tabulated.

**Bold marks the result** in the prose of a Remark or in the lead sentence of a section, the object staying in plain roman: *the subspace **is a commutative Jordan algebra over $\mathbb{R}$ of degree two***; a displayed Theorem, Proposition or Proof is not bolded. The third derivative is `d^3/dt^3`, a gamma contraction is written out, and the characters `|`, `{`, `}`, `<` and `>` inside mathematics need no escaping. A malformed formula is rendered in red rather than reported as an error, so mathematics is checked by eye.
## Summary

A **label** is the upright roman name of a variant, two or three letters, lowercase, always in the subscript and never in the caret; where an index is already there, the label comes first and the index follows after a comma. A **subscript** takes a single token, so a two-letter label costs a brace. The **caret** carries a power, a conjugation, a transposition and a construction, and neither a label nor an index. Two labels run beside the glyphs: $\mathrm{fop}$ for a Fock operator and $\mathrm{opp}$ for the opposite algebra, read for one another by nobody. No index is raised anywhere in the corpus, and a contraction is a form.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{fop}$ | A Fock operator, an operator on the Fock space and not an element of the algebra; a label, low |
| $\mathrm{opp}$ | The opposite algebra, the algebra with the reversed product, and an element read in it where it names a tensor factor; a label, low; the two-letter $\mathrm{op}$ is not one |
| $\mathrm{opp}$, $\mathrm{fop}$, $\mathrm{axf}$, $\mathrm{nil}$ | The three-letter labels of a construction, a frame or a variant of an object; the full index is §*The Three-Letter Labels* |
| $L_{\mathrm{axf},e_\mu}$, $V_{\mathrm{fin},K}$ | A label in the subscript, first in the field, with the index that was already there after it and a comma between them; no label stands in the caret |
| $\mathrm{fn}$, $\mathrm{ab}$, $\mathrm{ax}$, $\mathrm{sp}$ | The two-letter labels, the word shortened to its initials or to its consonants, $\mathrm{sa}$ the self-adjoint part, $\mathrm{bl}$ the blow-up; $\mathrm{sp}$ is the spinor, the Dirac field $\tilde\Xi_{\mathrm{sp}}$ and the reading that $\mathrm{pau}$ gives as the Pauli one. The full index is §*The Two-Letter Labels* |
| $\mathrm{rgs}$, $\mathrm{tpl}$, $\mathrm{prm}$, $\mathrm{dfc}$, $\mathrm{obf}$, $\mathrm{adg}$ | The six codes that separate two words sharing one spelling: regularised from regular, topological from top, perimeter from periodic, defective from defining, orbifold from orbital, adjugate from adjoint; a code is cheaper than a second meaning on the same letters |

| $\operatorname{sym}$, $\operatorname{gal}$ | An operator name written in the caret with its argument, $\operatorname{sym}(P)$, $\gamma_n^{\operatorname{sym}}$, $K^{\operatorname{gal}(K/F)}$; lowercase, and read by its argument |
| $\tilde Q_1\tilde Q_2$, $\tilde Q_1\tilde Q_2^{*}$, $\tilde Q_1^{\natural}\tilde Q_2$, $\tilde Q_1^{\natural}\tilde Q_2^{*}$, $\tilde Q_1\bullet\tilde Q_2$, $\tilde Q_1\bullet_{*}\tilde Q_2$, $\tilde Q_1\bullet_{\natural}\tilde Q_2$, $\tilde Q_1\bullet_{\natural*}\tilde Q_2$, $\tilde Q_1\wedge\tilde Q_2$, $\tilde Q_1\wedge_{*}\tilde Q_2$, $\tilde Q_1\wedge_{\natural}\tilde Q_2$, $\tilde Q_1\wedge_{\natural*}\tilde Q_2$ | The twelve products of the algebraic structures, written by their two slots and the conjugation each one carries, never by a code: four general products, their four symmetric parts with $\bullet$ and their four antisymmetric parts with $\wedge$, the class carried by the subscript ${}_{*}$, ${}_{\natural}$, ${}_{\natural*}$ |
| $\mathrm{fn}$ | A function from a domain into the algebra; a two-letter label, §*The Two-Letter Labels* |
| $\mathrm{spin}$ | An element of $\mathrm{Spin}(n)$ or $\mathrm{Pin}(n)$ on a principal bundle; a label, low |
| `- Theory`, `- Operator Theory`, `- * Theory`, `- * Operator Theory` | The four groups of a category, in that order |
| `- Applications` | The group that closes a category with the concrete instances of its structure |
| `+` | A planned article, registered in the menu and not yet written |
| `articles_maths/<slug>.md` | The file of a mathematical article; the slug is the title in lower case with hyphens |
| Introduction, thematic sections, Summary, Summary of Notation, Further Reading | The skeleton of every article |
| $s_{\mathrm{tot}}$, $s_{\mathrm{tot},z}$, $\tilde S_{\mathrm{tot},k}$ | Total angular-momentum label, its projection, and the total generator; the orbital part is $L_k$ here and $\tilde L_k$ in the physical corpus |

## Further Reading

- Nicolas Bourbaki, *Éléments de mathématique* (Hermann, then Springer). The model for a notation fixed once and used without variation.
- Donald E. Knuth, *The TeXbook* (Addison-Wesley, 1984). The typographic conventions the source of the corpus follows.
