# __AI describes the Lorentz Group__

## Introduction

**The Lorentz group is $\mathrm{SO}^{+}(1,3)$.**

That is its one name in this article. It is the set of changes of inertial frame: the linear transformations of flat spacetime that leave the interval between two events unchanged, and that can be reached from the identity by a continuous change.

That group is built out of two kinds of transformation, the boosts and the rotations, and every element of it is a product of one of each. The same group sits inside the biquaternion algebra: its unit elements act on a four-vector by the two-sided product $\tilde X\mapsto\tilde U\tilde X\tilde U^{*}$, and the operators obtained that way are exactly the transformations of $\mathrm{SO}^{+}(1,3)$.

## The Lorentz Group

**The interval.** Write an event as $x^\mu=(x^0,\mathbf{x})$ with $x^0=ct$, and let

$$
\eta=\operatorname{diag}(1,-1,-1,-1),\qquad
s^2(x)=x^{\mathsf T}\eta\,x=(x^0)^2-\lvert\mathbf{x}\rvert^2 .
$$

The form is **indefinite**, and its zero set is the light cone. The sign of $s^2$ sorts events into those a signal can reach from the origin and those it cannot, so this one quadratic form carries the causal structure of flat spacetime.

**The defining equation.** The maps that preserve the form are the linear maps $\Lambda$ of $\mathbb{R}^4$ with

$$
\boxed{\ \Lambda^{\mathsf T}\eta\,\Lambda=\eta\ }
$$

which says exactly that $s^2(\Lambda x)=s^2(x)$ for every $x$. Every such map preserves all intervals, and every map preserving all intervals is such a map, because a quadratic form is determined by its values.

**Why this group.** The condition leaves the determinant free up to sign, $\det\Lambda=\pm1$, and the time-time entry satisfies

$$
\bigl(\Lambda^{0}{}_{0}\bigr)^2=1+\sum_i\bigl(\Lambda^{i}{}_{0}\bigr)^2\ \ge 1 ,
$$

so $\Lambda^{0}{}_{0}$ never vanishes and cannot change sign continuously. Two discrete signs are therefore available, and the group $\mathrm{SO}^{+}(1,3)$ is the part fixed by $\det\Lambda=+1$ and $\Lambda^{0}{}_{0}\ge1$. It is connected, it contains the identity, and no continuous motion of an observer leaves it. **This is the Lorentz group.**

**Six parameters.** The matrix $\Lambda$ has sixteen entries and the conditions form a symmetric $4\times4$ array, ten independent equations, so $16-10=6$ remain. Infinitesimally, with $\Lambda=I+\omega$,

$$
\omega^{\mathsf T}\eta+\eta\,\omega=0
\quad\Longleftrightarrow\quad
\omega_{\mu\nu}=-\omega_{\nu\mu},
$$

an antisymmetric array with $\binom{4}{2}=6$ entries. The six belong to $\mathrm{SO}^{+}(1,3)$, since a neighbourhood of the identity lies in it, and they are three planes containing the time axis and one space direction, the **boosts**, and three containing two space directions, the **rotations**.

## Boosts and Rotations

**The two families.** A **rotation** fixes the time axis and acts on space by an orthogonal matrix; it has an axis $\hat{\mathbf n}$ and an angle $\theta$, is $R(\hat{\mathbf n},\theta)=\exp(-\theta\,\hat{\mathbf n}\cdot\mathbf J)$, and returns to the identity at $\theta=2\pi$. A **boost** fixes a plane through the time axis and acts on the other two directions by a hyperbolic rotation. With $\boldsymbol\beta=\beta\hat{\mathbf n}$ and $\gamma=(1-\beta^2)^{-1/2}$,

$$
\Lambda_{\mathrm b}(\hat{\mathbf n},w)=
\begin{pmatrix}
\gamma & -\gamma\boldsymbol\beta^{\mathsf T}\\
-\gamma\boldsymbol\beta & I+(\gamma-1)\,\hat{\mathbf n}\hat{\mathbf n}^{\mathsf T}
\end{pmatrix},
\qquad
\beta=\tanh w,\quad \gamma=\cosh w .
$$

**Rapidity is the additive parameter.** The velocity addition law is the addition theorem of the hyperbolic tangent, so two collinear boosts of rapidities $w_1$ and $w_2$ compose to one of rapidity $w_1+w_2$. This is the whole difference between the families: the parameter of a rotation is periodic and bounded, the parameter of a boost is not, so the rotations form a compact set and the boosts do not.

**The group is made of their products.** Every element of $\mathrm{SO}^{+}(1,3)$ is a boost followed by a rotation,

$$
\boxed{\ \Lambda=\Lambda_{\mathrm b}(\vec\beta)\,\Lambda_{\mathrm{rot}}(\hat{\mathbf n},\theta)\ }
$$

and the three parameters are unique: the first column of $\Lambda$ is $(\gamma,-\gamma\vec\beta)$, so $\vec\beta$ is read off, and what remains after the boost is removed fixes the time axis and is therefore a rotation. So the boosts and the rotations generate the group, and two factors suffice: a frame is fixed by the velocity of the observer and the orientation of the observer's axes, and by nothing else.

**This is not a product of groups.** The boosts are not closed under composition, since two boosts about different axes compose to a boost and a rotation, so the group is not $\mathrm{Boost}\times\mathrm{Rot}$; what is a product is the set of elements.

**The half-angle enters every boost.** Because $\cosh w$ and $\sinh w$ factor through it, $\cosh\tfrac w2=\sqrt{(\gamma+1)/2}$ and $\sinh\tfrac w2=\sqrt{(\gamma-1)/2}$. At $\beta=0.6$ the values are $\gamma=1.25$, $w=0.693147$ and $\cosh\tfrac w2=1.060660$.

## The Same Group in the Biquaternion Algebra

Let $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ be the complexified quaternion algebra, with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, where $e_t$ is the identity and $\vec e_\eta^2=-e_t$. An element is $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ with complex coefficients. Let ${}^{\natural}$ fix the scalars and negate the vectors, and ${}^{*}=\bar{\cdot}\circ{}^{\natural}$ be its composition with complex conjugation.

**The norm.** The biquaternion norm is

$$
N(\tilde Q)=\tilde Q\tilde Q^{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2 ,
$$

and it is **multiplicative**, $N(\tilde Q_1\tilde Q_2)=N(\tilde Q_1)N(\tilde Q_2)$.

**The group.** The unit elements are closed under multiplication, the inverse of a unit element is $\tilde U^{\natural}$, which has norm one, and $e_t$ has norm one, so they form a group

$$
G=\{\tilde U\in\mathbb{B} : N(\tilde U)=1\}\cong\mathrm{SL}(2,\mathbb{C}).
$$

One complex equation on four complex coordinates leaves complex dimension $3$, that is real dimension $6$.

**The action is a two-sided Hermitian pair.** Four-vectors are the anti-Hermitian elements, with imaginary scalar and real vector. A unit element acts by conjugation with itself and with its star,

$$
\boxed{\ \tilde X\longmapsto\tilde U\,\tilde X\,\tilde U^{*}\ }
$$

The image is again anti-Hermitian, since $(\tilde U\tilde X\tilde U^{*})^{*}=\tilde U\tilde X^{*}\tilde U^{*}=-\tilde U\tilde X\tilde U^{*}$, and the interval is preserved, since the interval is the norm and

$$
N\bigl(\tilde U\tilde X\tilde U^{*}\bigr)
=N(\tilde U)\,N(\tilde X)\,N(\tilde U^{*})=N(\tilde X),
$$

because $N(\tilde U^{*})=\overline{N(\tilde U)}=1$. **The invariance of the interval is not imposed; it is the multiplicativity of the norm.**

**The operator group is the Lorentz group.** Write $\Theta_{\tilde U}$ for the map above. It is a homomorphism, $\Theta_{\tilde U}\Theta_{\tilde V}=\Theta_{\tilde U\tilde V}$, and every $\Theta_{\tilde U}$ lies in $\mathrm{SO}^{+}(1,3)$. The kernel is $\{\pm e_t\}$, since an operator that is the identity commutes with every element of the algebra and so is a scalar. Both sides have dimension six and are connected, so the image is all of $\mathrm{SO}^{+}(1,3)$, and

$$
\boxed{\ G/\{\pm e_t\}\;\cong\;\mathrm{SO}^{+}(1,3)\ }
$$

**The correspondence is one-to-one on operators.** The two elements $\tilde U$ and $-\tilde U$ are different but give the same operator, and nothing else is lost: the operator group is exactly the Lorentz group, and it acts on four-vectors by its defining representation.

| the standard object | the algebra's object |
|---|---|
| the interval $s^2$ | the norm $N$ |
| the condition $\det\Lambda=1$ | the condition $N=1$ |
| the two-to-one cover | the sign $\pm e_t$ |
| the four-vector | an anti-Hermitian element |
| the Lorentz transformation | the two-sided pair $\tilde U\tilde X\tilde U^{*}$ |
| the invariance of the interval | the multiplicativity of $N$ |

## The Unit Element Is a Boost Times a Rotation

**The word.** A boost of rapidity $\theta_{\mathrm{rpd}}$ along the unit vector $\vec u_{\mathrm b}$ and a rotation of angle $\theta_{\mathrm{axr}}$ about $\vec u_{\mathrm r}$ are the two exponentials

$$
\boxed{\ \tilde U=\tilde U_{\mathrm b}\,\tilde u_{\mathrm r},\qquad
\tilde U_{\mathrm b}=\exp\Bigl(i\tfrac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\Bigr),\qquad
\tilde u_{\mathrm r}=\exp\Bigl(\tfrac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}\Bigr)\ }
$$

with $\vec u_{\mathrm b},\vec u_{\mathrm r}\in S^{2}$, $\theta_{\mathrm{rpd}}\ge0$ and $\theta_{\mathrm{axr}}\in[0,2\pi)$. Spelled out,

$$
\tilde U_{\mathrm b}=\cosh\tfrac{\theta_{\mathrm{rpd}}}{2}\,e_t+i\sinh\tfrac{\theta_{\mathrm{rpd}}}{2}\,\vec u_{\mathrm b},
\qquad
\tilde u_{\mathrm r}=\cos\tfrac{\theta_{\mathrm{axr}}}{2}\,e_t+\sin\tfrac{\theta_{\mathrm{axr}}}{2}\,\vec u_{\mathrm r},
$$

so the boost factor is Hermitian, with real scalar part and imaginary vector part, and the rotation factor is real. Both have norm one, so the product has norm one, and conversely every unit element is such a product. **The unit elements are the products of a boost and a rotation.**

**The product is unique.** For any $\tilde U\in G$ the Hermitian positive factor is $\tilde U\tilde U^{*}$ square-rooted, and the rotation factor is what is left,

$$
\tilde H=\bigl(\tilde U\tilde U^{*}\bigr)^{1/2},\qquad
\tilde K=\tilde H^{-1}\tilde U,\qquad
\tilde U=\tilde H\tilde K ,
$$

with $\tilde K$ a real quaternion, so $\tilde K$ fixes the time axis. This is the left polar decomposition of the matrix; the other word exists too, with different factors, and the block's convention is this one, with the boost on the left. Three parameters in each factor, which is the $3+3=6$ of the group.

**Acting, it gives back the two transformations.** Because the pair is two-sided, each factor acts by its own conjugation, and the rotation may be taken first,

$$
\tilde X\longmapsto\tilde U_{\mathrm b}\bigl(\tilde u_{\mathrm r}\tilde X\tilde u_{\mathrm r}^{*}\bigr)\tilde U_{\mathrm b}^{*}.
$$

The congruence of $\tilde U_{\mathrm b}$ is the boost matrix written above and the congruence of $\tilde u_{\mathrm r}$ is $R(\hat{\mathbf n},\theta)$, so the algebra reproduces the group decomposition element by element. The angle is halved in the element and whole in its action, because the congruence squares it: the parameters acting on a four-vector are $\theta_{\mathrm{rpd}}$ and $\theta_{\mathrm{axr}}$, and not half of them.

**The half-angle is not a convenience.** The eigenvalues of $\tilde U_{\mathrm b}$ are $e^{\pm\theta_{\mathrm{rpd}}/2}$, and $\tilde u_{\mathrm r}$ is minus the identity at $\theta_{\mathrm{axr}}=2\pi$ while its congruence is the identity: the half is what the algebra needs so that its own elements square to the transformation, and the sign it produces is the two-to-one cover.

## Summary

**The group.** The Lorentz group is $\mathrm{SO}^{+}(1,3)$, the identity component of the set of linear maps with $\Lambda^{\mathsf T}\eta\Lambda=\eta$: six parameters, three boosts and three rotations.

**The products.** Every element is a boost times a rotation, uniquely, so the two families generate the group; but they are not a pair of subgroups, since only the rotations close.

**The algebra.** The unit biquaternions, $N(\tilde U)=1$, are the twofold cover of that group, and the multiplicativity of the norm is what preserves the interval.

**The action.** A unit element acts as the two-sided Hermitian pair $\tilde X\mapsto\tilde U\tilde X\tilde U^{*}$, and the operators so obtained are exactly the transformations of $\mathrm{SO}^{+}(1,3)$.

**The decomposition.** A unit element is a boost factor times a rotation factor, $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ with the two exponentials above, and under the pair those two factors are the boost and the rotation of the frame.

## Further Reading

- S. Weinberg, *The Quantum Theory of Fields*, vol. 1, chapter 2, for the group and its algebra.
- [The Rotations, the Boosts and the Groups](the-rotations-the-boosts-and-the-groups.html), for the five groups that contain the two families and what each leaves invariant.
- [The Group of Unit-Norm Biquaternions](the-group-of-unit-norm-biquaternions.html), for the group as a set inside the algebra.
- [The Lorentz Transformation as a Biquaternionic Rotation](the-lorentz-transformation-as-a-biquaternionic-rotation.html), for the two-sided action in detail.
- [A Frame Is a Boost Times a Rotation: The Cartan Word](a-frame-is-a-boost-times-a-rotation-the-cartan-word.html), for the proof of the decomposition and its degenerate cases.
