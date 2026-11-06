# __The Nonlinear Dirac Equation and the Thirring Model in Biquaternionic Form__

## Introduction

A **nonlinear Dirac equation** is a Dirac equation with a self-interaction term. The free equation is linear in the field, so that solutions superpose; a term built from the field itself destroys that superposability and makes the equation describe a fermion that acts on itself. The best-motivated case is geometric. In the **Einstein–Cartan–Sciama–Kibble** extension of general relativity, the spin of matter is the source of the antisymmetric part of the connection, the torsion; that torsion couples to the axial current of the field, and when it is eliminated from the field equations it leaves an effective **axial-axial spin–spin self-interaction** that is cubic in the field. The resulting equation is the standard example of a nonlinearly self-interacting Dirac field, and it is a toy model for the idea that the self-interaction of the fermion regulates its own short-distance behaviour.

The field of this article is an element $\tilde{Ξ}_{\mathrm{sp}}$ of the biquaternion algebra $\mathbb{B}$. Its two parts carry the two values of the subscript, $\tilde{Ξ}_{\mathrm{sp},L}$ and $\tilde{Ξ}_{\mathrm{sp},R}$, the mass couples them, and every interaction below is read on these two parts.

Two models dominate the literature, and they fill the two channels other than the axial one. The **Thirring model** (Thirring 1958) is a $1+1$-dimensional theory whose interaction is the square of the vector current, contracted with the metric, $-\frac{g}{2}\sum_\mu\varepsilon_\mu V_\mu V_\mu$; it is exactly solvable and is the field-theory side of the bosonisation correspondence with the sine-Gordon model. The **Soler model** (Soler 1970) is a $3+1$-dimensional theory whose interaction is the square of the scalar bilinear, $\frac{g}{2}S_{\mathrm d}^2$; it is the mean-field relative of the Nambu–Jona-Lasinio four-fermion interaction, and it is the model in which exact closed-form solutions have been found.

Here $S_{\mathrm d}$ and $V_\mu$ are the two scalar parts
$$S_{\mathrm d}=\mathrm{Sc}\bigl(\tilde{Ξ}_{\mathrm{sp}}^*i\tilde{Ξ}_{\mathrm{sp}}\vec e_x\bigr),
\qquad
V_\mu=\mathrm{Sc}\bigl(\tilde{Ξ}_{\mathrm{sp}}^*i\,(ie_\mu\tilde{Ξ}_{\mathrm{sp}}\vec e_{\nu(\mu)})\vec e_x\bigr),$$
with $\nu(t)=x$ and $\nu(k)=y$, and $\varepsilon_\mu=-g_{\mu\mu}$ the signature sign, $+1$ on the time index and $-1$ on the three spatial ones in the $\mathbb{B}_{\Phi}$ frame of the conventions article. The contraction is written as a sum because no index is summed silently in this corpus, and the sign on the time component is what makes $\sum_\mu\varepsilon_\mu V_\mu V_\mu$ a Lorentz scalar rather than a sum of squares.

This article states these equations, gives the Einstein–Cartan route that produces one of them from geometry, organises the possible interactions by the bilinears they use, and gives the biquaternion interpretation. Its contribution is a **placement of the channels**. The scalar density $S_{\mathrm d}$ is the mass channel, the object whose expectation is the dynamical mass of the companion article on the chiral condensate. The vector current $V_\mu$ is the material-sector current, the object of the companion articles on minimal coupling and on the Gordon decomposition. The axial current $A_\mu$ is the channel the linear mass breaks, so an axial-axial self-interaction is a coupling conjugate to the mass. A quartic interaction is also **bosonic**: it is even in the field and carries zero fermion number, so it passes through the framework's central phase untouched, which is why a self-interaction is compatible with the exact vector symmetry.

What the framework does **not** supply is equally definite. A bilinear here is a *pairing*, the scalar part of a product that carries the fixed element $i\vec e_x$; it is not a product of two elements of $\mathbb{B}$ alone. The free equation of the framework is a left multiplication by the gradient together with a mass that couples the two values, and it contains no such fixed element. The framework names the channels and places them in its sectors; it does not derive the self-interaction from a product in the algebra, and it adds no solution, coupling or prediction of its own.

The article is organised as follows. The next section fixes the field, the pairing and the two writings of the free equation. A section then explains why a self-interaction is cubic and how geometry produces one. A section states the Thirring and Soler models. A section writes the Hehl–Datta equation and fixes its coefficient. A section lists the local bilinears and the channel each model uses. A section gives the biquaternion interpretation. A section records the two-dimensional relations verified here in exact arithmetic. A later section states the same objects in the matrix notation of the sources, so that the two can be compared term by term. The closing sections are the open questions, the summary, the notation table and the literature.

## The Field, the Pairing and the Two Equations

The conventions are those of the companion articles: the algebra and its units, the gradient $\tilde\nabla$, the d'Alembertian $\Box$, the two values of the subscript, and the two sectors $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$. A bilinear of this article is a **pairing** and never an action. It is the scalar part of the product of the Hermitian conjugate of the field, one element built from the field, and the fixed element $i\vec e_x$,
$$\mathrm{Sc}\bigl(\tilde{Ξ}_{\mathrm{sp}}^*iX\vec e_x\bigr),$$
where $X$ is the element the bilinear reads. The fixed element $i\vec e_x$ is the only datum the pairing adds to the field, and it is the same one for every bilinear below. The **slot action** of the index $\mu$ is the action
$$\tilde Q\longmapsto ie_\mu\tilde Q\vec e_{\nu(\mu)},$$
in the element language; it is the derived form of the corresponding frame cell and it is the object every bilinear below is built from. The second line is a derived form again: the sources write the Dirac adjoint as an operator, and the scalar part written here is the same object with the operator spent.

### The Bilinear Pairing

The four densities are four elements at which the pairing is read:
$$S_{\mathrm d}=\mathrm{Sc}\bigl(\tilde{Ξ}_{\mathrm{sp}}^*i\tilde{Ξ}_{\mathrm{sp}}\vec e_x\bigr),
\qquad
P_5=\mathrm{Sc}\bigl(\tilde{Ξ}_{\mathrm{sp}}^*i\tilde{Ξ}_{\mathrm{sp}}\vec e_z\vec e_x\bigr),$$
$$V_\mu=\mathrm{Sc}\bigl(\tilde{Ξ}_{\mathrm{sp}}^*i\,(ie_\mu\tilde{Ξ}_{\mathrm{sp}}\vec e_{\nu(\mu)})\vec e_x\bigr),
\qquad
A_\mu=\mathrm{Sc}\bigl(\tilde{Ξ}_{\mathrm{sp}}^*i\,e_\mu\tilde{Ξ}_{\mathrm{sp}}\vec e_z\vec e_{\nu(\mu)}\vec e_x\bigr),$$
with $\nu(t)=x$ and $\nu(k)=y$. The scalar density carries the role subscript because the bare letter is the action of the corpus.

The four are real, and the reality is a computation and not a convention: over 100 generic elements the largest imaginary part of each is below $10^{-15}$. Each is worth a sentence.

The scalar density $S_{\mathrm d}$ pairs the two values and never a value with itself: an element of a single value gives $S_{\mathrm d}=0$.

The time component of the current is the Hermitian norm of the field. The two factors of $i$ multiply to $-1$, the two units $\vec e_x\vec e_x$ multiply to $-e_t$, and the two signs cancel:
$$V_0=\mathrm{Sc}\bigl(\tilde{Ξ}_{\mathrm{sp}}^*\tilde{Ξ}_{\mathrm{sp}}\bigr),$$
so the current is a density of the field and not a derivative of it.

The axial bilinear is the vector bilinear with the right unit displaced. Where the vector reads $\vec e_{\nu(\mu)}$ in the right slot, the axial reads the product $\vec e_z\vec e_{\nu(\mu)}$ and drops the factor $i$.

The tensor bilinear completes the list. Its element is the antisymmetric composite of two slot actions, which is a derived form of the two actions above and is written here in the element language of the body:
$$T_{0k}=\mathrm{Sc}\bigl(\tilde{Ξ}_{\mathrm{sp}}^*i\,i\vec e_k\tilde{Ξ}_{\mathrm{sp}}\vec e_z\vec e_x\bigr),
\qquad
T_{jk}=\mathrm{Sc}\bigl(\tilde{Ξ}_{\mathrm{sp}}^*i\,i\vec e_j\vec e_k\tilde{Ξ}_{\mathrm{sp}}\vec e_x\bigr)\quad(j\ne k),
\qquad
T_{\mu\mu}=0 .$$
The composite of the time slot action with the $k$-th space slot action is the left multiplication by $\vec e_k$ followed by the right multiplication by $\vec e_z$, and the composite of the $j$-th with the $k$-th is the left multiplication by the product $\vec e_j\vec e_k$. The two orders of each pair are opposite, so the antisymmetrised product is the composite itself, and the element of $T_{\mu\nu}$ is $i$ times that composite. The factor $i$ is what makes the entries real: with it the entries are real on the 100 elements, and without it the same pairing returns purely imaginary values. Every independent entry is real on that run: the three $T_{0k}$ and the three $T_{jk}$. The diagonal vanishes because the antisymmetrised product takes the same index twice.

### The Two Writings of the Free Equation

The free field obeys the linear chiral pair
$$\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=m\tilde{Ξ}_{\mathrm{sp},L},
\qquad
\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=m\tilde{Ξ}_{\mathrm{sp},R},$$
in which the gradient acts by left multiplication on the field and the mass couples the two values. This is the **one-sided** writing.

The **two-sided** writing is the action
$$\tilde Q\longmapsto i\sum_\mu e_\mu\frac{\partial\tilde Q}{\partial x_\mu}\vec e_{\nu(\mu)},$$
and it is the one this article needs, because every bilinear above carries a right slot as well as a left one. The two writings describe one dynamics, and each is first order.

The composition of the two-sided action is read slot by slot. Each slot action composed with itself multiplies the element by $+1$ on the time slot and by $-1$ on each spatial slot; two different slots composed in the two orders cancel in pairs, because the derivatives commute; so the action composed with itself is
$$\tilde Q\longmapsto\Box\tilde Q,
\qquad
\Box=\frac{\partial^2}{\partial x_t^2}-\sum_k\frac{\partial^2}{\partial x_k^2},$$
in this frame. The verification is exact: the six cross compositions sum to zero, and the four diagonal ones to the four signs above.

### The Two Values and the Axial Bilinear

The subscript takes two values: the element is $L$ when its value is the minus one and $R$ when its value is the plus one, and only the zero element carries both. The value is decided by the right slot: a left multiplication keeps the value, and a product takes the value of its right factor. These two facts are stated in words because every sentence below uses them and none computes them.

The mass is the coefficient that couples the two values, and the scalar density is the object it multiplies: $S_{\mathrm d}$ pairs one value with the other and vanishes on an element of a single value, so a field of one value alone carries no mass term.

The axial bilinear carries $\vec e_z$ in the right slot, before the space unit, and drops the factor $i$. The right slot is where the value is decided, so the insertion is what distinguishes the axial bilinear from the vector one; and the insertion is the smallest change of the vector bilinear that reaches the conjugate channel.

## Why the Dirac Equation Becomes Nonlinear

### Self-Interaction and the Cubic Form

The free equation is first order in space and in time, and every bilinear above is quadratic in the field. A Lagrangian term that is a product of two bilinears is therefore quartic in the field, and the field equation obtained from it is cubic: a bilinear coefficient multiplying one more power of the field. That is the whole origin of the name, and the alternative name **cubic Dirac equation** says the same thing.

The generic equation is
$$i\sum_\mu e_\mu\frac{\partial\tilde{Ξ}_{\mathrm{sp}}}{\partial x_\mu}\vec e_{\nu(\mu)}-m\tilde{Ξ}_{\mathrm{sp}}+g\,Ξ(\tilde{Ξ}_{\mathrm{sp}})=0,$$
with $Ξ$ cubic. The three standard models differ only in which bilinear builds $Ξ$, and a table is the clearest statement of the difference.

| Model | The bilinear it squares | The interaction in the Lagrangian | The cubic self-term in the equation |
|---|---|---|---|
| Thirring | $V_\mu$ | $-\frac{g}{2}\sum_\mu\varepsilon_\mu V_\mu V_\mu$ | $-g\sum_\mu\varepsilon_\mu V_\mu\,(ie_\mu\tilde{Ξ}_{\mathrm{sp}}\vec e_{\nu(\mu)})$ |
| Soler | $S_{\mathrm d}$ | $\frac{g}{2}S_{\mathrm d}^2$ | $g\,S_{\mathrm d}\,\tilde{Ξ}_{\mathrm{sp}}$ |
| Hehl–Datta | $A_\mu$ | $+\frac{3\kappa}{16}\sum_\mu\varepsilon_\mu A_\mu A_\mu$ | $+\frac{3\kappa}{8}\sum_\mu\varepsilon_\mu A_\mu\,(e_\mu\tilde{Ξ}_{\mathrm{sp}}\vec e_z\vec e_{\nu(\mu)})$ |

**Why the self-term is cubic.** The interaction is a square of a bilinear, $Ξ^{2}$ with $Ξ$ quadratic in the field. Varying a square gives twice the bilinear times the variation of the bilinear, and the variation of a bilinear is linear in the field: the result is cubic. The factor of two is visible in the table, between the Lagrangian column and the equation column of the Hehl–Datta row.

**The three channels are the three Lorentz types.** The scalar channel is the one the mass already uses. The vector channel is the one the electromagnetic current uses. The axial channel is the one the mass breaks. A model is a choice of channel and of coefficient, and it is the coupling that decides whether the equation has a closed-form solution or not.

### The Einstein–Cartan Route

The **Einstein–Cartan–Sciama–Kibble** theory is general relativity with an independent connection. The torsion is the antisymmetric part of the connection, and the field equation that follows from varying the connection makes the torsion proportional to the spin current of the matter. For a Dirac field the spin current is the axial current $A_\mu$ of this article, so the torsion is a function of $A_\mu$ rather than an independent field.

Eliminating the torsion returns an interaction of the matter with itself. The torsion enters the covariant derivative through an axial-axial term, so substituting its own expression for it gives a four-fermion interaction of the axial–axial type, with a coefficient fixed by the gravitational coupling. In the notation of this article the interaction is $+\frac{3\kappa}{16}\sum_\mu\varepsilon_\mu A_\mu A_\mu$, where $\kappa$ is the Einstein gravitational constant, $8\pi G/c^4$. The coefficient is fixed by the elimination and not adjustable, which is what makes the resulting equation a prediction of the geometric extension rather than a model.

## The Two Standard Models

The models below are the two the literature names, and the article records them in the form the sources state, so that the coefficients can be checked against them.

### The Thirring Model

The **Thirring model** (Thirring 1958) is the $1+1$-dimensional theory of a self-interacting fermion whose interaction is the square of the vector current. In the notation of this article the Lagrangian density is
$$\mathcal{L}=\mathrm{Sc}\bigl(\tilde{Ξ}_{\mathrm{sp}}^*i\,(i\sum_\mu e_\mu\frac{\partial\tilde{Ξ}_{\mathrm{sp}}}{\partial x_\mu}\vec e_{\nu(\mu)})\vec e_x\bigr)-m\,\mathrm{Sc}\bigl(\tilde{Ξ}_{\mathrm{sp}}^*i\tilde{Ξ}_{\mathrm{sp}}\vec e_x\bigr)-\frac{g}{2}\sum_\mu\varepsilon_\mu V_\mu V_\mu,$$
with the sums running over the two indices $t$ and $x$ of the plane. The field is an element of $\mathbb{B}$; its two values $\tilde{Ξ}_{\mathrm{sp},L}$ and $\tilde{Ξ}_{\mathrm{sp},R}$ are the two components the two-dimensional dynamics uses, and the mass term is the scalar density $S_{\mathrm d}$, which pairs the two values and vanishes when only one is present.

The integral $\int dt\,dx\,\mathcal{L}$ is the action, and the field equation is
$$i\sum_\mu e_\mu\frac{\partial\tilde{Ξ}_{\mathrm{sp}}}{\partial x_\mu}\vec e_{\nu(\mu)}-m\tilde{Ξ}_{\mathrm{sp}}-g\sum_\mu\varepsilon_\mu V_\mu\,(ie_\mu\tilde{Ξ}_{\mathrm{sp}}\vec e_{\nu(\mu)})=0,$$
with $\mu$ running over $t$ and $x$. The interaction is a **current–current** interaction: the field at a point multiplies the current at the same point.

**The model is exactly solvable.** The massless Thirring model was solved by Hagen (1964) and by Klaiber (1968): the spectrum is a free boson, and the fermion Green functions are explicit powers of the free ones. The model satisfies the Osterwalder–Schrader axioms with a suitable choice of the coupling (Carey and Ruijsenaars 1984), and the massive model is integrable by Bethe ansatz (Bergknoff and Thacker 1979). The exact solubility is the reason the model is used as a testing ground for approximation schemes: a method that cannot reproduce the Thirring model exactly is known to be wrong before it is applied to QCD.

**Bosonisation.** In $1+1$ dimensions the massless Thirring model is equivalent to a free massless scalar field. With a mass term the equivalence is the **sine-Gordon** correspondence, and the fermion mass is the cosine coupling (Coleman 1975, Mandelstam 1975). The correspondence is the prototype of the statement that a fermion in one space dimension can be traded for a boson, and it is the reason the model appears in the biquaternion literature beside the bosonisation article.

### The Soler Model

The **Soler model** (Soler 1970) is the $3+1$-dimensional theory whose interaction is the square of the scalar bilinear:
$$\mathcal{L}=\mathrm{Sc}\bigl(\tilde{Ξ}_{\mathrm{sp}}^*i\,(i\sum_\mu e_\mu\frac{\partial\tilde{Ξ}_{\mathrm{sp}}}{\partial x_\mu}\vec e_{\nu(\mu)})\vec e_x\bigr)-m\,\mathrm{Sc}\bigl(\tilde{Ξ}_{\mathrm{sp}}^*i\tilde{Ξ}_{\mathrm{sp}}\vec e_x\bigr)+\frac{g}{2}\Bigl(\mathrm{Sc}\bigl(\tilde{Ξ}_{\mathrm{sp}}^*i\tilde{Ξ}_{\mathrm{sp}}\vec e_x\bigr)\Bigr)^{2},$$
that is, with $S_{\mathrm d}$ for the scalar density, $\frac{g}{2}S_{\mathrm d}^2$. The interaction is a **scalar–scalar** interaction, and the field equation is
$$i\sum_\mu e_\mu\frac{\partial\tilde{Ξ}_{\mathrm{sp}}}{\partial x_\mu}\vec e_{\nu(\mu)}-m\tilde{Ξ}_{\mathrm{sp}}+g\,S_{\mathrm d}\,\tilde{Ξ}_{\mathrm{sp}}=0,$$
with the sum over the four indices $t,x,y,z$.

**The pseudoscalar variant.** The same construction with $P_5$ in place of $S_{\mathrm d}$ gives the pseudoscalar–pseudoscalar interaction $\frac{g}{2}P_5^2$. The two variants are not independent under the axial rotation $Q\mapsto Q\exp(\alpha\vec e_z)$: the pair $(S_{\mathrm d},P_5)$ rotates as a two-component object,
$$S_{\mathrm d}\longmapsto \cos 2\alpha\,S_{\mathrm d}+\sin 2\alpha\,P_5,
\qquad
P_5\longmapsto \cos 2\alpha\,P_5-\sin 2\alpha\,S_{\mathrm d},$$
so that $S_{\mathrm d}^2+P_5^2$ is invariant and $S_{\mathrm d}^2$ alone is not. The rotation is exact, and it is the algebraic content of the statement that the scalar and the pseudoscalar couplings are two projections of one coupling.

**The square of the density is not the square of the element.** The scalar density is a real number, and the interaction terms square it. The element $S_{\mathrm d}\vec e_z$ is a quaternion of the algebra, and its product with itself is $-S_{\mathrm d}^2$, not $+S_{\mathrm d}^2$: the Lagrangian term squares the density and not the element. This is the one place where a factor of $-1$ separates the two readings, and it is the reason the interaction terms are written with $S_{\mathrm d}^2$ and not with a product of elements.

**Relation to Nambu–Jona-Lasinio.** The scalar–scalar interaction is the mean-field approximation of the Nambu–Jona-Lasinio four-fermion interaction, and the closed-form solutions of the Soler model (Soler 1970; see also the review of Thaller 1992) are the standard testing ground for the mean-field treatment of dynamical mass generation. The scalar channel is the one the mass uses, so a scalar–scalar self-interaction is the self-consistent mass term.

## The Hehl–Datta Interaction from Torsion

With the torsion eliminated, the equation of the field is the Dirac equation plus the axial term, and it is the one model of the three whose coefficient is not fitted but fixed:
$$i\sum_\mu e_\mu\frac{\partial\tilde{Ξ}_{\mathrm{sp}}}{\partial x_\mu}\vec e_{\nu(\mu)}-m\tilde{Ξ}_{\mathrm{sp}}+\frac{3\kappa}{8}\sum_\mu\varepsilon_\mu A_\mu\,e_\mu\tilde{Ξ}_{\mathrm{sp}}\vec e_z\vec e_{\nu(\mu)}=0.$$
The term is the axial current multiplying the axial slot action on the field. Its coefficient is $3\kappa/8$, twice the $3\kappa/16$ of the Lagrangian, and the factor of two is the one that varying a square supplies.

**The spacelike case.** Where only the spacelike components of the current are nonzero, the equation separates into a time part and a space part,
$$i\Bigl((\nabla_t\tilde{Ξ}_{\mathrm{sp}})\vec e_x+\sum_k\vec e_k(\nabla_k\tilde{Ξ}_{\mathrm{sp}})\vec e_y\Bigr)+\frac{3\kappa}{8}\sum_k\varepsilon_k A_k\,\vec e_k\tilde{Ξ}_{\mathrm{sp}}\vec e_z\vec e_y=m\tilde{Ξ}_{\mathrm{sp}},$$
with $A_0=0$, and the two parts are read separately.

**Why the square is the d'Alembertian.** The three spatial slot actions composed with one another give $-\partial_k^2$ on each diagonal and cancel in pairs off it, so the square of the two-sided action restricted to the plane's space is $-\sum_k\partial_k^2$, the spatial part of $\Box$. The eliminated equation therefore has a square that is a wave operator, and no sign in it is chosen by hand.

## The Local Channels and Their Sectors

### The Bilinears

The five bilinears, with the element at which the pairing is read, and with the Lorentz type and the parity behaviour the sources give them:

| Bilinear | The element | Lorentz type | Behaviour under parity |
|---|---|---|---|
| $S_{\mathrm d}=\mathrm{Sc}(\tilde{Ξ}_{\mathrm{sp}}^*i\tilde{Ξ}_{\mathrm{sp}}\vec e_x)$ | $\tilde{Ξ}_{\mathrm{sp}}$ | scalar | even |
| $P_5=\mathrm{Sc}(\tilde{Ξ}_{\mathrm{sp}}^*i\tilde{Ξ}_{\mathrm{sp}}\vec e_z\vec e_x)$ | $\tilde{Ξ}_{\mathrm{sp}}\vec e_z$ | pseudoscalar | odd |
| $V_\mu=\mathrm{Sc}\bigl(\tilde{Ξ}_{\mathrm{sp}}^*i\,ie_\mu\tilde{Ξ}_{\mathrm{sp}}\vec e_{\nu(\mu)}\vec e_x\bigr)$ | $ie_\mu\tilde{Ξ}_{\mathrm{sp}}\vec e_{\nu(\mu)}$ | vector | $V_0$ even, $V_k$ odd |
| $A_\mu=\mathrm{Sc}\bigl(\tilde{Ξ}_{\mathrm{sp}}^*i\,e_\mu\tilde{Ξ}_{\mathrm{sp}}\vec e_z\vec e_{\nu(\mu)}\vec e_x\bigr)$ | $e_\mu\tilde{Ξ}_{\mathrm{sp}}\vec e_z\vec e_{\nu(\mu)}$ | axial vector | $A_0$ odd, $A_k$ even |
| $T_{\mu\nu}$ | the antisymmetric composite of two slot actions, read on $\tilde{Ξ}_{\mathrm{sp}}$ | antisymmetric tensor | $T_{0k}$ odd, $T_{jk}$ even |

The Lorentz-type column is the classification of the sources, recorded here and not derived: the algebra fixes which element each bilinear reads, and the sources fix which Lorentz type that element carries.

**The quaternion representative.** The element $P=S_{\mathrm d}\vec e_z$ is the quaternion into which the sources assemble the scalar density, and its product with itself is $-S_{\mathrm d}^2$. The two objects are different: the density $P_5$ is the parity-odd partner of $S_{\mathrm d}$, and $P$ is a vector of the algebra whose square is the negative of the scalar square. A Lagrangian term that squares the density is therefore not a product of two elements.

### Which Channel Each Model Uses

| Model | The bilinear | Coefficient | The channel |
|---|---|---|---|
| Thirring | $V_\mu$ | $-\frac{g}{2}$ | vector–vector; in $1+1$ equal to axial–axial up to sign |
| Soler | $S_{\mathrm d}$ | $+\frac{g}{2}$ | scalar–scalar; the mass channel |
| Hehl–Datta | $A_\mu$ | $+\frac{3\kappa}{16}$ | axial–axial; fixed by torsion |
| Nambu–Jona-Lasinio | $S_{\mathrm d}$ and $P_5$ | $G$ | the invariant combination $S_{\mathrm d}^2+P_5^2$ |

**The quartic terms are not independent.** A Fierz rearrangement reduces any product of two bilinears to a sum of products of the others, so a model is defined by a point in the space of couplings and not by a single term. The table lists the term each model is named after; the models differ also in the terms they omit, and the omissions are conventions of the literature.

## The Biquaternion Reading

### The Interaction Is Bosonic, So the Central Phase Passes Through It

A bilinear of the field is even in the field and carries zero fermion number. A product of two bilinears is even as well, so every interaction term in this article is invariant under the central phase $Q\mapsto e^{i\alpha}Q$: the phase meets an even number of fields and cancels. The invariance is what makes the vector symmetry exact in all three models, and it holds at the level of the algebra and not only after the Lagrangian is written.

The axial rotation is the one that does not pass. Under $Q\mapsto Q\exp(\alpha\vec e_z)$ the scalar and pseudoscalar densities rotate into one another, and the mass term, which is a single density, is not invariant. The interaction terms that are invariant under it are the ones built from the invariant combination $S_{\mathrm d}^2+P_5^2$.

### The Three Channels in the Framework's Sectors

The framework's own equation is the chiral pair, and its two-sided form is the one the models use. The three channels then sit in three places.

**The scalar channel is the mass channel.** The mass term of the framework pairs $\tilde{Ξ}_{\mathrm{sp},L}$ with $\tilde{Ξ}_{\mathrm{sp},R}$ through a coefficient, and the scalar density $S_{\mathrm d}$ is exactly the object that pairing multiplies. A scalar–scalar interaction is therefore a coefficient of the same linear chiral pair: the Soler model and the framework's mass term use one channel, and a strong coupling in it produces a mass of the same kind.

**The vector channel is the material-sector current.** The vector current is the object minimal coupling differentiates against and the Gordon decomposition splits into its spin and orbital parts. It is the channel of the electromagnetic interaction, and the Thirring model is its self-interacting version.

**The axial channel is the one the mass breaks.** The linear mass term is the object whose divergence the axial current acquires, and the axial–axial interaction is therefore the coupling conjugate to the mass. The geometric route puts its interaction precisely there.

### What the Framework Does Not Supply

The identification above is a placement, not a derivation. A bilinear here is a pairing, and every pairing of this article carries the fixed element $i\vec e_x$; it is not a product of two elements of $\mathbb{B}$ alone, and the free equation of the framework contains no such fixed element. The consequence is the one recorded in the minimal-coupling article: a bilinear built only from $\tilde{Ξ}_{\mathrm{sp}}$ and $\tilde{Ξ}_{\mathrm{sp}}^*$ inside $\mathbb{B}$ cannot supply these objects on its own, and the self-interaction, like the current, is a statement about a pairing and not about a product. The framework transcribes the models, verifies the two-dimensional algebra of their channels, and locates each channel in its sectors. It supplies no coupling, no solution, no spectrum and no prediction.

Two further limits are inherited from other gaps. The Einstein–Cartan route needs a torsionful connection with a field equation; the companion article on curved spacetime records that the framework can carry the connection as an object of its own Lie subspace but generates no dynamics for it, so a biquaternion torsion belongs to that agenda and not to the constructed part. And the exact solubility of the massless Thirring model is a property of two-dimensional quantum field theory with no biquaternion counterpart: the framework can write the two-dimensional reduction in its own objects, and it does not reproduce the solution.

## Verified Two-Dimensional Relations

The two-dimensional identities on which the Thirring model's one coupling rests were checked directly, in exact arithmetic on the algebra over the Gaussian integers, so every residual below is exactly $0$ and not merely small. The frame is the $\mathbb{B}_{\Phi}$ frame of the conventions article, whose metric has $g_{tt}=+1$ and $g_{xx}=-1$.

### The Two Slot Actions

The two-dimensional plane uses two slot actions,
$$\tilde Q\longmapsto ie_t\tilde Q\vec e_x,
\qquad
\tilde Q\longmapsto i\vec e_x\tilde Q\vec e_y .$$
Each composed with itself returns the element in the first case and minus the element in the second. Composed in the two orders the two are opposite, and the composite in one order is the action $\tilde Q\mapsto\vec e_x\tilde Q\vec e_z$, whose square is the identity. The four statements are exact, and they are the two-dimensional content of the signs that the four-dimensional section reads slot by slot.

### The Current Duality

The axial current of the two-dimensional theory inserts the plane's own value element, $\vec e_x$ on the left and $\vec e_z$ on the right, and reads
$$A_\mu=\mathrm{Sc}\bigl(\tilde{Ξ}_{\mathrm{sp}}^*i\,(ie_\mu\vec e_x\tilde{Ξ}_{\mathrm{sp}}\vec e_z\vec e_{\nu(\mu)})\vec e_x\bigr);$$
that is not the four-dimensional axial bilinear of the earlier section, and the difference is one factor $i$. The four-dimensional chirality is $-i$ on the right, so the $i$ of the slot action is spent there; the plane's insertion is the product of the two slot actions and carries no factor $i$ of its own, so the $i$ survives in the plane. The difference is a property of the dimension and not of the field. With the two-dimensional one the duality is an identity, with no free constant:
$$A_0=V_1,\qquad A_1=V_0,
\qquad\text{that is}\qquad
A_\mu=\sum_\nu\epsilon_{\mu\nu}\varepsilon_\nu V_\nu,$$
with $\epsilon^{01}=+1$, hence $\epsilon_{01}=-1$. The signature sign on the summed index is part of the statement, because $\epsilon_{\mu\nu}\varepsilon_\nu$ is what the dual of a covector carries. The warrant is the composite above: it converts the time slot action into the space one, and the units supply the relative sign. The largest deviation over 100 generic elements is zero.

### The Single Coupling

Consequently
$$\sum_\mu\varepsilon_\mu A_\mu A_\mu=\varepsilon_0A_0^2+\varepsilon_1A_1^2=V_1^2-V_0^2=-\left(V_0^2-V_1^2\right)=-\sum_\mu\varepsilon_\mu V_\mu V_\mu,$$
so the vector–vector and axial–axial quartic terms differ only by sign and a single coupling covers the current–current interactions. The plain sums of squares are equal instead, $A_0^2+A_1^2=V_0^2+V_1^2$, which is exactly why the signature signs cannot be dropped: without them the two invariants would coincide rather than being opposite. No cross term mixes the two currents either: because $\epsilon_{\mu\nu}\varepsilon_\mu\varepsilon_\nu V_\nu V_\mu$ is antisymmetric in $\mu$ and $\nu$ while the product of two components is symmetric, the contraction $\sum_\mu\varepsilon_\mu A_\mu V_\mu$ vanishes. All three identities are exact on the same 100 elements.

The duality is the exact reason the two-dimensional model has one coupling. It is a property of the dimension and of the metric, and not of the framework.

## Open Questions

1. **A biquaternion-natural self-interaction.** Is there a functional of $\mathbb{B}$-valued bilinears whose variation reproduces the Soler or Thirring interaction without the pairing's fixed element $i\vec e_x$? This is the question of the minimal-coupling article met from the interaction side. The pseudoscalar square of the NJL combination belongs to the same question: the quaternion $P=S_{\mathrm d}\vec e_z$ squares to $-S_{\mathrm d}^2$, so the parity-odd density $P_5$ and an invariant built from two quaternions are not the same object, and no biquaternion form of $S_{\mathrm d}^2+P_5^2$ is written here.

2. **Torsion in the framework's own notation.** The curved-spacetime article carries the connection in the Lie subspace but gives it no equation. The antisymmetric (torsion) part of that connection, and the algebraic elimination that produces the Hehl–Datta term, are not written in the framework's notation.

3. **The condensate and the nonlinear equation.** A strong coupling in the scalar channel generates a mass; the axial channel, where the geometry puts its interaction, is repulsive and does not condense on its own. Is the biquaternion form of the self-consistent (gap) equation the same statement as the framework's linear mass term with $m$ promoted to an expectation, and can the two be written as one equation?

4. **Two dimensions and the central charge.** The bosonisation article matches the central charges $c_{\mathrm{Dirac}} = 1 = c_{\mathrm{boson}}$. Does the nonlinear (massive Thirring) case add a biquaternion statement about the interacting central charge, or is it entirely the bosonic side's renormalisation?

5. **The exact solutions.** Closed-form solutions of the Soler model exist, and the massive Thirring model is Bethe-ansatz solvable. Neither has been transcribed into the framework's notation, and it is not known whether the biquaternion form of the equations makes either more transparent.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, $\gamma_0^2=I_4$ and $\gamma_k^2=-I_4$. The frame belongs to the coordinate, not to the array.

This section writes the same cells in the $\gamma$ notation, so that each formula the sources state can be checked against the cell it names. The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\tilde{Ξ}_{\mathrm{sp}}=a\tilde{Ξ}_{\mathrm{sp}}$ and $R_b\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp}} b$.

$$
\begin{aligned}
\gamma_0 &= iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x}, &\gamma_1 &= iL_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_y},\\[2pt]
\gamma_2 &= iL_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y}, &\gamma_3 &= iL_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_y},\\[2pt]
\gamma_5 &= -iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z}.
\end{aligned}
$$

The same in the axis-free display:

$$
\begin{aligned}
\gamma_0 &= iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x}, &\gamma_1 &= iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y},\\[2pt]
\gamma_2 &= iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y}, &\gamma_3 &= iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y},\\[2pt]
\gamma_5 &= -iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z}.
\end{aligned}
$$

A single product $L_{a}R_{b}$ is a pure tensor $a\otimes b$; the single products form a seven-dimensional cone, of rank at most one, and a general element of the algebra is a sum of at most four of them.

The axial cells are the products of a generator and the chirality cell: $c^{(5)}_\mu=\gamma_\mu\gamma_5$, since $L_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x}\cdot L_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z}=L_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z\vec e_x}=L_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_y}$ is exactly $c^{(5)}_0$, and the three spatial products agree the same way. That is the dictionary entry the sources need: the Hehl–Datta term of this article **is** the $\left(\tilde{Ξ}_{\mathrm{sp}}^{\dagger}iR_{\mathrm{axf},\vec e_x}\gamma_\mu\gamma_5\tilde{Ξ}_{\mathrm{sp}}\right)\gamma^\mu\gamma_5\tilde{Ξ}_{\mathrm{sp}}$ of the torsion literature.

$\gamma_5$ is the reference-frame cell of the chirality operator; the central grading $\chi=i\tilde{Ζ}_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The cell dictionary is complex-linear. With the central $i$ dropped, the four cells are real $4\times4$ matrices, and they square to $-g=(-1,+1,+1,+1)$: the timelike one to $-I_4$ and the three spacelike ones to $+I_4$. They span the full algebra $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$ of real $4\times4$ matrices. Restoring the $i$ flips every square, because $i^2=-1$, and the cells then square to $+g$ and span $M_4(\mathbb{C})\cong\mathrm{Cl}_{1,3}(\mathbb{C})$, which is the algebra the $\gamma$ notation uses. The whole difference between the real and the complex reading is that single factor of $-1$.

### The Identities the Sources Cite

The identities the literature quotes were written in the $\gamma$ notation, and they are recorded once here, in that notation, so that each can be checked against the sources. In the $\gamma$ reading, with $\epsilon_{0123}=+1$:

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
=4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr).
$$

The weight $\varepsilon_\mu$ in the contractions below is exactly what raises the index, $\gamma^\mu=\varepsilon_\mu\gamma_\mu$, so the Hehl–Datta sum $\sum_\mu\varepsilon_\mu A_\mu c^{(5)}_\mu$ is the sources' $A_\mu\gamma^\mu\gamma_5$ with the sum written out.

$S_{cd}=\tfrac14[\gamma_c,\gamma_d]$ is the Lorentz generator in the $\gamma$ basis, and the $\sigma_{\mu\nu}$ of the tensor bilinear is the same generator rescaled, $\sigma_{\mu\nu}=\tfrac i2[\gamma_\mu,\gamma_\nu]=2iS_{\mu\nu}$; the factor $2i$ is the whole difference between the two, and it is a convention.

### The Four Contraction Sums

A cell's square is a frame statement, and every contraction of the frame inherits that. Written with the signature sign $\varepsilon_\mu$ on the summed index, the way every other contraction in this article is written, the four sums hold in either frame:

$$
\sum_\mu\varepsilon_\mu\gamma_\mu\gamma_\mu=4I_4,\qquad
\sum_\mu\varepsilon_\mu\gamma_\mu\gamma_\alpha\gamma_\mu=-2\gamma_\alpha,\qquad
\sum_\mu\varepsilon_\mu\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\mu=4\varepsilon_\alpha\delta_{\alpha\beta}I_4,\qquad
\sum_\mu\varepsilon_\mu\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\gamma\gamma_\mu=+2\gamma_\alpha\gamma_\beta\gamma_\gamma ,
$$

In each of the four the contracted generator is the same one on both sides, so it is never moved past another generator and no reordering sign enters. With the summed index raised, $\gamma^\mu=-\varepsilon_\mu\gamma_\mu$, the weights become signs and the sums read $-4I_4$, $+2\gamma_\alpha$, $-4\varepsilon_\alpha\delta_{\alpha\beta}I_4$ and $-2\gamma_\gamma\gamma_\beta\gamma_\alpha$. With every index low only the first keeps a closed form, $\sum_\mu\gamma_\mu\gamma_\mu=-2I_4$, and the second is $4\gamma_\alpha$ on the time index and $0$ on each spatial one, so the unweighted form is a signature statement and not an identity of four dimensions alone.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the corpus. The two are carried into one another by $L_{\mathrm{axf},e_\mu}=C_{\Pi}L_{\mathrm{pau},e_\mu}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

A nonlinear Dirac equation adds a self-interaction built from the field's bilinears to the free equation. The physically motivated case is geometric: in Einstein–Cartan theory the torsion sourced by the field's own spin, eliminated through its field equation, leaves the axial-axial Hehl–Datta term $+\frac{3\kappa}{8}\sum_\mu\varepsilon_\mu A_\mu\,e_\mu\tilde{Ξ}_{\mathrm{sp}}\vec e_z\vec e_{\nu(\mu)}$ with a coefficient fixed by the gravitational constant. The two standard models use the other two channels: the Thirring model in $1+1$ dimensions uses the square of the vector current and is exactly solvable, with the massive case equivalent to sine-Gordon; the Soler model in $3+1$ dimensions uses the square of the scalar bilinear and is the mean-field relative of the NJL interaction.

The biquaternion interpretation places the channels. The scalar density is the mass channel, whose expectation is the dynamical mass of the chiral-condensate article. The vector current is the material-sector current of the minimal-coupling and Gordon articles. The axial current is the channel the linear mass breaks, so an axial-axial interaction couples in the channel conjugate to the mass; the interaction the geometry supplies is repulsive, and the dynamical mass itself is generated in the scalar channel, where the mass term lives. Every quartic interaction is bosonic, so it passes through the framework's central phase and leaves the exact vector symmetry intact.

Each bilinear, however, is a pairing and not a product: it is the scalar part of $\tilde{Ξ}_{\mathrm{sp}}^*iX\vec e_x$, and the fixed element $i\vec e_x$ is not supplied by the free equation of the framework, which is a left multiplication by the gradient with a mass that couples the two values. The framework transcribes the models and locates their channels, and supplies no coupling, solution or prediction. The one exact algebraic fact about the models that the article verifies is two-dimensional: the axial current is the dual of the vector current, so $\sum_\mu\varepsilon_\mu A_\mu A_\mu=-\sum_\mu\varepsilon_\mu V_\mu V_\mu$ and the Thirring model has a single coupling.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra; $\vec e_k^2 = -e_t$, central $i$ |
| $\tilde Q\mapsto ie_\mu\tilde Q\vec e_{\nu(\mu)}$ | Slot action of the index $\mu$; $\nu(t)=x$, $\nu(k)=y$ |
| $i\sum_\mu e_\mu\frac{\partial\tilde Q}{\partial x_\mu}\vec e_{\nu(\mu)}$ | Two-sided Dirac action; composed with itself it is $\Box$ |
| $\mathrm{Sc}\bigl(\tilde{Ξ}_{\mathrm{sp}}^*iX\vec e_x\bigr)$ | The bilinear form; every density below is this scalar part read at one element $X$ |
| $S_{\mathrm d}=\mathrm{Sc}(\tilde{Ξ}_{\mathrm{sp}}^*i\tilde{Ξ}_{\mathrm{sp}}\vec e_x)$ | Scalar density (mass channel) |
| $P_5=\mathrm{Sc}(\tilde{Ξ}_{\mathrm{sp}}^*i\tilde{Ξ}_{\mathrm{sp}}\vec e_z\vec e_x)$ | Pseudoscalar density, the parity-odd partner of $S_{\mathrm d}$; the quaternion representative $P=S_{\mathrm d}\vec e_z$ has $P\cdot P=-S_{\mathrm d}^2$, a different object from the density square $P_5^2$ |
| $V_\mu=\mathrm{Sc}\bigl(\tilde{Ξ}_{\mathrm{sp}}^*i\,ie_\mu\tilde{Ξ}_{\mathrm{sp}}\vec e_{\nu(\mu)}\vec e_x\bigr)$ | Vector current (material sector in the framework); $V_0=\mathrm{Sc}(\tilde{Ξ}_{\mathrm{sp}}^*\tilde{Ξ}_{\mathrm{sp}})$ |
| $A_\mu=\mathrm{Sc}\bigl(\tilde{Ξ}_{\mathrm{sp}}^*i\,e_\mu\tilde{Ξ}_{\mathrm{sp}}\vec e_z\vec e_{\nu(\mu)}\vec e_x\bigr)$ | Axial current (channel broken by the mass); in two dimensions built with the plane's insertions and the factor $i$ kept |
| $T_{\mu\nu}$ | Tensor bilinear; $T_{0k}=\mathrm{Sc}(\tilde{Ξ}_{\mathrm{sp}}^*i\,i\vec e_k\tilde{Ξ}_{\mathrm{sp}}\vec e_z\vec e_x)$, $T_{jk}=\mathrm{Sc}(\tilde{Ξ}_{\mathrm{sp}}^*i\,i\vec e_j\vec e_k\tilde{Ξ}_{\mathrm{sp}}\vec e_x)$ for $j\ne k$, $T_{\mu\mu}=0$ |
| $\varepsilon_\mu = -g_{\mu\mu}$ | Signature sign of the index $\mu$ |
| $g$ | Self-coupling of the Thirring and Soler models |
| $\kappa = 8\pi G/c^4$ | Einstein gravitational constant |
| $\frac{3\kappa}{8}\sum_\mu\varepsilon_\mu A_\mu\,e_\mu\tilde{Ξ}_{\mathrm{sp}}\vec e_z\vec e_{\nu(\mu)}$ | Hehl–Datta term in the equation ($\frac{3\kappa}{16}\sum_\mu\varepsilon_\mu A_\mu A_\mu$ as a Lagrangian term) |
| $X$, $M$ | Spin–torsion coupling and torsion mass (propagating-torsion case) |
| $\sum_\mu\varepsilon_\mu A_\mu A_\mu = -\sum_\mu\varepsilon_\mu V_\mu V_\mu$ | Two-dimensional current duality (verified exactly) |
| $\mathbb{B}_{\Psi}$, $\mathbb{B}_{\Phi}$ | Informational and material sectors |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- W. E. Thirring, "A soluble relativistic field theory," *Annals of Physics* **3** (1958) 91–112, for the original two-dimensional model.
- M. Soler, "Classical, stable, nonlinear spinor field with positive rest energy," *Physical Review D* **1** (1970) 2760–2765, for the scalar-interaction model in four dimensions.
- F. W. Hehl and B. K. Datta, "Nonlinear spinor equation and asymmetric connection in general relativity," *Journal of Mathematical Physics* **12** (1971) 1334–1339, for the torsion-induced axial-axial interaction.
- F. W. Hehl, P. von der Heyde, G. D. Kerlick and J. M. Nester, "General relativity with spin and torsion: foundations and prospects," *Reviews of Modern Physics* **48** (1976) 393–416, for the Einstein–Cartan–Sciama–Kibble theory and its matter couplings.
- S. Coleman, "Quantum sine-Gordon equation as the massive Thirring model," *Physical Review D* **11** (1975) 2088–2097, for the equivalence of the massive Thirring and sine-Gordon models.
- C. R. Hagen, "Quantum sine-Gordon equation and the Thirring model," and B. Klaiber, "The Thirring model," in *Lectures in Theoretical Physics* (Gordon and Breach, 1968), for the exact solution of the massless model.
- Y. Nambu and G. Jona-Lasinio, "Dynamical model of elementary particles based on an analogy with superconductivity," *Physical Review* **122** (1961) 345–358, for the four-fermion interaction whose mean field gives a dynamical mass.
- L. H. Ryder, *Quantum Field Theory* (Cambridge, 2nd ed. 1996), and W. Greiner, *Relativistic Quantum Mechanics: Wave Equations* (Springer, 2000), for the nonlinear spinor equations and their soliton-like solutions.
- The companion articles of this series: [The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism](the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html), [The Gordon Decomposition of the Dirac Current in Biquaternionic Form](the-gordon-decomposition-of-the-dirac-current-in-biquaternionic-form.html), [The Chiral Condensate and Dynamical Symmetry Breaking in Biquaternionic Form](the-chiral-condensate-and-dynamical-symmetry-breaking-in-biquaternionic-form.html), [Bosonization in Biquaternionic Form](bosonization-in-biquaternionic-form.html), and [Curved Spacetime and the Biquaternion Framework](curved-spacetime-and-the-biquaternion-framework.html).
