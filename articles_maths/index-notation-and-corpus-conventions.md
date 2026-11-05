# __Index, Notation and Corpus Conventions__

## Introduction

This article closes the series with the marks that are read on a glyph rather than on the object: the superscript tokens and the labels they carry, the subscript rules and their admitted forms, the working conventions of the corpus and the typography of the source. It assumes the eight companions, whose glyphs it indexes.

The superscripts come first because the tokens are two and their labels are an index of three letters; the subscripts next, because their rule depends on the derivation convention fixed in *Operator and Calculus Conventions*. The working conventions of the corpus follow — the menus, the groups inside a category, the article files, the skeleton and the boundaries — and the typography closes the article.

The article is the ninth of the ten and the index of the notation: the table below collects the tokens and the working marks that belong to the corpus rather than to the algebra, while the table of *Algebra and Element Conventions* collects the glyphs of the algebra.

## The Upper and Low Marks

**These rules are real, and partial.** They fix the marks of the common uses and they bind wherever they apply. They do not cover every use: a mark that falls outside them is governed by the section that fixes it, and a stricter rule stated in the corpus overrides them — the derivation convention of *Operator and Calculus Conventions*, §*Conventions for Derivation*, the Fock and opposite tokens of §*The Superscripts*, and the forms of §*The Subscripts*.

**A caret is the exclusive carrier of those things:**

- a power, $2^k$, $e^\lambda$, $(-1)^j$, $\alpha^k$, $2^{k/2-1}$;
- a conjugation, $a^{*}$, $a^{\dagger}$, $a^{\natural}$;
- a transposition, $L^T$, $\psi^T$;
- a construction, $\mathbb{B}^\times$, $S^{\otimes n}$, $\mathrm{sym}^l$, $\Lambda^kTM$ (degree);
- a label naming the object, $\mathrm{opp}$, $\mathrm{fop}$, $\mathrm{axf}$, $\mathrm{nil}$, and the rest of §*The Three-Letter Labels*.

**A low mark is the exclusive carrier of two things: an index and a label.**

- an index — a numeric count, $Q_1$, $M_2$; the slot of a coordinate, $q_i$, $x_i$, $p_i$, $Q_i$, $\theta_i$, $\xi_k$, $v_i$; the slot of a basis vector or a gamma, $\vec e_i$, $\gamma_i$; the slots of an invariant symbol, $\delta_{ij}$, $\varepsilon_{ijk}$, $\eta_{ij}$; the generator of a gauge, colour, isospin or spin family, $T_a$, $G_a$, $\sigma_z$; the slot of a connection or curvature component, $\Gamma_k$, $R_{ij}$, $\omega_i$, $g_{ij}$; the slot of a differential, $dx_i$.
- a label naming a part or a role, $s_{\mathrm{tot}}$, $S_{\mathrm{int}}$, with the labels of §*The Three-Letter Labels* read in the two slots; the family letters of a regular matrix are of this kind, $L$ and $R$ naming the left and the right part, $\mathsf M_{4L}$ and $\mathsf M_{4R}$.

**The word *metric* has one meaning in the corpus. There is one metric, the unit metric $\delta_{\mu\nu}=(1,1,1,1)$: diagonal, all four coefficients $+1$, the matrix of the interval $\sum_\mu Q_\mu^2$. A frame carries a coordinate, not a metric. The minus of the material sector is not a metric: it is $i^2=-1$ in $Q_t=iq'_t$, made once on the time.**

**No index is raised, because the one metric is the identity.** The series has one metric, the unit metric $\delta_{\mu\nu}=(1,1,1,1)$, and raising with it changes nothing: a raised index would be the same index. A gamma is written low, $\gamma_\mu$, and the weight does the only work a raising could do, $\gamma^\mu=-\varepsilon_\mu\gamma_\mu$. A text that needs a raised index on a coefficient is writing a metric the corpus does not have.

**The object is not the role.** A coordinate, a basis vector, a gamma, an invariant symbol, a gauge generator, a component of a connection and a differential are seven kinds of object, and the low mark does one thing on all seven: it gives the index that names the slot of the family the glyph belongs to. The index says **which** member, never **what kind**, and the kind is carried by the glyph itself, $x_i$ against $\gamma_i$ against $\delta_{ij}$. A differential carries the same mark as the coordinate it differentiates, $x_i$ and $dx_i$, because the slot is the same in both. Nor does the alphabet divide the work: a letter is an index in $q_i$ and a number is an index in $Q_1$, and the two are of different kinds only where a coefficient and an element meet (§*The Subscripts*).

**The lists rule on these uses, not on the names.** A raised grade, parameter, sector or order is a name, not a power, a conjugation, a transposition or a construction, and the article that uses it says which name it is. A label is a name of that kind, and the slot says what it names: on the caret it names the object the glyph denotes, $\mathbb{B}^{\mathrm{opp}}$, $a^{\mathrm{fop}}$, $L^{\mathrm{axf}}$, and low it names a part or a role of that object, $s_{\mathrm{tot}}$, $S_{\mathrm{int}}$, and it is then a subscript label.

## The Superscripts

Two superscript tokens run beside the marks of the elements and the marks of the conjugations, on the glyphs of elements and algebras, and neither is to be read for the other:

| Token | Written on | Meaning |
|---|---|---|
| $^{\mathrm{fop}}$ | a Fock-operator glyph | an operator on the Fock space, the Fock-operator mark |
| $^{\mathrm{opp}}$ | an algebra name, or an element naming a tensor factor | the opposite algebra, the algebra with the reversed product; never the two-letter $\mathrm{op}$ |

Two further upright superscripts belong to objects outside the algebra — $\mathrm{fn}$ on a function and $\mathrm{spin}$ on a group element — and are recorded in §*Summary of Notation*.

**A caret marks a power or a name, never a frame slot.** The superscript slot carries the tokens above, and on an object it carries a power or a name: $e^\lambda$, $2^k$ and $(-1)^k$ are powers; $M_4^\sigma$ and $B^\sigma$ are names; and the names $\mathrm{Cl}_i$ and $K_0$ carry their index low. A coordinate, a field component, a basis vector, a gamma and a sign symbol are written with a low index — $x_\mu$, $A_\mu$, $\vec e_i$, $\gamma_i$, $\varepsilon_{ijk}$ — and a contraction is written as an explicit sum with the sign vector or as the quaternionic product that carries it: the form $\langle\tilde\nabla,\tilde Q_{\mathrm f}\rangle_{\natural}$ for a derivative with a field, and $\langle\tilde\nabla\rangle_{\natural}=\Box$ for two derivatives (*Operator and Differential Calculus Conventions*, §*The Krein Product, Its Form and Its Norm*). Where a contraction is written with indices, the sum names the summed index — $\sum_\mu e_\mu\partial/\partial Q_\mu$, $\sum_k\vec e_kA_k$ — and is never a repeated index left to the summation convention. The rule is the one of the physical corpus (*Operator and Calculus Conventions*, §*Conventions for Derivation*).

**The mark, and its one use.** The marks of the elements say what a glyph **is**, not that it is an **operator** (*Operator and Calculus Conventions*, §*The Operators*). The single exception is the **Fock layer** of the physical corpus, whose operators act on a Fock space and are **not** elements of the algebra. Only these carry the upright superscript $\mathrm{fop}$, set on the glyph:

$$
a^{\mathrm{fop}},\quad b^{\mathrm{fop}},\quad a^{\mathrm{fop}\dagger},\quad \psi^{\mathrm{fop}},\quad N^{\mathrm{fop}},\quad H^{\mathrm{fop}},\quad F^{\mathrm{fop}},\quad Q^{\mathrm{fop}},\quad U^{\mathrm{fop}} .
$$

The mark says exactly one thing — the glyph is not an element, it is an operator on the Fock space — and it is written on nothing else. It is not a general mark of operators: the momentum $\vec p$, the position $x$, the spin $S$ and the parity, charge-conjugation and reversal maps $P$, $C$ and $T$ carry no superscript, because each keeps the glyph of its element or is a map with a glyph of its own.

**It combines with the dagger, the mark first.** The dagger is the general adjoint (*Operator and Calculus Conventions*, §*The Operators*). Where both marks fall on one glyph the Fock mark comes first and the adjoint follows, $(a^{\mathrm{fop}})^{\dagger}$, contracted to $a^{\mathrm{fop}\dagger}$; the dagger alone never marks a glyph as an operator, and the superscript alone never asserts self-adjointness.

**The opposite algebra carries a different token.** The **opposite algebra**, whose multiplication is reversed, $a\cdot b=ba$, carries the superscript $\mathrm{opp}$ — $A^{\mathrm{opp}}$, $\mathbb{B}^{\mathrm{opp}}$, $M_n(D)^{\mathrm{opp}}$ — and it is the **algebra name** that takes the mark; the Fock token $\mathrm{fop}$ marks a Fock-operator glyph. The two meanings are separated by the token itself and not by context.

**On an element the mark names a tensor factor.** Written on an element it means the same element read in the opposite algebra, $e_\nu^{\mathrm{opp}}$, and it is written there for that one purpose: to name the second factor of the tensor product $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}$, whose elementary tensors $e_\mu\otimes e_\nu^{\mathrm{opp}}$ are the cells $L_{e_\mu}R_{e_\nu}$ of the two-sided operators. The element is not thereby an operator, the mark says nothing about a side, and on an operator glyph it is a defect. It marks an algebra, a module of one, and an element read in that algebra; it never marks a set or a bare vector space.

**The two-letter form $\mathrm{op}$ is forbidden.** It differs from $\mathrm{opp}$ by one letter, at the size a superscript is set, and a page carrying both would be undecidable at reading speed. It is therefore not a token of the corpus in any sense. In particular it does not mark the operator norm: the norm is written $\lVert A\rVert$ bare, and the norms it is compared with carry their own labels, $\lVert A\rVert_{\mathrm{HS}}$, $\lVert A\rVert_{\mathrm{nuc}}$, $\lVert A\rVert_F$, $\lVert A\rVert_*$, so that the unmarked bar is the operator norm by default and never by elimination. It does not mark an operator either: an operator glyph is the element's glyph, and the explicit form is written where the letter is taken, as in the gradient $\tilde\nabla$ and the momentum $-i\hbar\nabla$.

**A caret carries a label as it carries a power.** Beyond the two tokens, the caret is the slot where the corpus names a variant of its object, in upright roman letters: $\mathbb{B}^{\mathrm{opp}}$, $a^{\mathrm{fop}}$, $L^{\mathrm{axf}}$, $\partial^{\mathrm{nil}}$, $\pi_1^{\mathrm{orb}}$. Italic is a power and upright is a name, so the two are told apart at sight, and a label is never read as an exponent: $L_{\vec e_x}^{\mathrm{axf}}$ is the matrix of $\vec e_x$ in the axis-free frame and not the $x$-th power of an operator. **The label is three lowercase letters by default**, and for the reason that forbids $\mathrm{op}$ beside $\mathrm{opp}$ — one letter out of three, at the size a superscript is set, does not separate two meanings; a fourth letter is admitted where three do not carry the word, $\mathrm{lift}$, $\mathrm{dual}$, $\mathrm{deph}$, $\mathrm{refl}$, and the shorthands $\mathrm{fn}$ and $\mathrm{spin}$ of §*Summary of Notation* are of the same kind. The table below is the index of the three-letter labels of the corpus.

### The Three-Letter Labels

The table is an index of labels and not a list of tokens: a label names an object, a construction, a frame or a variant of one, the article that introduces it fixes what it abbreviates, and a label enters the table with that article.

**The section holds two tables.** The first indexes the caret for the labels that name an object, a construction, a frame or a variant, and it carries seventy-nine rows, one of which, $\mathrm{lcm}$, is written by its operator name and never as a label. The second table carries the thirty angle labels.

**The split is the rule of the angle applied to the caret.** Where one formula holds two angles the first keeps the bare $\theta$ and the second takes a label, so an angle label names a role and not an object, and the two tables never share a row: a label of an object may stand in either slot, an angle label stands only in the caret of $\theta$. Sixty-nine labels stand only in the low slot and are outside both tables, and they, with the thirteen that stand in both slots, are counted in *The Lower Labels and the Obstruction to the Caret*.

**Every label is written in lowercase.** The caret is set at superscript size, where the case of a three-letter word is not read reliably, so the corpus writes every one of them in lowercase; the rule is the one that forbids the two-letter $\mathrm{op}$ beside $\mathrm{opp}$, applied to case instead of to length.

**No three-letter token in the caret carries a capital.** The rule is total, and it reaches two families. A label, $\mathrm{opp}$, $\mathrm{fop}$, $\mathrm{axf}$. And an **operator name** written in the caret with its argument, $\gamma_n^{\operatorname{sym}}$ on a divided-power structure, and the fixed field $K^{\operatorname{gal}(K/F)}$ — here the caret carries the acting group as $K^{\sigma}$ carries an automorphism, so the word does not name a variant of $K$ and stays out of the table below. The twelve algebraic structures carry no code at all: a product is written by its two slots and the conjugation each one carries, $\tilde Q_1\tilde Q_2$, $\tilde Q_1\tilde Q_2^{*}$, $\tilde Q_1^{\natural}\tilde Q_2$, $\tilde Q_1^{\natural}\tilde Q_2^{*}$, $\tilde Q_1\bullet\tilde Q_2$, $\tilde Q_1\bullet_{*}\tilde Q_2$, $\tilde Q_1\bullet_{\natural}\tilde Q_2$, $\tilde Q_1\bullet_{\natural*}\tilde Q_2$, $\tilde Q_1\wedge\tilde Q_2$, $\tilde Q_1\wedge_{*}\tilde Q_2$, $\tilde Q_1\wedge_{\natural}\tilde Q_2$, $\tilde Q_1\wedge_{\natural*}\tilde Q_2$, and the operator names the structure of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* on its own. A code is written in the caret, on the object it qualifies: $h^{\mathrm{tpl}}$ the topological entropy, $\Lambda^{\mathrm{top}}$ the top exterior power. The low slot of a code is a defect, as a capital in the caret is. A capital in any of these positions is a defect. **Six codes of a second kind separate two spellings.** Where one three-letter word carries two English words, the rarer reading takes a code of its own, made the same way and written in the same place: $\mathrm{rgs}$ beside $\mathrm{reg}$, $\mathrm{tpl}$ beside $\mathrm{top}$, $\mathrm{prm}$ beside $\mathrm{per}$, $\mathrm{dfc}$ beside $\mathrm{def}$, $\mathrm{obf}$ beside $\mathrm{orb}$, $\mathrm{adg}$ beside $\mathrm{adj}$. Each of the six names one word only, and a glyph may carry either member of a pair. The caret therefore carries six codes in all, and every one of them is lowercase.

**A label that names the object is written on the caret; a label that names a part stays low.** Three cases keep the low slot. One is the indexed label, where the label and an index are one field, $s_{\mathrm{tot},z}$, $\tilde K^{\mathrm{mod}}_{W}$, $\tilde H_{\mathrm{pos},l}$. One is the part or the role, $\lVert A\rVert_{\mathrm{nuc}}$, $M_{\mathrm{tor}}$, $S_{\mathrm{int}}$, $E_{\mathrm{vac}}$. One is the operator name, $\operatorname{col}A$, $\operatorname{row}A$, $\sum_{\mathrm{cyc}}$. Fifteen labels name the object and were written low in the earlier corpus; each is now on the caret and each is in the table above: $\mathrm{aff}$, $\mathrm{amp}$, $\mathrm{app}$, $\mathrm{est}$, $\mathrm{geo}$, $\mathrm{hom}$, $\mathrm{hyp}$, $\mathrm{iso}$, $\mathrm{lab}$, $\mathrm{mat}$, $\mathrm{mix}$, $\mathrm{mot}$, $\mathrm{obs}$, $\mathrm{pot}$, $\mathrm{src}$. Thirteen qualifiers that already named the same object on the caret were written low as well, and they are now on the caret: $\mathrm{ret}$, $\mathrm{odd}$, $\mathrm{sgn}$, $\mathrm{opp}$, $\mathrm{fix}$, $\mathrm{lin}$, $\mathrm{nil}$, $\mathrm{wkb}$, $\mathrm{rep}$, $\mathrm{exp}$, $\mathrm{pol}$, $\mathrm{new}$, $\mathrm{imp}$. Six more carried two English words on one spelling; each took a code of its own and rose, and the six pairs are in §*The Three-Letter Labels*.

| Label | Names |
|---|---|
| $\mathrm{adg}$ | the adjugate matrix, $A^{\mathrm{adg}}$, the reading that shared $\mathrm{adj}$ before the code was made |
| $\mathrm{adj}$ | the adjoint spin of a representation |
| $\mathrm{aff}$ | the affine Weyl group of a root system |
| $\mathrm{alg}$ | the algebraic left multiplication |
| $\mathrm{amp}$ | the amplitude of a forced solution |
| $\mathrm{app}$ | the apparent transverse speed |
| $\mathrm{arc}$ | the arc-length parametrisation of a curve |
| $\mathrm{aut}$ | the automorphism attached to a triple isomorphism |
| $\mathrm{avg}$ | the group average of a projection |
| $\mathrm{axf}$ | the axis-free frame |
| $\mathrm{can}$ | the canonical energy–momentum tensor |
| $\mathrm{cop}$ | the coproduct of a Hopf algebra |
| $\mathrm{cov}$ | the universal cover here, the covariant fundamental solution there |
| $\mathrm{cts}$ | the continuous dual |
| $\mathrm{def}$ | the defining spin; the deformation stratum |
| $\mathrm{dfc}$ | the defective part, $\Sigma_{10}^{\mathrm{dfc}}$ |
| $\mathrm{dif}$ | the difference, or antisymmetrised, product |
| $\mathrm{epr}$ | the value of the EPR steering parameter |
| $\mathrm{est}$ | an unbiased estimator |
| $\mathrm{exp}$ | the experimental value |
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
| $\mathrm{inc}$ | the incident field |
| $\mathrm{ind}$ | the induced character |
| $\mathrm{inv}$ | the invariant measure |
| $\mathrm{iso}$ | the maximal isotropic real plane |
| $\mathrm{kin}$ | kinetic: the kinetic term, energy, or momentum |
| $\mathrm{lab}$ | the laboratory frame |
| $\mathrm{lcm}$ | the least common multiple |
| $\mathrm{lin}$ | the linearisation |
| $\mathrm{lor}$ | the Lorentz object, the group or the Green function |
| $\mathrm{mat}$ | the matrix imaginary, the image of the scalar imaginary |
| $\mathrm{mhv}$ | the MHV amplitude |
| $\mathrm{mix}$ | the mixture of a pair of states |
| $\mathrm{mod}$ | the modified Lagrangian here, the modular Hamiltonian there |
| $\mathrm{mon}$ | the monogenic Fischer operator |
| $\mathrm{mot}$ | the motional electric field |
| $\mathrm{new}$ | the new subspace |
| $\mathrm{nil}$ | the nilpotent direction |
| $\mathrm{obf}$ | the orbifold Euler characteristic, $\chi^{\mathrm{obf}}$ |
| $\mathrm{obs}$ | the observed frequency |
| $\mathrm{odd}$ | the odd part of a graded algebra |
| $\mathrm{old}$ | the old subspace |
| $\mathrm{opp}$ | the opposite algebra |
| $\mathrm{orb}$ | the orbital generators |
| $\mathrm{out}$ | the outgoing solution |
| $\mathrm{pau}$ | the standard Peirce frame of the regular matrices, $L^{\mathrm{pau}}(\tilde Q)$ |
| $\mathrm{per}$ | the periodic cyclic complex; the periodic integration domain |
| $\mathrm{pol}$ | the polarisation vector |
| $\mathrm{pot}$ | the potential energy |
| $\mathrm{pre}$ | the presheaf |
| $\mathrm{prm}$ | the perimeter coefficient, $\mu^{\mathrm{prm}}$ |
| $\mathrm{red}$ | the reduced object |
| $\mathrm{reg}$ | the regular representation, $\rho^{\mathrm{reg}}$, $\operatorname{Tr}^{\mathrm{reg}}$, $\chi^{\mathrm{reg}}$ |
| $\mathrm{rel}$ | the relative transfer |
| $\mathrm{rep}$ | the representing function |
| $\mathrm{res}$ | the residual part; the residue field |
| $\mathrm{ret}$ | the retarded field |
| $\mathrm{rev}$ | the reversed process |
| $\mathrm{rgs}$ | the regularised kernel, $G_R^{\mathrm{rgs}}$ |
| $\mathrm{set}$ | the underlying set of a structure |
| $\mathrm{sgn}$ | the sign |
| $\mathrm{src}$ | the source point of a short-time kernel |
| $\mathrm{str}$ | the structure group |
| $\mathrm{sub}$ | the submultiplicative seminorm |
| $\mathrm{sym}$ | the symmetrised form; on a divided-power structure, the symmetric one |
| $\mathrm{top}$ | the top exterior power |
| $\mathrm{tot}$ | the total tensor |
| $\mathrm{tpl}$ | the topological entropy and susceptibility, $h^{\mathrm{tpl}}$ |
| $\mathrm{vol}$ | the volume cell of a frame, $\mathsf{V}^{\mathrm{vol}}$, the chirality operator of the frame |
| $\mathrm{wkb}$ | the WKB approximation |

**The second table is the angle family.** Each row is a role that a second angle plays in one formula, and the glyph is the same in every row: the label is what tells one angle from another. The table reads alphabetically by the label, and no angle label names an object — the object is the element and the angle is one of its coordinates.

| Label | Names |
|---|---|
| $\theta^{\mathrm{axc}}$ | the axicon angle of a Bessel beam |
| $\theta^{\mathrm{axr}}$ | the rotation angle about an arbitrary axis |
| $\theta^{\mathrm{axs}}$ | the rotation angle about $\vec u_y$ in the Majorana chart |
| $\theta^{\mathrm{azm}}$ | the azimuthal angle |
| $\theta^{\mathrm{blc}}$ | the angle the Bloch vector turns |
| $\theta^{\mathrm{btw}}$ | the angle between two directions |
| $\theta^{\mathrm{dfl}}$ | the small deflection angle |
| $\theta^{\mathrm{drb}}$ | the angle from the Darboux to the Frenet frame |
| $\theta^{\mathrm{drc}}$ | the direction angle of a unit vector |
| $\theta^{\mathrm{dua}}$ | the duality-rotation angle of an electromagnetic wave |
| $\theta^{\mathrm{eul}}$ | the spin angle of a symmetric top |
| $\theta^{\mathrm{foc}}$ | the colatitude of a point on the sphere |
| $\theta^{\mathrm{hpa}}$ | the hyperbolic angle of a split-complex number |
| $\theta^{\mathrm{intr}}$ | the rotation angle of the internal clock |
| $\theta^{\mathrm{lna}}$ | the angle of the line $a$ |
| $\theta^{\mathrm{lnb}}$ | the angle of the line $b$ |
| $\theta^{\mathrm{mgn}}$ | the angle between a magnetic moment and the field |
| $\theta^{\mathrm{pha}}$ | the phase angle of a complex number |
| $\theta^{\mathrm{pla}}$ | the angle in the first invariant plane |
| $\theta^{\mathrm{plb}}$ | the angle in the second invariant plane |
| $\theta^{\mathrm{prc}}$ | the precession angle of a gyroscope |
| $\theta^{\mathrm{rat}}$ | the angle a rate forms with time, $\omega t'$ |
| $\theta^{\mathrm{rgp}}$ | the second rotation angle about one axis |
| $\theta^{\mathrm{sct}}$ | the scattering angle |
| $\theta^{\mathrm{sol}}$ | the solid angle |
| $\theta^{\mathrm{stk}}$ | the rotation angle in Stokes space |
| $\theta^{\mathrm{tnp}}$ | the rotation angle in the tangent plane |
| $\theta^{\mathrm{vac}}$ | the vacuum angle of a gauge field |
| $\theta^{\mathrm{wav}}$ | the angle between a wave vector and a boost |
| $\theta^{\mathrm{wgn}}$ | the Wigner angle of a boost product |

**An angle label enters with the article that spends it, and it enters this table and not the other.** The thirty rows stand for thirty roles and 1,330 occurrences in the two corpora; the largest, $\theta^{\mathrm{hpa}}$, names the hyperbolic angle, because the exponential polar decomposition of a split-complex number recurs across a family of articles.

**A label is read in its slot.** The word is the same in the two slots and the slot says what it names: the caret names the object the glyph denotes and the low mark a part or a role of it, $s_{\mathrm{tot}}$, $S_{\mathrm{int}}$, and §*The Subscripts* rules on the low slot. One word is carried by four uses and is read with its argument: $\operatorname{sym}(P)$ the symmetric group, $\operatorname{sym}^2(E)$ the symmetric square, $\gamma_n^{\operatorname{sym}}$ the divided-power structure, $f^{\operatorname{sym}}$ the symmetrised part. The word is one and it is lowercase in all four; the argument says which. The vocabulary is not private to a slot, and it is not ambiguous either: $\mathrm{cov}$ names the universal cover in one article and the covariant fundamental solution in another, $\mathrm{res}$ names the residual part and the residue field, and the article that writes a label says which object it names. Where one spelling would name two objects that a reader must tell apart at a glance, the rarer reading takes a code of its own rather than a second height: $\mathrm{rgs}$, $\mathrm{tpl}$, $\mathrm{prm}$, $\mathrm{dfc}$, $\mathrm{obf}$, $\mathrm{adg}$ stand beside $\mathrm{reg}$, $\mathrm{top}$, $\mathrm{per}$, $\mathrm{def}$, $\mathrm{orb}$, $\mathrm{adj}$, and each of the twelve names one word only.

## The Subscripts

A subscript is written with the underscore, `_`, inside the math delimiters, and the underscore takes a single token: one character is written bare, $Q_t$ and $Q_k$, and two characters or more are wrapped in braces, $Q_{n+1}$ and $\mathbb{B}^{\mathrm{red}}$, because a bare underscore would take the first character alone. A subscript label is written in the upright roman of the caret labels, and the two lists are read together (§*The Three-Letter Labels*). The family letters $L$ and $R$ of a regular matrix are labels of that kind, and they are written italic as the letters of the operators rather than upright as a word; they follow the size in the same subscript, $\mathsf M_{4L}$ and $\mathsf M_{4R}$.

**A subscript is never a partial derivative.** The subscript is an index or a label, a partial derivative is written with $\partial$, and the rule is fixed in *Operator and Calculus Conventions*, §*Conventions for Derivation*.

**A coefficient carries a letter index and an element a number.** In the quaternionic layers a coefficient is indexed by the direction it multiplies, $Q_x$ and $q_x$, and an element that is counted carries a number on its tilde, $\tilde Q_1, \tilde Q_2$. In the commutative layers, which have no direction, both the element and its coefficients carry the number of the element, $Q_1 = q_1 + iq'_1$. The two indices are of different kinds, a letter against a number, so a coefficient index is never read as the number of an element, nor the reverse.

**It is allowed to add subscripts when several elements of the same kind are used.** The permission covers the units, the roots, the idempotents and the nilpotents as well as the general elements: wherever a statement carries more than one element of one kind, the occurrences are told apart by a subscript.

**A subscript counts, or it names.** A subscript that only tells one occurrence from another is numeric, so that a family is $\tilde Q_1, \tilde Q_2, \dots$ and a second numbered family of the same statement takes the next numbers. A subscript that names the object or the role it qualifies is a **role label**, and a role label is written in upright roman, as in $\mathbb{B}^{\mathrm{red}}$ and $\tilde U_{\mathrm b}$.

**A role-labelled element carries its label in its coefficients.** The generic element-valued field is $\tilde Q_{\mathrm f}=Q_{\mathrm{f}t}e_t+\vec Q_{\mathrm f}$, and its components are $Q_{\mathrm{f}t}$ and $Q_{\mathrm{f}\mu}$: the label $\mathrm f$ belongs to the element and is carried once into the component subscript, beside the direction, so that the components are $Q_{\mathrm{f}t}$ and $Q_{\mathrm{f}\mu}$; it does not count a family. A numbered family is unaffected, $\tilde Q_1=Q_{1t}e_t+\vec Q_1$.

**An angular-momentum total takes the role subscript, and its projection the axis.** A spin label is $s$ with projection $s_z$; the total of an orbital and a spin part, or of several spins, is $s_{\mathrm{tot}}$ with projection $s_{\mathrm{tot},z}$. The generator is $\tilde S_k$ in both corpora, with $\tilde S_k=\tfrac12i\vec e_k$ here and $\tilde S_k=\tfrac{\hbar}{2}i\vec e_k$ in the physical one; the tilde marks the operator and keeps it distinct from the simple module $S$ and its minimal left ideals $S_\pm(\vec u)$. The total generator carries the role subscript and the vector index: $\tilde S_{\mathrm{tot},k}=L_k\otimes1+1\otimes\tilde S_k$ on a coupled module here, and $\tilde S_{\mathrm{tot},k}=\tilde L_k+\tilde S_k$ in the physical corpus, where the orbital part also carries the tilde. The role is a subscript in both, and the vector index $k$ follows it. The subscript $k$ is the vector index; the projection is the scalar weight, the eigenvalue of the third component on $|s_{\mathrm{tot}},s_{\mathrm{tot},z}\rangle$, and it names the axis $z$ of the measurement and no vector index. The role is repeated in the projection so that $s_{1z}$, $s_{2z}$ and $s_{\mathrm{tot},z}$ are told apart without the context. The role and the axis share one pair of braces, $s_{\mathrm{tot},z}$, with a comma between them. The letter $j$ is the hyperbolic unit in the biquaternion corpus and does not label a spin there; the letter $m$ is the mass in the physical corpus and an index elsewhere.

**A sign is a subscript where the statement needs one**, the member attached to $+1$ taking the subscript $+$ and the member attached to $-1$ the subscript $-$, as in $\tilde\Pi_+$ and $\tilde\Pi_-$. In the reduced biquaternion layer the sign belongs to the idempotent pair and to its coordinates, $\Pi_\pm$, $Q_{+}$ and $Q_{-}$, the two basis coordinates carrying the triangles, $Q_{\blacktriangle}$ and $Q_{\blacktriangledown}$, and a numbered element putting its number first in either case, $Q_{1+}$ and $Q_{1\blacktriangle}$; the element they build is $\breve Q$. The sign is read with the glyph, and no identity is implied between the pairs: $\tilde Q_\pm$ names the two quaternionic components of a split-biquaternion, $\vec Q_\pm$ their vector parts, and $Q_\pm$ the idempotent coordinates of $\breve Q$.

The forms a subscript takes are these.

| The subscript is | Example |
|---|---|
| a digit | $\tilde Q_1$, $\tilde Q_2$ |
| a letter | $Q_k$, $Q_\mu$ |
| two indices | $Q_{ab}$ |
| a sign | $\tilde\Pi_\pm$ |
| an upright word | $\mathbb{B}^{\mathrm{red}}$, $\tilde U_{\mathrm b}$ |
| a grouped expression | $Q_{n+1}$ |

**The size and the family share one subscript.** A regular matrix carries the size of its array and the letters of its family in the same subscript, the size first and the family after it with no separator: $\mathsf M_{4L}$ and $\mathsf M_{4R}$ for the one-sided families, $\mathsf M_{4LR}$ and $\mathsf M_{4LR\ast}$ for the two-sided one. The family letters keep the italic capitals of the operators $L$ and $R$, against the upright roman of a role label, and the caret is left free for the frame, $\mathsf M_{4L}^{\mathrm{pau}}$. A bare size, as in $M_4(\mathbb{C})$, names a matrix algebra and no family.


The decorations that may stand in the subscript slot are these: all 451 distinct glyphs of the KaTeX 0.16.9 symbol table, one entry per glyph, with a single command written where several commands draw the same glyph. An entry that takes an argument is shown on $n$, and an entry that is text is written inside \text.

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
${}_{\mho}$, ${}_{\Game}$, ${}_{\forall}$, ${}_{\complement}$, ${}_{\partial}$, ${}_{\exists}$, ${}_{\nexists}$, ${}_{\emptyset}$, ${}_{\nabla}$, ${}_{\surd}$,
${}_{\infty}$, ${}_{\angle}$, ${}_{\measuredangle}$, ${}_{\sphericalangle}$, ${}_{\top}$, ${}_{\varvdots}$, ${}_{\circledS}$, ${}_{\diagup}$, ${}_{\diagdown}$, ${}_{\blacksquare}$,
${}_{\Box}$, ${}_{\blacktriangle}$, ${}_{\blacktriangledown}$, ${}_{\Diamond}$, ${}_{\bigstar}$, ${}_{\spadesuit}$, ${}_{\heartsuit}$, ${}_{\diamondsuit}$, ${}_{\clubsuit}$, ${}_{\flat}$,
${}_{\natural}$, ${}_{\sharp}$, ${}_{\checkmark}$, ${}_{\maltese}$, ${}_{\blacklozenge}$

**Letters.** ${}_{\text{\AE}}$, ${}_{\text{\O}}$, ${}_{\text{\ss}}$, ${}_{\text{\ae}}$, ${}_{\eth}$, ${}_{\text{\o}}$, ${}_{\text{\i}}$, ${}_{\text{\OE}}$, ${}_{\text{\oe}}$, ${}_{\text{\j}}$,
${}_{\Gamma}$, ${}_{\Delta}$, ${}_{\Theta}$, ${}_{\Lambda}$, ${}_{\Xi}$, ${}_{\Pi}$, ${}_{\Sigma}$, ${}_{\Upsilon}$, ${}_{\Phi}$, ${}_{\Psi}$,
${}_{\Omega}$, ${}_{\alpha}$, ${}_{\beta}$, ${}_{\gamma}$, ${}_{\delta}$, ${}_{\varepsilon}$, ${}_{\zeta}$, ${}_{\eta}$, ${}_{\theta}$, ${}_{\iota}$,
${}_{\kappa}$, ${}_{\lambda}$, ${}_{\mu}$, ${}_{\nu}$, ${}_{\xi}$, ${}_{\omicron}$, ${}_{\pi}$, ${}_{\rho}$, ${}_{\varsigma}$, ${}_{\sigma}$,
${}_{\tau}$, ${}_{\upsilon}$, ${}_{\varphi}$, ${}_{\chi}$, ${}_{\psi}$, ${}_{\omega}$, ${}_{\vartheta}$, ${}_{\phi}$, ${}_{\varpi}$, ${}_{\digamma}$,
${}_{\varkappa}$, ${}_{\varrho}$, ${}_{\epsilon}$, ${}_{\hbar}$, ${}_{\Im}$, ${}_{\ell}$, ${}_{\Re}$, ${}_{\Finv}$, ${}_{\aleph}$, ${}_{\beth}$,
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

## Conventions of the Corpus Itself

The corpus has a small number of working conventions that are not mathematical.

**The menus.** Every article is registered in exactly one menu: `maths.md` for the mathematical corpus and `physics.md` for the physics corpus. An entry has the form of a link to the article followed by a comment that lists the contents of the article in outline. The mathematical menu opens with the category *Introduction and Conventions*, placed outside the parts. It has two subcategories: *Introduction to Mathematics*, which holds *Introduction to the Mathematical Corpus* and *AI Maths Review*, and *Algebra and Element Conventions*, which holds this article and its nine companions. An entry that begins with `+` is a **planned** article, one that is registered in the menu and not yet written; an entry without the marker has its article on disk.

**The groups inside a category.** A category of Parts I to IV lists its articles in four groups, each of which adds one thing to the group before it. The group `- Theory` holds the structure itself, read with the product of its elements. The group `- Operator Theory` holds the operators on that structure — the left and right multiplications, the derivations, the automorphisms, the actions and the sandwich — and adds an operator layer and nothing else. The group `- * Theory` holds the same structure read with an involution on its **elements**. The group `- * Operator Theory` holds the operators built from the **involution**, of which the adjoint is the archetype. The front-matter category *Introduction and Conventions* is the exception: it lists two subcategories and no group.

**The two involutions.** The star names the involutive layer in both groups, and the layer of the elements and the layer of the operators are two structures and not one: the involution of `- * Theory` sits on the elements and the adjoint of `- * Operator Theory` sits on the operators. They need not coincide: an involution on the elements does not by itself produce an adjoint on the operators, and two adjoints of the same structure may differ — the transpose and the Hermitian adjoint of a matrix are both adjoints, taken with respect to different pairings. When the two do agree the representation is a `*`-representation, and the agreement is proved in the article, never assumed by the menu.

**The order and the fill rule.** The four groups are placed in the order above, and the group `- Applications`, which holds the concrete instances of the structure, closes the category. The groups `- Operator Theory` and `- * Operator Theory` are present in a category whenever it has an operator layer, and the group `- * Theory` is present in every category of Parts I to IV, whether or not it yet holds an article.

**The category names and numbers.** The menu numbers its categories, and an article elsewhere in the corpus may address one by number rather than by name: *category n* means the n-th category of Parts I to VI, read in order, the front matter *Introduction and Conventions* not being counted. This article refers to categories by **name** throughout, because the names are the stable thing and the numbers shift whenever a category is inserted or split. A reader who meets a bare number in another article can resolve it in the menu.

**The article files.** The corpus is split into two collections, each with its own folder: a mathematical article is a file `articles_maths/<slug>.md` and a physical article is a file `articles_physics/<slug>.md`, where the slug is the title in lower case with hyphens in place of spaces and punctuation. The folder and the menu agree — an article lies in the folder whose menu lists it, and no article lies in both.

**The article skeleton.** Every article opens with its title as the first heading, followed by an *Introduction* that states what the article does and what it assumes, then the thematic sections, and closes with three sections in this order: *Summary*, *Summary of Notation*, and *Further Reading*. The introduction states the article's boundaries — what it deliberately does not cover, and where the reader will find it. This article is the one exception: its notation is merged into the Summary and its table closes the article.

**Cross-references and boundaries.** A concept is introduced once, in the category that owns it, and referred to afterwards rather than restated. Articles do not duplicate the content of other articles; they cite them. Every article that touches a structure belonging to a later part states the deferral explicitly, which is the mechanism by which Rule 1 is enforced.

**The word "interval".** Two different objects share the word, and the corpus keeps them apart. In the mathematical corpus an **interval** is an order-theoretic or lattice object: a convex subset of a linearly ordered set, the interval $[a,b]=\{x:a\le x\le b\}$ of a lattice or of a poset of effects, defined by the order and not by a form. In the physical corpus the **interval** is the value of the quadratic form, $\langle\tilde Q\rangle_{\natural}=-\lvert Q_t\rvert^2+\lvert Q_x\rvert^2+\lvert Q_y\rvert^2+\lvert Q_z\rvert^2$ on the material sector, defined by the form and not by an order. A statement about the sign of the interval is therefore never a statement about a lattice interval, and a lattice interval is never the line element; where the two senses could meet, the corpus writes *the form value* or *the quadratic form* for the physical one.

**The letter $\iota$ is not used in Part VI.** Every article registered under *Part VI : Synthetic Studies* of `maths.md` writes no $\iota$, in any spelling. The letter is not reserved there and names no object of those studies: a comparison with a Clifford algebra is written by its values or by the words "the Clifford image", an interior product as the pairing $\omega(X_f,\,\cdot\,)=df$, and an inner automorphism in words. A display in Part VI that introduces $\iota$ is defective.

## LaTeX and Typesetting

The articles are rendered with KaTeX on the page, and the following rules are observed in the source.

- Inline mathematics is written between single dollars, and display mathematics between double dollars on lines of their own.
- Inline mathematics never spans a line break. If a formula is too long, it is displayed.
- Display mathematics inside a list is indented four spaces.
- A prime may follow a subscript as well as precede it: the forms `q'_t` and `q_t'` are both admitted, and an article keeps one order throughout.
- Tables are Markdown tables. A LaTeX array is never used for a table.
- Every heading that introduces a comparison or a classification is a real `###` heading, and the objects are defined before they are tabulated.
- **Bold marks the result.** In a Remark that states a verdict, the clause carrying the outcome is
  set in bold, `**...**`, the object of the sentence staying in plain roman: *the subspace **is a
  commutative Jordan algebra over $\mathbb{R}$ of degree two***. A statement already displayed as a
  Theorem, a Proposition or a Proof is not bolded; the convention applies to the prose of a Remark and
  to the lead sentence of a section that states an outcome.
- The third derivative is written `d^3/dt^3`. The macro `\slashed` is retired and is not used; a gamma contraction is written out, as *Matrix Representations Conventions* states. The characters `|`, `{`, `}`, `<` and `>` inside mathematics need no escaping.
- A malformed formula is rendered in red on the page rather than reported as an error, so mathematics is checked by eye and not by the absence of a warning.

## Summary

Two **superscript tokens** run beside the marks of the elements: $\mathrm{fop}$ marks a Fock operator, an operator on the Fock space and not an element of the algebra, and $\mathrm{opp}$ marks the opposite algebra, whose product is reversed. The two are not read for one another: $\mathrm{fop}$ is written on a glyph, $\mathrm{opp}$ on an algebra name or on an element that names a tensor factor. The Fock mark combines with the dagger, the mark first, $a^{\mathrm{fop}\dagger}$, and the dagger alone never marks a glyph as an operator. Two further upright superscripts, $\mathrm{fn}$ on a function and $\mathrm{spin}$ on a group element, name objects outside the algebra. No index is raised anywhere in the corpus: every index is written low, and a contraction is a form. The caret also carries the corpus's **labels**, upright roman names of three lowercase letters by default — $\mathrm{opp}$, $\mathrm{fop}$, $\mathrm{axf}$, $\mathrm{nil}$ — indexed in §*The Three-Letter Labels*; a label names the object the glyph denotes when it is written on the caret, and a part or a role of that object when it is written low, $s_{\mathrm{tot}}$, $S_{\mathrm{int}}$. **No token the caret carries begins with a capital**: a label, and an operator name such as $\operatorname{sym}$ or $\operatorname{gal}$, are both lowercase, and a capital in that position is a defect. A product is written with its two slots and not in the caret at all, so it raises no question of case: $\tilde Q_1\tilde Q_2$, $\tilde Q_1\wedge_{\natural*}\tilde Q_2$.

A **subscript** is written with the underscore and takes a single token: one character bare, two or more in braces. It counts when it only distinguishes occurrences and names when it is a role label; a role-labelled element carries its label in its coefficients. The admitted forms are a digit, a letter, two indices, a sign, an upright word and a grouped expression, and the slot takes any KaTeX expression beyond them. A regular matrix puts the size and the family in one subscript, $\mathsf M_{4L}$ and $\mathsf M_{4LR\ast}$, the family in italic capitals after the size and the caret kept for the frame. A subscript is never a partial derivative. An **angular-momentum total** takes the role subscript, $s_{\mathrm{tot}}$, and its projection the axis, $s_{\mathrm{tot},z}$; the total generator carries the role subscript and then the vector index, $\tilde S_{\mathrm{tot},k}$; the orbital part is $L_k$ here and $\tilde L_k$ in the physical corpus.

The **working conventions of the corpus** are these. Every article is registered in exactly one menu, `maths.md` or `physics.md`, with a comment that outlines it, and a leading `+` marks a planned article. A category of Parts I to IV lists its articles in the four groups Theory, Operator Theory, `*` Theory and `*` Operator Theory, and `- Applications` closes it. The article files are `articles_maths/<slug>.md` and `articles_physics/<slug>.md`, and every article follows the skeleton Introduction, thematic sections, Summary, Summary of Notation, Further Reading.

The **category numbers** count the categories of the parts in menu order; the front matter is not counted. Since a number shifts when a category is inserted or split, an article addresses a category by name, and the name is the stable thing. The letter $\iota$ is not used in Part VI, where a comparison with a Clifford algebra is written by its values or as the Clifford image, an interior product as a pairing and an inner automorphism in words. The **typography** is KaTeX on the page: inline mathematics between single dollars and never across a line break, display mathematics between double dollars on lines of their own, tables in Markdown and never as a LaTeX array, and a malformed formula rendered in red rather than reported.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $^{\mathrm{fop}}$ | A Fock operator, an operator on the Fock space and not an element of the algebra |
| $^{\mathrm{opp}}$ | The opposite algebra, the algebra with the reversed product, and an element read in it where it names a tensor factor; the two-letter $\mathrm{op}$ is not a token |
| $\mathrm{opp}$, $\mathrm{fop}$, $\mathrm{axf}$, $\mathrm{nil}$ | The three-letter labels of a construction, a frame or a variant of an object; the full index is §*The Three-Letter Labels* |
| $\operatorname{sym}$, $\operatorname{gal}$ | An operator name written in the caret with its argument, $\operatorname{sym}(P)$, $\gamma_n^{\operatorname{sym}}$, $K^{\operatorname{gal}(K/F)}$; lowercase, and read by its argument |
| $\tilde Q_1\tilde Q_2$, $\tilde Q_1\tilde Q_2^{*}$, $\tilde Q_1^{\natural}\tilde Q_2$, $\tilde Q_1^{\natural}\tilde Q_2^{*}$, $\tilde Q_1\bullet\tilde Q_2$, $\tilde Q_1\bullet_{*}\tilde Q_2$, $\tilde Q_1\bullet_{\natural}\tilde Q_2$, $\tilde Q_1\bullet_{\natural*}\tilde Q_2$, $\tilde Q_1\wedge\tilde Q_2$, $\tilde Q_1\wedge_{*}\tilde Q_2$, $\tilde Q_1\wedge_{\natural}\tilde Q_2$, $\tilde Q_1\wedge_{\natural*}\tilde Q_2$ | The twelve products of the algebraic structures, written by their two slots and the conjugation each one carries, never by a code: four general products, their four symmetric parts with $\bullet$ and their four antisymmetric parts with $\wedge$, the class carried by the subscript ${}_{*}$, ${}_{\natural}$, ${}_{\natural*}$ |
| $^{\mathrm{rgs}}$, $^{\mathrm{tpl}}$, $^{\mathrm{prm}}$, $^{\mathrm{dfc}}$, $^{\mathrm{obf}}$, $^{\mathrm{adg}}$ | The six codes that separate two words sharing one spelling: regularised from regular, topological from top, perimeter from periodic, defective from defining, orbifold from orbital, adjugate from adjoint; a code is cheaper than a second meaning on the same letters |
| $^{\mathrm{fn}}$ | A function from a domain into the algebra |
| $^{\mathrm{spin}}$ | An element of $\mathrm{Spin}(n)$ or $\mathrm{Pin}(n)$ on a principal bundle |
| `- Theory`, `- Operator Theory`, `- * Theory`, `- * Operator Theory` | The four groups of a category, in that order |
| `- Applications` | The group that closes a category with the concrete instances of its structure |
| `+` | A planned article, registered in the menu and not yet written |
| `articles_maths/<slug>.md` | The file of a mathematical article; the slug is the title in lower case with hyphens |
| Introduction, thematic sections, Summary, Summary of Notation, Further Reading | The skeleton of every article |
| $s_{\mathrm{tot}}$, $s_{\mathrm{tot},z}$, $\tilde S_{\mathrm{tot},k}$ | Total angular-momentum label, its projection, and the total generator; the orbital part is $L_k$ here and $\tilde L_k$ in the physical corpus |

## Further Reading

- Nicolas Bourbaki, *Éléments de mathématique* (Hermann, then Springer). The model for a notation fixed once and used without variation.
- Donald E. Knuth, *The TeXbook* (Addison-Wesley, 1984). The typographic conventions the source of the corpus follows.
