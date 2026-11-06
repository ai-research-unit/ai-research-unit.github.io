# __Parra's Four Options of the Dirac Equation and the Discrete Symmetries__

## Introduction

Parra's observation, taken up and used by Fauser, is that the Dirac theory, written out in its eight real equations, admits a **vectorial** reading — each equation a statement about a scalar and a pair of three-vectors — and that the reading can be set up in **four inequivalent ways**. The four readings give four equations, which differ only in the relative signs of the derivative term and of the coupling term. One of the four is the Dirac–Hestenes equation; one of the others is Daviau's space formulation; the remaining two are new to the corpus.

The four options are not four theories. They are four **inequivalent rewritings** of one theory, carried into one another by the discrete symmetries. The corpus treats each symmetry in its own article (charge conjugation in *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*, the full set in *The CPT Theorem in Biquaternionic Form*). What it does not contain is the statement that the symmetries act as a **permutation group** on a set of inequivalent equations, and that the four particle labels — electron and positron, spin up and spin down — are the four points of that orbit. This article records that statement.

Three things are fixed here once and used without repetition below.

- **The field is an element.** Every field of the article is an element of $\mathbb{B}$, written $\tilde{Ξ}_{\mathrm{sp}}$, and every product is a product of elements. The four options differ in how the eight real coordinates of that one element are read, not in the size of the object that carries them. The field is never written as a list of components anywhere in this article.
- **The derivative is the corpus's gradient.** The only derivative is the biquaternionic gradient $\tilde\nabla$ of *Operator and Calculus Conventions*, with its quaternion conjugate $\tilde\nabla^{\natural}$ and its d'Alembertian $\Box=\tilde\nabla\tilde\nabla^{\natural}$. Parra's derivative, written with a frame element in each term, is translated into it once, in *The Four Options*.
- **Parra's right multipliers.** Parra's imaginary unit is the element $\omega:=-\vec e_z$, his spin bivector $e_{21}$; it multiplies the field **on the right**, and it is not the central $i$. The article uses that one element read with and without the central $i$,
  $$
  \omega^2=-e_t,\qquad (i\omega)^2=e_t,
  $$
  a complex structure on the right and an involution on the right. The central $i$ is the whole of the difference between them, and no other object of the article is identified with it.

**The two values of the subscript.** An element, a product and a field carry the subscript $L$ or $R$ fixed in *Special Element Conventions*: $L$ is the value minus one and $R$ the value plus one. The values are two, and only the zero element carries both. The article needs the letters in one place, the two parts of the massive equation.

The article is an **equivalent rewriting**, as everywhere in this series: the four options are four forms of the standard equation, and nothing new is predicted. What is new to the corpus is the object: the discrete group organising the four types, and the algebraic datum that keeps them apart. The construction is taken from Parra as reported by Fauser; the corpus reproduces the report and does not claim to have consulted Parra's papers, which are unpublished or difficult to obtain.

## The Four Options

**Parra's assumption.** Parra starts from the four complex coefficients of the field and inspects the eight real equations. His assumption is that the **real part of the first coefficient** transforms as a scalar; under that assumption the eight equations acquire a vector character once the **spin vector** $\vec s$ is introduced, an imaginary spatial vector — a real three-vector multiplied by $i$. It has no material part, and the star fixes the informational space and negates the material blocks, so $\vec s=\vec s^{*}$ and $\vec s$ lies in $X_{\mathrm i}$ of the block table below. Two scalars and two vectors remain. Writing the scalars as $\alpha$ and $\lambda$ and the vectors as $\vec E=(E_1,E_2,E_3)$ and $\vec B=(B_1,B_2,B_3)$, the option-$\{0\}$ field is

$$
\tilde{Ξ}_{\mathrm{sp},\{0\}}=(\alpha+iB_3)\,e_t+(-B_2+iB_1)\,\vec e_x+(E_3+i\lambda)\,\vec e_y+(E_1+iE_2)\,\vec e_z .
$$

The eight real fields are the eight real coordinates of one element, and the option decides which coordinate carries which.

**The four fields.** The assumption "the real part of the first coefficient is a scalar" can be made, after a suitable renaming, for **any of the four coefficients**, and this is the origin of the four options. Three fixed real-linear maps carry the option-$\{0\}$ field to the other three,

$$
\tilde{Ξ}_{\mathrm{sp},\{3\}}=\Pi\,\tilde{Ξ}_{\mathrm{sp},\{0\}},\qquad
\tilde{Ξ}_{\mathrm{sp},\{2\}}=J_2\,\overline{\tilde{Ξ}_{\mathrm{sp},\{0\}}},\qquad
\tilde{Ξ}_{\mathrm{sp},\{1\}}=J_1\,\overline{\tilde{Ξ}_{\mathrm{sp},\{0\}}},
$$

where the bar is the coefficient conjugation of *Algebra and Element Conventions*, $\Pi$ replaces the four coefficients $(Q_t,Q_x,Q_y,Q_z)$ by $(Q_y,Q_z,Q_t,Q_x)$, and the two signed exchanges $J_2$ and $J_1$ replace them by $(-Q_x,Q_t,Q_z,-Q_y)$ and $(Q_z,-Q_y,-Q_x,Q_t)$. Two of the three maps are therefore **antilinear** and the third, $\Pi$, is **complex-linear**. The options fall into two classes under the complex-linear maps, $\{0\}\sim\{3\}$ and $\{2\}\sim\{1\}$, and all four transitions between the classes are the conjugation. The three relations were recomputed on generic real fields.

**The four equations.** Parra's equation multiplies the field by the derivative on the left and by the spin bivector on the right. Read in this algebra, with $ϙ$ the charge and $A$ the potential,

$$
\boxed{\;\pm\tilde\nabla\tilde{Ξ}_{\mathrm{sp}}\,\omega\pmϙA\,\tilde{Ξ}_{\mathrm{sp}}+i\,\lambda_m^{-1}\overline{\tilde{Ξ}_{\mathrm{sp}}}\,\omega=0\;}
$$

the derivative acting on everything to its right, $\omega$ multiplying on the right, and **two independent signs**, one on the derivative term and one on the coupling term. Parra's derivative, written with a frame element in each term, is this gradient: the frame elements of his terms are the units of $\tilde\nabla$, and his imaginary unit $e_{21}$ is $\omega$. The four options are the four combinations of the signs, and the last entry of the table is Parra's identification of each with a "particle".

| option | derivative term | coupling term | Parra's label |
|---|---|---|---|
| $\{2\}$ | $+$ | $+$ | $e^{+}_{\uparrow}$ |
| $\{0\}$ | $-$ | $+$ | $e^{+}_{\downarrow}$ |
| $\{3\}$ | $+$ | $-$ | $e^{-}_{\uparrow}$ |
| $\{1\}$ | $-$ | $-$ | $e^{-}_{\downarrow}$ |

The sign of the coupling term distinguishes electron from positron, and the sign of the derivative term distinguishes spin up from spin down. The identification is a choice — one may exchange the two labels within each pair — and the corpus records it as Parra's interpretation rather than as a derivation.

**The mass term.** Parra's mass term is the right multiplication by the fixed velocity $e_0$ of his frame. The corpus writes the same structure on the conjugated field, as the right multiplication by $i\omega$: the conjugation supplies the second field, and the fixed direction plays the part of the velocity. The sign pattern of the four options is unaffected by the replacement, because the mass term is common to all four; *The Two Dirac Equations* gives the reason for it and its price.

**Proposition (the options are one theory in four sign conventions).** The four equations differ only in the **sign of the derivative term** and the **sign of the coupling term**, each of them $+$ or $-$, while the spin bivector and the mass term are the same in all four. Consequently each option is the Dirac equation of the corpus in its own sign conventions: reading the sign of the derivative as defining the orientation of the frame and the sign of the coupling as the charge convention, the four options become one equation.

*Proof.* Compare the four equations term by term; they have the same structure and differ in the two signs displayed. The mass term $i\,\lambda_m^{-1}\overline{\tilde{Ξ}_{\mathrm{sp}}}\,\omega$ and the right factor $\omega$ are common to all four, and the derivative term is the same up to its overall sign.

**The free equation, once.** Set $m=0$ and $A=0$. The right multiplier $\omega$ is invertible, $\omega^{-1}=-\omega$, so the two options whose derivative sign is $+$ hold exactly when $\tilde\nabla\tilde{Ξ}_{\mathrm{sp}}=0$, and the two whose derivative sign is $-$ likewise. The four options therefore share one free equation, first order and in one field, and they are distinguished by the relative signs of the two terms and not by the propagation.

**Corollary (which options the corpus already knows).** Option $\{2\}$ **is** the Dirac–Hestenes equation. The source writes it $\nabla\tilde{Ξ}_{\mathrm{sp}} e_{21}+ϙA\tilde{Ξ}_{\mathrm{sp}}+\lambda_m^{-1}\tilde{Ξ}_{\mathrm{sp}} e_0=0$ in his own letters, and *The Dirac–Hestenes Equation and Spacetime Algebra in Biquaternionic Form* writes the same equation as $\tilde\nabla\tilde{Ξ}_{\mathrm{sp}}\,\omega-eA\tilde{Ξ}_{\mathrm{sp}}=\lambda_m^{-1}\tilde{Ξ}_{\mathrm{sp}} v_0$: the derivative on the left, and the two multipliers on the right, the spin plane $\omega$ and the fixed timelike velocity $v_0$. The two differ only in the two sign conventions of the charge and of the mass: with $ϙ=-e$ both coupling terms read $-eA\tilde{Ξ}_{\mathrm{sp}}$, and with $m\to-m$ both mass terms read $-m$ times the field, so they coincide term by term, the source's $e_{21}$ being the corpus's $\omega$, as Fauser states. Option $\{1\}$ **is** the Daviau equation of *The Daviau Map and the Space Clifford Formulation of the Dirac Equation* — the charge is written $q$ there, and the generator of his space algebra is not the one of this article — upon the passage between the two formulations described in that article. That two of the corpus's three formulations appear as two of Parra's four options, and the other two options are new, is the article's first structural result. Here $\lambda_m=\hbar/(mc)$ is the mass length.

**Remark (the right action is common to all four).** In every option the spin bivector $\omega$ multiplies $\tilde{Ξ}_{\mathrm{sp}}$ on the right and $i\omega$ multiplies $\overline{\tilde{Ξ}_{\mathrm{sp}}}$ on the right, while the derivative and the coupling act on the left. This is the bi-module structure of *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*, and it is the same feature the corpus records for the Dirac–Hestenes equation. The four options do not differ in the left/right pattern; they differ only in the two signs.

## The Two Dirac Equations

The corpus writes the massive Dirac equation twice: once on the two parts of the field, and once on one field with the mass term carrying the conjugation. Parra's options sit with the second of the two, and this section gives the passage and its price.

**The pair on the two parts.** The biquaternion Dirac field is an element of $\mathbb{B}$, and its equation is the pair

$$
\boxed{\;\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=\lambda_m^{-1}\tilde{Ξ}_{\mathrm{sp},L},\qquad \tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=\lambda_m^{-1}\tilde{Ξ}_{\mathrm{sp},R}\;}
$$

of *Operator and Calculus Conventions*, with $\tilde\nabla$ the gradient and $\tilde\nabla^{\natural}$ its quaternion conjugate. **Two equations, one per value of the subscript.** Both act on the left, so the pair is one-sided; at $m=0$ the two lines decouple, and at $m\ne0$ the mass couples them off the diagonal. The pair is also what carries the mass: composing the two lines gives $\tilde\nabla\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=\lambda_m^{-2}\tilde{Ξ}_{\mathrm{sp},L}$, that is $\Box\tilde{Ξ}_{\mathrm{sp},L}=\lambda_m^{-2}\tilde{Ξ}_{\mathrm{sp},L}$, while neither line alone squares to a scalar operator. The reason is a derived form: the two squares carry the time–space cross terms with opposite signs, and only the mixed product cancels them.

**The same pair on one field.** Read on one element, the pair is one display whose two sides are the two actions,

$$
\tilde\nabla^{\natural}\tilde F=i\,\lambda_m^{-1}\overline{\tilde F}\,\omega ,
$$

with $\overline{\tilde F}$ the coefficient conjugate. The derivative acts on the left and the mass on the right; the mass term carries the conjugation, and it is that conjugation which supplies the second field of the pair. The display is not a second equation.

**Where Parra's options sit.** In this parlance an option of Parra is a **two-sided** equation: the derivative on the left, the spin bivector and the mass on the right. The right multiplier of the spin bivector is a **complex structure** on the element, $\omega^2=-e_t$, and the right multiplier the corpus's display carries is its multiple by the central $i$, an **involution**, $(i\omega)^2=e_t$. The two differ by the factor $i$, and $i^2=-1$ is the whole of the difference: the phase belongs to the spin plane and not to the second multiplier. That is the precise sense in which the options join the two-sided operator theory to the two values of the subscript: the element Parra multiplies on the right and the element the corpus's display multiplies on the right differ only by the central $i$.

**The two mass terms, and linearity.** Parra's mass term is a right multiplication by a fixed unit and is linear in the field. The corpus's is a conjugation together with a right multiplication by $i\omega$ and is antilinear. The two are one structure in two carriers, and what the passage costs is linearity: that is the difference the companion article *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form* records between the two kinds of mass. Daviau's mass term is the same replacement in his algebra.

## The Discrete Group and the Discrete Symmetries

**Statement (the permutations of the options).** The transformations that connect the four Parra options form the quotient

$$
\boxed{\;D=\Gamma_{1,3}/\Gamma^{0}_{1,3},\;}
$$

the group generated by the units, modulo its identity component. The identity component is the set of norm-one elements, $\langle\tilde U\rangle_{\natural}=e_t$, the proper orthochronous part (*Norm and Pairing Conventions*). Its three non-identity cosets are **space inversion** (the three space directions inverted, time kept), **time reversal** (time inverted, space kept) and their product $PT$ (all four inverted), which the convention of the source calls **charge conjugation**. The four options are the orbit of any one of them under $D$, and the four labels $e^{\pm}_{\uparrow\downarrow}$ are the labels of that orbit.

The quotient $D$ is a discrete group of order four. A unit either keeps or inverts the sense of the time direction, and either keeps or inverts the sense of the three space directions; the two signs are independent and preserved by multiplication, so there are exactly four cosets, one per pair of signs, and the three non-identity ones are the three discrete reflections. The quotient by the **products of an even number of units** is not this group. That quotient has order two: it carries the single sign of the number of factors, and it cannot separate four options, because space inversion and time reversal are each the product of an odd number of units. The four options therefore require the quotient by the identity component and not by the even part, and the article uses that one.

Acting on the field, a discrete reflection — any element outside the identity component — changes the relative signs of the derivative and coupling terms in the way displayed above, and the four options are the four sign patterns so obtained. Which of the three non-identity cosets flips which sign is the content of open question 3; the counting does not fix it, and nothing below depends on the choice.

**What the corpus already has.** The corpus contains each of the three symmetries separately:

- *Charge conjugation* is built in *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form* from the algebra's real structure $\flat$ and the $\mathrm{Spin}^{\mathrm c}$ structure, and in the spacetime-algebra language it is a right multiplication by a fixed bivector, as recorded in *The Dirac–Hestenes Equation and Spacetime Algebra in Biquaternionic Form*.
- *Parity and time reversal* are the reflections of *The Reflection and the Rotation in Biquaternionic Form*.
- The combined statement is the corpus's *The CPT Theorem in Biquaternionic Form*.

**What the corpus does not have.** Nowhere does the corpus assemble these three symmetries into a **group acting on a set of inequivalent equations**, and nowhere does it identify the four particle types with the orbit of that action. That is the new object this article contributes. In the corpus's usual interpretation the symmetries act on **one field** and the particle types are labels on the solution space; here the symmetries act on the **set of equations**, and the particle types are labels on the orbit. The two interpretations are compatible, and the second makes explicit what the first leaves implicit: the four types are not four solutions of one equation but four sign conventions of one equation, permuted by the discrete group.

**Remark (the discrete group is the quotient, not the full group of units).** The quotient $D$ has order four, and its action on the options is free and transitive, so the four options form a single orbit of four elements — the permutation being the one the source records, not one the article derives. The double cover is invisible at this level: a unit and its negative give the same transformation of the equation. The article does not claim that $D$ is the group of units; it is the quotient, and the quotient is what acts on the options.

## The Klein Four of the Conjugations

The discrete group $D$ of the previous section is the quotient of the group of units by its identity component. The same abstract group is met again, purely inside the algebra, as the group generated by the algebra's conjugations, and the structure of the remarkable subspaces binds the two. This section writes the table and reads the three symmetries on it.

**The blocks.** The eight real coordinates group into four blocks, written here $(T_{\mathrm m},T_{\mathrm i},X_{\mathrm m},X_{\mathrm i})$: the material time $T_{\mathrm m}=\mathbb R(ie_t)$, the informational time $T_{\mathrm i}=\mathbb R(e_t)$, the material space $X_{\mathrm m}=\mathbb R(\vec e_x,\vec e_y,\vec e_z)$ and the informational space $X_{\mathrm i}=iX_{\mathrm m}$. These are the blocks $A_2,A_1,B_1,B_2$ of *The Biquaternion Space, the Group of Involutions and the Six Subspaces*, which writes them in the order $A_1,A_2,B_1,B_2$. With the blocks in the order $(T_{\mathrm m},T_{\mathrm i},X_{\mathrm m},X_{\mathrm i})$, the sign of each map on each of the four blocks is

| map | sign on $(T_{\mathrm m},T_{\mathrm i},X_{\mathrm m},X_{\mathrm i})$ | fixed space | type |
|---|---|---|---|
| $1$ | $(+,+,+,+)$ | $\mathbb{B}$ | identity |
| $\bar{\cdot}$ | $(-,+,+,-)$ | $\mathbb{B}_{H}$, the real quaternions | anti-linear automorphism |
| ${}^{\natural}$ | $(+,+,-,-)$ | $\mathbb{B}_{C}$, the centre | linear anti-automorphism |
| ${}^{*}={}^{\natural}\bar{\cdot}$ | $(-,+,-,+)$ | $\mathbb{B}_{\Psi}$, the informational sector | anti-linear anti-automorphism |
| $\flat=-{}^{*}$ | $(+,-,+,-)$ | $\mathbb{B}_{\Phi}$, the material sector | anti-linear, reverses products with a twist: $(\tilde Q_1\tilde Q_2)^{\flat}=-\tilde Q_2^{\flat}\tilde Q_1^{\flat}$ |

The first four rows are the Klein four $\{1,\bar{\cdot},{}^{\natural},{}^{*}\}\cong\mathbb{Z}_2\times\mathbb{Z}_2$, and the four blocks are indexed by its four characters: each block is a joint eigenspace, and the sign pattern on it is the value of the character that indexes it. That is why the block decomposition is canonical. The last row is **not** a fifth group element: $\flat$ differs from ${}^{*}$ by the central sign, and its sign pattern is the negative of the row of ${}^{*}$. It is the fifth pattern and not a fifth character, and the charge-conjugation pairing is read on it below. The entries and the fixed spaces belong to *The Biquaternion Space, the Group of Involutions and the Six Subspaces*; the table is restated here because the discrete symmetries are read on it.

**Interpretation (the three symmetries on the characters).** The block action identifies the non-trivial characters with the discrete symmetries, the assignment being fixed by the standard transformation properties.

- **Parity $P$ is ${}^{\natural}$.** It fixes the two temporal blocks and negates the two spatial ones, sending the material four-displacement $i c r'_t\,e_t+r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ to $i c r'_t\,e_t-(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)$: space inverted, time kept. It is $\mathbb{C}$-linear, the algebraic form of the unitarity of parity.
- **Time reversal $T$ is $\bar{\cdot}$.** It negates the material time $T_{\mathrm m}=\mathbb{R}(ie_t)$ — the $i c r'_t$ direction — and the informational space $X_{\mathrm i}$, and fixes the material space, so on the material sector it is the flip of the time direction alone. It is **anti-linear**, which is the anti-unitarity of time reversal. The corpus reaches the same object as the anti-linear part of $T$ (*The CPT Theorem in Biquaternionic Form*).
- **The full reflection $PT$ is ${}^{*}=\bar{\cdot}\circ{}^{\natural}$**, negating both material blocks, that is $x_\mu\mapsto-x_\mu$ on the material sector.
- **Charge conjugation is read on $\flat=-{}^{*}$, the real structure.** It fixes the material sector and negates the informational one, and it is anti-linear. It is level 1 of the four levels at which the corpus uses the name (*Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*): at the algebra level $\flat$ carries the **shape** of the pairing, whereas the operation itself is level 3 and lives on the carrier,
  $$
  \mathcal{C}[\tilde{Ξ}_{\mathrm{sp}}]=\eta_C\,\tilde{Ξ}_{\mathrm{sp}}^*,\qquad \eta_C:\ \tilde{Ξ}_{\mathrm{sp}}\mapsto-\vec e_y\tilde{Ξ}_{\mathrm{sp}}\vec e_y,\qquad \eta_C^2=e_t ,
  $$
  with $\eta_C$ the fixed element of the map (*Charge Conjugation and the Division Ring*). The bilinear is its second realization, $\tilde{Ξ}_{\mathrm{sp}}^{\mathsf T}\eta\tilde{Ξ}_{\mathrm{sp}}$, with the element $\eta:=\vec e_x$ acting on the right, $\tilde{Ξ}_{\mathrm{sp}}\mapsto\tilde{Ξ}_{\mathrm{sp}}\vec e_x$, whose square is $\vec e_x^2=-e_t$; the sign that separates the two squares is the division-ring sign the companion article records. That the shape is a pattern and not a group element is the algebraic statement that $C$ does not join $\{1,P,T,PT\}$ as an independent factor but is the sign that turns $PT$ into its negative.

**Caution (the second dictionary).** The literature of the source attaches the names differently: with the generators $i\vec e_k$ read as the generators of the spatial algebra, it reads $P$, $T$ and $PT$ as the three operations which, in the corpus's letters, are $\bar{\cdot}$, ${}^{*}$ and ${}^{\natural}$ (*The CPT Theorem in Biquaternionic Form*, quoting the literature). That dictionary reads $P=\bar{\cdot}$, $T={}^{*}$, $PT={}^{\natural}$ — the transpose of the interpretation above. Both dictionaries are labelled and neither is proved in the corpus; the difference is the choice of which structure is called space inversion, and the interpretation above is the one whose parity fixes time and negates space. The table is the fact, the naming is the interpretation, and the article keeps the two apart.

The two dictionaries are visible even inside this article. The previous section's quotient $D$ has for its three non-identity cosets space inversion, time reversal and their product, and its orbit of four options therefore reads $C$ as that product $PT$ — the convention of the source. The interpretation above instead places the three characters on $\{P,T,PT\}$ and the **shape** of the charge-conjugation pairing on the fourth pattern $\flat$; the operation itself is defined at the carrier level, and the four levels of the name are tabulated in *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*. The section records the difference rather than hiding it: the symmetries are a group of order four either way, and the question is only which of the four characters each one occupies.

## Why a Formalism of Components Mixes the Options

The reason the four options are worth isolating is what a formalism built on a list of complex components cannot do with them. In such a formalism a **complex linear combination** of the components is a standard operation — it is how one rotates the field, changes basis, or forms a plane wave — and such a combination **mixes the four options**: a complex linear combination of two fields of different options is, in general, a field of none of the four, and the relative signs cannot be undone. Fauser's formulation of the point: a complex linear combination intermingles the different Parra options "without any chance to re-obtain them as different equations".

The exact reason is the one displayed with the three maps, and it is narrower than the remark suggests. Of the three maps between the options one is real-linear in the coefficients and two are the coefficient conjugation; since a map that preserves the complex structure is complex-linear, the four options fall into the two classes $\{0\}\sim\{3\}$ and $\{2\}\sim\{1\}$, and the four transitions between the classes are antilinear. The invariant of the class is the product of the two signs of the equation: options $\{2\}$ and $\{1\}$ have agreeing signs, options $\{0\}$ and $\{3\}$ disagreeing ones, and the conjugation is exactly what turns agreement into disagreement. A formalism whose operations on the field are complex-linear therefore separates the options into two types and no further; the datum that separates the two members of a class is the choice of the real form, which is precisely what the complex formalism does not carry.

A change of display is not the cause and cannot repair it. The change of display of *Matrix Representations Conventions* is the conjugation by $C_{\Pi}$; it preserves every product, every trace and every determinant, so it carries no option into another and separates none.

This is the algebraic content of a familiar physical fact. In passing from the Dirac equation to quantum electrodynamics one must introduce **separate creation and annihilation operators for each of the four types** — a distinct pair for the particle and for the antiparticle, and for each spin polarisation. The formalism of the second quantised theory already "takes care of the different types", in Fauser's phrase, precisely because the first-quantised formalism of components does not: the distinction is carried by a conjugation, and the operations of that formalism are complex-linear. Parra's four options make the distinction manifest by refusing the complexification — the fields are real, the equations are real, and the four types are four inequivalent real equations rather than four components of one complex field.

**What this does and does not say.** It does **not** say that the second quantisation of the Dirac field is derivable from the four options, and it does not say that the four options replace the spin polarisation sum of quantum electrodynamics. It says that the algebraic necessity of separate field operators for the four types has a first-quantised shadow: the four options are not equivalent under the complex-linear operations that formalism performs, so it cannot represent the four types by one complex field without losing the distinction. The corpus records this as the source's **physical interpretation** and does not go further.

## The Quaternion Form of the Parra Fields

Parra's four fields have a compact quaternion form. Each of them is an element of $\mathbb{B}$, and every element splits into its two quaternion halves,

$$
\tilde{Ξ}_{\mathrm{sp},\{r\}}=\tilde q_{r1}+i\,\tilde q_{r2},
$$

the sum of a real quaternion $\tilde q_{r1}\in\mathbb{B}_{H}$ and the central $i$ times a real quaternion $\tilde q_{r2}$ — the decomposition of an element into the two halves $\mathbb{B}_{H}$ and $\mathbb{B}_{iH}$ fixed in *Algebra and Element Conventions*. (Parra writes the second quaternion through its quaternion conjugation, which is the natural sign on the real quaternions and names the same four real coefficients.)

**Proposition (the Parra field is the corpus's field).** The map $q_{r1}+i\bar q_{r2}\mapsto\tilde{Ξ}_{\mathrm{sp},\{r\}}$ sends the Parra field of each option into the algebra $\mathbb{B}$, and a general element of $\mathbb{B}$ has eight real parameters — exactly the eight real fields of the source.

*Proof.* A real quaternion has four real parameters and $i$ times a real quaternion has four more, so the sum ranges over the eight-dimensional real algebra, and every element of $\mathbb{B}$ is of that form. No further structure is used.

This places the four Parra fields in the same family as the Daviau field and the Dirac–Hestenes field: all of them are general elements of the biquaternion algebra on eight real parameters, and the differences between the formulations are the sign conventions and the basis choices, not the size of the field. The quaternion form shows this directly, and it shows why the four options are four bases of one eight-dimensional real space.

## The Spin-Particle Bundle

Fauser draws a structural conclusion from the four options. The literature of the source builds its carrier bundle from a finer fibre than the corpus uses, and Fauser submits that this fibre is **too large**: two carriers related by a rotor describe the same object, and nothing in the construction separates the four Parra types. What the four options suggest is a smaller bundle, the **spin-particle bundle**, whose fibre identifies two carriers exactly when a rotor carries one to the other, so that two carriers lie in the same class exactly when they are of the same Parra type.

**The same statement in the algebra, and why it holds.** A rotor is a unit element, an element of norm one, and the units form a connected group. The four options are discrete: they are the four sign pairs of the equation, and each is a label that no continuous motion of the unit can reach from another. Hence a fibre that identifies everything a rotor can reach is blind to the option, and a refinement by the option is exactly what the construction lacks. This is the content of Fauser's "too large", and it is a counting argument and not a new structure: the discrete label is invariant under the connected group.

**Relation to the corpus.** The corpus's account of the field is the statement that it is an element of $\mathbb{B}$ and that its two parts are the two values of the subscript; the discrete quotient $D$ acts on the set of options, and the rotor group does not. The refinement is therefore: the carrier is the same for all four options, and the option is the label that the quotient of the previous section permutes. The four Parra types are the four labels, and the finer fibre is the fibre with the label kept.

*Proof sketch.* An element carrying one option to another lies outside the identity component, and every norm-one element lies inside it, so no rotor changes the option; the classes of the rotor relation are therefore unions of options. Fauser's proposal is that they are the options themselves, and the corpus records it as a proposal, since the source does not exhibit the relation.

## Open Questions

1. **The equivalence relation on the options.** What exactly is the relation whose classes are the four Parra types? In the corpus's terms the options are the four sign pairs of one equation, and the relation should be exhibited on the elements themselves: which real-linear map of $\mathbb{B}$ carries one option to another, and what does it do to $\omega$?

2. **Which option is the framework's?** The corpus's Dirac equation as written in *The Dirac Equation in Biquaternionic Form* has its own sign conventions. Which of the four Parra options does it correspond to under the corpus's dictionary, and is the correspondence stable across the article's solutions and its non-relativistic limit?

3. **The discrete symmetries as a permutation group.** The corpus has each of $P$, $C$, $T$ acting on one field. Does the extension to a group acting on the set of four equations reproduce the corpus's $C$ (the $\flat$ real structure and the right multiplication by a bivector) and its $P$, $T$ (the reflections of the article on reflection and rotation) with the correct permutation, and which of the three maps between the options is the charge conjugation? Two of the three are antilinear, so the question is a sharp one.

4. **The mass term.** The mass term $i\,\lambda_m^{-1}\overline{\tilde{Ξ}_{\mathrm{sp}}}\,\omega$ replaces Parra's right multiplication by the fixed velocity with a conjugation together with a right multiplication by $i\omega$. Is that replacement unique, or is it one of several representatives of the same structure, and does the choice leave the four options' orbit intact?

5. **Spin polarisation and second quantisation.** The four options are four first-quantised equations. Is there a sense in which the four creation and annihilation operator pairs of the second quantised theory — one per type — are the four Fourier components of the option orbit, and does the corpus's path-integral formalism see them?

6. **The spin-particle bundle in the corpus's topology.** The corpus has a topology of the biquaternion unit group and of the null cone (*The Biquaternion Unit Group as a Topological Group*). Does the spin-particle bundle, with its finer fibres, have a characteristic class that the coarser bundle does not, and is that class visible in the corpus's topological articles?

7. **Empirical contact.** None is claimed. The options are equivalent rewritings; the question, as everywhere, is whether isolating them makes a structural fact of the framework easier to see.

## Summary

Parra's four options are four inequivalent ways of reading the eight real Dirac equations as vector equations, arising from the four choices of which coefficient's real part is declared scalar. They yield four equations differing only in the signs of the derivative and coupling terms, with the same spin bivector and the same mass term. Option $\{2\}$ is the Dirac–Hestenes equation and option $\{1\}$ is the Daviau space formulation; the other two are new. All four multiply the field on the right by the spin bivector, so they share the two-sided structure of the corpus's algebra, and the right multiplier of the mass is the spin bivector times the central $i$: a complex structure in the source, an involution in the corpus's display. The four fields are related by three fixed real-linear maps, one complex-linear and two antilinear; that split is the two complex-linear classes of options, and it is the first-quantised shadow of the separate creation and annihilation operators of quantum electrodynamics, one pair per type.

The options are permuted by the quotient of the group of units by its identity component, whose three non-identity cosets are space inversion, time reversal and their product, and Parra labels the orbit by electron and positron, spin up and spin down. The quotient is taken by the identity component and not by the even part: the even part has index two and cannot separate four options. The Parra fields have a quaternion form, and they are general elements of the biquaternion algebra, exactly the corpus's Dirac field on eight real parameters. Fauser's structural conclusion is a refinement of the carrier bundle to the **spin-particle bundle**, whose fibre keeps the option because no rotor, the units being connected, can change it; in the corpus's terms the four Parra types are the four labels that the discrete quotient permutes. The article records the construction as Parra's and Fauser's, reproduces it with the corpus's gradient, and claims no new physics.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde{Ξ}_{\mathrm{sp},\{r\}}$, $r=0,1,2,3$ | The Parra field of option $\{r\}$, an element of $\mathbb{B}$ on eight real parameters |
| $\alpha,\lambda$ | The two scalars of the vector interpretation |
| $\vec E=(E_1,E_2,E_3)$, $\vec B=(B_1,B_2,B_3)$ | The two vectors of the vector interpretation |
| $\vec s$ | The spin vector, an imaginary spatial vector; $\vec s=\vec s^{*}$ under the star, and $\vec s$ lies in $X_{\mathrm i}$ |
| $\omega=-\vec e_z$ | The source's imaginary unit and spin bivector, $e_{21}=\omega$; a right multiplier, $\omega^2=-e_t$ |
| $i\omega$ | The same element read with the central $i$; a right multiplier, $(i\omega)^2=e_t$ |
| $\tilde\nabla$, $\tilde\nabla^{\natural}$ | Biquaternionic gradient and its quaternion conjugate, acting on the left; $\tilde\nabla$ is the only derivative of the article |
| $\Box=\tilde\nabla\tilde\nabla^{\natural}$ | The d'Alembertian of *Operator and Calculus Conventions* |
| $A$, $m$, $ϙ$ | The potential, the mass and the charge of the source's displays; $ϙ$ is the corpus glyph and is not the quaternion coefficient $q_{rj}$ |
| $\Gamma_{1,3}$, $\Gamma^{0}_{1,3}$ | The group generated by the units, and its identity component, the norm-one elements |
| $D=\Gamma_{1,3}/\Gamma^{0}_{1,3}$ | The discrete quotient; order four, permuting the four options |
| $e^{\pm}_{\uparrow\downarrow}$ | Parra's particle labels: electron and positron, spin up and down |
| $\Pi$, $J_2$, $J_1$ | The three maps relating the four fields, in the source's letters; $\Pi$ is the permutation of the four coordinates and not an element of the algebra, and it acts complex-linearly, $(Q_t,Q_x,Q_y,Q_z)\mapsto(Q_y,Q_z,Q_t,Q_x)$; $J_2$ and $J_1$ after the coefficient conjugation, by $(-Q_x,Q_t,Q_z,-Q_y)$ and $(Q_z,-Q_y,-Q_x,Q_t)$ |
| $\tilde q_{r1}+i\tilde q_{r2}$ | The two quaternion halves of the Parra field, $\mathbb{B}_{H}$ and $\mathbb{B}_{iH}$ |
| $T_{\mathrm m},T_{\mathrm i},X_{\mathrm m},X_{\mathrm i}$ | The four blocks: material time $\mathbb R(ie_t)$, informational time $\mathbb R(e_t)$, material space, informational space $iX_{\mathrm m}$ |
| $\eta=\vec e_x$ | The element of the charge-conjugation bilinear, $\tilde{Ξ}_{\mathrm{sp}}^{\mathsf T}\eta\tilde{Ξ}_{\mathrm{sp}}$, a right multiplier; $\eta^2=-e_t$ |
| $\eta_C:\tilde{Ξ}_{\mathrm{sp}}\mapsto-\vec e_y\tilde{Ξ}_{\mathrm{sp}}\vec e_y$ | The element of the operation $\mathcal{C}[\tilde{Ξ}_{\mathrm{sp}}]=\eta_C\tilde{Ξ}_{\mathrm{sp}}^*$; $\eta_C^2=e_t$ |
| $\mathbb B$ | The biquaternion algebra; the corpus's Dirac field on eight real parameters |

## Further Reading

- B. Fauser, "On the equivalence of Daviau's space Clifford algebraic, Hestenes' and Parra's formulations of (real) Dirac theory," arXiv:hep-th/9908200, 1999, §2.3, for the four options, their permutation group and the spin-particle bundle; the source of this article.
- J. M. Parra-Serra, "On Dirac and Darwin–Hestenes equation," in the proceedings of the conference on the algebraic formulation of the Dirac theory (1989), and "Dirac's theory in real geometric formalism: multivectors versus spinors" (unpublished), for the original analysis. The corpus has not consulted these; they are cited through Fauser.
- W. A. Rodrigues Jr. and E. C. de Oliveira, referred to by Fauser for the comparison with the carrier bundle of the source.
- A. Crumeyrolle, *Orthogonal and Symplectic Clifford Algebras* (Kluwer, 1990), for the invariance of the structure under the transformations of the group of units outside the identity component.
- The companion articles of this series: [The Daviau Map and the Space Clifford Formulation of the Dirac Equation](the-daviau-map-and-the-space-clifford-formulation-of-the-dirac-equation.html), [The Dirac–Hestenes Equation and Spacetime Algebra in Biquaternionic Form](the-dirac-hestenes-equation-and-spacetime-algebra-in-biquaternionic-form.html), [Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form](antilinear-structure-and-the-two-kinds-of-mass-in-biquaternionic-form.html), [The CPT Theorem in Biquaternionic Form](the-cpt-theorem-in-biquaternionic-form.html), [The Reflection and the Rotation in Biquaternionic Form](the-reflection-and-the-rotation-in-biquaternionic-form.html), [The Spinor Module in Biquaternionic Form and Its Lorentz Action](the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html), and [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html).
