# __Algebra and Element Conventions__

## Introduction

A framework built on a non-standard algebra, and on a non-standard choice of which part of it counts as "real", is a framework in which a reader will repeatedly find things that look wrong and are not. Two examples fix the idea. The series takes the **anti**-Hermitian subspace as the material sector, where the more familiar convention would take the Hermitian one. And the series' d'Alembertian carries a sign opposite to the one used in the articles on Weyl spinors. In both cases it is the "correction" that is the error.

This article opens the conventions of the series. It states the conventions of the base: the algebra and its basis, the units, the element and its coefficients, the remarkable subspaces and the conjugations. The conventions of the products and the forms, of the norms and the pairings, of the special elements, of the frames, of the matrix models, of the operators and the calculus, of the indices and the notation, and of the physical units and the common elements are carried by the nine companion articles of the category, in that order, and the rule that decides which concepts the corpus uses, with the concepts it prefers and the concepts it prefers not to use, by the last of the nine. The split follows the dependency order and introduces no new convention: each article states what it needs and cites the one before it, and together they hold what one article held before.

It states conventions only: the proofs, the properties and the physical interpretations of the objects it names belong to the articles cited beside them. It is meant to be read before any other article is edited, and its reader is anyone writing or revising an article of the series, for whom the conventions are load-bearing — a change that looks local, a sign or a factor of $i$, generally propagates into a dozen dependent articles.

The word *metric* has one meaning in the series, and there is one metric. It is the **unit metric** $\delta_{\mu\nu}=(1,1,1,1)$: diagonal, all four coefficients $+1$, the matrix of the interval $\sum_\mu Q_\mu^2$. A frame carries a coordinate, not a metric. The minus of the material sector is not a metric: it is the square of the $i$ in $Q_t=i r'_t$, $i^2=-1$, made once on the time slot. The Clifford tool is a translation of the algebra and never a reason to change it. The biquaternion norm and the four forms are set out in *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*.

One warning applies throughout. **A convention recorded here is not a claim that the alternative is wrong.** Several of these choices are freely made where either choice would be defensible; they are conventions, not theorems. What is not free is *consistency*: once a convention is fixed, the dependent articles inherit it, and a change to it is a change to all of them. Where a convention is instead forced — where the alternative leads to a demonstrable contradiction — the article says so explicitly, and that distinction is the difference between a convention and a result.

## The Algebra and Its Basis

The framework is set in the **biquaternion algebra**

$$
\mathbb{B} = \mathbb{C} \otimes_\mathbb{R} \mathbb{H},
$$

the complexification of the quaternions. Every element is written in the basis

$$
\tilde{Q} = Q_t e_t + Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z,
$$

where $e_t = 1$ and $\vec e_x, \vec e_y, \vec e_z$ are the quaternion units,

$$
\vec e_x^2 = \vec e_y^2 = \vec e_z^2 = -e_t, \qquad \vec e_x \vec e_y = -\vec e_y \vec e_x = \vec e_z,
$$

and the four coefficients $Q_\mu$ are **complex** numbers. The scalar imaginary, denoted $i$, is the complex unit of the complexification:

$$
i^2 = -1.
$$

Everything that follows turns on how each complex coefficient is split, so the split is fixed here, at the outset. Writing every coefficient as a real part plus $i$ times a real part,

$$
R_t = r_t + ir'_t, \qquad R_x = r_x + ir'_x, \qquad R_y = r_y + ir'_y, \qquad R_z = r_z + ir'_z, \qquad r_\mu, r'_\mu \in \mathbb{R},
$$

replaces the four complex coefficients of the point by **eight real parameters**: $r_\mu$ is the real part of $R_\mu$, the coefficient of $e_\mu$, and $r'_\mu$ its imaginary part, the coefficient of $ie_\mu$, so the prime marks the parameter that carries the $i$. **The prime stays on the parameter letter and the slot goes into the subscript**: the coefficient is written $r'_t$, never the old $t'$ written as a superscript on the slot, because the prime qualifies the parameter and not the slot. The four coefficients are lengths and no factor stands on any of them: the temporal slot is a length like the three spatial ones, so $r_t$ and $r'_t$ are lengths, and $R_x, R_y, R_z$ are read the same way. The generic element of the mathematics keeps its own coefficient letters, $\tilde Q=\sum_\mu Q_\mu e_\mu$ with $Q_\mu=q_\mu+iq'_\mu$, and those letters carry no physical reading; the position letter is $R$ and its parameters are $r$ and $r'$. As a real vector space $\mathbb{B}$ is eight-dimensional, and the remarkable subspaces below are what the eight parameters are grouped into. The full set of parametrisations, and the two conventions they embody, are in *The Elements and their Coefficients* and *Remarkable Subspaces* below; nothing in them changes the split stated here.

One structural fact governs the whole series, so it is worth isolating. **The scalar unit $i$ is central**: it commutes with every element of $\mathbb{B}$, because it belongs to the $\mathbb{C}$ factor of the tensor product, while the quaternion units belong to the $\mathbb{H}$ factor. Multiplication by a *central* phase $\exp(i\alpha)$ therefore commutes with every operator constructed from the algebra — in particular with the biquaternionic gradient $\tilde{\nabla}$ — and this is why the central phase is the algebra's natural continuous symmetry. The articles on Noether's theorem and the gauge principle rest on it.

**The central phase is carried by the first coordinate.** The phase is the unit complex number $\lambda=\exp(i\theta)$ multiplying $e_t$, and it acts on an element by left multiplication, $\tilde Q\mapsto\lambda e_t\tilde Q=\lambda\tilde Q$. On the coefficients this is $Q_t\mapsto\lambda Q_t$ and, with the same $\lambda$, $Q_x\mapsto\lambda Q_x$, $Q_y\mapsto\lambda Q_y$, $Q_z\mapsto\lambda Q_z$. **The first line is the definition**: the phase acts on $Q_t$, the coefficient of $e_t$, the first coordinate of the element, and there it rotates the two parameters $q_t$ and $q'_t$ of the centre $\mathbb{B}_{C}=\mathrm{span}_{\mathbb{R}}\{e_t,ie_t\}$. The other three coordinates follow, with the same $\lambda$, because the multiplication is $\mathbb{C}$-linear and $e_t$ is the unit. **The action is therefore fixed by its value on one coordinate**, and there is no second choice to make. The element carries one complex structure, $J=L_{ie_t}$, of which the phase is the exponential, $\lambda e_t=\exp(i\theta J)$; a second complex structure exists in the double $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B}_{\mathbb{R}}$ and in no element of $\mathbb{B}$.

**A statement about the phase is a statement about the first coordinate and its forced extension.** It is never a statement about one summand of a decomposition of the carrier. The words *on one half*, *on the other half* and *on both halves* are not written of the phase, because the element is not a sum of halves.

**The split is not written on the element.** No definition, no field and no carrier is written "in $S_+(\vec u)\oplus S_-(\vec u)$". Each coefficient splits as $Q_\mu=q_\mu+iq'_\mu$, so the coefficient split has two halves: the quaternion subspace $\mathbb{B}_{H}$, carried by $e_t,\vec e_x,\vec e_y,\vec e_z$, and the antiquaternion subspace $\mathbb{B}_{iH}$, carried by $ie_t,i\vec e_x,i\vec e_y,i\vec e_z$. The word *halves* is reserved for those two. A decomposition of the carrier into two minimal left ideals is **the polarization**, it is a point of the projective line of directions, and its two parts are **the two planes**. The two planes are not halves, they are not fixed, and they are named with the direction that defines them: a sentence that needs them says *the two planes at $\vec u$*, and a sentence that wants a decomposition without a direction has none.

The split is also a split of **roles**, and the two roles belong to the two **factors** of the tensor product and cannot be exchanged. The central unit $i$ is the scalar imaginary: it is what enters the phase $\exp(\frac{k_m\,i\,S}{m\,c})$, and it multiplies a whole element from inside the centre. The three units $\vec e_x,\vec e_y,\vec e_z$ are the vector directions: they are the relativistic and rotational structure, and they enter through the quaternion factor. A central scalar and a vector direction are different kinds of object — one commutes with everything, the other rotates — so no product of the four general products may read $i$ through the quaternion direction or a unit through the scalar one. The mirror statement, that the two conjugations act on the two factors separately, is the subject of *The Four General Products: Composition, Probability, Causality, Gauge*.

**The opposite algebra is written with three letters.** The opposite of the biquaternion algebra, with the product reversed, is $\mathbb{B}_{\mathrm{opp}}$, with $a\cdot_{\mathrm{opp}}b=ba$; the same three-letter superscript is used for any algebra, $A_{\mathrm{opp}}$.

**The opposite algebra is a mark of an algebra, and never of an operator.** The superscript $\mathrm{opp}$ belongs to algebras and to the spaces built on them: $\mathbb{B}_{\mathrm{opp}}$, $A_{\mathrm{opp}}$, $M_n(D)_{\mathrm{opp}}$, a module of one of them. Written on an element it means the same element read in that algebra, $e_{\mathrm{opp},\nu}$, which is how the tensor factor is named in $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}_{\mathrm{opp}}$ and in the two-sided operators $T_{\mu\nu}$ built on it; the element is not thereby an operator, and the mark says nothing about a side. An operator is named by its own letter, $L_{\tilde Q}$, $R_{\tilde Q}$, $L_{\tilde Q_1}R_{\tilde Q_2}$, and carries no $\mathrm{opp}$. The token is fixed for algebras in *Index and Notation Conventions*, §*The Labels*, which states the same rule from the other side: $\mathbb{B}_{\mathrm{opp}}$ is never an operator.

**The two-letter form $\mathrm{op}$ is forbidden.** It sits one letter away from $\mathrm{opp}$ and differs from it by nothing a reader can see at a glance, so a page that carried both would be undecidable at reading speed. The corpus therefore does not use it, in any sense: not for the opposite algebra, not for an operator, not for the operator norm, which is written $\lVert A\rVert$ bare, the competing norms carrying their own labels; and not for a quantized object, which keeps its own letter, $p$ for the momentum and $\xi_{\mathrm{odw},\mu}$ for the odd worldline variable, the quantization being a fact about the object and not a mark on the glyph. A mark is admitted only when it separates two things that would otherwise be read for one another, and $\mathrm{op}$ separates nothing that the letter and the sentence do not already separate.

**The named objects of the source disciplines are written as roman words when their letter is taken.** The letter $L$ is the left multiplication and the letter $R$ the right multiplication, so the four symbols of the neighbouring disciplines that would otherwise be read for them carry the roman word: $\mathrm{Ric}_{\mu\nu}$ and $\mathrm{Ric}$ for the Ricci tensor and its trace, $\mathrm{Riem}_{\mu\nu\rho\sigma}$ for the Riemann tensor, $\mathrm{Lag}$ for the Lagrangian and its derivative, and $\mathrm{lor}$ for the Lorentz rotor and for anything labelled by the Lorentz action. A two-letter or three-letter roman glyph is admitted on exactly the rule stated above, that it separates two things a reader would otherwise take for one another: $R_{\mu\nu}$ and $R_{\mathrm{axf},e_\nu}$ differ by one letter, and so do $L$ the Lagrangian and $L_{\mathrm{axf},e_\mu}$ the operator. **The rank decides between the two curvature words.** A four-index object is $\mathrm{Riem}$ and a two-index one is $\mathrm{Ric}$. The trace over a pair takes both its indices with it, so a contraction is written with the two-index word, $\delta_{\rho\sigma}\mathrm{Riem}_{\mu\rho\nu\sigma}=\mathrm{Ric}_{\mu\nu}$; where the trace is the point of the display it is left index by index, as in $\delta_{\mu\nu}\mathrm{Riem}_{\alpha\mu\alpha\nu}$, and the result is read as the scalar $\mathrm{Ric}$. **The Lagrangian and its density keep their two letters.** The mechanical or point Lagrangian is $\mathrm{Lag}$ and the field density is $\mathcal{L}$, so a line that relates them reads $\mathrm{Lag}=\int d^3r\,\mathcal{L}$; the calligraphic letter is available because the multiplication operator has taken the roman one. The roman word is never a mark on a biquaternion; it names an object of the algebra's applications.

As a complex algebra $\mathbb{B}$ is isomorphic to the full matrix algebra,

$$
\boxed{\;\mathbb{B} \cong M_2(\mathbb{C})\;},
$$

and this identification is used constantly. It is fixed by a single isomorphism, written $\mathsf{M}_2$; its four basis images, and the rule that neither the factor $i$ nor the sign is a free choice, are stated in *Matrix Representations Conventions*, §*The 2×2 Matrix Representation*, and the development of the representation — the general element, the remarkable subspaces as matrices, the conjugations, the trace and the determinant — is in the companion article *The Element and Operator Representations*. Its two **Peirce carriers**, the minimal left ideals here, are two copies of the spinor module $S$ — a copy index, not a chirality. Chirality is the side on which an operator multiplies, and one basis operator realises it: the fifth basis operator, whose eigenspaces in this display are $S$ and $S^{\mathrm{c}}$. The label needs no basis operator, and the basis operator is one example of one of its four cases. The spinor module and the mass term a field equation builds on that structure are the subject of *The Dirac Equation in Biquaternionic Form*.

## The Base and Its Units

The base is written with the letter $e$, one unit to a direction. The scalar unit is $e_t = 1$ and the three vector units are $\vec e_x, \vec e_y, \vec e_z$; the arrow is the only mark that separates the scalar unit from the vector units. **The three vector units are the quaternion units, the series' replacement for Hamilton's $i, j, k$.** A general element is written in the base,

$$
\tilde Q = Q_t e_t + Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z = \sum_{\mu\in\{t,x,y,z\}} Q_\mu e_\mu ,
$$

with $e_\mu$ the unit of the direction $\mu$ — the arrowless $e_t$ at $\mu = t$ and the arrowed $\vec e_\mu$ at $\mu = x, y, z$. The three vector units close on the scalar unit and on one another,

$$
e_t = 1, \qquad \vec e_x^2 = \vec e_y^2 = \vec e_z^2 = -e_t , \qquad \vec e_x \vec e_y = -\vec e_y \vec e_x = \vec e_z ,
$$

and cyclically, the space index running over $k = x, y, z$. **The notation is the unit along the axis.** A coefficient carries the name of the direction it multiplies, as in $\vec v = v_x\vec e_x + v_y\vec e_y + v_z\vec e_z$ of the vector calculus: $Q_x$ is the coefficient of $\vec e_x$, the label on the unit names the direction and the label on the coefficient names the same direction, so $q_x = x$ reads without ambiguity. **The base letter is $e$ and the unit-element letter is $u$, and the two are never exchanged.** The base units carry $e$, so $e$ is not available for the exponential, which is written $\exp(\cdot)$; a unit element of a layer carries the glyph of the unit element, $\tilde u$ or $\tilde Q$ (§*The Unitary Convention*).

**The replacement of Hamilton's $i, j, k$ by the base rests on three reasons:**

- **The letters $i$ and $j$ are already taken.** Hamilton's $i, j, k$ collides with the complex $i$, kept for the central imaginary, and with the hyperbolic unit $j$, so a vector unit written with either letter would be misread.
- **The base names the directions of spacetime.** The labels $t, x, y, z$ name the four directions of spacetime, so the base states the physics directly, and $e_\mu$ remains an acceptable notation in mathematics, the unit along the axis $\mu$.
- **The base spends no digit.** The labels carry no digit, so every digit stays free to count the generic objects: $Q_1, Q_2$, $\tilde Q_1, \tilde Q_2$ and $\tilde q_1, \tilde q_2$.

## The Elements and their Coefficients

The case and the tilde of the glyph are fixed first, and the element is written after. A generic element is written so that the glyph alone identifies its algebra, two features being read together: the **case** separates a real scalar from a complex one, and a **tilde** marks the quaternionic factor. **The generic element belongs to the Q family and to no other letter**: $\tilde q$ is the quaternion or split-quaternion element, $\tilde Q$ the biquaternion or split-biquaternion one, in every layer of the quaternion family. A letter outside the family is never generic: it names an object, or an element bound at the point of use.

**The generic field belongs to the $\xi$ family.** A field is not an element, so it takes its own letter and the same two features decide its form. The case carries the coefficient: $\xi$ is real and $Ξ$ is complex. Every field is this letter, and each named field below is the letter with a caret that names its role. The tilde carries the element: $\xi$ is a scalar at each point, and the field whose value is an element of the algebra takes the tilde, $\tilde\xi$ in the quaternion layer and $\tilde{Ξ}$ in the biquaternion one. The four forms are one letter and one field.

| form | what it is | where |
|---|---|---|
| $\xi$ | a real scalar field | the central coefficient when it is real |
| $Ξ$ | a complex scalar field | the central coefficient when it is complex, the majuscule following the case rule |
| $\tilde\xi$ | a field whose value is a quaternion | the central case beside a real scalar, the layer $\mathbb{B}_{H}$ |
| $\tilde{Ξ}$ | a field whose value is a biquaternion | the general algebra-valued field, $\tilde{Ξ}=Ξ e_t$ when central |

**The majuscule is written as the glyph, not as the command.** The upper-case xi is written directly, `Ξ`, U+039E, and the command that prints it, `\Xi`, is not used, so that the majuscule of the field is a glyph of its own at reading speed and never a capital to be resolved against the element $X$. The precedent is the stigma: the majuscule of rho is taken by the four-momentum, so the state is written `Ϛ`, U+03DA, §*The Observables, the States and the Quantum Objects*. The minuscule $ξ$ carries its command, `\xi`, since nothing collides with it.

**The two families do not overlap.** $Q$ is the element, a quantity with four coefficients, and $\xi$ is the field, a quantity defined at each point of space-time. An article that needs to say which element a field takes writes the tilde, $\tilde{Ξ}$, and an article that needs a number writes the case, $\xi$ or $Ξ$. The field operator, the Grassmann variable and the second state are carets on the same letter, never a second letter. The letter therefore stands once for the field and for every named field: the complex scalar field is $Ξ$, the algebra-valued one $\tilde{Ξ}$, the Dirac field $\tilde{Ξ}_{\mathrm{sp}}$, the field operator $\tilde{Ξ}_{\mathrm{fop}}$, and the case and the tilde alone separate them.

| System | Name | Generic element | Scalar part | Vector part |
|---|---|---|---|---|
| $\mathbb{R}$ | Reals | $q$ | $q$, real | — |
| $\mathbb{C}$ | Complex numbers | $Q = q + iq'$ | $q$, real; $q'$, real | — |
| $\mathbb{C}^2$ | Duo-complex numbers | $Q = (Q_{\blacktriangle}, Q_{\blacktriangledown})$ | $Q_{\blacktriangle}$, complex; $Q_{\blacktriangledown}$, complex | — |
| $\mathbb{B}_{\mathrm{red}}$ | Reduced biquaternions | $\breve Q = Q_{\blacktriangle} + jQ_{\blacktriangledown}$ | $Q_{\blacktriangle}$, complex; $Q_{\blacktriangledown}$, complex | — |
| $\mathbb{H}$ | Quaternions | $\tilde q = q_te_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z$ | $q_t$, real | $q_x\vec e_x$, $q_y\vec e_y$, $q_z\vec e_z$, real |
| $\mathbb{B}$ | Biquaternions | $\tilde Q = Q_te_t + Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z$ | $Q_t$, complex | $Q_x\vec e_x$, $Q_y\vec e_y$, $Q_z\vec e_z$, complex |

Under this framework, the **vector part** is the part carried by the three vector units $\vec e_x,\vec e_y,\vec e_z$; it exists only in the four quaternionic layers.

**The two part columns.** The fourth column gives the scalar part — the $\mathbb{C}$ scalar part in $\mathbb{B}$ and $\mathbb{B}_{\mathrm{red}}$ — and the fifth the vector part, each coefficient with its nature. In $\mathbb{C}$, $\mathbb{C}^2$ and $\mathbb{B}_{\mathrm{red}}$ there is no vector direction, so both coefficients are scalars of the coefficient field and the vector column is empty.

**The reals come first, written $q$.** The reals have no vector part and carry no tilde and no prime: the generic real element is the lower-case $q$, and it is the glyph every coefficient of the layers is a real parameter of — the $q_\mu$ of the quaternions, and the real part of $Q_\mu = q_\mu + iq'_\mu$ of the biquaternions.

**Several elements of one kind take subscripts.** Where a statement needs more than one element of the same kind, each occurrence takes a number: three generic biquaternions are $\tilde Q_1, \tilde Q_2, \tilde Q_3$, two quaternions are $\tilde q_1, \tilde q_2$, and two complex numbers are $Q_1 = q_1 + iq'_1$ and $Q_2 = q_2 + iq'_2$. The number counts the element and never names a direction; a letter names the direction. **Every element of a numbered statement is numbered**: a bare $\tilde Q$ stands alone, in a statement about one element, and never beside $\tilde Q_1$ or $\tilde Q_2$. The numbers count the elements in the order the statement introduces them, $\tilde Q_1, \tilde Q_2, \tilde Q_3$, and the coefficients follow their element, $Q_{1t}, \vec Q_1$ for $\tilde Q_1$.

**The coefficient index is the label of its unit.** The four slots are labelled $t,x,y,z$, and a coefficient takes the label of the unit it multiplies: $Q_t$ with $e_t$, and $Q_x,Q_y,Q_z$ with $\vec e_x,\vec e_y,\vec e_z$. A sum over the four runs over those labels,

$$
\tilde Q=\sum_{\mu\in\{t,x,y,z\}}Q_\mu e_\mu,
$$

with $e_t$ at $\mu=t$ and $\vec e_\mu$ at $\mu=x,y,z$. The same rule reads a quaternion, $\tilde q=\sum_\mu q_\mu e_\mu$. The label names the unit, not the time coordinate: the material time is $r'_t$ and the informational time is $t$.

**The coefficient prime marks the slot that carries the $i$.** Each complex coefficient is a real part plus $i$ times a real part,

$$
R_\mu = r_\mu + ir'_\mu, \qquad r_\mu, r'_\mu \in \mathbb{R}, \qquad \mu \in \{t, x, y, z\},
$$

with the four coefficients in one unit, $R_t = r_t + ir'_t$, so $r_\mu$ multiplies $e_\mu$ and $r'_\mu$ multiplies $ie_\mu$, the same rule for the four slots:

| Coefficient | Real part | Attached to | Imaginary part | Attached to |
|---|---|---|---|---|
| $R_t$ | $r_t$ | $e_t$ | $r'_t$ | $ie_t$ |
| $R_x$ | $r_x$ | $\vec e_x$ | $r'_x$ | $i\vec e_x$ |
| $R_y$ | $r_y$ | $\vec e_y$ | $r'_y$ | $i\vec e_y$ |
| $R_z$ | $r_z$ | $\vec e_z$ | $r'_z$ | $i\vec e_z$ |

**The element is a scalar part plus, where the layer has one, a vector part.** The scalar part is carried by $1$ in $\mathbb{C}$ and $\mathbb{B}_{\mathrm{red}}$ and by $e_t$ in $\mathbb{H}$ and $\mathbb{B}$; the vector part exists in the quaternionic layers alone and carries the arrow, $\tilde Q = Q_te_t + \vec Q$ with $\vec Q = Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z$. In $\mathbb{C}$ the second term $iq'$ is the imaginary part of a single coefficient, and in $\mathbb{B}_{\mathrm{red}}$ the second term $jQ_{\blacktriangledown}$ is its $j$-part, neither being a vector part. The reduced biquaternion layer writes $\breve Q = Q_{\blacktriangle} + jQ_{\blacktriangledown}$, with complex $Q_{\blacktriangle}$ and $Q_{\blacktriangledown}$; the breve tells it from the complex element $Q$ of the same capital, its algebra $\mathbb{B}_{\mathrm{red}} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ is commutative and has no quaternionic factor, and its second unit is the hyperbolic $j$, $j^{2} = +1$ with $ji = ij$, on the basis $1, i, j, ij$.

**A duo-complex number carries the same two triangles.** The pair $(Q_{\blacktriangle},Q_{\blacktriangledown})$ is a point of $\mathbb{C}^2$, two complex coordinates with no product, and it is the reduced biquaternion $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ read without the multiplication by $j$, the basis of the algebra over $\mathbb{C}$ being $1,j$. **The ascending triangle is the first coordinate and the descending triangle the second**; the breve is what makes the pair an element of the algebra, and a point is never written with it. The coordinates of two points are numbered before the triangle, $Q_{1\blacktriangle}$ and $Q_{2\blacktriangle}$, and the prime marks the slot that carries the $i$, $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$. **The triangles mark the coordinates and the digits mark the basis**: in the basis $e_1,e_2$ the point is $Q=Q_{\blacktriangle}e_1+Q_{\blacktriangledown}e_2$, the ascending triangle on $e_1$ and the descending triangle on $e_2$. A column of the $2\times2$ representation takes the same pair when it is read as a point of $\mathbb{C}^2$; attached to an element it is the pair of coordinates of that element, and the object it is attached to says which.

**A pure element carries the arrow.** A pure element is one with no scalar part, a vector of its layer, written $\vec q$ or $\vec Q$ without the tilde; the arrow names the vector part of a named element and the element read on its own, the two never stacked (§*The Centre and the Vector Subspace*).

**The forms and the operators are written on the Q family.** Two elements of one statement are $\tilde Q_1$ and $\tilde Q_2$, a third taking the next number. The plain form is $\langle\tilde{Q}_1,\tilde{Q}_2\rangle = \operatorname{Sc}(\tilde{Q}_1\tilde{Q}_2)$, with plain norm $\langle\tilde{Q}\rangle=\langle\tilde{Q},\tilde{Q}\rangle$ and unit $\langle e_t\rangle=1$; the trace pairing $2\langle\tilde{Q}_1,\tilde{Q}_2\rangle = \operatorname{Tr}(\tilde{Q}_1\tilde{Q}_2)$ is its $2\times2$ reading, the commutator bracket $[\tilde{Q}_1,\tilde{Q}_2] = \tilde{Q}_1\tilde{Q}_2 - \tilde{Q}_2\tilde{Q}_1$, the general quaternionic bilinear form $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural}$ and the multiplicativity $\langle\tilde{Q}_1\tilde{Q}_2\rangle_{\natural} = \langle\tilde{Q}_1\rangle_{\natural}\,\langle\tilde{Q}_2\rangle_{\natural}$. The argument of an operator, the dummy of an annihilator, the second entry of a bracket and the element a field or a map is applied to carry the same glyph: $L_{\tilde Q_1}(\tilde Q_2) = \tilde Q_1 \bullet \tilde Q_2$, $\{\tilde Q_2 : \tilde Q_1 \star \tilde Q_2 = 0\}$, $[\tilde Q_1, \tilde Q_2]$. **The letter $\tilde P_{\Phi}$ is never a generic element**; it is the four-momentum, $\tilde P_{\Phi} = m\tilde V_{\Phi}$. **In the layers of the biquaternion family the glyph $Q$ belongs to the element and never to an operator**: an operator generated by an element carries the structural capital and the element in the subscript, $L_{\tilde Q}$, and an operator that is not the multiplication by an element takes a letter of its own.

**The letters of the physical quantities.** The glyphs are fixed one to a quantity, so that a reader meets the same letter for the same thing in every article; the tables of *Physics Units and Common Elements Conventions*, §*The Most Common Quaternions and Biquaternions*, and §*Summary of Notation* list them all.

**A logarithm carries the glyph of its element and the subscript $\log$.** The logarithm is a solution of the exponential equation in the same algebra, not an object of a new kind, so it carries the glyph of the element and the subscript, and the definition reads $\exp(\tilde Q_{\log}) = \tilde Q$. The glyph is $\tilde Q_{\log}$ in this algebra, $\tilde q_{\log}$ in the quaternion and split-quaternion layers, $\breve Q_{\log}$ in the reduced biquaternions, and $Q_{\log}$ in the complex, split-complex and dual ones. The subscript is a word, so it competes neither with the direction labels, $Q_t$ and $Q_x$, nor with the counts, $Q_1$; a numbered element keeps its number in front of the subscript, $\tilde Q_{1\log}$. The subscript is dropped when the logarithm is written as an operator, $\log\tilde Q$ or $\operatorname{Log}\tilde Q$. The coordinates of a logarithm follow the coefficient rule: in the complex, split-complex and dual layers, $Q_{\log}=q_{\log}+iq'_{\log}$ has real part $q_{\log}$ and imaginary part $q'_{\log}$, with $j$ in place of $i$ in the split-complex case, and the prime marks the imaginary coordinate alone. The logarithm of a real number is the ordinary real logarithm, written $\log q$; the glyph $q_{\log}$ is the real coordinate of $Q_{\log}$, not the logarithm of $q$.

## The Angle and Its Two Cases

**A real angle is $\theta$ and a complex angle is $\Theta$, and the case is the field.** The rule is the one the case already states for an element: an upper-case glyph has a sector larger than the reals, a lower-case one has the reals. For the angle the sector is the field of the argument.

$$
\Theta=\theta+i\theta',\qquad \theta\in\mathbb{R},\quad\theta'\in\mathbb{R}.
$$

**The prime marks the slot that carries the $i$**, as it does in a coefficient, $R_t=r_t+ir'_t$. The real part $\theta$ is an angle and the imaginary part $\theta'$ is a real number; the two are one angle read at a real and at an imaginary argument.

**The central phase is the real case.** $\lambda e_t=\exp(i\theta J)$ with $\theta$ real and $J=L_{ie_t}$: the phase turns the centre by a real angle, and the rotor of a rotation is the same case at half the angle, $\tilde u_{\mathrm r}=\cos(\theta/2)e_t+\sin(\theta/2)\vec u_{\mathrm r}$.

**The boost factor is the pure imaginary case.** The four-vector element carries $\mathcal B_{\Psi}$ with $\tilde U_{\Psi,\mathrm b}^{-2}=\cosh\theta_{\mathrm{rpd}}\,e_t-i\sinh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b}$, which is $e^{\vec U\Theta}$ at $\Theta=-i\theta_{\mathrm{rpd}}$: in the two-parameter form $\theta=0$ and $\theta'=\theta_{\mathrm{rpd}}$. The rapidity takes the angle's letter with the caret `rpd`, so that no second letter is spent on it. The sign is the article's and it carries the direction of the boost; the magnitude of the imaginary part is the rapidity.

**The circle and the hyperbola are one formula.** With $\Theta=\theta+i\theta'$,

$$
\cos\Theta=\cos\theta\cosh\theta'-i\sin\theta\sinh\theta',\qquad
\sin\Theta=\sin\theta\cosh\theta'+i\cos\theta\sinh\theta'.
$$

At $\theta'=0$ this is $\cos\theta$ and $\sin\theta$; at $\theta=0$ it is $\cosh\theta'$ and $i\sinh\theta'$. A rotation, a boost and the intermediate case are three readings of one letter, and the case of the letter states which of them is meant.

**Neither glyph carries a second role.** The roles that once shared the letter have glyphs of their own: the involution and the orbit map are $\mathrm{J}$; the curvature is $\Omega$; the two-sided operator is $\mathrm{Sd}$; the Heaviside step is $\mathrm{H}_{\mathrm{hvs}}$; the generalised angle of a congruence is $\vartheta_{\mathrm{cng}}$. A subscript on $\theta$ names the angular coordinate itself: $p_\theta$ is the momentum conjugate to it.

## The Remarkable Subspaces of Biquaternions

The eight real parameters of a general element group into **remarkable subspaces**: the centre, the vector subspace, the two halves of the coefficient split, and the two sectors. Each is cut out by a conjugation:

| Subspace | Defining condition | Dimension over $\mathbb{R}$ |
|---|---|---|
| $\mathbb{B}_{C}$, the centre | $\tilde{Q}^{\natural} = \tilde{Q}$ | $2$ |
| $\mathbb{B}_{V}$, the vector subspace | $\tilde{Q}^{\natural} = -\tilde{Q}$ | $6$ |
| $\mathbb{B}_{H}$, the quaternion subspace | $\bar{\tilde{Q}} = \tilde{Q}$ | $4$ |
| $\mathbb{B}_{iH}$, the antiquaternion subspace | $\bar{\tilde{Q}} = -\tilde{Q}$ | $4$ |
| $\mathbb{B}_{\Psi}$, the Hermitian subspace | $\tilde{Q}^{*} = \tilde{Q}$ | $4$ |
| $\mathbb{B}_{\Phi}$, the anti-Hermitian subspace | $\tilde{Q}^{\flat} = \tilde{Q}$ | $4$ |

### The Basis, the Parameters and the Coordinates

**There is one alphabet, and it is the position letter.** The parameters are the coordinates, so the dictionary that once mapped one set of letters onto another is not restated: it is deleted. The slot names the coordinate, the prime marks the half of the coefficient that carries the $i$, and $c$ is the conversion between the length coordinate and the second, quoted only where a clock is read. The eight real parameters are therefore read as

$$
(r_t,\ r_x,\ r_y,\ r_z) \quad \text{and} \quad (r'_t,\ r'_x,\ r'_y,\ r'_z),
$$

the unprimed set the real halves and the primed set the imaginary halves, with the four coefficients $R_t = r_t + ir'_t$, $R_x = r_x + ir'_x$, $R_y = r_y + ir'_y$, $R_z = r_z + ir'_z$. The material temporal coordinate is $r'_t$ and the material space is $r_x, r_y, r_z$; the informational temporal coordinate is $r_t$ and the informational space is $r'_x, r'_y, r'_z$. All eight are lengths, and the speed of light is not in the element: it is the conversion $t'=r'_t/c$ between the length coordinate and the second, $c=1/\sqrt{\epsilon\mu}$ in a medium and $c_0$ in vacuum.

| Subspace | Algebraic name | Physical name | Basis | Parameters | Coordinates |
|---|---|---|---|---|---|
| $\mathbb{B}_{C}$ | The centre | Complex time sector | $e_t,\ ie_t$ | $r_t,\ r'_t$ | $r_t,\ i r'_t$ |
| $\mathbb{B}_{V}$ | Vector | Complex space sector | $\vec e_x,\ \vec e_y,\ \vec e_z,\ i\vec e_x,\ i\vec e_y,\ i\vec e_z$ | $r_x,\ r_y,\ r_z,\ r'_x,\ r'_y,\ r'_z$ | $r_x,\ r_y,\ r_z,\ i r'_x,\ i r'_y,\ i r'_z$ |
| $\mathbb{B}_{H}$ | Quaternion | Real sector | $e_t,\ \vec e_x,\ \vec e_y,\ \vec e_z$ | $r_t,\ r_x,\ r_y,\ r_z$ | $r_t,\ r_x,\ r_y,\ r_z$ |
| $\mathbb{B}_{iH}$ | Antiquaternion | Imaginary sector | $ie_t,\ i\vec e_x,\ i\vec e_y,\ i\vec e_z$ | $r'_t,\ r'_x,\ r'_y,\ r'_z$ | $i r'_t,\ i r'_x,\ i r'_y,\ i r'_z$ |
| $\mathbb{B}_{\Psi}$ | Hermitian | Informational sector | $e_t,\ i\vec e_x,\ i\vec e_y,\ i\vec e_z$ | $r_t,\ r'_x,\ r'_y,\ r'_z$ | $r_t,\ i r'_x,\ i r'_y,\ i r'_z$ |
| $\mathbb{B}_{\Phi}$ | Anti-Hermitian | Material sector | $ie_t,\ \vec e_x,\ \vec e_y,\ \vec e_z$ | $r'_t,\ r_x,\ r_y,\ r_z$ | $i r'_t,\ r_x,\ r_y,\ r_z$ |

Each subspace carries an **algebraic name**, taken from the involution that defines it, and a **physical name**, taken from the role it plays; the companion articles are titled by the physical name.

### The Centre and the Vector Subspace

The algebra is the direct sum

$$
\mathbb{B} = \mathbb{B}_{C} \oplus \mathbb{B}_{V},
$$

the centre with the traceless part.

**The centre and the vector subspace carry a glyph each.** The centre is written with the tilde-free coefficient of $e_t$, $Q_te_t$, a complex scalar times the unit; the vector subspace is written $\vec Q$, the pure element, with the arrow and without the tilde.

A **pure element** is an element with no scalar part. The notion belongs to $\mathbb{H}$ and $\mathbb{B}$ alone: $\mathbb{C}$ and $\mathbb{B}_{\mathrm{red}}$ have no vector part, their second term being an imaginary or $j$-part carried by a single coefficient. In $\mathbb{B}$ the scalar part is carried by $e_t$, so a pure element is one whose $e_t$-coefficient vanishes, $\mathrm{Sc}(\tilde{Q}) = Q_t = 0$, and which is carried by the three vector directions alone. The pure elements are exactly the elements of the **vector subspace** $\mathbb{B}_{V}$, the anti-fixed space of quaternion conjugation,

$$
\vec{Q}^{\natural} = -\vec{Q},
$$

of real dimension six; the pure quaternions of the quaternion layer are the vectors of $\mathbb{R}^{3}$.

**The glyph drops the tilde and carries the arrow.** The tilde marks the quaternionic factor of an element that is read with its scalar part beside its vector part; a pure element is read on its vector part alone, so it is written with the arrow and without the tilde, $\vec q$ in the quaternion layer and $\vec Q$ in the biquaternion layer. The case is unchanged, and the arrow is the only mark: the vector part of a named element and a pure element standing by itself are one object, written with the one glyph, so a pure element is never written with a tilde.

**The arrow is reserved for pure elements.** Three rules follow from this. First, **the arrow marks a pure element and nothing else**: an element with a nonzero scalar part is never written with an arrow, whatever its magnitude or its role. Second, **a unit element carries the arrow only if it is pure**: the unit pure quaternion $\vec u$ and the unit pure biquaternion $\vec U$ carry it, whereas a unit element that has a scalar part — a rotor $\tilde q$ of unit norm, say — carries no arrow, its unit length being carried by the construction that names it. Third, **a unit in the direction of an element takes that element as a subscript**, written $\vec u_{e}$ as in $\vec u_B$ for the unit along the field $B$; the subscript names the element whose direction is taken, and the arrow on $\vec u$ records that the unit is pure.

| System | Name | Pure element | Pure unit element | Scalar part | Coefficients |
|---|---|---|---|---|---|
| $\mathbb{H}$ | Quaternions | $\vec q = q_x\vec e_x + q_y\vec e_y + q_z\vec e_z$ | $\vec u$ | $q_t = 0$ | Real, $q_\mu$ |
| $\mathbb{B}$ | Biquaternions | $\vec{Q} = Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z$ | $\vec U$ | $Q_t = 0$ | Complex, $Q_\mu = q_\mu + iq'_\mu$ |

Three rules are read off the table. **A pure element is the vector part of an element read on its own.** For $\tilde{Q} = Q_te_t + \vec{Q}$ the vector part $\vec{Q}$ is a pure biquaternion, and for $\tilde q = q_te_t + \vec q$ the vector part $\vec q$ is a pure quaternion; the vector part of a named element and a pure element standing by itself are one object, and the arrow names both. **A pure element is anti-fixed by quaternion conjugation**, $\vec{Q}^{\natural} = -\vec{Q}$, having no scalar part to be fixed. **The arrow marks purity, not magnitude.** A pure element is of arbitrary magnitude; a unit pure element — a unit pure quaternion $\vec u$ — carries no second mark, its unit length being carried by the construction.

**The pure glyphs.** The arrow is laid on the glyph of a special element on the same case rule that governs the layer: the pure root is $\vec{Ζ}$ in the biquaternion layer and $\vec\zeta$ in the quaternion layer, and the pure nilpotent is $\vec\Upsilon$ in the biquaternion layer and $\vec\nu$ in the quaternion layer.

**The arrow has priority over the tilde.** Where an element is pure, the arrow is written whatever else the element is, and the tilde of a special glyph is dropped: a pure root is $\vec{Ζ}$ and a pure nilpotent is $\vec\Upsilon$ (or $\vec\zeta$ and $\vec\nu$ in the quaternion layer), never $\tilde{Ζ}$ or $\tilde\Upsilon$. The tilde belongs to the general element, read with its scalar part beside its vector part, and a pure element has no scalar part to be read against; purity therefore decides the mark. The special conventions that write the root $\tilde{Ζ}$ or the nilpotent $\tilde\Upsilon$ name the **general** element of that class, which need not be pure, and an element that is at once special and pure is written with the arrow and only the arrow. **The two marks are never stacked.** The arrow replaces the tilde rather than being laid on it, so no glyph of the corpus carries both: the general element is $\vec Q$ and not an arrowed $\tilde Q$, and an idempotent has no arrowed form at all. The spin generator is the case that occurs in every formula of the rotation theory: its components are $\tilde S_{\Psi,k}=\frac{m\,c}{2\,k_m}i\vec e_k$, each a pure element, and the vector they form is $\vec S$, written with the arrow and without the tilde, so that $\vec u\cdot\vec S=u_k\tilde S_{\Psi,k}$.

**The field glyphs.** Three objects, three glyphs. The real field is $\vec E$, $\vec H$ and $\vec B=\mu\vec H$, and it is real in every article. The complex combination is $\vec N=\vec E+ic\vec B$, with components $N_k$, and every complex statement about the field is written on it: self-duality is $\vec N=0$, the null condition is $\vec N\cdot\vec N=0$, and the invariants are its self-product. The biquaternion is $\tilde F=i\sqrt{\epsilon}\,\vec N$. A field that is complex in its own right keeps its plain glyph and is stated in words to be complex, as the complex potential's $\vec E$ and $\vec H$ are; a complexified *field strength* takes the subscript $\mathbb C$, $\tilde F_{\mathbb C}$, as in *The Self-Dual and Anti-Self-Dual Split*. No field glyph carries a tilde.

**The arrowed $\vec S$ carries two meanings, separated by scope.** In the rotation and spin articles it is the spin generator, with components $\tilde S_{\Psi,k}$. In the electromagnetic articles it is the Poynting flux, $\vec S=\vec E\times\vec H$, and the spin generator does not occur there. No article uses both senses, and where the two would stand together the flux takes the role subscript, $\vec S_{\mathrm P}$.

A pure glyph is given from the quaternions to the biquaternions only, the layers this convention reaches; the commutative layers carry their imaginary part in a single coefficient, $Q = q + iq'$.

### The Quaternion and Antiquaternion Subspaces

The algebra is the direct sum

$$
\mathbb{B} = \mathbb{B}_{H} \oplus \mathbb{B}_{iH},
$$

the quaternion subspace $\mathbb{B}_{H}$, whose elements carry real coefficients throughout, with the antiquaternion subspace $\mathbb{B}_{iH}$, whose elements carry purely imaginary ones: the two are the **real and imaginary halves** of the algebra. The prime splits the element into the two parts,

$$
\tilde Q = \tilde q + i\tilde q',\qquad
\tilde q = q_t\,e_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z \in \mathbb{B}_{H},\qquad
\tilde q' = q'_t\,e_t + q'_x\vec e_x + q'_y\vec e_y + q'_z\vec e_z \in \mathbb{B}_{H}.
$$

The prime marks the second glyph and the split is uniform: $\tilde q$ takes the unprimed parameters and $\tilde q'$ the primed ones.

### The Hermitian and Anti-Hermitian Subspaces

The algebra is the direct sum

$$
\mathbb{B} = \mathbb{B}_{\Psi} \oplus \mathbb{B}_{\Phi},
$$

the Hermitian subspace with the anti-Hermitian one; without qualification, *the sectors* in this series are these two, and the relativistic articles are written in terms of this split. The element splits a second time, across the coefficient slots,

$$
\tilde R = \tilde R_\Psi + \tilde R_\Phi,\qquad
\tilde R_\Psi = r_t\,e_t + i\bigl(r'_x\vec e_x + r'_y\vec e_y + r'_z\vec e_z\bigr),\qquad
\tilde R_\Phi = i r'_t\,e_t + r_x\vec e_x + r_y\vec e_y + r_z\vec e_z.
$$

$\tilde R_\Psi$ is the **informational part**: it takes the real scalar slot with the imaginary vector slots. $\tilde R_\Phi$ is the **material part**: the imaginary scalar slot with the real vector slots. The primed set therefore holds the material time $r'_t$ and the three informational spaces $r'_k$; the unprimed set holds the informational time $r_t$ and the three material spaces $r_k$.

**The two letters are reserved for the two sectors.** $\Phi$ marks the material sector and $\Psi$ the informational one, and each letter serves twice: as the subscript of the sector itself, $\mathbb{B}_{\Phi}$ and $\mathbb{B}_{\Psi}$, and as the sector label of every glyph whose sector is fixed. No other object in the series may take either letter for any other purpose. Each subscript is the label of the sector its element lives in, since $\tilde R_\Phi\in\mathbb{B}_{\Phi}$ and $\tilde R_\Psi\in\mathbb{B}_{\Psi}$, so the subscript and the sector cannot drift apart. The capitals are held free for exactly this use, and the rest of the Greek set is in service, so a half named with any other letter would collide with a symbol already in use.

**A glyph with a fixed sector carries it first.** The sector is the coarsest label, so it stands before the role and the index: $\tilde S_{\Psi,\mathrm{tot},k}$ reads sector, role, index, and $\tilde\Lambda_{\Phi,\mathrm{ret}}$ reads sector, role. The label does not pass into the coefficients, for the reason given below for $\tilde R_\Psi$ and $\tilde R_\Phi$: $\tilde J_\Phi$ keeps the components $J_\nu$. The label is idempotent — for an element already in a sector, $\tfrac12(\tilde Q\pm\tilde Q^{*})$ returns the element itself, so $\tilde P_\Phi=\tilde P$ is a theorem and not a new axiom. A glyph whose sector depends on its value takes no label: $\tilde Q$, $\tilde U$ and $\tilde F$ carry none, and the reader computes the sector from that same line. The mnemonic survives the capital: $\Phi$ opens the word *physics* and $\Psi$ is the letter a quantum state is written with. **The definitions are the authority**: the halves are the $\pm1$ eigenspaces of the Hermitian conjugation,

$$
\tilde R_\Psi = \tfrac12\bigl(\tilde R + \tilde{R}^{*}\bigr) \in \mathbb{B}_{\Psi},\qquad
\tilde R_\Phi = \tfrac12\bigl(\tilde R - \tilde{R}^{*}\bigr) \in \mathbb{B}_{\Phi},
$$

and a reader who does not know the letters computes either half from that line.

<!-- retired notation, kept for reference -->
**The operator reading is retired.** Earlier versions of this series wrote the informational coordinate in the letters of an operator rather than of a coordinate: its four real parameters were named $h_t, h_x, h_y, h_z$ in place of $r_t, r'_x, r'_y, r'_z$, and the element was written

$$
H = h_te_t + ih_x\vec e_x + ih_y\vec e_y + ih_z\vec e_z, \qquad h_t, h_x, h_y, h_z \in \mathbb{R}.
$$

That second name is gone. It was the licence to write one number two ways, and a pair of names for one number is a defect, not a notation. The element has one name on each side of the split: $\tilde R_\Psi$ for the informational half and $\tilde R_\Phi$ for the material half. The parameters are the position letters,

$$
\tilde R_\Psi = r_t\,e_t + i\vec r_\Psi, \qquad \vec r_\Psi = r'_x\vec e_x + r'_y\vec e_y + r'_z\vec e_z ,
$$

with $r'_t$ and $r_t$ the material and informational temporal coordinates, both lengths. Under the unit images of *Matrix Representations Conventions*, §*The 2×2 Matrix Representation* ($\mathsf{M}_2(e_t) = I_2$ and the vector units $-i$ times the Pauli matrices $\sigma_1, \sigma_2, \sigma_3$), the matrix image is the general Hermitian $2\times2$ matrix $r_t I_2 + r'_x\sigma_1 + r'_y\sigma_2 + r'_z\sigma_3$ of *The Native Qubit and the Defining Module of the Biquaternion Algebra*. The readable part of the old convention survives: the coefficient of $e_t$ is a length, $r_t$, and it is read as an energy only when $\frac{m\,c^{2}}{k_m}$ is carried in the reading, in the exponent $\exp(-\frac{k_m\,i\,\tilde{R}_{\Psi}\,r'_{t}}{m\,c^{2}})$ and not in the coefficient.

**One abbreviation is allowed.** In an article that does evolution, $H$ may be written for $\tilde R_\Psi$ in its energy reading, and it must be declared at first use as

$$
H := \tilde R_\Psi, \qquad H = r_t\,e_t + i\vec r_\Psi ,
$$

with the $\frac{m\,c}{k_m}$ in the exponent and not in the coefficient. The tilde is not carried, because $H$ is not a second element. A bare $h$ without a subscript remains the Planck constant, and $\vec r_\Psi$ stays distinct from the Bloch vector $\vec r$ of the state $\tilde{Ϛ}_{\Psi}=\tfrac12(e_t+i\vec r)$.

## The Conjugations

The biquaternion algebra carries three natural involutions and the anti-Hermitian sign derived from them, all of them used in the series:

| Map | Mark | What it is |
|---|---|---|
| Complex conjugation | $\bar{\cdot}$ | The involution of the base, extended to the element |
| Quaternion conjugation | ${}^{\natural}$ | The intrinsic conjugate: it fixes the scalars and negates the vectors |
| Hermitian conjugation | ${}^{*}$ | The involution of the algebra, $\bar{\cdot}\circ{}^{\natural}$ |
| Anti-Hermitian conjugation | ${}^{\flat} = -{}^{*}$ | The negative of the star |

Which of the marks has a sense depends on the system, since a mark degenerates wherever the structure it conjugates is absent. The examples below fix it system by system.

**The complex numbers $\mathbb{C}$.** Only the bar has a sense, the algebra carrying a single non-trivial involution:

$$
\bar Q = q - iq' .
$$

**The quaternions $\mathbb{H}$.** Only the natural sign has a sense, the coefficients being real and the conjugation intrinsic to the quaternion factor:

$$
\tilde q^{\natural} = q_te_t - q_x\vec e_x - q_y\vec e_y - q_z\vec e_z .
$$

**The biquaternions $\mathbb{B}$.** All four have a sense, the bar conjugating the coefficient, which is complex:

$$
\bar{\tilde Q} = \bar Q_te_t + \bar Q_x\vec e_x + \bar Q_y\vec e_y + \bar Q_z\vec e_z, \qquad \tilde Q^{\natural} = Q_te_t - Q_x\vec e_x - Q_y\vec e_y - Q_z\vec e_z,
$$

$$
\tilde Q^{*} = \overline{\tilde Q^{\natural}} = \bar Q_te_t - \bar Q_x\vec e_x - \bar Q_y\vec e_y - \bar Q_z\vec e_z, \qquad \tilde Q^{\flat} = -\tilde Q^{*} .
$$

**The fourth mark is a sign, not a fourth conjugation.** $\flat=-{}^{*}$ is the negative of the star, it reverses products with a twist, $(\tilde Q_1\tilde Q_2)^{\flat}=-\tilde Q_2^{\flat}\tilde Q_1^{\flat}$, and it is an involution of the underlying real space only, not of the ring. Its fixed space is the material sector $\mathbb{B}_{\Phi}$, and the sector split is its work in the series. It is retained for that split, for the bilinear pairings built on it, and for the real-form question of Dirac against Majorana fermions. It is not the mass — the retired form $\tilde\nabla\tilde{Ξ}_{\mathrm{sp}}=k_m\tilde{Ξ}_{\mathrm{sp}}^{\flat}$ conflated the two — and it is not the charge conjugation of the module, the operation defined in *Charge Conjugation and the Division Ring: Charged, Neutral and Truly Neutral Particles in Biquaternionic Form*. Here $k_m=mc/\hbar$ is the mass wave number, the inverse of the mass length.

**The biquaternion norm.** The natural sign carries the algebra's **biquaternion norm**,

$$
\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = Q_t^2 + Q_x^2 + Q_y^2 + Q_z^2 ,
$$

used throughout the series and read on the four forms and their norms in *Product and Form Conventions*, §*The Involutions and the Four Forms* and *Norm and Pairing Conventions*, §*The Four Algebraic Norms and the $*$-Unitary Convention*. It is **multiplicative** and complex-valued in general, and it is not an analytic norm; its unit group and its invertibility reading are *N-Regularity and N-Degeneracy in the Biquaternion Algebra*, §*The Group of Units*.

Each of the four marks has a fixed space, and each of these is one of the **remarkable subspaces** of the algebra. Which involution defines which subspace, and which of them are anti-fixed, is recorded with the subspaces themselves, in *The Remarkable Subspaces* above.

## Summary

The base conventions are one object read in order. The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$ satisfying $\vec e_k^2=-e_t$, over complex coefficients; the scalar unit $i$ is central, and multiplication by it is one map whose restrictions are read in *Special Element Conventions*. The element is written with its case and its tilde, and its coefficients $Q_\mu=q_\mu+iq'_\mu$ split it into a quaternion part and an antiquaternion part.

The conjugations cut the algebra into the remarkable subspaces, and the subspaces carry the two sector names. **There is no dictionary**, because there is nothing to map: the parameters are the coordinates, $(r_t,\ i r'_t)$ on the time slot and $(r_x,r_y,r_z)$ with $(i r'_x,i r'_y,i r'_z)$ on the space slots, and the only conversion in the scheme is $c$, between the length coordinate and the second. The pure elements — those with no scalar part — are written with the arrow and without the tilde, $\vec Q$. A duo-complex number is written $Q=(Q_{\blacktriangle},Q_{\blacktriangledown})$, a pair of complex coordinates with no product, and the reduced biquaternion $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ is that pair together with the multiplication by $j$.

The angle is one letter in two cases: $\theta$ is a real angle and $\Theta=\theta+i\theta'$ a complex one, with the central phase the real case and the boost $\Theta=-i\theta_{\mathrm{rpd}}$ the pure imaginary case. The rest of the conventions is in the eight companion articles — products and forms, norms and pairings, special elements, frames, matrix models, operators and calculus, indices and notation, and physical units and common elements — each stated after the one it depends on.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | The biquaternion algebra, isomorphic to $M_2(\mathbb{C})$ |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\lambda e_t=\exp(i\theta J)$ | The central phase, carried by the first coordinate $Q_t$ and extended to the four by $\mathbb{C}$-linearity |
| $\theta$; $\Theta=\theta+i\theta'$ | The generic real angle and the generic complex angle, with real part $\theta$ and imaginary part $\theta'$; the case is the field of the angle — the central phase is the real case and the boost $\Theta=-i\theta_{\mathrm{rpd}}$ the pure imaginary one (§*The Angle and Its Two Cases*) |
| $J=L_{ie_t}$ | The one complex structure of $\mathbb{B}$, of which the phase is the exponential |
| $S_+(\vec u)\oplus S_-(\vec u)$ | The polarization, the two planes; a frame datum, not a pair of halves |
| $\tilde Q = \tilde q + i\tilde q'$ | The element and its split into a quaternion part and an antiquaternion part |
| $\vec Q$ | The vector part of an element, a pure element when read on its own, $\mathrm{Sc}(\vec Q)=0$ |
| $\vec q$ | Position, the pure quaternion $\vec q=r_x\vec e_x+r_y\vec e_y+r_z\vec e_z$ |
| $\mathbb{B}_{C} = \{Q_t e_t\}$ | Centre subspace, the complex time sector |
| $\mathbb{B}_{V}$ | The vector subspace, the complex space sector, real dimension six |
| $\mathbb{B}_{H}$, $\mathbb{B}_{iH}$ | Real-quaternion and antiquaternion subspaces, the real and imaginary halves |
| $\mathbb{B}_{\Psi}$ | Hermitian subspace, the informational sector |
| $\mathbb{B}_{\Phi} = \{\tilde Q : \tilde Q^\flat=\tilde Q\}$ | Anti-Hermitian subspace, the material sector; $\flat=-{}^{*}$ |
| $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ | The reduced biquaternion, a duo-complex pair with the multiplication by $j$ |
| $\xi$; $Ξ$ | The generic field, real and complex: $\xi$ a real scalar field, $Ξ$ a complex one, the case following the coefficient, §*The Elements and their Coefficients* |
| $\tilde\xi$; $\tilde{Ξ}$ | The generic field as an element, quaternion layer and biquaternion layer, $\tilde{Ξ}=Ξ e_t$ when central; the caret names the role, `scl` the scalar, `sp` the spinor, `fop` the field operator |
| $\theta_{\mathrm{rpd}}$ | The rapidity, the imaginary part of the angle, $\Theta=-i\theta_{\mathrm{rpd}}$ |

## Further Reading

- [Conventions of the Products and the Forms](product-and-form-conventions.html), for the twelve products and the four forms.
- [Conventions of the Norms and the Pairings](norm-and-pairing-conventions.html), for the four norms, the unitary convention, the polar word and the three pairings.
- [Conventions of the Special Elements](special-element-conventions.html), for the central map, the root, the idempotent, the nilpotent and spin.
- [Conventions of the Frames](frame-and-metric-conventions.html), for the $\mathbb{B}$ frame, the $\mathbb{B}_{\Phi}$ frame, the Clifford map and the one metric they share.
- [Conventions of the Matrix Models](matrix-representations-conventions.html), for the $2\times2$ isomorphism, the $4\times4$ regular representation and the Clifford structure.
- [Operator and Calculus Conventions](operator-and-calculus-conventions.html), for the operators and for the derivative marks, the gradient and the d'Alembertian.
- [Physics Units and Common Elements Conventions](physics-units-and-common-elements-conventions.html), for the SI units, the two writings of the temporal slot and the catalogue of the tilde glyphs.
- [Index and Notation Conventions](index-and-notation-conventions.html), for the two superscript tokens and the rules of the subscripts.
- [The Biquaternion Space, the Group of Involutions and the Six Subspaces](the-biquaternion-space-the-group-of-involutions-and-the-six-subspaces.html), companion article, for the relations among the subspaces defined here — their coordinate blocks, intersections, spans, gradings and biquaternion norms.
- W. R. Hamilton, *Lectures on Quaternions* (Hodges and Smith, 1853), for the original quaternion algebra and its units.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for idempotents, minimal left ideals and the conjugations of a Clifford algebra.
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for real structures and real forms on Clifford algebras.
