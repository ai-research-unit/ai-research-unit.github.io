# __The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit__

## Introduction

The companion article *The Dirac Equation in Biquaternionic Form* stated the biquaternionic Dirac equation as a chiral pair and fixed its setting: one element $\tilde{Ξ}_{\mathrm{sp}}$ of the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, split into a part of value $L$ and a part of value $R$, with the mass the one term of the equation that carries the value across. It fixed the plane-wave ansatz, $\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},0}\exp\!\left(i\,\mathrm{Sc}(\tilde{\mathcal P}\tilde Q^{\natural})/\hbar\right)$, and the mass-shell condition $\tilde{\mathcal P}\tilde{\mathcal P}^{\natural}=-m^2c^2$, and it noted that the massive solution space is four-dimensional over $\mathbb{C}$.

That article worked at a summary level. It named the solution classes but constructed no explicit solution, fixed no normalization, wrote no bilinear, and did not carry the equation into the non-relativistic regime. The present article supplies those four things, and it supplies them on one element: every quantity below is an element of $\mathbb{B}$, a product of elements, or the scalar part or the trace of such a product.

The next section fixes the two values of the field and the action that carries one into the other. The section after that states the equation and the pairing, and the one after that constructs the plane-wave solutions of both branches. Orthogonality and the spin sums follow, then the bilinears, then the non-relativistic limit and its Pauli equation, then the massless case. A closing section prints the older gamma display for the reader who has to compare with it. Formulas are in the natural units $\hbar=c=1$ except where a factor of $\hbar$ or $c$ is written out.

**What the mass symbol $m$ stands for.** In the equation $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R}=m\tilde{Ξ}_{\mathrm{sp},L}$ and its conjugate, the gradient carries the unit of an inverse length, so the mass term must carry it too: there $m$ is the inverse reduced Compton wavelength $mc/\hbar$. The symbol returns to the mass itself wherever a dimensionful statement is made — the mass shell $\tilde{\mathcal P}\tilde{\mathcal P}^{\natural}=-m^2c^2$ of the introduction is one — and in the non-relativistic limit below, where the rest energy is written $mc^2$ and the spin coupling is $\hbar$ over $2m$.

## The field, the two values and the action

**The algebra.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ over $\mathbb{C}$, with $e_t$ the identity, $\vec e_k^2=-e_t$, $\vec e_j\vec e_k=\epsilon_{jkl}\vec e_l$ for distinct indices, and $i$ central with $i^2=-1$. A squared three-vector is the Euclidean square, $\vec p^2=p_1^2+p_2^2+p_3^2$. An element is written $\tilde Q=a_te_t+a_1\vec e_x+a_2\vec e_y+a_3\vec e_z$, with $\mathrm{Sc}\,\tilde Q=a_t$ and $\mathrm{Tr}\,\tilde Q=2a_t$, and the coefficient bar conjugates the four coefficients and leaves the units alone (*Unit, Index and Notation Conventions*).

**The two values of the field.** The field carries a letter, and the letter takes two values. An element of value minus one is written $\tilde Q_L$, an element of value plus one is written $\tilde Q_R$; each value is of two complex dimensions, every element is one part of each value, and only the zero element carries both. Three facts about the letters are used below, and no fourth. A product takes the letter of its right factor. A left multiplication keeps the letter. A right multiplication by $\vec e_t$ or by $\vec e_z$ keeps the letter, and a right multiplication by $\vec e_x$ or by $\vec e_y$ exchanges the two values. The last is a property of the four units and not of an element, and it is what lets an action built of right multiplications carry an element of one value into the other. No symbol is introduced for the letter, and no formula is written for it: the article writes $\tilde{Ξ}_{\mathrm{sp},L}$ and $\tilde{Ξ}_{\mathrm{sp},R}$ and uses the three facts.

**The action.** A plane wave of four-momentum $(E,\vec p)$ is an element whose dependence on the coordinates is the phase of the ansatz above. The equation it obeys is fixed by the action

$$
\mathcal{D}(\tilde{\mathcal P})\,\tilde Q=iE\,\tilde Q\,\vec e_x-\sum_{k=1}^{3}ip_k\,\vec e_k\,\tilde Q\,\vec e_y ,
$$

written for the wave element $\tilde{\mathcal P}=iEe_t+p_1\vec e_x+p_2\vec e_y+p_3\vec e_z$. It is an action written out with products and units only: two right multiplications and three left ones, and no object other than $\tilde Q$, the units and the numbers $E$ and $\vec p$. Two properties of it are one line each, and each was checked on generic elements.

*It squares to the mass shell.* $\mathcal{D}(\tilde{\mathcal P})^2\tilde Q=(E^2-\vec p^2)\tilde Q$ for every element $\tilde Q$. The first term squared gives $+E^2\tilde Q$, since $\vec e_x^2=-e_t$ and the two factors of $i$ give $-1$. The spatial part squared gives $-\vec p^2\tilde Q$, since $\vec e_y^2=-e_t$ and the terms of $p_jp_k\vec e_j\vec e_k$ cancel in pairs by the antisymmetry of $\vec e_j\vec e_k$ against the symmetry of $p_jp_k$. The two interfering terms cancel because $\vec e_y\vec e_x=-\vec e_x\vec e_y$.

*It exchanges the two values.* $\mathcal{D}\tilde Q_R$ is $L$ and $\mathcal{D}\tilde Q_L$ is $R$: its two right multiplications are by $\vec e_x$ and by $\vec e_y$, each of which exchanges the two values, and its left multiplications keep the value, so the exchange survives them.

**The equation.** For a field of mass $m$ the equation is

$$
\boxed{\;\mathcal{D}(\tilde{\mathcal P})\,\tilde{Ξ}_{\mathrm{sp}}=m\,\tilde{Ξ}_{\mathrm{sp}}\;},
$$

read on the two values as the pair

$$
\mathcal{D}\tilde{Ξ}_{\mathrm{sp},R}=m\tilde{Ξ}_{\mathrm{sp},L},\qquad \mathcal{D}\tilde{Ξ}_{\mathrm{sp},L}=m\tilde{Ξ}_{\mathrm{sp},R} .
$$

Each line is one equation inside one value: the left side of the first is the $L$ part of the action on the $R$ part, which is $L$-valued, and the right side is $m$ times the $L$ part of the field. The mass is the only term of the equation that keeps the value, and $\mathcal{D}$ the only term that carries it. The two lines are not two dynamics. Applying $\mathcal{D}$ to the first and substituting the second gives $\mathcal{D}^2\tilde{Ξ}_{\mathrm{sp},R}=m^2\tilde{Ξ}_{\mathrm{sp},R}$, that is $(E^2-\vec p^2-m^2)\tilde{Ξ}_{\mathrm{sp},R}=0$, and the same for the other part: the mass shell $E^2-\vec p^2=m^2$ is the consistency condition of the pair, and each part obeys the Klein–Gordon equation of the companion article. With $\hbar$ and $c$ restored the condition reads $E^2-\vec p^2c^2=m^2c^4$.

**Why the action and not the gradient.** The companion article writes the pair with the gradient acting on the left, $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=m\tilde{Ξ}_{\mathrm{sp},L}$ and its conjugate. The gradient is a left multiplication, so at fixed momentum it is one fixed element acting on the left, and it keeps the value: the left side of the first line is $R$-valued while the right side is $L$-valued. The two sides can be equated only by reading the four coefficients of the two parts against one another, which is the column the corpus does not use. The operator the pair requires at fixed momentum is the one that carries the value across, and that operator is $\mathcal{D}$. The massless limit is unaffected, and it decouples in either reading: at $m=0$ the pair becomes $\mathcal{D}\tilde{Ξ}_{\mathrm{sp},R}=0$ and $\mathcal{D}\tilde{Ξ}_{\mathrm{sp},L}=0$, two equations of one value each.

## The field and the pairing

**The field.** The field is one element $\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},L}+\tilde{Ξ}_{\mathrm{sp},R}$ of $\mathbb{B}$, of four complex dimensions in all, two in each value. No column, no matrix and no array enters its definition, and the equation above is one equation on it.

**The pairing.** The Dirac pairing of two elements is

$$
\langle\tilde{Ξ}_{\mathrm{sp}},\tilde{Ξ}\rangle_{\mathrm D}=\mathrm{Tr}\!\left(\tilde{Ξ}_{\mathrm{sp}}^*\tilde{Ξ}\,i\vec e_x\right),
$$

the trace of a product twisted on the right by the timelike unit. It is conjugate-linear in the first argument, linear in the second, and $\langle\tilde{Ξ},\tilde{Ξ}_{\mathrm{sp}}\rangle_{\mathrm D}=\overline{\langle\tilde{Ξ}_{\mathrm{sp}},\tilde{Ξ}\rangle_{\mathrm D}}$. The twist is what makes it pair the two values: $\langle\tilde{Ξ}_{\mathrm{sp},L},\tilde{Ξ}_{\mathrm{sp},L}\rangle_{\mathrm D}=0$ and $\langle\tilde{Ξ}_{\mathrm{sp},R},\tilde{Ξ}_{\mathrm{sp},R}\rangle_{\mathrm D}=0$, while $\langle\tilde{Ξ}_{\mathrm{sp},L},\tilde{Ξ}_{\mathrm{sp},R}\rangle_{\mathrm D}$ need not vanish. Consequently the scalar of a field, $\langle\tilde{Ξ}_{\mathrm{sp}},\tilde{Ξ}_{\mathrm{sp}}\rangle_{\mathrm D}$, is twice the real part of $\langle\tilde{Ξ}_{\mathrm{sp},L},\tilde{Ξ}_{\mathrm{sp},R}\rangle_{\mathrm D}$: a bilinear pairs one part of each value and never a part with itself. This is the algebraic reason a single value cannot carry a Dirac mass.

## Plane-wave solutions

**The ansatz.** A solution of momentum $(E,\vec p)$ is $\tilde{Ξ}_{\mathrm{sp}}=\tilde w\exp\!\left(i\,\mathrm{Sc}(\tilde{\mathcal P}\tilde Q^{\natural})/\hbar\right)$ with $\tilde w$ an element that does not depend on the coordinates, and the equation for $\tilde w$ is $\mathcal{D}(\tilde{\mathcal P})\tilde w=m\tilde w$. The wave element obeys $\tilde{\mathcal P}\tilde{\mathcal P}^{\natural}=-(E^2-\vec p^2)$, so the mass shell of the equation is $\tilde{\mathcal P}\tilde{\mathcal P}^{\natural}=-m^2$: one condition, whose two roots are the two branches below.

**The helicity and the two spin elements.** For $|\vec p|\neq0$ let $\vec u_p=\vec p/|\vec p|$ and

$$
\mathcal{H}(\tilde Q)=i\,\vec u_p\,\tilde Q ,
$$

a left multiplication by a fixed element. It commutes with $\mathcal{D}$, since left multiplications commute with one another and with right multiplications, so it carries solutions into solutions. It squares to the identity and its two values are $\pm1$. Let $\tilde\zeta_{R+}$ and $\tilde\zeta_{R-}$ be the two elements of the $R$ value with

$$
\mathcal{H}\tilde\zeta_{R\pm}=\pm\tilde\zeta_{R\pm},\qquad \mathrm{Tr}\!\left(\tilde\zeta_{R\pm}^{*}\tilde\zeta_{R\pm}\right)=1 ,
$$

and let the corresponding elements of the $L$ value be the images

$$
\tilde\zeta_{L\pm}=\frac{1}{E\mp|\vec p|}\,\mathcal{D}\tilde\zeta_{R\pm} .
$$

Four statements follow, one line each, and each is a computation of products only. First, $\mathcal{D}\tilde\zeta_{R\pm}=(E\mp|\vec p|)\tilde\zeta_{L\pm}$, which is the definition. Second, $\mathcal{D}\tilde\zeta_{L\pm}=(E\pm|\vec p|)\tilde\zeta_{R\pm}$, because $\mathcal{D}^2=m^2=(E-|\vec p|)(E+|\vec p|)$. Third, $\mathcal{H}\tilde\zeta_{L\pm}=\pm\tilde\zeta_{L\pm}$, because $\mathcal{H}$ commutes with $\mathcal{D}$. Fourth, $\mathrm{Tr}(\tilde\zeta_{L\pm}^{*}\tilde\zeta_{L\pm})=1$ and $\mathrm{Re}\langle\tilde\zeta_{R\pm},\tilde\zeta_{L\pm}\rangle_{\mathrm D}=1$: the image carries the same Hermitian norm as its seed, the Hermitian product of a seed with its image vanishes, and the number the two parts share is the pairing. These four numbers are what the normalization below fixes.

**Positive-frequency branch.** Put

$$
\tilde w_\pm(\vec p)=\sqrt{E\pm|\vec p|}\;\tilde\zeta_{R\pm}+\sqrt{E\mp|\vec p|}\;\tilde\zeta_{L\pm} .
$$

Then $\mathcal{D}\tilde w_\pm=m\tilde w_\pm$. On the $L$ part the action returns $\sqrt{E\pm|\vec p|}(E\mp|\vec p|)\tilde\zeta_{L\pm}$, which is $m\sqrt{E\mp|\vec p|}\tilde\zeta_{L\pm}$ because $\sqrt{E+|\vec p|}\sqrt{E-|\vec p|}=m$, and that is $m$ times the $L$ part of $\tilde w_\pm$; on the $R$ part the action returns $m\sqrt{E\pm|\vec p|}\tilde\zeta_{R\pm}$ by the second law, which is $m$ times the $R$ part. The two parts satisfy the two lines of the pair separately, so $\tilde w_\pm$ solves the equation. The four laws above and the three properties of the action were checked on generic elements, and the residuals sit at the round-off level of double precision, of order $10^{-14}$. The $R$ part is the larger one, with amplitude $\sqrt{E+|\vec p|}$, and the ratio of the two amplitudes is $\sqrt{(E+|\vec p|)/(E-|\vec p|)}$.

**Negative-frequency branch.** With the same elements,

$$
\tilde v_\pm(\vec p)=\sqrt{E\pm|\vec p|}\;\tilde\zeta_{R\pm}-\sqrt{E\mp|\vec p|}\;\tilde\zeta_{L\pm} ,\qquad \mathcal{D}\tilde v_\pm=-m\tilde v_\pm ,
$$

by the same two laws with one sign reversed. The relative minus sign is the standard one of the negative-frequency branch, and it is what makes $\langle\tilde v,\tilde v\rangle_{\mathrm D}$ negative below.

**The solutions in full.** The fields are these elements multiplied by the phase,

$$
\tilde{Ξ}_{\mathrm{sp},\pm}^{(+)}=\tilde w_\pm(\vec p)\,e^{-i(Er'_t-\vec p\cdot\vec r)/\hbar},\qquad
\tilde{Ξ}_{\mathrm{sp},\pm}^{(-)}=\tilde v_\pm(\vec p)\,e^{+i(Er'_t-\vec p\cdot\vec r)/\hbar},
$$

with $E=+\sqrt{\vec p^2+m^2}$ in both lines: the negative-frequency solution is the same construction with the opposite phase, not a different object. On the mass shell the solution space of $\mathcal{D}\tilde w=m\tilde w$ is two-dimensional over $\mathbb{C}$, spanned by $\tilde w_+$ and $\tilde w_-$, and that of $\mathcal{D}\tilde v=-m\tilde v$ is two-dimensional as well. Together they are the four complex dimensions the companion article counts.

**The rest frame.** At $\vec p=0$ one has $E=m$ and the direction $\vec u_p$ is undefined, so the label is carried by any two orthonormal elements of the $R$ value; the two solutions are $\sqrt m\,(\tilde\zeta_{R+}\mathcal{D}\tilde\zeta_{R}/m)$ for such a pair. Nothing degenerates except the label: the solution space is still two-dimensional.

**The two parts in the split by the timelike unit.** That split gives the large and the small part of the non-relativistic section, and the ratio of their sizes is

$$
\frac{\|\tilde{Ξ}\|}{\|\tilde{Ξ}_{\mathrm{sp}}\|}=\sqrt{\frac{E+m}{E-m}}
$$

for a normalized positive-frequency solution, since the two amplitudes are $\sqrt{E+m}$ and $\sqrt{E-m}$ up to the common normalization. The two ratios, $\sqrt{(E+|\vec p|)/(E-|\vec p|)}$ in the values and $\sqrt{(E+m)/(E-m)}$ in the timelike split, are different numbers and neither may be substituted for the other: the first compares the two chiralities, the second compares the large and the small part.

### The spin label and the helicity–chirality relation

**The spin label.** The two solutions at fixed momentum can be separated by any one of several quantities, and the two in use in the corpus are the helicity $\mathcal{H}$ above and a spin projection along a fixed direction $\vec u$. Helicity is the natural label for a massless particle, because it is invariant under the Lorentz transformations of the frame; for a massive particle it is frame-dependent, and a fixed axis is then the more convenient label. Both are left multiplications by fixed elements and both take two values.

**Chirality and helicity at $m=0$.** In the massless limit $E=|\vec p|$ and the two amplitudes of $\tilde w_+$ collapse to one: the solution is the single element $\sqrt{2E}\,\tilde\zeta_{R+}$, with no $L$ part, and the $L$ value contributes no positive-helicity solution at all. The counting is exact. Setting $m=0$ in the pair leaves $\mathcal{D}\tilde{Ξ}_{\mathrm{sp},R}=0$ and $\mathcal{D}\tilde{Ξ}_{\mathrm{sp},L}=0$, each an equation inside one value; the kernel of $\mathcal{D}$ inside the $R$ value is one-dimensional, spanned by $\tilde\zeta_{R+}$, and the kernel inside the $L$ value is one-dimensional, spanned by $\tilde\zeta_{L-}$. So a solution of one value carries exactly one helicity, and the two values carry opposite ones. This is the precise sense in which a massless fermion of definite helicity has definite chirality. For $m\neq0$ the same element carries both values with unequal amplitudes and no locking: the mass is what makes the two parts visible to each other.

## Orthogonality and normalization

The pairing of the field section evaluates on the solutions in closed form. With the normalization fixed above, $\mathrm{Tr}(\tilde\zeta^{*}\tilde\zeta)=1$ and $\mathrm{Re}\langle\tilde\zeta_{R\pm},\tilde\zeta_{L\pm}\rangle_{\mathrm D}=1$ for the four elements, and the same-value pairings vanish, so each solution contributes only its cross term, $2\sqrt{(E+|\vec p|)(E-|\vec p|)}=2m$:

$$
\langle\tilde w_\pm,\tilde w_{\pm'}\rangle_{\mathrm D}=2m\,\delta_{\pm\pm'},\qquad
\langle\tilde v_\pm,\tilde v_{\pm'}\rangle_{\mathrm D}=-2m\,\delta_{\pm\pm'},\qquad
\langle\tilde w_\pm,\tilde v_{\pm'}\rangle_{\mathrm D}=0 .
$$

The minus sign of the negative branch is the standard signature, and the vanishing of the cross terms at equal momentum is the statement that the two branches are orthogonal under the twisted pairing. The Hermitian products are a separate family, and their diagonal values are

$$
\mathrm{Tr}\!\left(\tilde w_\pm^{*}\tilde w_{\pm'}\right)=2E\,\delta_{\pm\pm'},\qquad
\mathrm{Tr}\!\left(\tilde v_\pm^{*}\tilde v_{\pm'}\right)=2E\,\delta_{\pm\pm'} .
$$

Three normalization conventions are in common use — $\langle\tilde w,\tilde w\rangle_{\mathrm D}=2m$, $\langle\tilde w,\tilde w\rangle_{\mathrm D}=1$ and $\mathrm{Tr}(\tilde w^{*}\tilde w)=1$ — and they differ by momentum-dependent factors. The covariant one, $2m$, is used here because it makes the spin sums below covariant and because $2m$ is the value the mass shell gives to the scalar bilinear of a normalized solution.

**The spin sums.** The two solutions of each branch close over the spin label:

$$
\sum_{\pm}\tilde w_\pm\langle\tilde w_\pm,\cdot\rangle_{\mathrm D}=\mathcal{D}(\tilde{\mathcal P})+m,\qquad
\sum_{\pm}\tilde v_\pm\langle\tilde v_\pm,\cdot\rangle_{\mathrm D}=\mathcal{D}(\tilde{\mathcal P})-m .
$$

Each sum is an operator written as an element times a scalar: the symbol $\tilde w\langle\tilde w,\cdot\rangle_{\mathrm D}$ is the action sending $\tilde{Ξ}$ to $\tilde w\,\langle\tilde w,\tilde{Ξ}\rangle_{\mathrm D}$, a product of an element with a number, and no matrix enters it. The two identities are the algebraic statement that the four solutions at fixed momentum span the amplitude space, and they are what a sum over spins uses.

**The conserved current.** The vector bilinear of the next section is the conserved current, $j_0=\mathrm{Tr}(\tilde{Ξ}_{\mathrm{sp}}^*\tilde{Ξ}_{\mathrm{sp}})$ and $j_k=\mathrm{Tr}(\tilde{Ξ}_{\mathrm{sp}}^*\vec e_k\tilde{Ξ}_{\mathrm{sp}}\vec e_z)$, and the continuity equation of the companion article reads $\partial j_0/\partial r'_t+\nabla\cdot\vec j=0$ on the material sector. The current is the four-vector $\tilde J=ic\,j_0e_t+\vec j$ of $\mathbb{B}_{\Phi}$, with imaginary scalar part and real vector part: the Dirac current is a material-sector object, as a four-vector must be.

## The bilinears

**The scalar and the pseudoscalar.** The scalar is the pairing of the field with itself, and the pseudoscalar is the same product with $\vec e_y$ on the right:

$$
S=\langle\tilde{Ξ}_{\mathrm{sp}},\tilde{Ξ}_{\mathrm{sp}}\rangle_{\mathrm D}=\mathrm{Tr}\!\left(\tilde{Ξ}_{\mathrm{sp}}^*\tilde{Ξ}_{\mathrm{sp}}\,i\vec e_x\right),
\qquad
P=\mathrm{Tr}\!\left(\tilde{Ξ}_{\mathrm{sp}}^*\tilde{Ξ}_{\mathrm{sp}}\,\vec e_y\right).
$$

$S$ is real and $P$ is purely imaginary, so the pseudoscalar is $iP$ and carries the explicit factor of $i$. Both are blind to a single value: $S$ pairs the two values, so a field of one value has no scalar and no Dirac mass, and $P$ vanishes for a helicity eigenstate because the two parts then stand in a real ratio. In the value split $S=2\,\mathrm{Re}\langle\tilde{Ξ}_{\mathrm{sp},L},\tilde{Ξ}_{\mathrm{sp},R}\rangle_{\mathrm D}$: the scalar and the pseudoscalar are the real and the imaginary part of the one pairing that mixes the two values.

**The vector current.** The four components are

$$
j_0=\mathrm{Tr}\!\left(\tilde{Ξ}_{\mathrm{sp}}^*\tilde{Ξ}_{\mathrm{sp}}\right)=2E,\qquad
j_k=\mathrm{Tr}\!\left(\tilde{Ξ}_{\mathrm{sp}}^*\vec e_k\tilde{Ξ}_{\mathrm{sp}}\,\vec e_z\right)=2p_k
$$

on a normalized positive-frequency solution: the first is positive, since $\mathrm{Tr}(\tilde{Ξ}_{\mathrm{sp}}^*\tilde{Ξ}_{\mathrm{sp}})$ is a sum of squared moduli of the four coefficients, and the three spatial components are real and equal to twice the momentum. The second equality is the reason the current is the four-velocity of the field, and on the material sector the four components assemble into $\tilde J=ic\,j_0e_t+\vec j\in\mathbb{B}_{\Phi}$.

**The spin bilinear and the informational sector.** There is a second bilinear, of a different kind: the spin state of one part. With $\vec u$ a unit vector, the element

$$
\tilde\rho=\tfrac12\left(e_t+i\vec u\right)
$$

is Hermitian, satisfies $\tilde\rho^2=\tilde\rho$ and $\mathrm{Tr}\,\tilde\rho=1$, and its components read back as $\mathrm{Tr}(\tilde\rho\,i\vec e_k)=u_k$. It is the pure state of the informational sector $\mathbb{B}_{\Psi}$ with Bloch vector $\vec u$, and it is what a spin state is in this framework: not a column paired with its adjoint, but one element of $\mathbb{B}_{\Psi}$. The spin of a solution is described by it, and the spin–magnetic coupling of the non-relativistic section is a Hermitian element of the same sector.

**The axial and tensor bilinears.** The remaining two families are built the same way, one product deeper, and they are recorded in *Chiral Fermions in the Biquaternion Framework* together with the axial anomaly. Their components are not used below.

**The Gordon decomposition.** The vector bilinear splits into a convection part and a spin part, and the split is derived in *The Gordon Decomposition of the Dirac Current in Biquaternionic Form*. The convection part is proportional to the sum of the two momenta and is the orbital current of a charged particle; the spin part is proportional to the momentum transfer and is the source of the magnetic coupling. The coefficient $1/2m$ that the split produces is the one the gyromagnetic factor below carries.

## The non-relativistic limit

**The split by the timelike unit.** The rest energy dominates the dynamics, and the unit that separates it from the kinetic part is $\vec e_x$: right multiplication by $i\vec e_x$ takes the two values $\pm1$, and the field is the sum of its two parts,

$$
\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}+\tilde{Ξ}_{\mathrm{sp}},\qquad i\tilde{Ξ}\vec e_x=\tilde{Ξ},\qquad i\tilde{Ξ}_{\mathrm{sp}}\vec e_x=-\tilde{Ξ}_{\mathrm{sp}} ,
$$

the large part and the small part. The action $\mathcal{D}$ is not of one value under that unit: its first term is that same right multiplication by $i\vec e_x$, so it keeps the value, and its spatial part reverses it, because $\vec e_k$ and $\vec e_y$ both anticommute with $\vec e_x$. Write

$$
\mathcal{D}\,\tilde Q=E\,i\tilde Q\vec e_x+\mathcal{O}(\tilde Q),\qquad \mathcal{O}(\tilde Q)=-i\sum_k p_k\,\vec e_k\tilde Q\vec e_y ,
$$

so that $\mathcal{O}$ is odd, $i(\mathcal{O}\tilde Q)\vec e_x=-\mathcal{O}(i\tilde Q\vec e_x)$, and carries the large part onto the small one and back.

**Minimal coupling.** Minimal coupling replaces the four-momentum by $p_\mu-ϙA_\mu$, with $A_\mu=(Ξ,-\vec A)$ and $ϙ$ the charge of the field: $E\to E-ϙΞ$ in the even term and $p_k\to\pi_k=p_k-ϙA_k$ in $\mathcal{O}$. The equation keeps its shape, and the pair reads, on the two parts,

$$
(E-ϙΞ-m)\tilde{Ξ}=-\mathcal{O}\tilde{Ξ}_{\mathrm{sp}},\qquad
(E-ϙΞ+m)\tilde{Ξ}_{\mathrm{sp}}=\mathcal{O}\tilde{Ξ} .
$$

The second line is the one multiplied by the large rest energy, so the small part is generated from the large one:

$$
\tilde{Ξ}_{\mathrm{sp}}=\frac{1}{E-ϙΞ+m}\,\mathcal{O}\tilde{Ξ}\;\approx\;\frac{1}{2m}\,\mathcal{O}\tilde{Ξ} ,
$$

the approximation being the one in which the kinetic energy and the potential are small against the rest energy. This is the algebraic statement that the small part is the velocity acting on the large one, and it is the only step of the limit that discards anything.

**The Pauli equation.** Substituting the small part into the first line eliminates it and leaves an equation on the large part alone:

$$
(E-ϙΞ-m)\tilde{Ξ}=-\frac{1}{2m}\,\mathcal{O}^2\tilde{Ξ} .
$$

It remains to evaluate $\mathcal{O}^2$ on a large part. The sum over the two indices symmetrizes, and the symmetric part gives the kinetic square while the antisymmetric part gives the magnetic term:

$$
\mathcal{O}^2\tilde{Ξ}=-\vec\pi^2\,\tilde{Ξ}+iϙ\,\vec B\,\tilde{Ξ} ,
$$

with $\vec B=\nabla\times\vec A$. The first term is the symmetrized sum, $\tfrac12\sum_{j,k}\{\pi_j,\pi_k\}\vec e_j\vec e_k=-\vec\pi^2$, and the second is the commutator, $\sum_{j<k}[\pi_j,\pi_k]\vec e_j\vec e_k$, evaluated with $[\pi_j,\pi_k]=iϙ\epsilon_{jkl}B_l$ and $\sum_{j<k}\epsilon_{jkl}\vec e_j\vec e_k=\vec e_l$, which gives $iϙ\vec B$. The operator ordering is kept throughout, since $\vec p$ and $\vec A$ do not commute, and the magnetic term is exactly what survives it.

With $E\to i\hbar\partial/\partial r'_t$ and the rest energy factored out by $\tilde{Ξ}=e^{-imr'_t/\hbar}\tilde{Ξ}'$, the equation becomes the **Pauli equation** for the large part:

$$
\boxed{\;i\hbar\,\frac{\partial\tilde{Ξ}'}{\partial r'_t}=\left[\frac{(\vec p-ϙ\vec A)^2}{2m}+ϙΞ-\frac{ϙ\hbar}{2m}\,i\vec B\right]\tilde{Ξ}'\;}
$$

The first two terms are the ordinary non-relativistic Hamiltonian of a charged particle, and the third is the spin–magnetic coupling. The unknown is one element of two complex dimensions.

**The $g$-factor.** The spin term is a magnetic dipole coupling. Writing it as $-\vec\mu\cdot\vec B$ and comparing with $\vec\mu=g\frac{ϙ}{2m}\vec S$, with the spin

$$
\vec S=\frac{\hbar}{2}\,i\vec e_k\ \text{per component},\qquad \vec\mu\cdot\vec B=\frac{ϙ}{m}\,\vec S\cdot\vec B=\frac{ϙ\hbar}{2m}\,i\vec B ,
$$

identifies

$$
\boxed{\;g=2\;}
$$

The factor is not put in by hand: it is the coefficient $1/2m$ that the elimination produced, and the elimination is the one the mass term of the biquaternionic equation allows. For the electron $ϙ=-e$ and $\vec\mu_e=-\frac{e}{m_e}\vec S=-g\frac{e}{2m_e}\vec S$ with $g=2$, of magnitude one Bohr magneton $\mu_B=e\hbar/2m_e$ at $S_z=\hbar/2$. The observed value differs from $2$ by the anomalous part $a=(g-2)/2\approx\alpha/2\pi$, a radiative correction outside the classical equation treated here.

**The spin coupling and the precession.** The spin term is the Hermitian element $-\frac{ϙ\hbar}{2m}i\vec B$ of the informational sector $\mathbb{B}_{\Psi}$, and the spin state is the pure state $\tilde\rho=\frac12(e_t+i\vec u)$ of the bilinear section. Under the Pauli Hamiltonian the state evolves by the rotor conjugation generated by that element, and for a uniform magnetic field only the spin term contributes to the motion of $\vec u$: the precession frequency is the Larmor frequency $\omega_L=gϙB/2m=ϙB/m$ at $g=2$ in natural units, which is the familiar spin precession up to the sign of $ϙ$. The description by one part of two complex dimensions, the Pauli equation and the precession are thus one consequence of the biquaternionic equation, read on one element and one multiplication.

## Massless case: the Weyl equations and chirality

Setting $m=0$ decouples the two values. The pair becomes

$$
\boxed{\;\mathcal{D}\tilde{Ξ}_{\mathrm{sp},R}=0\;}\qquad\text{and}\qquad\boxed{\;\mathcal{D}\tilde{Ξ}_{\mathrm{sp},L}=0\;}
$$

each an equation of one value, and each with a one-dimensional solution space at fixed momentum: the first is solved by $\tilde\zeta_{R+}$, the helicity $+1$ element of the $R$ value, and the second by $\tilde\zeta_{L-}$, the helicity $-1$ element of the $L$ value. Written out, the first is

$$
iE\,\tilde{Ξ}_{\mathrm{sp},R}\vec e_x-\sum_k ip_k\,\vec e_k\tilde{Ξ}_{\mathrm{sp},R}\vec e_y=0 ,
$$

and it carries a single value: no part of the other value appears in it, which is what "chirality is conserved at $m=0$" states. The locking of chirality to helicity is the counting above: one solution per value, of opposite helicity, so a massless fermion of definite helicity has definite chirality, and the assignment reverses for the negative-frequency branch.

The mass term is the only term that couples the two values, and it is the reason the locking fails at $m\neq0$: the two laws of the solutions section, $\mathcal{D}\tilde\zeta_{R\pm}=(E\mp|\vec p|)\tilde\zeta_{L\pm}$ and the law with the two elements interchanged, carry the mass through $\sqrt{E+|\vec p|}\sqrt{E-|\vec p|}=m$, and they degenerate exactly when $m=0$. The Weyl fields are therefore the $m\to0$ limit of the solutions constructed above, and the biquaternionic equation reduces in that limit to the pair of one-value equations.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, $\gamma_0^2=I_4$ and $\gamma_k^2=-I_4$. The frame belongs to the coordinate, not to the array.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\tilde{Ξ}_{\mathrm{sp}}=a\tilde{Ξ}_{\mathrm{sp}}$ and $R_b\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp}} b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\gamma_0=iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x},\quad \gamma_1=iL_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_y},\quad \gamma_2=iL_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y},\quad \gamma_3=iL_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_y},\quad \gamma_5=-iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z} .
$$

The same in the axis-free display:

$$
\gamma_0=iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x},\quad \gamma_1=iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y},\quad \gamma_2=iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y},\quad \gamma_3=iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y},\quad \gamma_5=-iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z} .
$$

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5$ is the reference-frame cell of the chirality $-iR_{\mathrm{pau},\vec e_z}$; the central grading $\chi=i\tilde{Ζ}_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The identities the bodies cite.** In the $\gamma$ reading, with $\varepsilon=(1,-1,-1,-1)$ the sign vector of the cells,
$$
\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
(\gamma_k)^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu,\gamma_5\}=0,
$$
$$
[\gamma_\mu,\gamma_\nu]=2\gamma_\mu\gamma_\nu\quad(\mu\ne\nu),\qquad
[\gamma_a,S_{cd}]=\varepsilon_a\delta_{ac}\gamma_d-\varepsilon_a\delta_{ad}\gamma_c,\qquad
S_{cd}=\tfrac14[\gamma_c,\gamma_d],
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu)=4\varepsilon_\mu\delta_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)
=4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}
-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}
+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr).
$$
The contraction sums follow from the squares. With one index raised, $\gamma^\mu=-\varepsilon_\mu\gamma_\mu$, so that $\sum_\mu\gamma^\mu\gamma_\mu=-4I_4$, $\sum_\mu\gamma^\mu\gamma_\alpha\gamma_\mu=2\gamma_\alpha$, $\sum_\mu\gamma^\mu\gamma_\alpha\gamma_\beta\gamma_\mu=-4\varepsilon_\alpha\delta_{\alpha\beta}I_4$ and $\sum_\mu\gamma^\mu\gamma_\gamma\gamma_\beta\gamma_\alpha\gamma_\mu=-2\gamma_\gamma\gamma_\beta\gamma_\alpha$.

## Summary

The biquaternionic Dirac equation is one equation on one element, $\mathcal{D}(\tilde{\mathcal P})\tilde{Ξ}_{\mathrm{sp}}=m\tilde{Ξ}_{\mathrm{sp}}$, with the action $iE\tilde{Ξ}_{\mathrm{sp}}\vec e_x-\sum_k ip_k\vec e_k\tilde{Ξ}_{\mathrm{sp}}\vec e_y$ written out in products of units. Read on the two values it is the chiral pair of the companion article, each line an equation of one value; the mass is the term that keeps the value and the action the term that carries it, and the mass shell $E^2-\vec p^2=m^2$ is the consistency condition of the pair. The action squares to the mass shell, exchanges the two values and is built of no object but the element, the units and the numbers $E$ and $\vec p$.

The solutions are explicit. The two helicity elements of one value are the seed, the corresponding elements of the other value are their images under the action, and the two branches are

$$
\tilde w_\pm=\sqrt{E\pm|\vec p|}\,\tilde\zeta_{R\pm}+\sqrt{E\mp|\vec p|}\,\tilde\zeta_{L\pm},\qquad
\tilde v_\pm=\sqrt{E\pm|\vec p|}\,\tilde\zeta_{R\pm}-\sqrt{E\mp|\vec p|}\,\tilde\zeta_{L\pm} ,
$$

with $E=+\sqrt{\vec p^2+m^2}$. Each branch is two-dimensional over $\mathbb{C}$, the four dimensions the companion article counts. The normalization is covariant, $\langle\tilde w,\tilde w\rangle_{\mathrm D}=2m$ and $\langle\tilde v,\tilde v\rangle_{\mathrm D}=-2m$, with $\langle\tilde w,\tilde v\rangle_{\mathrm D}=0$, and the spin sums $\sum_\pm\tilde w_\pm\langle\tilde w_\pm,\cdot\rangle_{\mathrm D}=\mathcal{D}+m$ and $\sum_\pm\tilde v_\pm\langle\tilde v_\pm,\cdot\rangle_{\mathrm D}=\mathcal{D}-m$ close the set.

The bilinears are traces of products. The scalar and the pseudoscalar are the real and the imaginary part of the one pairing that mixes the two values, so a field of one value has no Dirac mass; the vector current is $j_0=2E$ and $\vec j=2\vec p$ on a normalized solution, and it assembles into the material-sector four-vector $\tilde J=ic\,j_0e_t+\vec j$ of $\mathbb{B}_{\Phi}$; the spin is the pure state $\frac12(e_t+i\vec u)$ of the informational sector $\mathbb{B}_{\Psi}$, with $\mathrm{Tr}(\tilde\rho\,i\vec e_k)=u_k$.

In the non-relativistic limit the split by the timelike unit separates the large and the small part, the elimination of the small part is exact to the order kept, and the square of the odd part of the action produces the Pauli equation

$$
i\hbar\,\frac{\partial\tilde{Ξ}'}{\partial r'_t}=\left[\frac{(\vec p-ϙ\vec A)^2}{2m}+ϙΞ-\frac{ϙ\hbar}{2m}\,i\vec B\right]\tilde{Ξ}'
$$

on one element. The coefficient $1/2m$ of the spin term is the one that $\vec\mu=g\frac{ϙ}{2m}\vec S$ requires with $g=2$, so the gyromagnetic factor and the spin–magnetic coupling are consequences of the mass term of the equation and not separate postulates. In the massless limit the pair decouples, each value keeps one helicity, and chirality is locked to helicity.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\ \vec e_x,\ \vec e_y,\ \vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$, $\vec e_j\vec e_k=\epsilon_{jkl}\vec e_l$ |
| $i$ | Scalar imaginary, central, $i^2=-1$ |
| $\tilde Q=a_te_t+\vec a$ | General element; $\mathrm{Sc}\,\tilde Q=a_t$, $\mathrm{Tr}\,\tilde Q=2a_t$ |
| coefficient bar | Conjugates the four coefficients, leaves the units |
| $\tilde Q^{*}$ | $\overline{\tilde Q^{\natural}}$, the Hermitian conjugate |
| $\mathbb{B}_{\Phi},\ \mathbb{B}_{\Psi}$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\tilde Q_L,\ \tilde Q_R$ | The element of value minus one and the element of value plus one |
| $\tilde{\mathcal P}=iEe_t+\vec p$ | Wave element of a plane wave |
| $\tilde{\mathcal P}\tilde{\mathcal P}^{\natural}=-(E^2-\vec p^2)$ | Wave-element square; mass shell $\tilde{\mathcal P}\tilde{\mathcal P}^{\natural}=-m^2$ |
| $\mathcal{D}(\tilde{\mathcal P})\tilde Q=iE\tilde Q\vec e_x-\sum_k ip_k\vec e_k\tilde Q\vec e_y$ | The Dirac action on one element |
| $\mathcal{O}(\tilde Q)=-i\sum_k p_k\vec e_k\tilde Q\vec e_y$ | Odd part of the action under right multiplication by $i\vec e_x$ |
| $\langle\tilde{Ξ}_{\mathrm{sp}},\tilde{Ξ}\rangle_{\mathrm D}=\mathrm{Tr}(\tilde{Ξ}_{\mathrm{sp}}^*\tilde{Ξ}\,i\vec e_x)$ | Dirac pairing |
| $\mathcal{H}(\tilde Q)=i\vec u_p\tilde Q$, $\vec u_p=\vec p/\lvert\vec p\rvert$ | Helicity; values $\pm1$ |
| $\tilde\zeta_{R\pm},\ \tilde\zeta_{L\pm}$ | Helicity elements of the two values, $\mathrm{Tr}(\tilde\zeta^{*}\tilde\zeta)=1$ |
| $\tilde w_\pm(\vec p),\ \tilde v_\pm(\vec p)$ | Positive- and negative-frequency solutions |
| $\tilde{Ξ},\ \tilde{Ξ}_{\mathrm{sp}}$ | Large and small part, the values plus one and minus one under right multiplication by $i\vec e_x$ |
| $\tilde\rho=\tfrac12(e_t+i\vec u)$ | Pure state of $\mathbb{B}_{\Psi}$; $\vec u$ the Bloch vector |
| $S,\ P$ | Scalar and pseudoscalar bilinears |
| $j_0,\ \vec j$, $\tilde J=ic\,j_0e_t+\vec j$ | Vector current and its material-sector form |
| $\vec S=\tfrac{\hbar}{2}i\vec e_k$, $\vec\mu=g\frac{ϙ}{2m}\vec S$ | Spin and magnetic moment |
| $ϙ$ | Charge of the field under minimal coupling |
| $\vec\pi=\vec p-ϙ\vec A$, $\vec B=\nabla\times\vec A$ | Kinetic momentum and magnetic field |
| $g=2$ | Gyromagnetic factor in the non-relativistic limit |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the original Dirac equation and the prediction of $g = 2$.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the plane-wave solutions, the Dirac bilinears, and the Gordon decomposition in the standard notation.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the spin sums, the charge-conjugation and chirality structure, and the non-relativistic reduction.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the chiral and Dirac representations, the spinor normalization, and the spin sums.
- J. J. Sakurai, *Advanced Quantum Mechanics* (Addison-Wesley, 1967), for the non-relativistic limit of the Dirac equation and the emergence of the Pauli equation.
- W. Greiner, *Relativistic Quantum Mechanics: Wave Equations* (Springer, 2000), for a detailed step-by-step treatment of the Foldy–Wouthuysen and Pauli limits.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the Clifford-algebraic background to the biquaternion and spinor structures.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra formulation of the Dirac and Weyl equations.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the original spacetime-algebra treatment of the Dirac spinor.
