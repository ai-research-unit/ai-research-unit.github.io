# __Wave–Particle Duality and the Galilean Limit: Why the Schrödinger Symbol Is Affine__

## Introduction

**The Galilean limit does not approximate a solution. It truncates the degree of the symbol in the energy, and the residue is affine.** The relativistic symbol is quadratic in the energy wave number and carries the constant $-k_m^{2}$; the non-relativistic one is linear in the energy above rest. A symbol that is linear in one variable and quadratic in another is called affine, and that word is the whole content of the article. §*What Affine Means* tests the claim by scaling the two kinematic variables with the mass held fixed. §*Degree in the energy, and homogeneity* then says which scalings make either symbol homogeneous, because the naive answer is wrong: neither symbol is homogeneous in the kinematic variables alone, and the two failures are not the same failure.

**The affineness is forced, not chosen.** A linear symbol vanishes at the origin of the energy variable; the Schrödinger symbol does not, and it must not. The Galilei boost law carries a quadratic term in the boost velocity, so a symbol of degree one cannot be invariant under it. Among the symbols of degree at most one in the energy and at most two in the momentum, the invariant ones form exactly a two-dimensional space, spanned by $\sigma_{\mathrm{s}}$ and the constant $1$: the energy and momentum coefficients are locked to one another by the mass, at the ratio $-2k_m$, and only the additive constant is free. Fix that constant, as fixing the zero of the energy does, and the symbol is unique up to scale. §*Why Affine and Not Linear* proves that in two lines, identifies the locking constant as the cocycle of the boost, and says why the free constant is the same freedom.

**The degree fixes three counts at once.** The order in the energy, the number of sheets of the zero set, and the number of initial data are one integer. For the relativistic symbol it is two, twice over: second order in time, two sheets of the hyperbola, and a value plus a derivative at $t=0$. For the Schrödinger symbol it is one, three times: first order in time, one sheet of the paraboloid, one datum. §*The Count That the Degree Fixes* states the triangle, and §*The Rank That the Degree Does Not Fix* says what the same change does to the rank computations of the two preceding articles.

**The second sheet is not deleted. It is at a distance.** The two roots in the energy variable are separated by $2\sqrt{k_m^{2}+k_\Phi^{2}}$, which is at least $2k_m$ and never vanishes. The retained root sits at $k_{\mathrm{s}}\approx k_\Phi^{2}/(2k_m)$ and the discarded one at $k_{\mathrm{s}}\approx-2k_m$, so the discarded one is outside the region $\lvert k_{\mathrm{s}}\rvert\ll2k_m$ in which the truncation holds. The gap that makes the truncation consistent is the mass. **The antiparticle is excluded by the region of validity, not by a declaration.**

**Why this belongs to the series.** *Wave–Particle Duality and the Fourier Transform* turns the operator into a multiplication by an element. *Wave–Particle Duality and the Count of Degrees of Freedom* reads the rank of that multiplication as a count of polarisations. *Wave–Particle Duality and Charge Conservation: The Cokernel of Maxwell's Symbol* reads its cokernel as a condition on the data. Each of the three is a statement about a symbol, and each presupposes a symbol of a definite shape. This article asks what fixes that shape, and the answer is the degree. Without the degree, the rank and the cokernel of the earlier articles are computations about a symbol the non-relativistic equation does not have.

**The strongest objection is that this is a Taylor expansion about the mass shell, and that the content is standard.** The expansion is real, and the article does not deny it. What the objection misses is that the truncation is exact in closed form, that the dropped term is a single named quantity rather than an error estimate, and that three qualitative facts change with the degree and none of them is small. The zero set changes topology: a two-sheeted hyperbola becomes a one-sheeted parabola. The rank changes character: a graded three-then-two becomes an all-or-nothing two-then-zero. The invariance group changes: the Lorentz group becomes the Galilei group, and with it the mass changes from a Casimir of the Poincaré algebra to a central charge of the Galilei algebra. A correction of order $k_\Phi^{4}/k_m^{3}$ in the position of the level set is not the same statement as any of those.

**What is used and what is new.** *Wave–Particle Duality and the Fourier Transform*, §*Worked Case: The Schrödinger Equation*, writes the non-relativistic condition as $k_{t}^{\prime}-k_m-k_{\Phi}^{2}/(2k_m)=0$, records the quartic error $-k_{\Phi}^{4}/(8k_m^{3})$, and states that no element of $\mathbb{B}$ has that symbol for a norm. *The Non-Relativistic Limit of Relativistic Mechanics in Biquaternionic Form* supplies the truncation rule and the statement that the limit is taken on the state and not on $c$. *The Count of Degrees of Freedom* supplies the rank of the first-order symbol. What is new here is the degree as an object: the exact identity between the two symbols, the affine variable and its two homogeneous pieces, the uniqueness of the invariant symbol, the sheet count as a count of initial data, and the collapse of the graded rank.

## The Symbol of the Second-Order Operator

### One scalar, not an element

**The Klein–Gordon operator is second order, and its symbol is a number.** Write $\mathcal{P}=\Box-k_m^{2}$ for the operator of *The First-Order Root of the Biquaternion Klein–Gordon Operator*, with $\Box$ the material d'Alembertian. On a plane wave the gradient is replaced by its symbol and

$$
\sigma_{\mathcal{P}}(k_{t}^{\prime},\vec k_\Phi)=k_{t}^{\prime\,2}-k_{\Phi}^{2}-k_m^{2}.
$$

This is a complex number and not an element of $\mathbb{B}$, and the reason is one line: $\Box$ is the composition $\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}$, whose symbol is the norm $\tilde K_\Phi\tilde K_\Phi^{\natural}$, and the norm of a quaternion is central. **The second-order symbol is left multiplication by a scalar.** The first-order symbol $i\tilde K_\Phi$ is not, and that single difference is the source of everything in this article.

**A scalar symbol has an all-or-nothing rank.** Left multiplication by $\sigma$ is invertible when $\sigma\ne0$ and zero when $\sigma=0$. There is no third case and no intermediate dimension. The graded ranks of the two preceding articles — three off the light cone and two on it — belong to $L_{i\tilde K_\Phi}$, which is not scalar. The second-order symbol has rank four on the whole algebra the moment it is non-zero, and rank zero on the set where it vanishes:

| Frequency point | $L_{i\tilde K_\Phi}$ on $\mathbb{B}_{V}$ | $L_{i\tilde K_\Phi}$ on $\mathbb{B}\tilde\Pi$ | $L_{\sigma_{\mathcal{P}}}$ on $\mathbb{B}$ | $L_{\sigma_{\mathcal{P}}}$ on $\mathbb{B}\tilde\Pi$ |
|---|---|---|---|---|
| neither surface: $k_{t}^{\prime}\ne k_{\Phi}$ and $\sigma_{\mathcal{P}}\ne0$ | 3 | 2 | 4 | 2 |
| light cone, $k_{t}^{\prime}=k_{\Phi}$ | 2 | 1 | 4 | 2 |
| mass shell, $k_{t}^{\prime\,2}=k_{\Phi}^{2}+k_m^{2}$ | 3 | 2 | 0 | 0 |

The light-cone row is not a subcase of the first row but a separate line: there $\sigma_{\mathcal{P}}=-k_m^{2}\ne0$, so the second-order symbol is still a unit. The two columns on the left are the previous articles' object and are reproduced here for contrast; the two on the right are this article's. **The drop from three to two happens only in the first-order column, and only on the light cone. The second-order symbol knows nothing of it.** On the mass shell the first-order symbol still has full rank on the vector part, while the second-order symbol has vanished entirely. **The module column has a one-line derivation.** Under $\mathbb{B}\cong M_2(\mathbb{C})$ with $e_t\mapsto I$ and $\vec e_\mu\mapsto-i\sigma_\mu$, the symbol $i\tilde K_\Phi$ becomes $-k_{t}^{\prime}I+\vec k_\Phi\cdot\vec\sigma$, whose determinant is $a^{2}-\lvert\vec b\rvert^{2}=k_{t}^{\prime\,2}-k_{\Phi}^{2}$. So the rank on the module is two off the light cone and one on it, the vanishing there being of rank one because the matrix itself is not zero. **The light-cone row is therefore derived, and the mass-shell row follows because the scalar symbol multiplies that same matrix by zero.** The remaining columns were taken by singular value decomposition at a tolerance of $10^{-9}$.

**The mass shell is where the non-relativistic physics lives, and the light cone is not.** This is the reason the Galilean limit can keep so little of the earlier bookkeeping: the surface on which the non-relativistic equation admits a plane wave is the surface on which its symbol vanishes, and the surface on which the earlier ranks drop is a different surface, on which the non-relativistic symbol is a non-zero constant. The two degeneracies are not the same degeneracy, and only one of them survives to the non-relativistic description.

### Degree in the energy, and homogeneity

**The operative integer is the degree in the energy variable, and it is two against one.** $\sigma_{\mathcal{P}}$ is quadratic in $k_{t}^{\prime}$ and $\sigma_{\mathrm{s}}$ is linear in $k_{\mathrm{s}}$. That is the degree the next section uses, and it is the only degree the article needs.

**In all three wave numbers together, both symbols are homogeneous.** The mass is a wave number, $k_m=mc/\hbar$, and it is a coordinate of the same kind as the other two. Scaling the triple gives

$$
\sigma_{\mathcal{P}}(\lambda k_{t}^{\prime},\lambda\vec k_\Phi,\lambda k_m)=\lambda^{2}\sigma_{\mathcal{P}}(k_{t}^{\prime},\vec k_\Phi,k_m),
\qquad
\sigma_{\mathrm{s}}(\lambda k_{t}^{\prime},\lambda\vec k_\Phi,\lambda k_m)=\lambda\,\sigma_{\mathrm{s}}(k_{t}^{\prime},\vec k_\Phi,k_m).
$$

The first is degree two and the second degree one, and both statements are exact. This is what lets the corpus treat the three numbers as coordinates of one element, and nothing here contradicts it.

**In the two kinematic wave numbers alone, with the mass held fixed, neither symbol is homogeneous, and the two failures have different shapes.** For the relativistic symbol,

$$
\sigma_{\mathcal{P}}(\lambda k_{t}^{\prime},\lambda\vec k_\Phi)=\lambda^{2}\bigl(k_{t}^{\prime\,2}-k_{\Phi}^{2}\bigr)-k_m^{2}
=\lambda^{2}\sigma_{\mathcal{P}}+k_m^{2}(\lambda^{2}-1),
$$

so the failure is a constant, and its size is the mass squared. **That is the precise sense in which the mass shell is a level set and not a zero set**: the mass shell is $\{\sigma_{\mathcal{P}}=0\}$, which is $\{k_{t}^{\prime\,2}-k_{\Phi}^{2}=k_m^{2}\}$, a level set of the homogeneous quadratic form $k_{t}^{\prime\,2}-k_{\Phi}^{2}$, and not the zero set of any homogeneous polynomial in the two kinematic variables. The quadratic form is homogeneous; the symbol is a quadratic form minus a constant; the level set of the first is the zero set of the second.

**For the Schrödinger symbol the failure is a whole term, and it is of lower degree, not of degree zero alone.** Scaling the kinematic pair gives $\lambda k_{\mathrm{s}}-\lambda^{2}k_{\Phi}^{2}/(2k_m)$, which is degree one in one piece and degree two in the other. So $\sigma_{\mathrm{s}}$ is the sum of two homogeneous pieces of different degree, with no constant. **That is why it is affine and not merely inhomogeneous**, and it is why its zero set is a paraboloid: $\{\sigma_{\mathrm{s}}=0\}$ cannot be written as $\{$quadratic form$=0\}$ or as $\{$quadratic form$=$constant$\}$, because either would be homogeneous in the kinematic variables, and $\sigma_{\mathrm{s}}$ is not.

**The two kinds of inhomogeneity are therefore different in kind and not only in size.** A constant offset keeps the surface a level set of a quadratic form, and a quadratic form has a signature, an axis, and two sheets. A lower-degree term does not, and its surface has one sheet and no axis of symmetry. **The single integer that separates the two is the degree in the energy: two gives a constant offset and a hyperboloid, one gives a linear term and a paraboloid.**

**Two sheets, from one square root.** Solving $\sigma_{\mathcal{P}}=0$ for the energy wave number gives

$$
k_{t}^{\prime}=\pm\sqrt{k_{\Phi}^{2}+k_m^{2}},
$$

and the two signs are two sheets, related by $k_{t}^{\prime}\to-k_{t}^{\prime}$. The symbol is even in $k_{t}^{\prime}$ because it depends on $k_{t}^{\prime}$ only through the square, which is exactly the statement that its offset is of degree zero and not of degree one. **That evenness is what the Galilean limit destroys**, and with it the symmetry that pairs the two sheets.

## The Rest Clock and the Affine Variable

**The one change of variable.** Write the energy wave number as its rest value plus an excess,

$$
k_{t}^{\prime}=k_m+k_{\mathrm{s}},\qquad k_{\mathrm{s}}:=\frac{E-mc^{2}}{\hbar c},
$$

so that $k_{\mathrm{s}}$ is the energy above rest, in the units of the corpus. It is the quantity the companion article writes as $k_{t}^{\prime}-k_m$ whenever it writes the affine condition, and it deserves a name because it is the only variable in which the non-relativistic symbol is simple. It is non-negative for a physical state, vanishes at rest, and is small compared with $k_m$ in the non-relativistic regime.

**The identity, and nothing is expanded to obtain it.** Substitute and expand:

$$
\sigma_{\mathcal{P}}=(k_m+k_{\mathrm{s}})^{2}-k_{\Phi}^{2}-k_m^{2}
=2k_mk_{\mathrm{s}}+k_{\mathrm{s}}^{2}-k_{\Phi}^{2}
=2k_m\bigl(k_{\mathrm{s}}-k_{\Phi}^{2}/(2k_m)\bigr)+k_{\mathrm{s}}^{2}.
$$

Define the bracket as the non-relativistic symbol,

$$
\sigma_{\mathrm{s}}(k_{\mathrm{s}},\vec k_\Phi)=k_{\mathrm{s}}-\frac{k_{\Phi}^{2}}{2k_m},
$$

and the identity reads

$$
\sigma_{\mathcal{P}}=2k_m\,\sigma_{\mathrm{s}}+k_{\mathrm{s}}^{2}.
$$

Both sides are polynomials with constant coefficients, so the identity is also an identity of operators: $\mathcal{P}=2k_m\,\mathcal{S}+\mathcal{R}$, where $\mathcal{S}$ has symbol $\sigma_{\mathrm{s}}$ and $\mathcal{R}$ has symbol $k_{\mathrm{s}}^{2}$. In position space,

$$
\mathcal{S}=\frac{1}{i}\frac{\partial}{\partial r'_t}-k_m+\frac{1}{2k_m}\Delta_\Phi ,
$$

with $\Delta=\vec\nabla^{2}$, and $\mathcal{S}\chi=0$ is the free Schrödinger equation for the envelope, after the rest clock $e^{-i\theta_{\mathrm{rst}}}$ has been divided out. **The division of the rest clock and the subtraction of $k_m$ from the energy are the same operation**, and they are the same operation as passing from $\mathcal{P}$ to $\mathcal{S}$ up to the coefficient $2k_m$.

The angle is $\theta_{\mathrm{rst}}=k_m r'_t$: the mass wave number and the real interval give a real angle.

**The dropped term is one named quantity, and its size is exact.** The residue is $k_{\mathrm{s}}^{2}$ and nothing else. Its size relative to the retained linear term is

$$
\frac{k_{\mathrm{s}}^{2}}{2k_mk_{\mathrm{s}}}=\frac{k_{\mathrm{s}}}{2k_m}=\frac{\gamma-1}{2},
$$

which is $\frac{\beta^{2}}{4}$ at leading order: at $\beta=0.01$ the exact value is $2.5002\times10^{-5}$ against $\beta^{2}/4=2.5000\times10^{-5}$. The truncation is therefore specified by one number at each mode, and not by an order symbol.

**The zero set is a paraboloid.** Setting $\sigma_{\mathrm{s}}=0$ gives

$$
k_{\mathrm{s}}=\frac{k_{\Phi}^{2}}{2k_m},
$$

a single sheet, opening along the energy variable, with the momentum squared as its parameter. **It is the zero set of no homogeneous polynomial in the kinematic variables**, since $\sigma_{\mathrm{s}}$ has a linear term and a quadratic one, and it is therefore no level set of a quadratic form: a level set of a quadratic form is the zero set of that form minus a constant, and subtracting a constant from $\sigma_{\mathrm{s}}$ leaves the linear term in place. That is the precise sense in which the companion article's "not a norm's level set" is a statement about degree. **The parabola is not a small perturbation of the hyperbola in shape. It is a different surface: one sheet against two, no asymptote against two asymptotes at the light cone, and a lowest point at $k_{\mathrm{s}}=0$ against one at $k_{t}^{\prime}=k_m$.**

**The parity is gone.** $\sigma_{\mathrm{s}}$ is not even in the energy variable: $\sigma_{\mathrm{s}}(-k_{\mathrm{s}},\vec k_\Phi)=-k_{\mathrm{s}}-k_{\Phi}^{2}/(2k_m)$ is not a multiple of $\sigma_{\mathrm{s}}(k_{\mathrm{s}},\vec k_\Phi)$. The relativistic symbol is even in $k_{t}^{\prime}$ and this one is not, so the reflection that exchanged the two sheets of the hyperbola is no longer a symmetry of the equation. Something has to be lost, and this is the first thing.

## What Affine Means

### Two degrees, and no third

**A scaling test settles the word.** Apply $k_{\mathrm{s}}\to\lambda k_{\mathrm{s}}$ and $\vec k_\Phi\to\lambda\vec k_\Phi$ with $\lambda>0$. Then

$$
\sigma_{\mathrm{s}}(\lambda k_{\mathrm{s}},\lambda\vec k_\Phi)=\lambda k_{\mathrm{s}}-\lambda^{2}\frac{k_{\Phi}^{2}}{2k_m},
$$

so the first term scales as $\lambda$ and the second as $\lambda^{2}$. A homogeneous symbol of degree $n$ would scale as $\lambda^{n}$, and no $n$ does both. **The symbol is the sum of one homogeneous piece of degree one and one of degree two, and that is exactly what affine means.**

**Affine is not linear, and the offset is the test.** A linear symbol vanishes when all its arguments vanish. Here

$$
\sigma_{\mathrm{s}}(0,\vec k_\Phi)=-\frac{k_{\Phi}^{2}}{2k_m}\ne0
$$

whenever the momentum is non-zero. The symbol therefore does not come from a linear operator in the energy variable alone, and the non-vanishing offset is not an artefact of bookkeeping: it is the kinetic energy, which does not vanish at zero frequency because it does not depend on frequency at all.

**Affineness survives any choice of the energy zero.** Replace $k_{\mathrm{s}}$ by $k_{\mathrm{s}}+\delta$ for any constant $\delta$; the symbol becomes $k_{\mathrm{s}}+\delta-k_{\Phi}^{2}/(2k_m)$, which is affine with the same slope and a different offset. A shift that depends on the momentum changes the offset by a function of the momentum, and the slope is again untouched. **What is invariant under every redefinition of the zero is that the symbol is affine, and the reason is that a change of the zero can only add to the offset.**

### No element has it for a norm

**The norm is homogeneous of degree two in all four slots, and the symbol has no single degree at all.** Since $\tilde K\tilde K^{\natural}$ is a quadratic form, no element of $\mathbb{B}$ has $\sigma_{\mathrm{s}}$ for its norm. This is the companion article's observation, and the degree makes the reason exact: the norm's scaling is $\lambda^{2}$ in every coordinate, while $\sigma_{\mathrm{s}}$ has a term of degree one in the energy. **One disagreement of degree, and the question is closed.** A reader who tries to find a $\tilde K$ with $\tilde K\tilde K^{\natural}=\sigma_{\mathrm{s}}$ is looking for an element whose norm is not homogeneous, and no such element exists in any dimension.

**The converse also holds, and it is worth stating.** A norm is homogeneous of degree two, so a symbol that is a norm has a cone for a zero set and hyperboloids for its level sets, and it is the symbol of a second-order operator with equal orders in time and space. The relativistic case is the only shape in which the wave arm of the duality is a level set of a norm, and the reason is not that the relativistic physics is special: it is that a norm is special, and only a degree-two symbol can be one.

### The operator's two orders

**The degree in the energy is the order in time, and the degree in the momentum is the order in space.** The substitution $\partial/\partial r'_t\to i k_{t}^{\prime}$ carries degree one in the energy to one derivative in $r'_t$, and $\partial/\partial x_j\to ik_j$ carries degree two in the momentum to two derivatives. So a symbol with degrees one and two is the symbol of an operator with one time derivative and two space derivatives, and conversely. Applying the substitution to $\sigma_{\mathrm{s}}$ gives $\mathcal{S}$ above.

**The asymmetry of the equation is therefore not a convention.** The Schrödinger equation is first order in $t$ and second in $x$ because its symbol has one homogeneous piece of degree one and one of degree two. Any equation whose symbol has that shape is first order in one variable and second in the others, and no equation whose symbol is homogeneous of a single degree can have the asymmetry. **This is the sense in which the Galilean limit is a statement about shape rather than about size.**

## Why Affine and Not Linear

### The boost law, and its quadratic term

**A Galilei boost acts on the wave numbers.** With boost velocity $\vec v_b=c\vec\beta_b$, the momentum and the energy above rest transform as

$$
\vec k_\Phi\longrightarrow\vec k_\Phi-k_m\vec\beta_b ,
\qquad
k_{\mathrm{s}}\longrightarrow k_{\mathrm{s}}-\vec k_\Phi\cdot\vec\beta_b+\tfrac{1}{2}k_m\lvert\vec\beta_b\rvert^{2} ,
$$

which is the non-relativistic limit of the Lorentz transformation written in the corpus's wave numbers. The third term is the one that matters. **The energy above rest does not transform linearly: it acquires a term quadratic in the boost velocity, and that term is proportional to the mass.**

### The affine symbol is invariant, exactly

**Substituting the boost law into $\sigma_{\mathrm{s}}$ leaves it unchanged.** Write the transformed symbol and expand the transformed momentum squared:

$$
k_{\mathrm{s}}-\vec k_\Phi\cdot\vec\beta_b+\tfrac{1}{2}k_m\beta_b^{2}
-\frac{\lvert\vec k_\Phi-k_m\vec\beta_b\rvert^{2}}{2k_m}
=k_{\mathrm{s}}-\frac{k_{\Phi}^{2}}{2k_m},
$$

because the cross term of the square is $-2k_m\vec k_\Phi\cdot\vec\beta_b$, whose quotient by $2k_m$ cancels the linear term, and the square of the boost is $k_m^{2}\beta_b^{2}$, whose quotient by $2k_m$ cancels the quadratic one. Both cancellations are exact and neither is an approximation. **The symbol is Galilei-invariant for every momentum and every boost velocity**, and a numerical check over two hundred random points gives a worst relative residual of $1.8\times10^{-15}$, which is round-off.

**The general trial symbol has three coefficients, and the constant does not transform.** Take the most general symbol of degree at most one in $k_{\mathrm{s}}$ and at most two in $\vec k_\Phi$,

$$
\sigma=a\,k_{\mathrm{s}}+c\,k_{\Phi}^{2}+d,
$$

and impose invariance. The constant $d$ is untouched by the boost, because the boost law adds to $k_{\mathrm{s}}$ a term that does not depend on $k_{\mathrm{s}}$. The difference $\sigma'-\sigma$ has a term linear in $\vec\beta_b$ with coefficient $-(a+2ck_m)\vec k_\Phi\cdot\vec\beta_b$ and a term quadratic in $\vec\beta_b$ with coefficient $\bigl(\tfrac{1}{2}ak_m+ck_m^{2}\bigr)\beta_b^{2}$. The first must vanish for every momentum, so $a=-2ck_m$; and then the second vanishes identically, since $\tfrac{1}{2}(-2ck_m)k_m+ck_m^{2}=0$. **Two conditions, one free scale, one free constant, and the ratio of the two wave-number coefficients fixed by the mass.**

**So the invariant space is two-dimensional, and the honest statement is uniqueness modulo a constant.** Every Galilei-invariant symbol of the stated degrees is

$$
\sigma=c\Bigl(k_{\mathrm{s}}-\frac{k_{\Phi}^{2}}{2k_m}\Bigr)+d=c\,\sigma_{\mathrm{s}}+d,
$$

a two-parameter family: the scale $c$ and the additive constant $d$. The constant is not an accident of the ansatz and not a gap in the argument. **A constant added to a symbol is a constant potential**, and a constant potential is Galilei-invariant exactly: the boost multiplies the wave function by the phase $e^{i\theta_{\mathrm{gal}}}$, with the boost angle $\theta_{\mathrm{gal}}=m\vec v_b\cdot\vec r-\frac{1}{2}m\lvert\vec v_b\rvert^{2}h_t$ real because the mass, the boost velocity, the position and the time are real, and the cross terms it brings to $i\partial_{h_t}$ and to $-\nabla^{2}/(2k_m)$ cancel against it. The free constant of the symbol and the phase of the boost are the same freedom, seen from the two sides.

**Modulo that freedom the symbol is unique up to scale, and the affineness is forced.** Fixing the zero of the energy so that $d=0$, which is what the rest clock does, leaves the one-dimensional line spanned by $\sigma_{\mathrm{s}}$. Setting $c=0$ leaves only constants, and a constant symbol has no dispersion relation at all: its zero set is empty or the whole space. **So there is no Galilei-invariant symbol of degree one in the wave numbers other than the zero symbol, and every invariant shape of these degrees is affine. Affineness is not a choice among invariant shapes, and it is not merely one member of the family: the family is affine as a whole.**

### The mass is the cocycle

**The two numbers are the same number.** The locking constant $a=-2ck_m$ and the quadratic term $\tfrac{1}{2}k_m\beta_b^{2}$ of the boost law both carry $k_m$, and they must: the one is what makes the symbol invariant and the other is what has to be cancelled for it to be. **The mass appears in the symbol because it appears in the boost law, and it appears in the boost law as the cocycle.**

**The group-theoretic name for that.** In the Poincaré algebra the mass is a Casimir, an element built from the generators; in the Galilei algebra it is not in the algebra at all. It is a central charge of the extension, the boost acts on the wave function up to a phase rather than exactly, and the algebra closes only on the extended space. The quadratic term $\tfrac{1}{2}k_m\beta_b^{2}$ is precisely the phase, and the affine offset of the symbol is precisely its transform. **The statement is an identification and not a derivation**: the article computes the algebra of the symbol and the algebra of the boost, shows that the two constants coincide, and names the coincidence. What the coincidence means for the representation theory of the Galilei group is the content of the corpus's non-relativistic limit article, and nothing here adds to it.

## The Count That the Degree Fixes

### One integer, three names

**Order in the energy, sheets of the zero set, initial data: one number.** A polynomial in $k_{\mathrm{s}}$ of degree $n$ has $n$ roots, so its zero set has $n$ sheets over the momentum; and a constant-coefficient equation that is order $n$ in $\partial/\partial r'_t$ needs $n$ data at $r'_t=0$. For $\sigma_{\mathcal{P}}$ the degree is two and all three counts are two. For $\sigma_{\mathrm{s}}$ the degree is one and all three are one. **The three counts cannot disagree, because they are one count.**

**The relativistic case, in the affine variable.** The exact roots are

$$
k_{\mathrm{s},\pm}=-k_m\pm\sqrt{k_m^{2}+k_{\Phi}^{2}},
$$

so the two sheets are separated by $2\sqrt{k_m^{2}+k_{\Phi}^{2}}$, which tends to $2k_m$ as the momentum vanishes and grows from there. **The separation never vanishes, and its minimum is the mass.** The two roots are not a small perturbation of one root: they are a distance $2k_m$ apart at zero momentum, and no change of the momentum closes the gap.

### The gap is the mass, and the region is the argument

**The retained root and the discarded root, read in the affine variable.** Expanding the positive root gives $k_{\mathrm{s},+}=k_{\Phi}^{2}/(2k_m)-k_{\Phi}^{4}/(8k_m^{3})+\cdots$, which is the affine relation plus the companion article's quartic error. The negative root gives $k_{\mathrm{s},-}=-2k_m-k_{\Phi}^{2}/(2k_m)-\cdots$, which is the mirror of the first, translated by $-2k_m$. **So the discarded sheet is not at infinity and is not removed: it sits at $k_{\mathrm{s}}\approx-2k_m$.**

**That is the argument for the truncation.** The retained term is $2k_mk_{\mathrm{s}}$ and the dropped term is $k_{\mathrm{s}}^{2}$; their ratio is $k_{\mathrm{s}}/(2k_m)$, which is small exactly in the region where $\lvert k_{\mathrm{s}}\rvert\ll2k_m$. The discarded sheet is at $\lvert k_{\mathrm{s}}\rvert\approx2k_m$, which is the boundary of that region, and the retained sheet is at $k_{\mathrm{s}}\approx k_{\Phi}^{2}/(2k_m)$, which is inside it whenever the momentum is small compared with the mass. **The truncation is consistent precisely because the two sheets are far apart, and the distance between them is the mass.** A massless theory would have the two sheets meeting at the origin, no region in which one is far from the other, and no Galilean limit of this kind.

### The datum that disappears

**A second-order equation in time needs a value and a derivative; a first-order one needs a value.** This is the third face of the same integer, and it is the one that carries the physics. In the relativistic theory the two data at $r'_t=0$ are the field and its time derivative, and the two sheets are the two independent ways of choosing them. In the Schrödinger theory there is one datum, the envelope, and one sheet.

**The missing datum is the negative-frequency amplitude.** It is not that the amplitude is set to zero by hand at the end; it is that the equation has no room for it, because the degree is one. A reader who asks where the antiparticle went should be told that the second initial datum went with it, and that the second datum exists only where the degree is two. **The count of initial data and the count of polarisations are both counts of independent amplitudes**, and the Galilean limit halves the first and replaces the second by a property of the module, as the next section shows.

## The Rank That the Degree Does Not Fix

### What happens to the graded rank

**The Schrödinger symbol is scalar, so its rank is all-or-nothing.** Left multiplication by $\sigma_{\mathrm{s}}$ on the module $\mathbb{B}\tilde\Pi$ is invertible exactly when $\sigma_{\mathrm{s}}\ne0$, and then it has the module's dimension; it is zero exactly on the paraboloid. With the module two complex-dimensional, the rank is two off the paraboloid and zero on it, and the cokernel is zero and two respectively:

| Frequency point | rank of $L_{\sigma_{\mathrm{s}}}$ | $\dim\ker$ | $\dim\operatorname{coker}$ |
|---|---|---|---|
| off the paraboloid, $k_{\mathrm{s}}\ne k_{\Phi}^{2}/(2k_m)$ | 2 | 0 | 0 |
| on the paraboloid, $k_{\mathrm{s}}=k_{\Phi}^{2}/(2k_m)$ | 0 | 2 | 2 |

**The budget of four becomes a budget of two, and the graded step disappears.** In the relativistic case the rank went from three to two across the light cone, and the cokernel from one to two; the step was the whole content of the count of degrees of freedom. Here there is no step: the rank is the module's dimension or it is nothing, and the cokernel is nothing or it is the module. **The two-stage count of the earlier articles has no non-relativistic analogue**, and this is not a defect of the limit: it is the statement that the earlier count was a property of a first-order element with a non-central symbol, and the Galilean symbol is neither first order nor non-central.

### So the polarisation count changes its origin

**Relativistically the count of polarisations is a rank; non-relativistically it is a dimension.** In the Maxwell case the symbol is an element of the algebra, its left multiplication on the vector part has rank two on the light cone, and the two is the number of transverse polarisations. The count is algebraic: it is a dimension of an image, computed from the symbol. In the Schrödinger case the symbol is a scalar and its rank carries no such information; the number of components of the wave function is the dimension of the module, chosen when the module is chosen.

**That is the honest statement of a difference the two counts hide.** Both are called a count of polarisations, and when the two happen to be equal they look like the same count. They are not the same count. One is computed from the symbol and one is a property of the space the symbol acts on. **In the non-relativistic theory the spin count is a tensor factor; in the relativistic theory it is an algebraic rank.** The Galilean limit is where the difference becomes visible, because that is where the symbol loses the structure that made the rank a count.

**The budget still closes, with a different total.** Rank plus cokernel equals the module's dimension at every point, exactly as rank plus cokernel equalled four in the earlier articles. **The identity is the same identity; only the total changes**, from the codomain's four to the module's two. What the limit removes is not the bookkeeping but the graded structure that made the bookkeeping interesting.

## The Same Shift, and What It Does to the Condition

**The conserved functional is the third article's, and it is homogeneous in the relativistic variable.** $\mathrm{Sc}(\tilde K_\Phi^{\natural}\tilde J_\Phi)=\vec k_\Phi\cdot\vec J-k_{t}^{\prime}c\rho$, so the condition is

$$
\vec k_\Phi\cdot\vec J=k_{t}^{\prime}c\rho ,
$$

which is homogeneous of degree one in the wave numbers: scale all of them and both sides scale once. There is no offset and no mass appears.

**Written with the energy split, it separates into a kinetic term and a rest term.** Substituting $k_{t}^{\prime}=k_m+k_{\mathrm{s}}$ gives

$$
\vec k_\Phi\cdot\vec J=k_mc\rho+k_{\mathrm{s}}c\rho .
$$

**The second term is not an offset in the condition; it is the rest frequency of the field the current belongs to.** $\rho$ and $\vec J$ are bilinear in the field, and a phase cancels between the two factors, so factoring the rest clock $e^{-i\theta_{\mathrm{rst}}}$ out of the field leaves the current unchanged. A field written with the rest clock oscillates at $k_{t}^{\prime}=k_m+k_{\mathrm{s}}$ and its condition is the line above; the same field written without it oscillates at $k_{\mathrm{s}}$ and its condition is $\vec k_\Phi\cdot\vec J=k_{\mathrm{s}}c\rho$. **The two lines are one equation with one current, read at two frequencies.** The term $k_mc\rho$ appears only when the current of the unfactored field is paired with the frequency of the factored one, and that pairing is a mixing of conventions and not a physical term.

**The convention is the one the rest clock fixes: the phase is factored out of the field, so the density is $|\psi|^2$ of the factored field and the frequency written for it is $k_{\mathrm{s}}$.** Writing $\rho=e^{-i\theta_{\mathrm{rst}}}\rho_{\mathrm{s}}$ instead, with the phase attached to the density and not to the field, would move the term to the other side with the opposite sign. **The sign is a convention; the identity of the two lines is not.**

| Variable | The symbol | The condition $\mathrm{Sc}(\tilde K_\Phi^{\natural}\tilde J_\Phi)=0$ |
|---|---|---|
| $k_{t}^{\prime}$, the frequency of the field with the rest clock | $k_{t}^{\prime\,2}-k_{\Phi}^{2}-k_m^{2}$; quadratic in $k_{t}^{\prime}$ plus a constant | $\vec k_\Phi\cdot\vec J=k_{t}^{\prime}c\rho$; homogeneous of degree one |
| $k_{\mathrm{s}}$, the frequency of the field without it | $k_{\mathrm{s}}-k_{\Phi}^{2}/(2k_m)$; linear in $k_{\mathrm{s}}$, affine | $\vec k_\Phi\cdot\vec J=k_{\mathrm{s}}c\rho$; homogeneous of degree one |

**So the condition is homogeneous in either variable and the symbol is not, and that asymmetry is the content of this section.** The shift of the energy zero changes the operator, and with it the degree structure of the symbol: a quadratic form plus a constant becomes a linear term plus a quadratic one. The shift does not change the current, and a condition that is homogeneous on a current stays homogeneous in whatever frequency that current carries. **Affineness is a property of the symbol and homogeneity is a property of the condition, and neither implies anything about the other.** A reader who assumes that an affine symbol must bring an affine conservation law with it, or that a homogeneous conservation law must bring a homogeneous symbol, is wrong in the same way in either direction.

**What survives unchanged is the identification and not the shape.** The third article's result is that the condition on the source is the cokernel of the symbol, read through the scalar pairing. That is a statement about which functional acts on the source, and a shift of the frequency variable does not change which functional it is: the element $\tilde K_\Phi^{\natural}$, its pairing with $\tilde J_\Phi$, and the vanishing that defines admissibility are the same three objects in either variable. **The Galilean limit changes the shape of the statement and leaves its content alone.**

**What does not survive is the second member of the cokernel.** On the light cone the cokernel had two members, one conservation and one selection. The non-relativistic equation has no light cone to be on, and the selection member was a statement about the two circular directions of a vector-valued symbol. A scalar symbol has no circular directions to select between. **The limit keeps the conserved member and drops the selection member**, and the reason is again the degree: the selection member was produced by the non-central part of a first-order symbol, and the Galilean symbol has no non-central part.

## What the Limit Costs

**Four losses, and none follows from another.** The article has met all four, and they are listed here in one place because a reader who notices one will not thereby notice the rest.

**The second sheet.** The zero set loses a sheet, and with it the discrete reflection $k_{t}^{\prime}\to-k_{t}^{\prime}$ that exchanged the sheets. The relativistic spectrum is symmetric under it; the non-relativistic spectrum is not.

**The second initial datum.** The equation is order one in time, so one datum suffices, and the datum that would have carried the negative-frequency amplitude has nowhere to go.

**The graded rank.** The symbol becomes scalar, so the rank becomes all-or-nothing, and the step from three to two that the count of degrees of freedom turned into a physical statement no longer exists.

**The algebraic origin of the polarisation count.** With the graded rank goes the computation of the polarisation number from the symbol. What remains is the dimension of the module, which is a choice.

**What is not lost.** The dispersion relation, to the order the limit keeps, and its first correction, which is quartic and computed. The conservation law, whose functional is the same functional in either variable. And the structure of the duality itself: a symbol, a transform that turns the operator into a multiplication, and a zero set that the particle arm calls a mass shell. **The duality survives; its counting device changes.**

## Limits

**The coefficients are constant and the frequency is fixed.** Everything here is at one wave number in a homogeneous medium, as in the two preceding articles. A position-dependent potential makes the symbol position-dependent, the level set a surface in a bundle, and the Galilean invariance of §*Why Affine and Not Linear* fails — a constant potential preserves both the affineness and the invariance, and a varying one preserves only the affineness.

**The region of validity is $\lvert k_{\mathrm{s}}\rvert\ll2k_m$, not $c\to\infty$.** Setting $c\to\infty$ would contradict the Maxwell equations that supply $k_m$, as *The Non-Relativistic Limit of Relativistic Mechanics in Biquaternionic Form* says. The limit is taken on the state: the excess of the energy over rest is small compared with twice the rest energy, and the truncation error is exactly $\frac{\gamma-1}{2}$ relative. At $\beta=0.01$ that is $2.5\times10^{-5}$; at $\beta=0.1$ it is $2.5\times10^{-3}$; at $\beta=0.5$ it is $7.7\times10^{-2}$ and the word approximation has stopped being useful.

**The module is a choice, and the rank statements are that choice's.** The dimension two quoted for the module is the two of $\mathbb{B}\tilde\Pi\cong\mathbb{C}^{2}$, which is the spin-$\tfrac{1}{2}$ module of *The Schrödinger Equation in Biquaternionic Form*. A scalar wave function gives dimension one and a different table; every statement about the rank is a statement about the module, and the article says so where it uses one.

**"No antiparticle" is a statement about the reduced description.** The article shows that the reduced equation has one sheet and one datum. It does not show that a relativistic antiparticle is absent from nature, and it does not need to: what it shows is that the reduced description has no room for one, which is a statement about the description and not about the world.

## Summary

The Klein–Gordon symbol is a scalar, $\sigma_{\mathcal{P}}=k_{t}^{\prime\,2}-k_{\Phi}^{2}-k_m^{2}$: quadratic in the energy, with a constant offset, homogeneous of degree two only when the mass is scaled with it, and with a two-sheeted zero set that is a level set of the quadratic form $k_{t}^{\prime\,2}-k_{\Phi}^{2}$. The graded rank of three or two belongs to the first-order symbol $i\tilde K_\Phi$ and not to it. Written in the excess of the energy over rest, $k_{\mathrm{s}}=k_{t}^{\prime}-k_m$, it factors exactly as $\sigma_{\mathcal{P}}=2k_m\sigma_{\mathrm{s}}+k_{\mathrm{s}}^{2}$ with $\sigma_{\mathrm{s}}=k_{\mathrm{s}}-k_{\Phi}^{2}/(2k_m)$, and the second term is the whole of what the Galilean limit drops.

The symbol $\sigma_{\mathrm{s}}$ is affine: one homogeneous piece of degree one and one of degree two, no single degree, and a non-vanishing offset. It is not linear, and it cannot be, because the Galilei boost law carries the quadratic term $\frac{1}{2}k_m\beta_b^{2}$ and a degree-one symbol cannot absorb it. Among symbols of degree at most one in the energy and at most two in the momentum, the invariant family is two-dimensional, $c\,\sigma_{\mathrm{s}}+d$, with the two wave-number coefficients locked at $a=-2ck_m$ and the additive constant free. The constant is a constant potential, which the boost phase absorbs exactly, so it is the same freedom seen from the two sides; fixing the zero of the energy at $d=0$ leaves the line of $\sigma_{\mathrm{s}}$. Setting $c=0$ leaves only constants, which have no dispersion, so there is no invariant symbol of degree one in the wave numbers other than zero. **Every invariant shape of these degrees is affine.**

The degree fixes one integer appearing three times: the order in the energy, the number of sheets, and the number of initial data. Two for the relativistic symbol and one for the Schrödinger symbol. The two sheets are separated by $2\sqrt{k_m^{2}+k_{\Phi}^{2}}$, at least $2k_m$, so the discarded sheet sits at $k_{\mathrm{s}}\approx-2k_m$ and is excluded by the region $\lvert k_{\mathrm{s}}\rvert\ll2k_m$ in which the truncation holds rather than by a declaration. The gap is the mass, and a massless theory would have no such region.

The scalar symbol has no graded rank. Its left multiplication is invertible off the paraboloid and zero on it, so the rank is the module's dimension or nothing, and the budget rank plus cokernel closes at the module's dimension instead of at four. **The polarisation count therefore changes its origin: relativistically it is the rank of a first-order element, non-relativistically it is the dimension of the module.** That is the deepest thing the limit does, and it is invisible in the two counts themselves, which are both two.

The condition on the source is homogeneous in either variable, and the symbol is not. $\vec k_\Phi\cdot\vec J=k_{t}^{\prime}c\rho$ and $\vec k_\Phi\cdot\vec J=k_{\mathrm{s}}c\rho$ are one equation with one current, read at the frequency of the field with the rest clock and at the frequency of the field without it; the term $k_mc\rho$ appears only when the current of one is paired with the frequency of the other. **The shift changes the operator and with it the degree of the symbol, and it does not change the current, so the affineness of the symbol and the homogeneity of the condition are independent statements and neither implies the other.** What survives the shift unchanged is the identification: the functional, the element $\tilde K_\Phi^{\natural}$, and the vanishing that defines admissibility are the same objects in either variable. What does not survive is the second member of the cokernel, which needed a vector-valued and non-central symbol and has neither.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma_{\mathcal{P}}$ | the symbol of $\Box-k_m^{2}$, $k_{t}^{\prime\,2}-k_{\Phi}^{2}-k_m^{2}$; a complex number |
| $\mathcal{S}$ | the operator with symbol $\sigma_{\mathrm{s}}$; first order in $r'_t$, second in space |
| $k_{\mathrm{s}}$ | the energy above rest, $k_{t}^{\prime}-k_m=(E-mc^{2})/(\hbar c)$ |
| $\sigma_{\mathrm{s}}$ | the Schrödinger symbol, $k_{\mathrm{s}}-k_{\Phi}^{2}/(2k_m)$; affine |
| $k_m$ | the mass wave number, $mc/\hbar$; the gap between the two sheets at zero momentum |
| $k_{t}^{\prime}$ | the energy wave number, $E/(\hbar c)$ |
| $k_{\Phi}$ | the modulus of the momentum wave number, $\lvert\vec p\rvert/\hbar$ |
| $\vec\beta_b$ | the boost velocity in units of $c$; its square enters the boost law with the coefficient $\frac{1}{2}k_m$ |
| $a$, $c$, $d$ | the coefficients of $k_{\mathrm{s}}$, $k_{\Phi}^{2}$ and the constant in a trial symbol; invariance forces $a=-2ck_m$ and leaves $d$ free |
| $\lambda$ | the scaling parameter that tests homogeneity |
| $\mathbb{B}\tilde\Pi$ | the state module, $\cong\mathbb{C}^{2}$; the domain on which the rank statements are made |
| $k_{\mathrm{s},\pm}$ | the two roots, $-k_m\pm\sqrt{k_m^{2}+k_{\Phi}^{2}}$ |
| $\rho$, $\vec J$ | the charge density and the current density of $\tilde J_\Phi=ic\rho\,e_t+\vec J$ |

## Further Reading

*Wave–Particle Duality and the Fourier Transform* for the affine condition as it first appears, the rest clock, and the quartic error.

*Wave–Particle Duality and the Count of Degrees of Freedom* for the rank of the first-order symbol, the graded drop on the light cone, and the polarisation count it produces.

*Wave–Particle Duality and Charge Conservation: The Cokernel of Maxwell's Symbol* for the cokernel as a condition on the source, and the conserved member that survives this limit.

*The Non-Relativistic Limit of Relativistic Mechanics in Biquaternionic Form* for the truncation rule, the ordering argument, and the statement that the limit is taken on the state and not on $c$.

*The Schrödinger Equation in Biquaternionic Form* for the state module, the scalar imaginary, and the reason the wave function is a spinor rather than a general element.

*The First-Order Root of the Biquaternion Klein–Gordon Operator* for the operator whose symbol is $\sigma_{\mathcal{P}}$ and for the block determinant that makes it scalar.

*The Three Wavenumbers of a Particle* for the relation between $k_{t}^{\prime}$, $k_{\Phi}$ and $k_m$ that the affine relation approximates.

*Maxwell's Equations in the Biquaternionic Formulation* for the covariant continuity equation whose non-relativistic limit is the last section's linear relation.
